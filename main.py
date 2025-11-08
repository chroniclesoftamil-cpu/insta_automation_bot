from PIL import Image, ImageEnhance, ImageDraw, ImageFont

template = Image.open("template.png").convert("RGBA")
news_img = Image.open("sample_news.jpg").resize((1080, 600)).convert("RGBA")

# Slight dark overlay to make text pop
overlay = Image.new("RGBA", news_img.size, (0, 0, 0, 100))
news_img = Image.alpha_composite(news_img, overlay)

template.paste(news_img, (0, 200), news_img)

# Add text now
draw = ImageDraw.Draw(template)
font = ImageFont.truetype("arial.ttf", 40)
draw.text((50, 900), "AI Revolution: The Next Wave", fill="white", font=font)

template.save("output.png")
