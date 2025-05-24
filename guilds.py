def show_members(guildname):
    from bs4 import BeautifulSoup
    import requests
    from PIL import Image, ImageDraw, ImageFont
    from io import BytesIO
    from datetime import datetime
    from math import ceil

    default_guildname = guildname.strip().title()
    guildname = guildname.strip().title().replace(" ", "%20")

    pagina = requests.get(f"https://www.rucoyonline.com/guild/{guildname}")
    dados_pagina = BeautifulSoup(pagina.text, 'html.parser')
    tabela_jogadores = dados_pagina.find_all("table", class_="table table-bordered")
    

    if not tabela_jogadores:
        return 0, [] 

    nome_jogador = []
    level = []
    data = []
    status = []
    agora = datetime.now().replace(microsecond=0)


    for div in tabela_jogadores:
        linhas = div.find_all('tr')[1:]  # Ignora o cabeçalho
    for tag in div.find_all('span', class_='label flat label-primary'):
        tag.decompose()
    for linha in linhas:
        colunas = linha.find_all('td')
        if linha.find("span", class_="label flat label-success"):
            status.append("online")
        else:
            status.append("offline")
        if len(colunas) >= 1:
            link = colunas[0].find("a")
            if link:
                nome_jogador.append(link.get_text(strip=True))
                level.append(colunas[1].get_text(strip=True))
                data.append(colunas[2].get_text(strip=True))

    helvetica = r"fonts/Helvetica.ttf"
    teko_medium = r"fonts/Teko-Medium.ttf"

    y = 160
    tamanho_fonte = 30
    max_por_pagina = 25
    imagens = []
    online = Image.open(r"backgrounds/sprites/online.png")
    offline = Image.open(r"backgrounds/sprites/offline.png")

    for a in range(ceil(len(nome_jogador) / max_por_pagina)):
        y = 160
        imagem = Image.open(r"backgrounds/guilds_background.png")
        desenhando = ImageDraw.Draw(imagem)
        desenhando.text((30, 20), f"List of Members ({len(nome_jogador)})", font=ImageFont.truetype(teko_medium, 80), fill=(61, 204, 212))
        desenhando.text((30, 90), f"{default_guildname}", font=ImageFont.truetype(teko_medium, 80))
        desenhando.text((1000, 35), f"Name", font=ImageFont.truetype(teko_medium, 80), fill=(61, 204, 212))
        desenhando.text((1362, 35), f"Level", font=ImageFont.truetype(teko_medium, 80), fill=(61, 204, 212))
        desenhando.text((1630, 35), f"Join date", font=ImageFont.truetype(teko_medium, 80), fill=(61, 204, 212))
        desenhando.text((35, 1000), f"Generated at {agora}", font=ImageFont.truetype(helvetica, 25))
        imagem.paste(online, (35, 950))
        imagem.paste(offline, (35, 975))
        desenhando.text((63, 947), f"= Online", font=ImageFont.truetype(helvetica, 25))
        desenhando.text((63, 972), f"= Offline", font=ImageFont.truetype(helvetica, 25))
        
        
        # Define o índice inicial e final para esta "página"
        inicio = a * max_por_pagina
        fim = min(inicio + max_por_pagina, len(nome_jogador))
        
        for i in range(inicio, fim):
            if status[i] == "online":
                imagem.paste(online, (970, y+3))
            else:
                imagem.paste(offline, (970, y+3))
            desenhando.text((1000, y), nome_jogador[i], font=ImageFont.truetype(helvetica , tamanho_fonte), fill=(255,255,255))
            desenhando.text((1400, y), level[i], font=ImageFont.truetype(helvetica , tamanho_fonte), fill=(255,255,255))
            desenhando.text((1660, y), data[i], font=ImageFont.truetype(helvetica , tamanho_fonte), fill=(255,255,255))
            y += 35
        buffer = BytesIO()
        imagem.save(buffer, format="PNG")
        buffer.seek(0)
        imagens.append(buffer)
    return 1, imagens

