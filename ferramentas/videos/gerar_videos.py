"""Gera um vídeo curto (e a capa) para cada pergunta frequente.

Requisitos: Python 3 com Pillow e FFmpeg disponível no terminal.
Uso:  python ferramentas/videos/gerar_videos.py [--only slug] [--output-dir pasta]
      [--serif-font arquivo.ttf] [--sans-font arquivo.ttf]
"""
from pathlib import Path
from tempfile import TemporaryDirectory
import argparse
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont, ImageOps

sys.path.insert(0, str(Path(__file__).resolve().parent))
from perguntas import PERGUNTAS, TEMAS  # noqa: E402

ASSETS = Path(__file__).resolve().parents[2] / "assets"
W, H = 1280, 720
VINHO, ROSA, ROSA_CLARO, CREME, FUNDO = "#792930", "#dc9096", "#f0aeb4", "#f7e8e7", "#2b2024"
SERIF_FONTS = ("Gelasio[wght].ttf", "georgia.ttf", "Georgia.ttf", "DejaVuSerif.ttf", "LiberationSerif-Regular.ttf")
SANS_FONTS = ("DMSans[opsz,wght].ttf", "arial.ttf", "Arial.ttf", "DejaVuSans.ttf", "LiberationSans-Regular.ttf")
FADE = 0.6
WHATSAPP = "(69) 99297-8268"
INSTAGRAM = "@fernandesesa.adv"


def find_font(path, candidates, option):
    if path:
        ImageFont.truetype(path, 24)
        return path
    for candidate in candidates:
        try:
            ImageFont.truetype(candidate, 24)
            return candidate
        except OSError:
            continue
    raise SystemExit(f"Fonte indisponível. Informe um arquivo TTF com {option}.")


def font(path, size, weight=None):
    f = ImageFont.truetype(path, size)
    if weight:
        try:
            f.set_variation_by_axes([weight] if "Gelasio" in path else [14, weight])
        except Exception:
            pass
    return f


def wrap(draw, text, fnt, width):
    lines, line = [], ""
    for word in text.split():
        candidate = f"{line} {word}".strip()
        if line and draw.textlength(candidate, font=fnt) > width:
            lines.append(line)
            line = word
        else:
            line = candidate
    lines.append(line)
    return "\n".join(lines)


def text_block(draw, text, xy, fnt, width, fill, spacing):
    value = wrap(draw, text, fnt, width)
    draw.multiline_text(xy, value, font=fnt, fill=fill, spacing=spacing)
    return draw.multiline_textbbox(xy, value, font=fnt, spacing=spacing)[3]


def base(photo):
    image = Image.new("RGB", (W, H), FUNDO)
    crop = ImageOps.fit(Image.open(ASSETS / "img" / photo).convert("RGB"), (516, H), centering=(.58, .5))
    image.paste(Image.blend(crop, Image.new("RGB", crop.size, "#53242d"), .25), (764, 0))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 13, H), fill=VINHO)
    draw.rectangle((64, 64, 128, 69), fill=ROSA)
    return image, draw


def footer(draw, sans, step, total):
    for index in range(total):
        x = 66 + index * 60
        draw.rounded_rectangle((x, 602, x + 44, 608), 3, fill="#eeabb1" if index <= step else "#73535b")
    draw.text((65, 642), "FERNANDES & SÁ  •  ADVOCACIA", font=font(sans, 20, 600), fill=CREME)


def frame_question(item, sans, serif, total):
    tema, photo = TEMAS[item["tema"]]
    image, draw = base(photo)
    draw.text((65, 95), f"PERGUNTA FREQUENTE  ·  {tema.upper()}", font=font(sans, 23, 600), fill=ROSA_CLARO)
    text_block(draw, item["pergunta"], (64, 190), font(serif, 60), 640, "#fefefe", 10)
    footer(draw, sans, 0, total)
    return image


def frame_answer(item, index, title, body, sans, serif, total):
    tema, photo = TEMAS[item["tema"]]
    image, draw = base(photo)
    draw.text((65, 95), f"{index} DE 3  ·  {tema.upper()}", font=font(sans, 23, 600), fill=ROSA_CLARO)
    bottom = text_block(draw, title, (64, 200), font(serif, 60), 650, "#fefefe", 8)
    text_block(draw, body, (68, bottom + 28), font(sans, 31), 629, CREME, 12)
    footer(draw, sans, index, total)
    return image


def frame_contact(item, sans, serif, total):
    tema, photo = TEMAS[item["tema"]]
    image, draw = base(photo)
    draw.text((65, 95), "CADA CASO TEM SUAS PARTICULARIDADES", font=font(sans, 23, 600), fill=ROSA_CLARO)
    bottom = text_block(draw, "Converse com o escritório", (64, 200), font(serif, 60), 650, "#fefefe", 8)
    y = bottom + 40
    for label, value in (("WhatsApp", WHATSAPP), ("Instagram", INSTAGRAM)):
        draw.text((68, y), label.upper(), font=font(sans, 20, 600), fill=ROSA_CLARO)
        draw.text((68, y + 28), value, font=font(sans, 34, 600), fill="#fefefe")
        y += 92
    footer(draw, sans, total - 1, total)
    return image


def render(item, out_dir, sans, serif):
    total = 5
    frames = [frame_question(item, sans, serif, total)]
    frames += [frame_answer(item, i + 1, t, b, sans, serif, total) for i, (t, b) in enumerate(item["telas"])]
    frames.append(frame_contact(item, sans, serif, total))
    durations = [5.5, 9, 9, 9, 6]
    with TemporaryDirectory() as tmp:
        work = Path(tmp)
        args = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y"]
        for i, (img, sec) in enumerate(zip(frames, durations)):
            img.save(work / f"{i}.png")
            args += ["-loop", "1", "-t", str(sec), "-i", str(work / f"{i}.png")]
        chain = [f"[{i}:v]fps=24,format=yuv420p,setsar=1[s{i}]" for i in range(len(frames))]
        prev, offset = "s0", 0.0
        for i in range(1, len(frames)):
            offset += durations[i - 1] - FADE
            out = f"x{i}"
            chain.append(f"[{prev}][s{i}]xfade=transition=fade:duration={FADE}:offset={offset:.2f}[{out}]")
            prev = out
        args += ["-filter_complex", ";".join(chain), "-map", f"[{prev}]",
                 "-c:v", "libx264", "-preset", "veryfast", "-crf", "23", "-pix_fmt", "yuv420p",
                 "-movflags", "+faststart", str(out_dir / f"{item['slug']}.mp4")]
        subprocess.run(args, check=True)
    frames[0].save(out_dir / f"{item['slug']}.webp", quality=82)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--serif-font")
    parser.add_argument("--sans-font")
    parser.add_argument("--output-dir", type=Path, default=ASSETS / "videos")
    parser.add_argument("--only", help="Gera só a pergunta com este slug.")
    args = parser.parse_args()
    serif = find_font(args.serif_font, SERIF_FONTS, "--serif-font")
    sans = find_font(args.sans_font, SANS_FONTS, "--sans-font")
    out_dir = args.output_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    for item in PERGUNTAS:
        if args.only and item["slug"] != args.only:
            continue
        render(item, out_dir, sans, serif)
        print("ok", item["slug"])


if __name__ == "__main__":
    main()
