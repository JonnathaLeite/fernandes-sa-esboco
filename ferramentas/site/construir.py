"""Monta as páginas do site a partir da pasta `fonte/`.

Cada página em `fonte/paginas/` e cada artigo em `fonte/blog/` começa com um
bloco de metadados em comentário HTML:

    <!--
    titulo: Nossos serviços
    descricao: Texto para o Google e para o compartilhamento.
    menu: servicos
    -->

O conteúdo é encaixado no layout `fonte/partes/base.html`, junto com o
cabeçalho e o rodapé, que ficam em um só lugar. Os marcadores `{{ nome }}`
são substituídos durante a montagem.

Uso:  python ferramentas/site/construir.py
"""
from datetime import date
from html import escape
from pathlib import Path
import re
import sys

RAIZ = Path(__file__).resolve().parents[2]
FONTE = RAIZ / "fonte"
URL_SITE = "https://jonnathaleite.github.io/fernandes-sa-esboco/"

sys.path.insert(0, str(RAIZ / "ferramentas" / "videos"))
from perguntas import PERGUNTAS, TEMAS  # noqa: E402

MENU = [
    ("inicio", "Home", "index.html"),
    ("servicos", "Nossos serviços", "servicos.html"),
    ("profissionais", "Profissionais", "profissionais.html"),
    ("duvidas", "Dúvidas em vídeo", "duvidas.html"),
    ("blog", "Blog", "blog.html"),
    ("contato", "Contato", "contato.html"),
]

MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
         "agosto", "setembro", "outubro", "novembro", "dezembro"]

MARCADOR = re.compile(r"{{\s*([\w-]+)\s*}}")
METADADOS = re.compile(r"\A\s*<!--(.*?)-->\s*", re.S)


def ler_documento(caminho):
    """Separa os metadados do conteúdo de um arquivo da pasta fonte/."""
    texto = caminho.read_text(encoding="utf-8")
    bloco = METADADOS.match(texto)
    if not bloco:
        raise SystemExit(f"{caminho}: faltam os metadados no início do arquivo.")
    meta = {}
    for linha in bloco.group(1).strip().splitlines():
        chave, _, valor = linha.partition(":")
        meta[chave.strip()] = valor.strip()
    return meta, texto[bloco.end():].strip()


def preencher(modelo, valores):
    def trocar(achado):
        nome = achado.group(1)
        if nome not in valores:
            raise KeyError(f"Marcador sem valor: {{{{ {nome} }}}}")
        return str(valores[nome])
    return MARCADOR.sub(trocar, modelo)


def parte(nome):
    return (FONTE / "partes" / f"{nome}.html").read_text(encoding="utf-8")


def data_por_extenso(iso):
    d = date.fromisoformat(iso)
    return f"{d.day} de {MESES[d.month - 1]} de {d.year}"


# Componentes gerados ---------------------------------------------------------

def montar_menu(ativo, raiz):
    itens = []
    for chave, rotulo, arquivo in MENU:
        atual = ' aria-current="page"' if chave == ativo else ""
        itens.append(f'<a href="{raiz}{arquivo}"{atual}>{rotulo}</a>')
    return "\n          ".join(itens)


def carregar_artigos():
    artigos = []
    for caminho in sorted((FONTE / "blog").glob("*.html")):
        meta, corpo = ler_documento(caminho)
        meta["slug"] = caminho.stem
        meta["corpo"] = corpo
        artigos.append(meta)
    return sorted(artigos, key=lambda a: a["data"], reverse=True)


def cartao_artigo(artigo, raiz):
    return f"""<article class="post-card">
  <a class="post-card-capa" href="{raiz}blog/{artigo['slug']}.html" tabindex="-1" aria-hidden="true">
    <img src="{raiz}assets/img/blog/{artigo['slug']}.webp" alt="" width="1200" height="675" loading="lazy" />
  </a>
  <div class="post-card-texto">
    <p class="post-card-tema">{escape(artigo['tema'])}</p>
    <h3><a href="{raiz}blog/{artigo['slug']}.html">{escape(artigo['titulo'])}</a></h3>
    <p>{escape(artigo['resumo'])}</p>
    <a class="post-card-mais" href="{raiz}blog/{artigo['slug']}.html">Leia mais <span aria-hidden="true">»</span></a>
  </div>
  <time datetime="{artigo['data']}">{data_por_extenso(artigo['data'])}</time>
</article>"""


