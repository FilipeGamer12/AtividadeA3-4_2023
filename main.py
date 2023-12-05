import os
import networkx as nx
import folium
from tkinter import Tk, simpledialog ,messagebox
import webbrowser
current_directory = os.path.dirname(__file__)

root = Tk()
root.withdraw()

# Defina as cidades e suas informações
cidades = {
    "Curitiba": {"latitude": -25.4284, "longitude": -49.2733, "cd_endereco": "..."},
    "Londrina": {"latitude": -23.3045, "longitude": -51.1696, "cd_endereco": "..."},
    "Foz do Iguaçu": {"latitude": -25.5478, "longitude": -54.5882, "cd_endereco": "..."},
    "União da Vitória": {"latitude": -26.2318, "longitude": -51.0851, "cd_endereco": "..."},
    "Joinville": {"latitude": -26.3032, "longitude": -48.8410, "cd_endereco": "..."},
    "Chapecó": {"latitude": -27.1005, "longitude": -52.6152, "cd_endereco": "..."},
    "Porto Alegre": {"latitude": -30.0330, "longitude": -51.2200, "cd_endereco": "..."},
    "Uruguaiana": {"latitude": -29.7601, "longitude": -57.0859, "cd_endereco": "..."},
    "Pelotas": {"latitude": -31.7649, "longitude": -52.3376, "cd_endereco": "..."},
}

# Defina as distâncias entre as cidades
distancias = {
    ("Curitiba", "Londrina"): 365,
    ("Curitiba", "Foz do Iguaçu"): 635,
    ("Curitiba", "União da Vitória"): 241,
    ("Curitiba", "Joinville"): 140,
    ("Curitiba", "Chapecó"): 481,
    ("Curitiba", "Porto Alegre"): 752,
    ("Curitiba", "Uruguaiana"): 1115,
    ("Curitiba", "Pelotas"): 1002,
    ("Londrina", "Curitiba"): 385,
    ("Londrina", "Foz do Iguaçu"): 512,
    ("Londrina", "União da Vitória"): 454,
    ("Londrina", "Joinville"): 513,
    ("Londrina", "Chapecó"): 631,
    ("Londrina", "Porto Alegre"): 1125,
    ("Londrina", "Uruguaiana"): 1260,
    ("Londrina", "Pelotas"): 1375,
    ("Foz do Iguaçu", "Curitiba"): 635,
    ("Foz do Iguaçu", "Londrina"): 510,
    ("Foz do Iguaçu", "União da Vitória"): 546,
    ("Foz do Iguaçu", "Joinville"): 764,
    ("Foz do Iguaçu", "Chapecó"): 444,
    ("Foz do Iguaçu", "Porto Alegre"): 908,
    ("Foz do Iguaçu", "Uruguaiana"): 645,
    ("Foz do Iguaçu", "Pelotas"): 1058,
    ("União da Vitória", "Curitiba"): 234,
    ("União da Vitória", "Londrina"): 453,
    ("União da Vitória", "Foz do Iguaçu"): 547,
    ("União da Vitória", "Joinville"): 273,
    ("União da Vitória", "Chapecó"): 243,
    ("União da Vitória", "Porto Alegre"): 607,
    ("União da Vitória", "Uruguaiana"): 877,
    ("União da Vitória", "Pelotas"): 815,
    ("Joinville", "Curitiba"): 140,
    ("Joinville", "Londrina"): 513,
    ("Joinville", "Foz do Iguaçu"): 765,
    ("Joinville", "União da Vitória"): 273,
    ("Joinville", "Chapecó"): 515,
    ("Joinville", "Porto Alegre"): 616,
    ("Joinville", "Uruguaiana"): 1235,
    ("Joinville", "Pelotas"): 866,
    ("Chapecó", "Curitiba"): 475,
    ("Chapecó", "Londrina"): 631,
    ("Chapecó", "Foz do Iguaçu"): 444,
    ("Chapecó", "União da Vitória"): 242,
    ("Chapecó", "Joinville"): 514,
    ("Chapecó", "Porto Alegre"): 452,
    ("Chapecó", "Uruguaiana"): 670,
    ("Chapecó", "Pelotas"): 658,
    ("Porto Alegre", "Curitiba"): 741,
    ("Porto Alegre", "Londrina"): 1124,
    ("Porto Alegre", "Foz do Iguaçu"): 904,
    ("Porto Alegre", "União da Vitória"): 609,
    ("Porto Alegre", "Joinville"): 616,
    ("Porto Alegre", "Chapecó"): 453,
    ("Porto Alegre", "Uruguaiana"): 632,
    ("Porto Alegre", "Pelotas"): 262,
    ("Uruguaiana", "Curitiba"): 1166,
    ("Uruguaiana", "Londrina"): 1318,
    ("Uruguaiana", "Foz do Iguaçu"): 646,
    ("Uruguaiana", "União da Vitória"): 933,
    ("Uruguaiana", "Joinville"): 1236,
    ("Uruguaiana", "Chapecó"): 727,
    ("Uruguaiana", "Porto Alegre"): 632,
    ("Uruguaiana", "Pelotas"): 565,
    ("Pelotas", "Curitiba"): 992,
    ("Pelotas", "Londrina"): 1375,
    ("Pelotas", "Foz do Iguaçu"): 1058,
    ("Pelotas", "União da Vitória"): 814,
    ("Pelotas", "Joinville"): 866,
    ("Pelotas", "Chapecó"): 657,
    ("Pelotas", "Porto Alegre"): 262,
    ("Pelotas", "Uruguaiana"): 565,
}