def show_online(guildname):
    from bs4 import BeautifulSoup
    import requests
    from PIL import Image, ImageDraw, ImageFont
    from io import BytesIO
    from datetime import datetime
    from math import ceil

    default_guildname = guildname.strip().title()
    guildname = guildname.strip().title().replace(" ", "%20")


    pagina = requests.get(f"https://www.rucoyonline.com/guild/{guildname}")
    dados_pagina = BeautifulSoup(pagina.text, 'html.parser')
    tabela_jogadores = dados_pagina.find_all("table", class_="table table-bordered")

    if not tabela_jogadores:
        return 0, [] 

    nome_jogador = []
    level = []
    data = []
    agora = datetime.now().replace(microsecond=0)


    for div in tabela_jogadores:
        linhas = div.find_all('tr')[1:]  # Ignora o cabeçalho
        for tag in div.find_all('span', class_='label flat label-primary'):
            tag.decompose()
        for linha in linhas:
            if linha.find("span", class_="label flat label-success"):  # Somente se estiver online
                colunas = linha.find_all('td')
                if len(colunas) >= 1:
                    link = colunas[0].find("a")
                    if link:
                        nome_jogador.append(link.get_text(strip=True))
                        level.append(colunas[1].get_text(strip=True))
                        data.append(colunas[2].get_text(strip=True))

    if len(nome_jogador) == 0:
        return 1, []

    # azul = (100, 149, 237)
    # vermelho = (255, 0, 0)
    # verde = (0, 255, 0)
    # amarelo_ouro = (255, 215, 0)
    # branco = (255, 255, 255)
    # azul_mana = (68, 187, 255)
    # laranja_mythic = (240, 160, 0)

    helvetica = r"fonts/Helvetica.ttf"
    teko_medium = r"fonts/Teko-Medium.ttf"

    y = 160
    x1 = 970
    x2 = 1200
    x3 = 1800
    tamanho_fonte = 30
    max_por_pagina = 25
    imagens = []
    online = Image.open(r"backgrounds/sprites/online.png").convert("RGBA")

    for a in range(ceil(len(nome_jogador) / max_por_pagina)):
        y = 160
        imagem = Image.open(r"backgrounds/guilds_background.png")
        desenhando = ImageDraw.Draw(imagem)
        desenhando.text((30, 20), f"List of Online Members ({len(nome_jogador)})", font=ImageFont.truetype(teko_medium, 80), fill=(61, 204, 212))
        desenhando.text((30, 90), f"{default_guildname}", font=ImageFont.truetype(teko_medium, 80))
        desenhando.text((1000, 35), f"Name", font=ImageFont.truetype(teko_medium, 80), fill=(61, 204, 212))
        desenhando.text((1362, 35), f"Level", font=ImageFont.truetype(teko_medium, 80), fill=(61, 204, 212))
        desenhando.text((1630, 35), f"Join date", font=ImageFont.truetype(teko_medium, 80), fill=(61, 204, 212))
        desenhando.text((35, 1000), f"Generated at {agora}", font=ImageFont.truetype(helvetica, 25))
        imagem.paste(online, (35, 975))
        desenhando.text((63, 972), f"= Offline", font=ImageFont.truetype(helvetica, 25))
        
        # Define o índice inicial e final para esta "página"
        inicio = a * max_por_pagina
        fim = min(inicio + max_por_pagina, len(nome_jogador))
        
        for i in range(inicio, fim):
            imagem.paste(online, (970, y+3))
            desenhando.text((1000, y), nome_jogador[i], font=ImageFont.truetype(helvetica , tamanho_fonte), fill=(255,255,255))
            desenhando.text((1400, y), level[i], font=ImageFont.truetype(helvetica , tamanho_fonte), fill=(255,255,255))
            desenhando.text((1660, y), data[i], font=ImageFont.truetype(helvetica , tamanho_fonte), fill=(255,255,255))
            y += 35
        buffer = BytesIO()
        imagem.save(buffer, format="PNG")
        buffer.seek(0)
        imagens.append(buffer)
    return 2, imagens
    