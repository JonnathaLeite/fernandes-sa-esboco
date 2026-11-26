# Fernandes & Sá Advocacia

Site institucional do escritório Fernandes & Sá Advocacia (Direito Previdenciário, Ji-Paraná/RO).

Site estático em HTML, CSS e JavaScript puro, sem framework e sem dependências em produção. As páginas são montadas por um gerador simples em Python (só biblioteca padrão), para que o cabeçalho, o rodapé e os componentes repetidos fiquem em um único lugar.

**Prévia:** <https://jonnathaleite.github.io/fernandes-sa-esboco/>

## Estrutura

```
.
├── fonte/                    ← edite aqui
│   ├── partes/               Layout base, cabeçalho, rodapé e componentes
│   ├── paginas/              Conteúdo de cada página (Home, Serviços, Contato…)
│   └── blog/                 Artigos do blog
├── ferramentas/
│   ├── site/construir.py     Monta as páginas a partir de fonte/
│   ├── site/gerar_capas.py   Gera as capas dos artigos e a imagem de compartilhamento
│   └── videos/               Perguntas frequentes e gerador dos vídeos
├── assets/
│   ├── css/estilo.css        Estilos, organizados por seção (índice no topo do arquivo)
│   ├── js/                   menu.js · duvidas.js · atendimento.js
│   ├── img/                  Logo, fotos, equipe e capas do blog
│   ├── fontes/               DM Sans e Gelasio (WOFF2, licença OFL)
│   └── videos/               Vídeos das dúvidas frequentes
├── index.html, servicos.html, profissionais.html, duvidas.html,
├── blog.html, contato.html, privacidade.html, cookies.html
└── blog/                     ← páginas geradas (não edite à mão)
```

## Rodar localmente

```sh
python -m http.server 8000
```

Abra <http://localhost:8000>. No VS Code, a extensão **Live Server** faz o mesmo com um clique em "Go Live".

## Fluxo de edição

1. Edite os arquivos em `fonte/` (ou as perguntas em `ferramentas/videos/perguntas.py`).
2. Monte o site: `python ferramentas/site/construir.py`
3. Confira localmente e publique.

Os `.html` da raiz e da pasta `blog/` são gerados pelo passo 2: alterações feitas direto neles se perdem na próxima montagem.

### Publicar um novo artigo

1. Crie `fonte/blog/nome-do-artigo.html` copiando um artigo existente e ajuste os metadados do topo (`titulo`, `resumo`, `titulo_capa`, `tema`, `data`, `autor`, `leitura`, `foto`).
2. Gere a capa e monte o site:

   ```sh
   python -m pip install Pillow
   python ferramentas/site/gerar_capas.py
   python ferramentas/site/construir.py
   ```

O artigo aparece automaticamente no Blog e, se estiver entre os três mais recentes, em "Últimas notícias" na Home.

### Vídeos das dúvidas frequentes

As perguntas ficam em `ferramentas/videos/perguntas.py`, que alimenta tanto os vídeos quanto a página `duvidas.html`. Requisitos: Python 3, Pillow e FFmpeg.

```sh
python ferramentas/videos/gerar_videos.py              # todos os vídeos
python ferramentas/videos/gerar_videos.py --only bpc   # apenas um
python ferramentas/site/construir.py                   # atualiza a página
```

Para usar vídeos gravados pelos advogados, basta manter o mesmo nome de arquivo em `assets/videos/`.

## Onde mudar o quê

| O que mudar                     | Onde                                            |
| ------------------------------- | ----------------------------------------------- |
| Menu                            | Lista `MENU` em `ferramentas/site/construir.py` |
| Cabeçalho e rodapé              | `fonte/partes/cabecalho.html` e `rodape.html`   |
| Cores, fontes e espaçamentos    | Variáveis no início de `assets/css/estilo.css`  |
| Horário do aviso aberto/fechado | Constantes `ABRE` e `FECHA` em `atendimento.js` |
| Fotos dos advogados             | `assets/img/equipe/` (proporção 4:5)            |

## Padrões do projeto

- Formatação com [Prettier](https://prettier.io) (`.prettierrc`) e [EditorConfig](https://editorconfig.org).
- Nenhum serviço de terceiros carregado por padrão, exceto o mapa do Google na página de contato.
- Acessibilidade: navegação por teclado, foco visível, textos alternativos e `prefers-reduced-motion`.
- Conteúdo dentro das regras de publicidade da OAB (Provimento nº 205/2021): informativo, sem promessa de resultado.

## Publicação

Qualquer hospedagem estática serve (GitHub Pages, Netlify, Vercel, Hostinger etc.): publique a raiz do repositório. As pastas `fonte/` e `ferramentas/` não são necessárias em produção. Ao trocar de hospedagem, atualize a seção 6 de `fonte/paginas/privacidade.html` e a constante `URL_SITE` em `construir.py`.

## Pendências antes da versão final

- [ ] Razão social, CNPJ e encarregado (LGPD) na política de privacidade.
- [ ] Apresentação profissional e fotos oficiais dos advogados.
- [ ] Revisão jurídica das políticas, das respostas em vídeo e dos artigos do blog.

---

Desenvolvido por JL Tecnologia.
