"""Gera as capas dos artigos do blog e a imagem de compartilhamento do site.

As capas usam o campo `titulo_capa` de cada artigo em `fonte/blog/`. O trecho
entre asteriscos é destacado em dourado: `*Pente-fino* do INSS`.

Requisitos: Python 3 com Pillow.
Uso:  python ferramentas/site/gerar_capas.py [--serif-font arq.ttf] [--sans-font arq.ttf]
"""
from pathlib import Path
import argparse
import re
import sys

from PIL import Image, ImageDraw, ImageFont, ImageOps

sys.path.insert(0, str(Path(__file__).resolve().parent))
from construir import FONTE, RAIZ, ler_documento  # noqa: E402

IMG = RAIZ / "assets" / "img"
W, H = 1200, 675
FUNDO, VINHO, DOURADO, CREME = "#2b2024", "#792930", "#d9b77e", "#f7e8e7"
SERIF = ("Gelasio[wght].ttf", "georgia.ttf", "Georgia.ttf", "DejaVuSerif.ttf")
SANS = ("DMSans[opsz,wght].ttf", "arial.ttf", "Arial.ttf", "DejaVuSans.ttf")


def achar_fonte(caminho, candidatas, opcao):
    for candidata in ([caminho] if caminho else candidatas):
        try:
            ImageFont.truetype(candidata, 20)
            return candidata
        except OSError:
            continue
    raise SystemExit(f"Fonte indisponível. Informe um arquivo TTF com {opcao}.")


def quebrar_em_linhas(draw, palavras, fonte, largura):
    """Agrupa (palavra, destaque) em linhas que cabem na largura."""
    linhas, atual = [], []
    for palavra in palavras:
        teste = " ".join(p for p, _ in atual + [palavra])
        if atual and draw.textlength(teste, font=fonte) > largura:
            linhas.append(atual)
            atual = [palavra]
        else:
            atual.append(palavra)
    linhas.append(atual)
    return linhas


def palavras_com_destaque(titulo):
    resultado = []
    for i, trecho in enumerate(re.split(r"\*", titulo)):
        resultado += [(p, i % 2 == 1) for p in trecho.split()]
    return resultado


def desenhar(titulo, rotulo, foto, serif, sans, tamanho=(W, H)):
    largura, altura = tamanho
    imagem = Image.new("RGB", tamanho, FUNDO)
    lado = int(largura * 0.42)
    recorte = ImageOps.fit(Image.open(IMG / foto).convert("RGB"), (lado, altura), centering=(0.6, 0.5))
    imagem.paste(Image.blend(recorte, Image.new("RGB", recorte.size, "#53242d"), 0.3), (largura - lado, 0))
    draw = ImageDraw.Draw(imagem)
    draw.rectangle((0, 0, 12, altura), fill=VINHO)

    pequena = ImageFont.truetype(sans, 22)
    pequena.set_variation_by_axes([14, 600])
    draw.text((64, 56), "@fernandesesa.adv", font=pequena, fill=CREME)
    draw.text((64, 120), rotulo.upper(), font=pequena, fill=DOURADO)

    grande = ImageFont.truetype(serif, 66)
    y = 170
    for linha in quebrar_em_linhas(draw, palavras_com_destaque(titulo), grande, largura - lado - 120):
        x = 64
        for palavra, destaque in linha:
            draw.text((x, y), palavra, font=grande, fill=DOURADO if destaque else "#fefefe")
            x += draw.textlength(palavra + " ", font=grande)
        y += 80

    draw.rectangle((64, altura - 110, 120, altura - 106), fill=DOURADO)
    draw.text((64, altura - 86), "FERNANDES & SÁ  •  ADVOCACIA", font=pequena, fill=CREME)
    return imagem


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--serif-font")
    parser.add_argument("--sans-font")
    args = parser.parse_args()
    serif = achar_fonte(args.serif_font, SERIF, "--serif-font")
    sans = achar_fonte(args.sans_font, SANS, "--sans-font")

    destino = IMG / "blog"
    destino.mkdir(parents=True, exist_ok=True)
    for caminho in sorted((FONTE / "blog").glob("*.html")):
        meta, _ = ler_documento(caminho)
        capa = desenhar(meta["titulo_capa"], f"Artigo · {meta['tema']}", meta["foto"], serif, sans)
        capa.save(destino / f"{caminho.stem}.webp", quality=84)
        print("ok", caminho.stem)

    compartilhar = desenhar("Direito *Previdenciário* em Ji-Paraná", "Fernandes & Sá Advocacia",
                            "arquitetura.webp", serif, sans, (1200, 630))
    compartilhar.save(IMG / "compartilhar.webp", quality=84)
    print("ok compartilhar")


if __name__ == "__main__":
    main()
