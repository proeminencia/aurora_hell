def show_leaderboard(leaderboard):
    from bs4 import BeautifulSoup
    import requests
    from PIL import Image, ImageDraw, ImageFont
    from io import BytesIO
    from datetime import datetime

    rank_names = ['Experience', 'Melee', 'Distance', 'Magic', 'Defense']
    background_paths = [r'backgrounds/exp_lb_pot.png', r'backgrounds/new_melee_lb_neck.png', r'backgrounds/new_dist_lb_neck.png', r'backgrounds/new_magic_lb_neck.png', r'backgrounds/new_def_lb_neck.png']
    helvetica = r"fonts/Helvetica.ttf"
    helvetica_bold = r"fonts/Helvetica-Bold.ttf"
    teko_medium = r"fonts/Teko-Medium.ttf"
    tamanho_fonte = 30

    ouro   = (212, 175, 55)
    prata  = (169, 169, 169)
    bronze = (205, 127, 50)
    branco = (255, 255, 255)
    # azul = (100, 149, 237)
    # vermelho = (255, 0, 0)
    # verde = (0, 255, 0)
    amarelo_ouro = (255, 215, 0)
    branco = (255, 255, 255)
    # azul_melee = (68, 187, 255)
    # laranja_mythic = (240, 160, 0)
    cores_classes = [(255, 215, 0), (68, 187, 255), (87, 242, 73), (224, 100, 245), (202, 204, 202)]

    # RANK EXPERIÊNCIA

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

        inicio = 0
        fim = 25

        for z in range(4):
            desenhando = ImageDraw.Draw(imagens[z])
            y = 160
            for a in range (inicio, fim):
                texto = str(rank[a])
                if a == 0:
                    cor = ouro
                    fonte = ImageFont.truetype(helvetica_bold , tamanho_fonte)
                elif a == 1:
                    cor = prata
                    fonte = ImageFont.truetype(helvetica_bold , tamanho_fonte)
                elif a == 2:
                    cor = bronze
                    fonte = ImageFont.truetype(helvetica_bold , tamanho_fonte)
                else:
                    cor = branco
                    fonte = ImageFont.truetype(helvetica , tamanho_fonte)
                posicao = (720, y)
                y += 35
                desenhando.text(posicao, texto, font=fonte, fill=cor)
            y = 160
            for b in range (inicio, fim):
                texto = str(nome[b])
                if b == 0:
                    cor = ouro
                    fonte = ImageFont.truetype(helvetica_bold , tamanho_fonte)
                elif b == 1:
                    cor = prata
                    fonte = ImageFont.truetype(helvetica_bold , tamanho_fonte)
                elif b == 2:
                    cor = bronze
                    fonte = ImageFont.truetype(helvetica_bold , tamanho_fonte)
                else:
                    cor = branco
                    fonte = ImageFont.truetype(helvetica , tamanho_fonte)
                posicao = (970, y)
                y += 35
                desenhando.text(posicao, texto, font=fonte, fill=cor)
            y = 160
            for c in range (inicio, fim): #level
                texto = str(level[c])
                if c == 0:
                    cor = ouro
                    fonte = ImageFont.truetype(helvetica_bold , tamanho_fonte)
                elif c == 1:
                    cor = prata
                    fonte = ImageFont.truetype(helvetica_bold , tamanho_fonte)
                elif c == 2:
                    cor = bronze
                    fonte = ImageFont.truetype(helvetica_bold , tamanho_fonte)
                else:
                    cor = branco
                    fonte = ImageFont.truetype(helvetica , tamanho_fonte)
                posicao = (1400, y)  # x, y
                y += 35
                desenhando.text(posicao, texto, font=fonte, fill=cor)
            y = 160
            for d in range (inicio, fim): #level
                texto = str(exp[d])
                if d == 0:
                    cor = ouro
                    fonte = ImageFont.truetype(helvetica_bold , tamanho_fonte)
                elif d == 1:
                    cor = prata
                    fonte = ImageFont.truetype(helvetica_bold , tamanho_fonte)
                elif d == 2:
                    cor = bronze
                    fonte = ImageFont.truetype(helvetica_bold , tamanho_fonte)
                else:
                    cor = branco
                    fonte = ImageFont.truetype(helvetica , tamanho_fonte)
                posicao = (1610, y)  # x, y
                y += 35
                desenhando.text(posicao, texto, font=fonte, fill=cor)
            desenhando.text((720, 35), f"Rank", font=ImageFont.truetype(teko_medium, 80), fill=cores_classes[leaderboard])
            desenhando.text((975, 35), f"Name", font=ImageFont.truetype(teko_medium, 80), fill=cores_classes[leaderboard])
            desenhando.text((1365, 35), f"Level", font=ImageFont.truetype(teko_medium, 80), fill=cores_classes[leaderboard])
            desenhando.text((1585, 35), f"Experience", font=ImageFont.truetype(teko_medium, 80), fill=cores_classes[leaderboard])
            
            desenhando.text((35, 70), "Experience Leaderboard", font=ImageFont.truetype(teko_medium, 80), fill=amarelo_ouro)
            desenhando.text((35, 1000), f"Generated at {agora}", font=ImageFont.truetype(helvetica, 35), fill=branco)
            inicio += 25
            fim += 25
            # imagens[z].show()
            buffer = BytesIO()
            imagens[z].save(buffer, format="PNG")
            buffer.seek(0)
            imagens_prontas.append(buffer)
        return imagens_prontas
    
    # RANKS SEM SER O DE EXP
    
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

        inicio = 0
        fim = 25
        
        for z in range(4):
            desenhando = ImageDraw.Draw(imagens[z])
            y = 160
            for a in range (inicio, fim):
                texto = str(rank[a])
                if a == 0:
                    cor = ouro
                    fonte = ImageFont.truetype(helvetica_bold , tamanho_fonte)
                elif a == 1:
                    cor = prata
                    fonte = ImageFont.truetype(helvetica_bold , tamanho_fonte)
                elif a == 2:
                    cor = bronze
                    fonte = ImageFont.truetype(helvetica_bold , tamanho_fonte)
                else:
                    cor = branco
                    fonte = ImageFont.truetype(helvetica , tamanho_fonte)
                posicao = (970, y)
                y += 35
                desenhando.text(posicao, texto, font=fonte, fill=cor)
            y = 160
            for b in range (inicio, fim):
                texto = str(nome[b])
                if b == 0:
                    cor = ouro
                    fonte = ImageFont.truetype(helvetica_bold , tamanho_fonte)
                elif b == 1:
                    cor = prata
                    fonte = ImageFont.truetype(helvetica_bold , tamanho_fonte)
                elif b == 2:
                    cor = bronze
                    fonte = ImageFont.truetype(helvetica_bold , tamanho_fonte)
                else:
                    cor = branco
                    fonte = ImageFont.truetype(helvetica , tamanho_fonte)
                posicao = (1200, y)
                y += 35
                desenhando.text(posicao, texto, font=fonte, fill=cor)
            y = 160
            for c in range (inicio, fim): #level
                texto = str(stat[c])
                if c == 0:
                    cor = ouro
                    fonte = ImageFont.truetype(helvetica_bold , tamanho_fonte)
                elif c == 1:
                    cor = prata
                    fonte = ImageFont.truetype(helvetica_bold , tamanho_fonte)
                elif c == 2:
                    cor = bronze
                    fonte = ImageFont.truetype(helvetica_bold , tamanho_fonte)
                else:
                    cor = branco
                    fonte = ImageFont.truetype(helvetica , tamanho_fonte)
                posicao = (1800, y)  # x, y
                y += 35
                desenhando.text(posicao, texto, font=fonte, fill=cor)
            desenhando.text((970, 35), f"Rank", font=ImageFont.truetype(teko_medium, 80), fill=cores_classes[leaderboard])
            desenhando.text((1200, 35), f"Name", font=ImageFont.truetype(teko_medium, 80), fill=cores_classes[leaderboard])
            desenhando.text((1770, 35), f"Stat", font=ImageFont.truetype(teko_medium, 80), fill=cores_classes[leaderboard])
            desenhando.text((35, 70), f"{rank_names[leaderboard]} Leaderboard", font=ImageFont.truetype(teko_medium, 100), fill=cores_classes[leaderboard])
            desenhando.text((35, 1000), f"Generated at {agora}", font=ImageFont.truetype(helvetica, 25), fill=branco)
            inicio += 25
            fim += 25
            # imagens[z].show()
            buffer = BytesIO()
            imagens[z].save(buffer, format="PNG")
            buffer.seek(0)
            imagens_prontas.append(buffer)
        return imagens_prontas