# Adicione automaticamente as conexões com base nas distâncias
conexoes = list(distancias.keys())

def distancia_entre_cidades(cidade_partida, ponto_intermediario, cidade_destino):
    valor_rota = 0

    if ponto_int == True and ponto_intermediario != cidade_destino:
        dist_int = distancias.get((cidade_partida, ponto_intermediario), None)
        dist_destino = distancias.get((ponto_intermediario, cidade_destino), None)

        if dist_int is not None and dist_destino is not None:
            valor_rota = dist_int + dist_destino
        else:
            print("ERRO: Distância não encontrada para as chaves "
                  f'({cidade_partida}, {ponto_intermediario}) e ({ponto_intermediario}, {cidade_destino}).')
    elif ponto_int == True and ponto_intermediario == cidade_destino:
        valor_rota = distancias.get((cidade_partida, cidade_destino), None)

        if valor_rota is None:
            print(f"ERRO: Distância não encontrada para a chave ({cidade_partida}, {cidade_destino}).")
    elif ponto_int == False:
        valor_rota = distancias.get((cidade_partida, cidade_destino), None)

        if valor_rota is None:
            print(f"ERRO: Distância não encontrada para a chave ({cidade_partida}, {cidade_destino}).")

    print(f"A distância da rota é {valor_rota} km.")
    return valor_rota

def gerar_rota_com_intermediario(cidade_partida, ponto_intermediario, cidade_destino):
    # Crie o mapa com Folium
    mapa_rota = folium.Map(location=[-25.4284, -49.2733], zoom_start=6)

    # Adicione o marcador para o ponto inicial
    folium.Marker(
        location=[cidades[cidade_partida]["latitude"], cidades[cidade_partida]["longitude"]],
        popup=f"{cidade_partida}",
        icon=folium.Icon(color='green')
    ).add_to(mapa_rota)

    # Se houver ponto intermediário, adicione o marcador correspondente
    if ponto_intermediario:
        folium.Marker(
            location=[cidades[ponto_intermediario]["latitude"], cidades[ponto_intermediario]["longitude"]],
            popup=f"{ponto_intermediario}",
            icon=folium.Icon(color='blue')
        ).add_to(mapa_rota)

    # Adicione o marcador para o ponto de destino
    folium.Marker(
        location=[cidades[cidade_destino]["latitude"], cidades[cidade_destino]["longitude"]],
        popup=f"{cidade_destino}",
        icon=folium.Icon(color='red')
    ).add_to(mapa_rota)

    # Se houver ponto intermediário, trace a linha passando pelos três pontos
    if ponto_intermediario:
        folium.PolyLine(
            locations=[
                [cidades[cidade_partida]["latitude"], cidades[cidade_partida]["longitude"]],
                [cidades[ponto_intermediario]["latitude"], cidades[ponto_intermediario]["longitude"]],
                [cidades[cidade_destino]["latitude"], cidades[cidade_destino]["longitude"]],
            ],
            color="purple"
        ).add_to(mapa_rota)
    # Se não houver ponto intermediário, trace a linha diretamente para o destino
    else:
        folium.PolyLine(
            locations=[
                [cidades[cidade_partida]["latitude"], cidades[cidade_partida]["longitude"]],
                [cidades[cidade_destino]["latitude"], cidades[cidade_destino]["longitude"]],
            ],
            color="blue"
        ).add_to(mapa_rota)

    # Exiba o mapa
    mapa_rota.save("mapa_rota_com_intermediario.html")

# Exemplo de uso

#cidade_partida = input("Insira a cidade de partida: ")
cidade_partida = simpledialog.askstring("Inserir Dados", "Insira a cidade de partida:")
#cidade_destino = input("Insira a cidade de destino: ")
cidade_destino = simpledialog.askstring("Inserir Dados", "Insira a cidade de destino:")
# Adicione os pontos intermediários conforme as regras
ponto_intermediario = None
if cidade_partida in ["Foz do Iguaçu", "União da Vitória"] and cidade_partida == "Foz do Iguaçu" or cidade_destino in ["Foz do Iguaçu", "União da Vitória"] and cidade_destino == "Foz do Iguaçu":
    ponto_intermediario = "União da Vitória"
elif cidade_partida in ["Foz do Iguaçu", "União da Vitória"] and cidade_partida == "União da Vitória" or cidade_destino in ["Foz do Iguaçu", "União da Vitória"] and cidade_destino == "União da Vitória":
    ponto_intermediario = "Foz do Iguaçu"
elif cidade_partida in ["Joinville", "Chapecó"] and cidade_partida == "Joinville" or cidade_destino in ["Chapecó", "Joinville"] and cidade_destino == "Joinville":
    ponto_intermediario = "Chapecó"
elif cidade_partida in ["Joinville", "Chapecó"] and cidade_partida == "Chapecó" or cidade_destino in ["Chapecó", "Joinville"] and cidade_destino == "Chapecó":
    ponto_intermediario = "Joinville"

# Atualize a chamada da função para incluir a variável ponto_int
if ponto_intermediario != None:
    ponto_int = True
else:
    ponto_int = False
gerar_rota_com_intermediario(cidade_partida, ponto_intermediario, cidade_destino)
distancia_total = distancia_entre_cidades(cidade_partida, ponto_intermediario, cidade_destino)

# Verifique se gerar_rota_com_intermediario retornou algum valor
if ponto_int:
    gerar_rota_com_intermediario(cidade_partida, ponto_intermediario, cidade_destino)

Valores_de_viagem = distancia_total*20
#print(f"valor da viagem em reais sera: {Valores_de_viagem},00")

tempo = distancia_total/500
horasA = str(tempo).split('.')
#print(horasA)
if len(horasA)>1 :
    horasb = float('0.'+ horasA[1])
    horasb = horasb*6.25
    #print(horasb)
horasc = str(horasb).split('.')
if len(horasc)>1 :
    horasd = float('0.'+ horasc[1])
    horasd = horasd*60
    #print(horasd)
horasd = str(horasd).split('.')
#print(f"o tempo de viagem em dias sera:{horasA[0]} Dias e {horasc[0]} horas e {horasd[0]} minutos")
resultado = messagebox.showinfo("Resultado", f"valor da viagem em reais sera: R${Valores_de_viagem},00 \nO tempo de viagem em dias sera: {horasA[0]} Dia(s) e {horasc[0]} hora(s) e {horasd[0]} minuto(s)")

html_file_path = os.path.join(current_directory, "mapa_rota_com_intermediario.html")

webbrowser.open(html_file_path)
