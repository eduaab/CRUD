import os
import json

arquivo_treino = "treino.txt"

# Função para carregar os treinos
def carregar_treinos():
    if os.path.exists(arquivo_treino):
        with open(arquivo_treino, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []  # Retorna uma lista vazia se o arquivo estiver corrompido
    return []

# Função para salvar os treinos no arquivo
def salvar_treinos(treinos):
    if not isinstance(treinos, list):
        print("Erro: os treinos devem ser uma lista.")
        return
    with open(arquivo_treino, "w", encoding="utf-8") as file:
        json.dump(treinos, file, ensure_ascii=False, indent=4)

def data_formatada():
    while True:
        try:
            dia = int(input("Insira o dia (1-31): "))
            mes = int(input("Insira o mês (1-12): "))
            ano = int(input("Insira o ano (ex: 2023): "))
            return f"{dia:02d}/{mes:02d}/{ano:04d}"
        except ValueError:
            print("Entrada inválida. Tente novamente.")

def dados_treino():
    distancia = float(input("Insira a distância percorrida (em km): "))
    tempo = int(input("Insira o tempo total (em minutos): "))
    localizacao = input("Insira a localização: ")
    clima = input("Insira as condições climáticas: ")
    return distancia, tempo, localizacao, clima

def um():
    treino = input("Digite o nome do treino que deseja criar: ")
    adicionar_info = input("Deseja adicionar informações detalhadas sobre o treino? (s/n): ").strip().lower()

    if adicionar_info == 's':
        data = data_formatada()
        distancia, tempo, localizacao, clima = dados_treino()
        treinos.append({
            "nome": treino,
            "data": data,
            "distancia": distancia,
            "tempo": tempo,
            "localizacao": localizacao,
            "clima": clima
        })
    else:
        treinos.append({
            "nome": treino,
            "data": "N/A",
            "distancia": 0,
            "tempo": 0,
            "localizacao": "N/A",
            "clima": "N/A"
        })
    salvar_treinos(treinos)
    print("Treino salvo com sucesso.")

def dois():
    if len(treinos) == 0:
        print("Não há treinos cadastrados.")
    else:
        print("\nTreinos cadastrados:")
        for i, treino in enumerate(treinos, 1):
            print(f"\nTreino {i}:")
            for chave, valor in treino.items():
                print(f"{chave.capitalize()}: {valor}")

# Outras funções permanecem inalteradas...

def seis():
    while True:
        print("\nMENU de Metas e Desafios:")
        print("1 -> Definir Metas")
        print("2 -> Visualizar Metas")
        print("3 -> Voltar para o MENU principal")

        opcao_metas = input("Escolha uma opção: ")

        if opcao_metas == "1":
                print("1 -> Meta de distância total em (km)")
                print("2 -> Meta de tempo total em (minutos)")
                tipo_de_meta = input("Escolha uma opção: ")
                if tipo_de_meta == "1":
                    distancia_meta = float(input("Insira a meta de distância total (em km): "))

                if tipo_de_meta =="2":
                    tempo_meta = float(input("Insira a meta de tempo total (em minutos): "))
                
                print("Metas definidas com sucesso!")
        
        elif opcao_metas == "2":
            distancia_total = print(sum(treino["distancia"] for treino in treinos))
            tempo_total = print(sum(treino.get("tempo", 0) for treino in treinos))
            
        elif opcao_metas == "3":
            break

        else:
                print("Opção inválida. Tente novamente.")

# Programa principal
treinos = carregar_treinos()

while True:
    print("\nMENU:")
    print("1 -> Criar treinos.")
    print("2 -> Visualizar treinos.")
    print("3 -> Atualizar treinos.")
    print("4 -> Deletar treinos.")
    print("5 -> Filtragem por Tempo ou Distância.")
    print("6 -> Metas e Desafios.")
    print("7 -> Sugestão de Treinos aleatórios.")
    print("8 -> Calculo IMC + Sugestões.")
    print("9 -> Sair.")

    opcao = input("Escolha uma opção: ")
    
    if opcao == '9':
        print("Saindo do programa. Até mais!")
        break

    elif opcao == '1':
        um()

    elif opcao == '2':
        dois()

    elif opcao == '3':
        tres()

    elif opcao == '4':
        quatro()

    elif opcao == '6':
        seis()

    # Outras opções do menu podem ser adicionadas conforme necessário...

    else:
        print("Opção inválida. Tente novamente.")
