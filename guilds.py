def show_members(guildname:str):
    from bs4 import BeautifulSoup
    import requests
    from PIL import Image, ImageDraw, ImageFont
    from io import BytesIO
    from datetime import datetime
    from math import ceil

    default_guildname = guildname.strip().title()
    guildname = guildname.strip().title().replace(" ", "%20")

    page = requests.get(f"https://www.rucoyonline.com/guild/{guildname}")
    page_data = BeautifulSoup(page.text, 'html.parser')
    player_table = page_data.find_all("table", class_="table table-bordered")
    guild_data_table = page_data.find_all("div", class_="guild-box")

    if not player_table:
        return 0, [] 

    player_name = []
    level = []
    join_date = []
    status = [] #Offline or Online
    leader = []
    today_date = datetime.now().replace(microsecond=0)

    for div in guild_data_table:
        lines = div.find_all('p') 
        for line in lines:
            creation_date_string = line.find('i')
            if creation_date_string:
                creation_date = creation_date_string.get_text(strip=True)


    for div in player_table:
        lines = div.find_all('tr')[1:]  # Ignora o cabeçalho
    for tag in div.find_all('span', class_='label flat label-primary'):
        tag.decompose()
    for line in lines:
        columns = line.find_all('td')
        leader.append(columns[0].get_text(strip=True))
        for members in leader:
            if "(Leader)" in members:
                leader_string = str(members)
        columns = line.find_all('td')
        if line.find("span", class_="label flat label-success"):
            status.append("online")
        else:
            status.append("offline")
        if len(columns) >= 1:
            link = columns[0].find("a")
            if link:
                player_name.append(link.get_text(strip=True))
                level.append(columns[1].get_text(strip=True))
                join_date.append(columns[2].get_text(strip=True))

    pos_parentesis = leader_string.find('(')
    leader = leader_string[:pos_parentesis]

    helvetica = r"fonts/Helvetica.ttf"
    teko_medium = r"fonts/Teko-Medium.ttf"

    white_color = (255,255,255)
    cyan_color = (61, 204, 212)

    final_images = []

    online_icon = Image.open(r"backgrounds/sprites/online.png")
    offline_icon = Image.open(r"backgrounds/sprites/offline.png")

    for index in range(ceil(len(player_name) / 25)):
        y = 160
        image = Image.open(r"backgrounds/guilds_background.png")
        image_modification = ImageDraw.Draw(image)
        image_modification.text((30, 300), f"{default_guildname}", font=ImageFont.truetype(teko_medium, 80))
        image_modification.text((30, 370), f"{creation_date}", font=ImageFont.truetype(teko_medium, 60))
        x = 30

        for text, color in [("Leader ", cyan_color), (f"{leader}", white_color)]:
            image_modification.text((x , 420), text, font=ImageFont.truetype(teko_medium, 60), fill=color)
            text_width = image_modification.textlength(text, font=ImageFont.truetype(teko_medium, 60))
            x += text_width

        image_modification.text((30, 470), f"List of Members ({len(player_name)})", font=ImageFont.truetype(teko_medium, 60), fill=cyan_color)
        image_modification.text((1000, 35), f"Name", font=ImageFont.truetype(teko_medium, 80), fill=cyan_color)
        image_modification.text((1362, 35), f"Level", font=ImageFont.truetype(teko_medium, 80), fill=cyan_color)
        image_modification.text((1630, 35), f"Join date", font=ImageFont.truetype(teko_medium, 80), fill=cyan_color)
        image_modification.text((35, 1000), f"Generated at {today_date}", font=ImageFont.truetype(helvetica, 25))

        image.paste(online_icon, (35, 950))
        image.paste(offline_icon, (35, 975))

        image_modification.text((63, 947), f"= Online", font=ImageFont.truetype(helvetica, 25))
        image_modification.text((63, 972), f"= Offline", font=ImageFont.truetype(helvetica, 25))
        
        
        start = index * 25
        end = min(start + 25, len(player_name))
        
        for index in range(start, end):
            if status[index] == "online":
                image.paste(online_icon, (970, y+3))
            else:
                image.paste(offline_icon, (970, y+3))
            image_modification.text((1000, y), player_name[index], font=ImageFont.truetype(helvetica, 30))
            image_modification.text((1400, y), level[index], font=ImageFont.truetype(helvetica, 30))
            image_modification.text((1660, y), join_date[index], font=ImageFont.truetype(helvetica, 30))
            y += 35

        buffer = BytesIO()
        image.save(buffer, format="PNG")
        buffer.seek(0)
        final_images.append(buffer)
    return 1, final_images

