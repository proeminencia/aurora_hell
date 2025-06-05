def contributions_list():
    from PIL import Image, ImageDraw, ImageFont
    from io import BytesIO
    helvetica = r"fonts/Helvetica.ttf"
    helvetica_bold = r"fonts/Helvetica-Bold.ttf"
    teko_medium = r"fonts/Teko-Medium.ttf"

    image = Image.open(r"backgrounds/contruibutions_background.png")
    image_modification = ImageDraw.Draw(image)

    pink_color = (255,20,147)
    white_color = (255, 255, 255)
    gold_color   = (212, 175, 55)
    silver_color  = (169, 169, 169)
    bronze_color = (205, 127, 50)

    contributors = ['Kocho Shinobu', 'Sweet Void', 'Divine Eagle Il']
    value = ['10,000,000', '5,000,000', '2,500,000']

    discord_icon = Image.open(r"backgrounds/sprites/discord_icon.png")

    image_modification.text((326, 20), "About the project", font=ImageFont.truetype(teko_medium, 100), fill=pink_color)
    image_modification.text((1345, 20), "Contributors", font=ImageFont.truetype(teko_medium, 100), fill=pink_color)
    image_modification.text((1220, 151), "Name", font=ImageFont.truetype(teko_medium, 80), fill=pink_color)
    image_modification.text((1680, 151), "Gold", font=ImageFont.truetype(teko_medium, 80), fill=pink_color)
    image_modification.text((50, 170), "Hello! Thank you for being a part of this project, I hope that my Discord bot is ", font=ImageFont.truetype(helvetica_bold, 30), fill=white_color)
    image_modification.text((50, 205), "being useful to you. I started this project in May 2025, inspired by the 'Biridim'", font=ImageFont.truetype(helvetica_bold, 30), fill=white_color)
    image_modification.text((50, 240), "bot, and since then I’ve been dedicating a good part of my free time to it. This", font=ImageFont.truetype(helvetica_bold, 30), fill=white_color)
    image_modification.text((50, 275), "project has been a great learning experience for me, and I plan to bring even", font=ImageFont.truetype(helvetica_bold, 30))
    image_modification.text((50, 310), "more useful features in the future. However some of them require more lear-", font=ImageFont.truetype(helvetica_bold, 30))
    image_modification.text((50, 345), "ing and time on my part — but I’m working on it!", font=ImageFont.truetype(helvetica_bold, 30))

    image_modification.text((50, 415), "Some graphics used in this project are not my own. All rights belong to their", font=ImageFont.truetype(helvetica_bold, 30))
    image_modification.text((50, 450), "respective creators.", font=ImageFont.truetype(helvetica_bold, 30))


    image_modification.text((50, 520), "On the right, you’ll see a list of contributors to this project. I’d like to sincerely", font=ImageFont.truetype(helvetica_bold, 30))
    image_modification.text((50, 555), "thank them and the people who actively give me feedback for their support ", font=ImageFont.truetype(helvetica_bold, 30))
    image_modification.text((50, 590), "and for motivating me to keep working on it. If you find this bot helpful and ", font=ImageFont.truetype(helvetica_bold, 30))
    image_modification.text((50, 625), "would like to contribute, feel free to contact me on Discord.", font=ImageFont.truetype(helvetica_bold, 30))
    image_modification.text((128, 685), "@proeminencia", font=ImageFont.truetype(helvetica_bold, 30))
    image.paste(discord_icon, (50, 665))

    y = 151+125

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

        image_modification.text((1220, y), f"{contributors[index]}", font=text_font, fill=color)
        image_modification.text((1680, y), f"{value[index]}", font=text_font, fill=color)

        y += 35
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer