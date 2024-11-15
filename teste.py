import os
import json

arquivo_treino = "treino.txt"

# Função para carregar os treinos
def carregar_treinos():
    if os.path.exists(arquivo_treino):
        with open(arquivo_treino, "r", encoding="utf-8") as file:
            try:
                return json.load(file)  # Carregar treinos como JSON
            except json.JSONDecodeError:
                return []  # Retorna uma lista vazia se o arquivo estiver corrompido
    return []

# Função para salvar os treinos no arquivo
def salvar_treinos(treinos):
    with open(arquivo_treino, "w", encoding="utf-8") as file:
        json.dump(treinos, file, ensure_ascii=False, indent=4)  # Salvar treinos em formato JSON

# Função para formatar a data
def data_formatada():
    while True:
        try:
            dia = int(input("Insira o dia (1-31): "))
            mes = int(input("Insira o mês (1-12): "))
            ano = int(input("Insira o ano (ex: 2023): "))
            return f"{dia:02d}/{mes:02d}/{ano:04d}"
        except ValueError:
            print("Entrada inválida. Tente novamente.")

# Função para coletar informações do treino
def dados_treino():
    distancia = float(input("Insira a distância percorrida (em km): "))
    localizacao = input("Insira a localização: ")
    clima = input("Insira as condições climáticas: ")
    return distancia, localizacao, clima

# Programa principal
treinos = carregar_treinos()

while True:
    print("\nMENU:")
    print("1 -> Criar treinos.")
    print("2 -> Visualizar treinos.")
    print("3 -> Atualizar treinos.")
    print("4 -> Deletar treinos.")
    print("5 -> Sair.")

    opcao = input("Escolha uma opção: ")
    
    if opcao == '5':
        print("Saindo do programa. Até mais!")
        break

    elif opcao == '1':
        treino = input("Digite o nome do treino que deseja criar: ")
        adicionar_info = input("Deseja adicionar informações detalhadas sobre o treino? (s/n): ").strip().lower()

        if adicionar_info == 's':
            data = data_formatada()
            distancia, localizacao, clima = dados_treino()
            treinos.append({
                "nome": treino,
                "data": data,
                "distancia": distancia,
                "localizacao": localizacao,
                "clima": clima
            })
        else:
            treinos.append({"nome": treino})
        
        salvar_treinos(treinos)
        print("Treino salvo com sucesso.")

    elif opcao == '2':
            if len(treinos) == 0:
                print("Não existe treinos ainda.")
            else:
                print("\nLista de treinos: ")
                for i, treino in enumerate(treinos):
                 print(f"{i+1}º treino: {treino}")

    elif opcao == '3':
        print("\nTreinos disponíveis:")
        if not treinos:
            print("Nenhum treino para atualizar.")
        else:
            for i, treino in enumerate(treinos, 1):
                print(f"{i} -> {treino['nome']}")

            try:
                indice = int(input("Escolha o número do treino que deseja atualizar: ")) - 1
                if 0 <= indice < len(treinos):
                    treinos[indice]["nome"] = input("Digite o novo nome do treino: ")
                    salvar_treinos(treinos)
                    print("Treino atualizado com sucesso.")
                else:
                    print("Número inválido.")
            except ValueError:
                print("Entrada inválida. Tente novamente.")

    elif opcao == '4':
        print("\nTreinos disponíveis:")
        if not treinos:
            print("Nenhum treino para deletar.")
        else:
            for i, treino in enumerate(treinos, 1):
                print(f"{i} -> {treino['nome']}")

            try:
                indice = int(input("Escolha o número do treino que deseja deletar: ")) - 1
                if 0 <= indice < len(treinos):
                    treino_removido = treinos.pop(indice)
                    salvar_treinos(treinos)
                    print(f"Treino '{treino_removido['nome']}' foi deletado com sucesso.")
                else:
                    print("Número inválido.")
            except ValueError:
                print("Entrada inválida. Tente novamente.")

    else:
        print("Opção inválida. Tente novamente.")