def lista_artigos(artigos, raiz):
    return "\n".join(cartao_artigo(a, raiz) for a in artigos)


def secao_duvidas():
    itens = []
    for numero, q in enumerate(PERGUNTAS, 1):
        tema = TEMAS[q["tema"]][0]
        video = f"assets/videos/{q['slug']}"
        respostas = "".join(f"<p>{escape(p)}</p>" for p in q["resposta"])
        links = f'<a class="qa-nojs" href="{video}.mp4">Assistir ao vídeo</a>'
        if q["link"]:
            rotulo, url = q["link"]
            externo = ' target="_blank" rel="noopener"' if url.startswith("http") else ""
            links += f'<a href="{escape(url)}"{externo}>{escape(rotulo)}</a>'
        roteiro = "".join(f"<li><strong>{escape(t)}.</strong> {escape(c)}</li>" for t, c in q["telas"])
        itens.append(f"""<details class="qa" id="{q['slug']}" data-topic="{q['tema']}" data-video="{video}.mp4" data-poster="{video}.webp">
  <summary>
    <span class="qa-num" aria-hidden="true">{numero:02d}</span>
    <span class="qa-q">{escape(q['pergunta'])}</span>
    <span class="qa-meta">{escape(tema)} · <span class="qa-play" aria-hidden="true">▶</span> {q.get('duracao', '0:36')}</span>
  </summary>
  <div class="qa-body">
    {respostas}
    <p class="qa-links">{links}</p>
    <details class="qa-transcript">
      <summary>Ler a transcrição do vídeo</summary>
      <ol>{roteiro}</ol>
    </details>
  </div>
</details>""")
    filtros = "".join(
        f'<button type="button" data-topic="{chave}" aria-pressed="false">{escape(nome)}</button>'
        for chave, (nome, _) in TEMAS.items()
    )
    return preencher(parte("duvidas"), {
        "total": len(PERGUNTAS),
        "filtros": filtros,
        "perguntas": "\n".join(itens),
    })


# Montagem ---------------------------------------------------------------------

def montar(meta, conteudo, raiz, caminho_saida, extras):
    valores = {
        "raiz": raiz,
        "url": URL_SITE + caminho_saida,
        "titulo_pagina": meta.get("titulo_pagina") or f"{meta['titulo']} | Fernandes &amp; Sá Advocacia",
        "descricao": meta["descricao"],
        "imagem": URL_SITE + meta.get("imagem", "assets/img/compartilhar.webp"),
        "menu": montar_menu(meta.get("menu", ""), raiz),
        "ano": date.today().year,
        **extras,
    }
    valores["capa"] = preencher(parte("capa-pagina"), {**valores, **meta}) if meta.get("capa") else ""
    valores["conteudo"] = preencher(conteudo, valores)
    html = preencher(parte("base"), {**valores, "cabecalho": preencher(parte("cabecalho"), valores),
                                     "rodape": preencher(parte("rodape"), valores)})
    destino = RAIZ / caminho_saida
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(html + "\n", encoding="utf-8")
    print("ok", caminho_saida)


def main():
    artigos = carregar_artigos()
    extras = {"duvidas": secao_duvidas(), "mapa": parte("mapa")}

    for caminho in sorted((FONTE / "paginas").glob("*.html")):
        meta, conteudo = ler_documento(caminho)
        extras["ultimas_noticias"] = lista_artigos(artigos[:3], "")
        extras["todos_artigos"] = lista_artigos(artigos, "")
        montar(meta, conteudo, "", caminho.name, extras)

    modelo_artigo = parte("artigo")
    for artigo in artigos:
        outros = [a for a in artigos if a["slug"] != artigo["slug"]][:2]
        conteudo = preencher(modelo_artigo, {
            **artigo,
            "raiz": "../",
            "data_extenso": data_por_extenso(artigo["data"]),
            "relacionados": lista_artigos(outros, "../"),
        })
        meta = {
            **artigo,
            "menu": "blog",
            "imagem": f"assets/img/blog/{artigo['slug']}.webp",
            "capa": artigo["foto"],
            "sobretitulo": artigo["tema"],
            "chamada": artigo["resumo"],
            "descricao": artigo["resumo"],
        }
        montar(meta, conteudo, "../", f"blog/{artigo['slug']}.html", extras)


if __name__ == "__main__":
    main()
