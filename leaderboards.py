def show_leaderboard(leaderboard:int):
    from bs4 import BeautifulSoup
    import requests
    from PIL import Image, ImageDraw, ImageFont
    from io import BytesIO
    from datetime import datetime

    rank_names = ['Experience', 'Melee', 'Distance', 'Magic', 'Defense']

    helvetica = r"fonts/Helvetica.ttf"
    helvetica_bold = r"fonts/Helvetica-Bold.ttf"

    teko_medium = r"fonts/Teko-Medium.ttf"

    gold_color   = (212, 175, 55)
    silver_color  = (169, 169, 169)
    bronze_color = (205, 127, 50)
    white_color = (255, 255, 255)
    classes_colors = [(255, 215, 0), (68, 187, 255), (87, 242, 73), (224, 100, 245), (202, 204, 202)]

    if leaderboard == 0:
        page = requests.get(f'https://www.rucoyonline.com/highscores/{rank_names[leaderboard].lower()}/2016/1')
        page_data = BeautifulSoup(page.text, 'html.parser')
        rank = []
        name = []
        level = []
        exp = []

        today_date = datetime.now().replace(microsecond=0)

        rank_table = page_data.find_all('table', class_='table table-striped table-highscores table-bordered')

        for div in rank_table:
            lines = div.find_all('tr')[1:]
            for tag in div.find_all('span', class_='label flat label-success'):
                tag.decompose()
            for line in lines:
                columns = line.find_all('td')
                if len(columns) >= 3:
                    rank.append(columns[0].get_text(strip=True))
                    name.append(columns[1].get_text(strip=True))
                    level.append(columns[2].get_text(strip=True))
                    exp.append(columns[3].get_text(strip=True))

        final_images = []

        start = 0
        end = 25

        for pages in range(4):
            if pages == 0:
                image = Image.open(r"backgrounds/exp_lb_background1.png")
            else:
                image = Image.open(r"backgrounds/exp_lb_background2.png")
            image_modification = ImageDraw.Draw(image)
            y = 160
            for index in range (start, end):
                text = str(rank[index])
                if index == 0:
                    color = gold_color
                    font = ImageFont.truetype(helvetica_bold, 30)
                elif index == 1:
                    color = silver_color
                    font = ImageFont.truetype(helvetica_bold, 30)
                elif index == 2:
                    color = bronze_color
                    font = ImageFont.truetype(helvetica_bold, 30)
                else:
                    color = white_color
                    font = ImageFont.truetype(helvetica, 30) 
                image_modification.text((720, y), text, font=font, fill=color)
                y += 35
            y = 160
            for index in range (start, end):
                text = str(name[index])
                if index == 0:
                    color = gold_color
                    font = ImageFont.truetype(helvetica_bold, 30)
                elif index == 1:
                    color = silver_color
                    font = ImageFont.truetype(helvetica_bold, 30)
                elif index == 2:
                    color = bronze_color
                    font = ImageFont.truetype(helvetica_bold, 30)
                else:
                    color = white_color
                    font = ImageFont.truetype(helvetica , 30)               
                image_modification.text((970, y), text, font=font, fill=color)
                y += 35
            y = 160
            for index in range (start, end):
                text = str(level[index])
                if index == 0:
                    color = gold_color
                    font = ImageFont.truetype(helvetica_bold, 30)
                elif index == 1:
                    color = silver_color
                    font = ImageFont.truetype(helvetica_bold, 30)
                elif index == 2:
                    color = bronze_color
                    font = ImageFont.truetype(helvetica_bold, 30)
                else:
                    color = white_color
                    font = ImageFont.truetype(helvetica, 30)
                image_modification.text((1400, y), text, font=font, fill=color)
                y += 35
            y = 160
            for index in range (start, end):
                text = str(exp[index])
                if index == 0:
                    color = gold_color
                    font = ImageFont.truetype(helvetica_bold, 30)
                elif index == 1:
                    color = silver_color
                    font = ImageFont.truetype(helvetica_bold, 30)
                elif index == 2:
                    color = bronze_color
                    font = ImageFont.truetype(helvetica_bold, 30)
                else:
                    color = white_color
                    font = ImageFont.truetype(helvetica, 30)
                image_modification.text((1610, y), text, font=font, fill=color)
                y += 35
            
            image_modification.text((720, 35), f"Rank", font=ImageFont.truetype(teko_medium, 80), fill=classes_colors[leaderboard])
            image_modification.text((975, 35), f"Name", font=ImageFont.truetype(teko_medium, 80), fill=classes_colors[leaderboard])
            image_modification.text((1365, 35), f"Level", font=ImageFont.truetype(teko_medium, 80), fill=classes_colors[leaderboard])
            image_modification.text((1585, 35), f"Experience", font=ImageFont.truetype(teko_medium, 80), fill=classes_colors[leaderboard])
            
            image_modification.text((40, 350), "Experience Leaderboard", font=ImageFont.truetype(teko_medium, 80), fill=classes_colors[leaderboard])
            image_modification.text((35, 1000), f"Generated at {today_date}", font=ImageFont.truetype(helvetica, 25))

            start += 25
            end += 25

            buffer = BytesIO()
            image.save(buffer, format="PNG")
            buffer.seek(0)
            final_images.append(buffer)
        return final_images
    
    
    else:
        page = requests.get(f'https://www.rucoyonline.com/highscores/{rank_names[leaderboard].lower()}/2016/1')
        page_data = BeautifulSoup(page.text, 'html.parser')

        rank = []
        name = []
        stat = []

        backgrounds_1 = [None, r"backgrounds/melee_lb_background1.png", r"backgrounds/dist_lb_background1.png", r"backgrounds/mage_lb_background1.png",r"backgrounds/def_lb_background1.png"]
        backgrounds_2 = [None, r"backgrounds/melee_lb_background2.png", r"backgrounds/dist_lb_background2.png", r"backgrounds/mage_lb_background2.png",r"backgrounds/def_lb_background2.png"]

        today_date = datetime.now().replace(microsecond=0)
        rank_table = page_data.find_all('table', class_='table table-striped table-highscores table-bordered')

        for div in rank_table:
            lines = div.find_all('tr')[1:]
            for tag in div.find_all('span', class_='label flat label-success'):
                tag.decompose()
            for line in lines:
                columns = line.find_all('td')
                if len(columns) >= 3:
                    rank.append(columns[0].get_text(strip=True))
                    name.append(columns[1].get_text(strip=True))
                    stat.append(columns[2].get_text(strip=True))

        final_images = []

        x_header = [0, 170, 125, 170, 135]

        start = 0
        end = 25
        
        for pages in range(4):
            if pages == 0:
                image = Image.open(backgrounds_1[leaderboard])
            else:
                image = Image.open(backgrounds_2[leaderboard])
            image_modification = ImageDraw.Draw(image)
            y = 160
            for index in range (start, end):
                text = str(rank[index])
                if index == 0:
                    color = gold_color
                    font = ImageFont.truetype(helvetica_bold, 30)
                elif index == 1:
                    color = silver_color
                    font = ImageFont.truetype(helvetica_bold, 30)
                elif index == 2:
                    color = bronze_color
                    font = ImageFont.truetype(helvetica_bold, 30)
                else:
                    color = white_color
                    font = ImageFont.truetype(helvetica, 30)
                image_modification.text((970, y), text, font=font, fill=color)
                y += 35
            y = 160
            for index in range (start, end):
                text = str(name[index])
                if index == 0:
                    color = gold_color
                    font = ImageFont.truetype(helvetica_bold, 30)
                elif index == 1:
                    color = silver_color
                    font = ImageFont.truetype(helvetica_bold, 30)
                elif index == 2:
                    color = bronze_color
                    font = ImageFont.truetype(helvetica_bold, 30)
                else:
                    color = white_color
                    font = ImageFont.truetype(helvetica, 30)
                image_modification.text((1200, y), text, font=font, fill=color)
                y += 35
            y = 160
            for index in range (start, end):
                text = str(stat[index])
                if index == 0:
                    color = gold_color
                    font = ImageFont.truetype(helvetica_bold, 30)
                elif index == 1:
                    color = silver_color
                    font = ImageFont.truetype(helvetica_bold, 30)
                elif index == 2:
                    color = bronze_color
                    font = ImageFont.truetype(helvetica_bold, 30)
                else:
                    color = white_color
                    font = ImageFont.truetype(helvetica, 30)
                image_modification.text((1800, y), text, font=font, fill=color)
                y += 35

            image_modification.text((970, 35), f"Rank", font=ImageFont.truetype(teko_medium, 80), fill=classes_colors[leaderboard])
            image_modification.text((1200, 35), f"Name", font=ImageFont.truetype(teko_medium, 80), fill=classes_colors[leaderboard])
            image_modification.text((1770, 35), f"Stat", font=ImageFont.truetype(teko_medium, 80), fill=classes_colors[leaderboard])
            image_modification.text((x_header[leaderboard], 350), f"{rank_names[leaderboard]} Leaderboard", font=ImageFont.truetype(teko_medium, 100), fill=classes_colors[leaderboard])
            image_modification.text((35, 1000), f"Generated at {today_date}", font=ImageFont.truetype(helvetica, 25))

            start += 25
            end += 25

            buffer = BytesIO()
            image.save(buffer, format="PNG")
            buffer.seek(0)
            final_images.append(buffer)
        return final_images
