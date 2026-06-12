from PIL import Image, ImageDraw, ImageFont
import os


def make_frame(title: str, goal: str, sections: list, highlight: int) -> Image.Image:
    W, H = 900, 600
    bg = Image.new("RGB", (W, H), color=(250, 250, 250))
    d = ImageDraw.Draw(bg)

    # Fonts
    try:
        header_font = ImageFont.truetype("arial.ttf", 36)
        title_font = ImageFont.truetype("arial.ttf", 20)
        mono = ImageFont.truetype("arial.ttf", 16)
    except Exception:
        header_font = ImageFont.load_default()
        title_font = ImageFont.load_default()
        mono = ImageFont.load_default()

    # Header
    d.rectangle([0, 0, W, 80], fill=(30, 30, 30))
    d.text((24, 18), title, font=header_font, fill=(255, 255, 255))

    # Goal box
    d.rectangle([24, 110, W - 24, 190], outline=(200, 200, 200), width=2, fill=(255, 255, 255))
    d.text((36, 122), "Goal:", font=title_font, fill=(50, 50, 50))
    d.text((36, 145), goal, font=mono, fill=(80, 80, 80))

    # Sections
    y = 220
    for i, sec in enumerate(sections):
        y0 = y + i * 80
        # highlight the active/visible section
        if i == highlight:
            fill = (240, 250, 255)
            outline = (100, 160, 220)
        else:
            fill = (245, 245, 245)
            outline = (220, 220, 220)

        d.rectangle([36, y0, W - 36, y0 + 64], fill=fill, outline=outline)
        d.text((52, y0 + 12), sec[0], font=title_font, fill=(20, 20, 20))
        d.text((52, y0 + 36), sec[1], font=mono, fill=(80, 80, 80))

    return bg


def main():
    out_dir = os.path.join(os.path.dirname(__file__), "..", "screenshots")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.abspath(os.path.join(out_dir, "agentic_demo.gif"))

    title = "Agentic Coach"
    goal = "Build a small Streamlit demo to showcase a learning roadmap"
    sections = [
        ("Learning Roadmap", "5 beginner-friendly steps"),
        ("Recommended Resources", "Curated links and guides"),
        ("Creative Project Ideas", "3 project prompts"),
        ("Documentation Suggestions", "README & architecture sections"),
    ]

    frames = []
    # show intro frame, then highlight each section
    frames.append(make_frame(title, goal, sections, highlight=-1))
    for i in range(len(sections)):
        frames.append(make_frame(title, goal, sections, highlight=i))

    # Save as animated GIF
    frames[0].save(
        out_path,
        save_all=True,
        append_images=frames[1:],
        duration=900,
        loop=0,
        optimize=True,
    )

    print(f"Wrote GIF to: {out_path}")


if __name__ == "__main__":
    main()