def show_online(guildname:str):
    from bs4 import BeautifulSoup
    import requests
    from PIL import Image, ImageDraw, ImageFont
    from io import BytesIO
    from datetime import datetime
    from math import ceil

    default_guildname = guildname.strip().title()
    guildname = guildname.strip().title().replace(" ", "%20")

    page = requests.get(f"https://www.rucoyonline.com/guild/{guildname}")
    page_data = BeautifulSoup(page.text, 'html.parser')
    player_table = page_data.find_all("table", class_="table table-bordered")
    guild_data_table = page_data.find_all("div", class_="guild-box")
    

    if not player_table:
        return 0, [] 

    player_name = []
    level = []
    join_date = []
    leader = []
    today_date = datetime.now().replace(microsecond=0)

    for div in guild_data_table:
        lines = div.find_all('p') 
        for line in lines:
            creation_date_string = line.find('i')
            if creation_date_string:
                creation_date = creation_date_string.get_text(strip=True)

    for div in player_table:
        lines = div.find_all('tr')[1:]  # Ignora o cabeçalho
        for tag in div.find_all('span', class_='label flat label-primary'):
            tag.decompose()
        for line in lines:
            columns = line.find_all('td')
            leader.append(columns[0].get_text(strip=True))
            for members in leader:
                if "(Leader)" in members:
                    leader_string = str(members)
            if line.find("span", class_="label flat label-success"):  # Somente se estiver online
                columns = line.find_all('td')
                if len(columns) >= 1:
                    link = columns[0].find("a")
                    if link:
                        player_name.append(link.get_text(strip=True))
                        level.append(columns[1].get_text(strip=True))
                        join_date.append(columns[2].get_text(strip=True))
    
    pos_parenthesis = leader_string.find('(')
    leader = leader_string[:pos_parenthesis]

    if len(player_name) == 0:
        return 1, []

    helvetica = r"fonts/Helvetica.ttf"
    teko_medium = r"fonts/Teko-Medium.ttf"

    white_color = (255,255,255)
    cyan_color = (61, 204, 212)

    final_images = []
    online_icon = Image.open(r"backgrounds/sprites/online.png").convert("RGBA")

    for index in range(ceil(len(player_name) / 25)):
        y = 160
        image = Image.open(r"backgrounds/guilds_background.png")
        image_modification = ImageDraw.Draw(image)
        image_modification.text((30, 300), f"{default_guildname}", font=ImageFont.truetype(teko_medium, 80))
        image_modification.text((30, 370), f"{creation_date}", font=ImageFont.truetype(teko_medium, 60))

        x = 30

        for text, color in [("Leader ", cyan_color), (f"{leader}", white_color)]:
            image_modification.text((x, 420), text, font=ImageFont.truetype(teko_medium, 60), fill=color)
            text_width = image_modification.textlength(text, font=ImageFont.truetype(teko_medium, 60))
            x += text_width
        image_modification.text((30, 470), f"List of Online Members ({len(player_name)})", font=ImageFont.truetype(teko_medium, 60), fill=cyan_color)

        image_modification.text((1000, 35), f"Name", font=ImageFont.truetype(teko_medium, 80), fill=cyan_color)
        image_modification.text((1362, 35), f"Level", font=ImageFont.truetype(teko_medium, 80), fill=cyan_color)
        image_modification.text((1630, 35), f"Join date", font=ImageFont.truetype(teko_medium, 80), fill=cyan_color)
        image_modification.text((35, 1000), f"Generated at {today_date}", font=ImageFont.truetype(helvetica, 25))
        image.paste(online_icon, (35, 975))
        image_modification.text((63, 972), f"= Online", font=ImageFont.truetype(helvetica, 25))
        
        start = index * 25
        end = min(start + 25, len(player_name))
        
        for index in range(start, end):
            image.paste(online_icon, (970, y+3))
            image_modification.text((1000, y),player_name[index], font=ImageFont.truetype(helvetica , 30), fill=white_color)
            image_modification.text((1400, y), level[index], font=ImageFont.truetype(helvetica , 30), fill=white_color)
            image_modification.text((1660, y), join_date[index], font=ImageFont.truetype(helvetica , 30), fill=white_color)
            y += 35

        buffer = BytesIO()
        image.save(buffer, format="PNG")
        buffer.seek(0)
        final_images.append(buffer)
    return 2, final_images
