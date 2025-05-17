def show_leaderboard(leaderboard):
    from bs4 import BeautifulSoup
    import requests
    from PIL import Image, ImageDraw, ImageFont
    from io import BytesIO
    from datetime import datetime

    rank_names = ['Experience', 'Melee', 'Distance', 'Magic', 'Defense']
    background_paths = [r'backgrounds\exp_lb_background.png', r'backgrounds\melee_lb_background.png', r'backgrounds\dist_lb_background.png', r'backgrounds\mage_lb_background.png', r'backgrounds\def_lb_background.png']
    fonte_arial = "fonts/arialbd.ttf"

    if leaderboard == 0:
        pagina = requests.get(f'https://www.rucoyonline.com/highscores/{rank_names[leaderboard].lower()}/2016/1')
        dados_pagina = BeautifulSoup(pagina.text, 'html.parser')
        rank = []
        nome = []
        level = []
        exp = []
        agora = datetime.now().replace(microsecond=0)
        # Encontra todas as tabelas com a classe específica
        ranks_exp = dados_pagina.find_all('table', class_='table table-striped table-highscores table-bordered')

        # Itera nas tabelas encontradas
        for div in ranks_exp:
            linhas = div.find_all('tr')[1:]  # Ignora o cabeçalho
            for tag in div.find_all('span', class_='label flat label-success'):
                tag.decompose()
            for linha in linhas:
                colunas = linha.find_all('td')
                if len(colunas) >= 3:
                    rank.append(colunas[0].get_text(strip=True))
                    nome.append(colunas[1].get_text(strip=True))
                    level.append(colunas[2].get_text(strip=True))
                    exp.append(colunas[3].get_text(strip=True))
        imagem_original = Image.open(background_paths[leaderboard])  # substitua pelo nome da sua imagem
        imagem1 = imagem_original.copy()
        imagem2 = imagem_original.copy()
        imagem3 = imagem_original.copy()
        imagem4 = imagem_original.copy()

        imagens = [imagem1, imagem2, imagem3, imagem4]
        imagens_prontas = []

        y = 10
        try:
            fonte = ImageFont.truetype(fonte_arial , 35)
        except:
            fonte = ImageFont.load_default()

        ouro   = (212, 175, 55)
        prata  = (169, 169, 169)
        bronze = (205, 127, 50)
        branco = (255, 255, 255)

        inicio = 0
        fim = 25

        for z in range(4):
            desenhando = ImageDraw.Draw(imagens[z])
            y = 35
            for a in range (inicio, fim):
                texto = str(rank[a])
                if a == 0:
                    cor = ouro
                elif a == 1:
                    cor = prata
                elif a == 2:
                    cor = bronze
                else:
                    cor = branco
                posicao = (900, y)
                y += 40
                desenhando.text(posicao, texto, font=fonte, fill=cor)
            y = 35
            for b in range (inicio, fim):
                texto = str(nome[b])
                if b == 0:
                    cor = ouro
                elif b == 1:
                    cor = prata
                elif b == 2:
                    cor = bronze
                else:
                    cor = branco
                posicao = (1000, y)
                y += 40
                desenhando.text(posicao, texto, font=fonte, fill=cor)
            y = 35
            for c in range (inicio, fim): #level
                texto = str(level[c])
                if c == 0:
                    cor = ouro
                elif c == 1:
                    cor = prata
                elif c == 2:
                    cor = bronze
                else:
                    cor = branco
                posicao = (1400, y)  # x, y
                y += 40
                desenhando.text(posicao, texto, font=fonte, fill=cor)
            y = 35
            for d in range (inicio, fim): #level
                texto = str(exp[d])
                if d == 0:
                    cor = ouro
                elif d == 1:
                    cor = prata
                elif d == 2:
                    cor = bronze
                else:
                    cor = branco
                posicao = (1600, y)  # x, y
                y += 40
                desenhando.text(posicao, texto, font=fonte, fill=cor)
            desenhando.text((35, 50), "Experience Leaderboard", font=ImageFont.truetype(fonte_arial, 70), fill=branco)
            desenhando.text((35, 1000), f"Generated at {agora}", font=ImageFont.truetype(fonte_arial, 35), fill=branco)
            inicio += 25
            fim += 25
            buffer = BytesIO()
            imagens[z].save(buffer, format="PNG")
            buffer.seek(0)
            imagens_prontas.append(buffer)
        return imagens_prontas
    else:
        pagina = requests.get(f'https://www.rucoyonline.com/highscores/{rank_names[leaderboard].lower()}/2016/1')
        dados_pagina = BeautifulSoup(pagina.text, 'html.parser')
        rank = []
        nome = []
        stat = []
        agora = datetime.now().replace(microsecond=0)
        # Encontra todas as tabelas com a classe específica
        ranks_exp = dados_pagina.find_all('table', class_='table table-striped table-highscores table-bordered')

        # Itera nas tabelas encontradas
        for div in ranks_exp:
            linhas = div.find_all('tr')[1:]  # Ignora o cabeçalho
            for tag in div.find_all('span', class_='label flat label-success'):
                tag.decompose()
            for linha in linhas:
                colunas = linha.find_all('td')
                if len(colunas) >= 3:
                    rank.append(colunas[0].get_text(strip=True))
                    nome.append(colunas[1].get_text(strip=True))
                    stat.append(colunas[2].get_text(strip=True))
        imagem_original = Image.open(background_paths[leaderboard])  # substitua pelo nome da sua imagem
        imagem1 = imagem_original.copy()
        imagem2 = imagem_original.copy()
        imagem3 = imagem_original.copy()
        imagem4 = imagem_original.copy()

        imagens = [imagem1, imagem2, imagem3, imagem4]
        imagens_prontas = []

        y = 10
        try:
            fonte = ImageFont.truetype("arialbd.ttf", 35)
        except:
            fonte = ImageFont.load_default()

        ouro   = (212, 175, 55)
        prata  = (169, 169, 169)
        bronze = (205, 127, 50)
        branco = (255, 255, 255)

        inicio = 0
        fim = 25
        # desenho.text((35, 50), "Mage Leaderboard", font=ImageFont.truetype("arialbd.ttf", 70), fill=branco)
        # desenho.text((35, 1000), f"Generated at {now}", font=ImageFont.truetype("arialbd.ttf", 35), fill=branco)

        for z in range(4):
            desenhando = ImageDraw.Draw(imagens[z])
            y = 35
            for a in range (inicio, fim):
                texto = str(rank[a])
                if a == 0:
                    cor = ouro
                elif a == 1:
                    cor = prata
                elif a == 2:
                    cor = bronze
                else:
                    cor = branco
                posicao = (900, y)
                y += 40
                desenhando.text(posicao, texto, font=fonte, fill=cor)
            y = 35
            for b in range (inicio, fim):
                texto = str(nome[b])
                if b == 0:
                    cor = ouro
                elif b == 1:
                    cor = prata
                elif b == 2:
                    cor = bronze
                else:
                    cor = branco
                posicao = (1200, y)
                y += 40
                desenhando.text(posicao, texto, font=fonte, fill=cor)
            y = 35
            for c in range (inicio, fim): #level
                texto = str(stat[c])
                if c == 0:
                    cor = ouro
                elif c == 1:
                    cor = prata
                elif c == 2:
                    cor = bronze
                else:
                    cor = branco
                posicao = (1800, y)  # x, y
                y += 40
                desenhando.text(posicao, texto, font=fonte, fill=cor)
            desenhando.text((35, 50), f"{rank_names[leaderboard]} Leaderboard", font=ImageFont.truetype(fonte_arial, 70), fill=branco)
            desenhando.text((35, 1000), f"Generated at {agora}", font=ImageFont.truetype(fonte_arial, 35), fill=branco)
            inicio += 25
            fim += 25
            buffer = BytesIO()
            imagens[z].save(buffer, format="PNG")
            buffer.seek(0)
            imagens_prontas.append(buffer)
        return imagens_prontas

# def top_farmers_ptrainers():
#     from bs4 import BeautifulSoup
#     import requests
#     from PIL import Image, ImageDraw, ImageFont
#     from io import BytesIO
#     from datetime import datetime
#     pagina = requests.get(f'https://www.rucoystats.com/leaderboards/experience')
#     dados_pagina = BeautifulSoup(pagina.text, 'html.parser')
#     nome = []
#     level = []
#     gain_exp = []
#     gain_lv = []
#     agora = datetime.now().replace(microsecond=0)
#     # Encontra todas as tabelas com a classe específica
#     ranks_exp = dados_pagina.find_all('table', class_='table table-striped table-highscores table-bordered')

#     # Itera nas tabelas encontradas
#     for div in ranks_exp:
#         linhas = div.find_all('tr')[1:]  # Ignora o cabeçalho
#         for tag in div.find_all('span', class_='label flat label-success'):
#             tag.decompose()
#         for linha in linhas:
#             colunas = linha.find_all('td')
#             if len(colunas) >= 3:
#                 rank.append(colunas[0].get_text(strip=True))
#                 nome.append(colunas[1].get_text(strip=True))
#                 level.append(colunas[2].get_text(strip=True))
#                 exp.append(colunas[3].get_text(strip=True))