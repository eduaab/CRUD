import os
import json

arquivo_treino = "treino.json"

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



# Arquivo para salvar as metas
arquivo_metas = "metas.json"

# Função para salvar metas no arquivo JSON
def salvar_metas_json(metas):
    try:
        with open(arquivo_metas, "w", encoding="utf-8") as file:
            json.dump(metas, file, indent=4)
        print("Metas salvas com sucesso.")
    except Exception as e:
        print("Erro ao salvar metas:", e)

# Função para carregar metas do arquivo JSON
def carregar_metas_json():
    if os.path.exists(arquivo_metas):
        try:
            with open(arquivo_metas, "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception as e:
            print("Erro ao carregar metas:", e)
    return []  # Retorna uma lista vazia se o arquivo não existir ou der erro

def verificar_metas_atingidas(metas, treinos):
    distancia_total = sum(treino.get("distancia", 0) for treino in treinos)
    tempo_total = sum(treino.get("tempo", 0) for treino in treinos)

    metas_concluidas = []
    for meta in metas[:]:  # Usa uma cópia da lista para evitar problemas ao modificar durante a iteração
        if meta["tipo"] == "Distância" and distancia_total >= meta["valor"]:
            print(f"🎉 Parabéns! Você atingiu a meta de {meta['valor']} km!")
            metas_concluidas.append(meta)
            metas.remove(meta)
        elif meta["tipo"] == "Tempo" and tempo_total >= meta["valor"]:
            print(f"🎉 Parabéns! Você atingiu a meta de {meta['valor']} minutos!")
            metas_concluidas.append(meta)
            metas.remove(meta)

    if metas_concluidas:
        salvar_metas_json(metas)  # Atualiza a lista de metas no arquivo
        print("\nAs seguintes metas foram concluídas e removidas:")
        for meta in metas_concluidas:
            print(f"- {meta['tipo']}: {meta['valor']} {meta['unidade']}")
    else:
        print("Nenhuma meta foi concluída ainda. Continue assim!")




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

def tres():
    print("\nTreinos disponíveis:")
    if not treinos:
        print("Nenhum treino para atualizar.")
    else:
        for i, treino in enumerate(treinos, 1):
            print(f"{i} -> {treino['nome']}")

        try:
            indice = int(input("Escolha o número do treino que deseja atualizar: ")) - 1
            escolha_modificação = int(input("O que você deseja atualizar?\n1. Nome\n2. Data\n3. Distância\n4. Localização\n5. Clima\nEscolha uma opção: "))
            if escolha_modificação == 1:
                treinos[indice]["nome"] = input("Digite o novo nome do treino: ")
            elif escolha_modificação == 2:
                treinos[indice]["data"] = input("Digite a nova data do treino: ")
            elif escolha_modificação == 3:
                treinos[indice]["distancia"] = float(input("Digite a nova distância do treino (em km): "))
            elif escolha_modificação == 4:
                treinos[indice]["localizacao"] = input("Digite a nova localização do treino: ")
            elif escolha_modificação == 5:
                treinos[indice]["clima"] = input("Digite as novas condições climáticas do treino: ")
            else:
                print("Opção inválida.")
            salvar_treinos(treinos)
            print("Treino atualizado com sucesso.")
        except ValueError:
            print("Entrada inválida. Tente novamente.")

def quatro():
    print("\nTreinos disponíveis:")
    if not treinos:
        print("Nenhum treino para deletar.")
    else:
        for i, treino in enumerate(treinos, 1):
            print(f"{i} -> {treino['nome']}")

        try:
            indice = int(input("Escolha o número do treino que deseja deletar: ")) - 1
            if 0 <= indice < len(treinos):  # Verifica se o índice está no intervalo válido
                treino_removido = treinos.pop(indice)
                salvar_treinos(treinos)
                print(f"Treino '{treino_removido['nome']}' foi deletado com sucesso.")
            else:
                print("Número inválido. Nenhum treino foi deletado.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")


def cinco():
    print("Saindo do programa. Até mais!")

def seis():
    metas = carregar_metas_json()  # Carregar metas existentes do JSON

    while True:
        print("\nMENU de Metas e Desafios:")
        print("1 -> Definir Metas")
        print("2 -> Visualizar Metas")
        print("3 -> Excluir Meta")
        print("4 -> Voltar para o MENU principal")

        opcao_metas = input("Escolha uma opção: \n")

        if opcao_metas == "1":
            print("1 -> Meta de distância total em (km)")
            print("2 -> Meta de tempo total em (minutos)")
            tipo_de_meta = input("Escolha uma opção: ")

            if tipo_de_meta == "1":
                distancia = float(input("Insira a meta de distância total (em km): "))
                metas.append({"tipo": "Distância", "valor": distancia, "unidade": "km"})
                print(f"Meta de distância definida: {distancia} km.")

            elif tipo_de_meta == "2":
                tempo = float(input("Insira a meta de tempo total (em minutos): "))
                metas.append({"tipo": "Tempo", "valor": tempo, "unidade": "minutos"})
                print(f"Meta de tempo definida: {tempo} minutos.")

            else:
                print("Opção inválida. Tente novamente.")
                continue
            
            # Salvar as metas no arquivo JSON após definir
            salvar_metas_json(metas)

        elif opcao_metas == "2":
            verificar_metas_atingidas(metas, treinos)
            print("\n---- Metas ----")
            if metas:
                for meta in metas:
                    print(f"{meta['tipo']}: {meta['valor']} {meta['unidade']}")
                
                # Progresso acumulado
                distancia_total = sum(treino["distancia"] for treino in treinos)
                tempo_total = sum(treino.get("tempo", 0) for treino in treinos)
                
                print("\nSeu progresso:")
                print(f"Distância total já percorrida: {distancia_total} km")
                print(f"Minutos totais já gastos: {tempo_total} minutos")
            else:
                print("Nenhuma meta definida.")

        elif opcao_metas == "3":
            print("\nMetas disponíveis:")
            if not metas:
                print("Nenhuma meta para deletar.")
            else:
                for i, meta in enumerate(metas, 1):
                    print(f"{i} -> {meta['tipo']}: {meta['valor']} {meta['unidade']}")

                try:
                    indice = int(input("Escolha o número da meta que deseja deletar: ")) - 1
                    if 0 <= indice < len(metas):
                        meta_removida = metas[indice]
                        confirmacao = input(f"Tem certeza que deseja deletar a meta '{meta_removida['tipo']} ({meta_removida['valor']} {meta_removida['unidade']})'? (s/n): ").strip().lower()
                        if confirmacao == 's':
                            metas.pop(indice)
                            salvar_metas_json(metas)
                            print("Meta deletada com sucesso.")
                        else:
                            print("Exclusão cancelada.")
                    else:
                        print("Número inválido. Nenhuma meta foi deletada.")
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número válido.")

        elif opcao_metas == "4":
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