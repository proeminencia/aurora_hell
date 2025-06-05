def contributions_list():
    from PIL import Image, ImageDraw, ImageFont
    from io import BytesIO
    helvetica = r"fonts/Helvetica.ttf"
    helvetica_bold = r"fonts/Helvetica-Bold.ttf"
    teko_medium = r"fonts/Teko-Medium.ttf"
    image = Image.open(r"backgrounds/contributions_neck.png")
    image_modification = ImageDraw.Draw(image)

    pink_color = (255,20,147)
    white_color = (255, 255, 255)
    gold_color   = (212, 175, 55)
    silver_color  = (169, 169, 169)
    bronze_color = (205, 127, 50)

    contributors = ['Kocho Shinobu', 'Sweet Void', 'Divine Eagle Il']
    value = ['10,000,000', '5,000,000', '2,500,000']

    image_modification.text((20, 20), f"Contributors", font=ImageFont.truetype(teko_medium, 100), fill=pink_color)
    image_modification.text((970, 35), f"Name", font=ImageFont.truetype(teko_medium, 80), fill=pink_color)
    image_modification.text((1600, 35), f"Gold", font=ImageFont.truetype(teko_medium, 80), fill=pink_color)
    image_modification.text((20, 130), f"This is a list of the players who have contributed to", font=ImageFont.truetype(helvetica_bold, 37), fill=white_color)
    image_modification.text((20, 165), f"the project ,if this bot is helpful for you and you", font=ImageFont.truetype(helvetica_bold, 37), fill=white_color)
    image_modification.text((20, 200), f"want to contribute with it, consider contacting me.", font=ImageFont.truetype(helvetica_bold, 37), fill=white_color)
    image_modification.text((20, 235), f"Discord:", font=ImageFont.truetype(helvetica_bold, 37))
    image_modification.text((180, 235), f"@proeminencia", font=ImageFont.truetype(helvetica_bold, 37), fill=(68, 187, 255))

    y = 160

    for index in range(len(contributors)):
        if index == 0:
            color = gold_color
            text_font = ImageFont.truetype(helvetica_bold, 30)
        elif index == 1:
            color = silver_color
            text_font = ImageFont.truetype(helvetica_bold, 30)
        elif index == 2:
            color = bronze_color
            text_font = ImageFont.truetype(helvetica_bold, 30)
        else:
            color = white_color
            text_font = ImageFont.truetype(helvetica, 30)

        image_modification.text((970,y), f"{contributors[index]}", font=text_font, fill=color)
        image_modification.text((1600,y), f"{value[index]}", font=text_font, fill=color)

        y += 35

    buffer = BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer
