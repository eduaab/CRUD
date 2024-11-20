import os
import csv
import random

arquivo_treino = "treino.csv"

def carregar_treinos():
    try:
        if os.path.exists(arquivo_treino):
            with open(arquivo_treino, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                treinos = []
                for row in reader:
                    row["distancia"] = float(row["distancia"]) 
                    row["tempo"] = int(row["tempo"])  
                    treinos.append(row)
                return treinos
        return []
    except (FileNotFoundError, ValueError) as e:
        print(f"Erro ao carregar treinos: {e}")
        return []
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return []


def salvar_treinos(treinos):
    try:
        with open(arquivo_treino, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["nome", "data", "distancia", "tempo", "localizacao", "clima"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(treinos)
    except PermissionError:
        print("Erro: Não foi possível salvar os treinos. Verifique as permissões do arquivo.")
    except Exception as e:
        print(f"Erro inesperado ao salvar treinos: {e}")

def data_formatada():
    while True:
        try:
            dia = int(input("Insira o dia (1-31): ")).strip()
            if dia < 1 or dia > 31:
                print("Dia inválido. Insira um valor entre 1 e 31.")
                continue
            mes = int(input("Insira o mês (1-12): ")).strip()
            if mes < 1 or mes > 12:
                print("Mês inválido. Insira um valor entre 1 e 12.")
                continue
            ano = int(input("Insira o ano (ex: 2023): ")).strip()
            if ano <1900:
                print("Ano inválido. Insira um ano a partir de 1900.")
                continue
            return f"{dia:02d}/{mes:02d}/{ano:04d}"
        except ValueError:
            print("Entrada inválida. Insira apenas números válidos.")
        except Exception as e:
            print(f"Erro inesperado: {e}")


def dados_treino():
    while True:
        try:
            distancia = float(input("Insira a distância percorrida (em km): ")).strip()
            if distancia < 0:
                print("Distância inválida. Por favor digite uma distância correta.")
                continue
            tempo = int(input("Insira o tempo total (em minutos): ")).strip()
            if tempo < 0:
                print("Cronometragem inválida. Digite um valor válido!")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira números válidos.")
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return 0, 0, "N/A", "N/A"

    try:
        localizacao = str(input("Insira a localização: ")).strip()
        clima = str(input("Insira as condições climáticas: ")).strip()
        return distancia, tempo, localizacao, clima
    except ValueError:
        print(f"Digite uma localização e clima válidos.") 
        return distancia, tempo, "N/A", "N/A"


arquivo_metas = "metas.csv"

def salvar_metas(metas):
    try:
        with open(arquivo_metas, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["tipo", "valor", "unidade"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(metas)
    except PermissionError:
        print("Erro: Não foi possível salvar as metas. Verifique as permissões do arquivo.")
    except Exception as e:
        print(f"Erro inesperado ao salvar metas: {e}")

def carregar_metas():
    try:
        if os.path.exists(arquivo_metas):
            with open(arquivo_metas, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                metas = []
                for row in reader:
                    row["valor"] = float(row["valor"])
                    metas.append(row)
                return metas
        return []
    except (FileNotFoundError, ValueError) as e:
        print(f"Erro ao carregar metas: {e}")
        return []
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return []

def verificar_metas_atingidas(metas, treinos):
    distancia_total = sum(float(treino["distancia"]) for treino in treinos)
    tempo_total = sum(int(treino["tempo"]) for treino in treinos)


    metas_concluidas = []
    for meta in metas[:]:
        if meta["tipo"] == "Distância" and distancia_total >= meta["valor"]:
            print(f"🎉 Parabéns! Você atingiu a meta de {meta['valor']} km!")
            metas_concluidas.append(meta)
            metas.remove(meta)
        elif meta["tipo"] == "Tempo" and tempo_total >= meta["valor"]:
            print(f"🎉 Parabéns! Você atingiu a meta de {meta['valor']} minutos!")
            metas_concluidas.append(meta)
            metas.remove(meta)

    if metas_concluidas:
        salvar_metas(metas)
        print("\nAs seguintes metas foram concluídas e removidas:")
        for meta in metas_concluidas:
            print(f"- {meta['tipo']}: {meta['valor']} {meta['unidade']}")
    else:
        print("Nenhuma meta foi concluída ainda. Continue tentando!")


def um():
    treino = input("Digite o nome do treino que deseja criar: ").strip()
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
        print("Nenhum treino disponível.")
        return

    for i, treino in enumerate(treinos, 1):
        print(f"{i} -> {treino['nome']}")

    try:
        indice = int(input("Escolha o número do treino que deseja atualizar: ")).strip() - 1
        if 0 <= indice < len(treinos):
            escolha_modificacao = int(input(
                "O que você deseja atualizar?\n"
                "1. Nome\n2. Data\n3. Distância\n4. Localização\n5. Clima\nEscolha uma opção: "
            )).strip()
            if escolha_modificacao == 1:
                treinos[indice]["nome"] = input("Digite o novo nome do treino: ").strip()
            elif escolha_modificacao == 2:
                treinos[indice]["data"] = data_formatada()
            elif escolha_modificacao == 3:
                treinos[indice]["distancia"] = float(input("Digite a nova distância do treino (em km): ")).strip()
            elif escolha_modificacao == 4:
                treinos[indice]["localizacao"] = input("Digite a nova localização do treino: ").strip()
            elif escolha_modificacao == 5:
                treinos[indice]["clima"] = input("Digite as novas condições climáticas do treino: ").strip()
            else:
                print("Opção inválida.")
                return

            salvar_treinos(treinos)
            print("Treino atualizado com sucesso.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida. Tente novamente.")

def quatro():
    print("\nTreinos disponíveis:")
    if not treinos:
        print("Nenhum treino para deletar.")
        return

    for i, treino in enumerate(treinos, 1):
        print(f"{i} -> {treino['nome']}")

    try:
        indice = int(input("Escolha o número do treino que deseja deletar: ")).strip() - 1
        if 0 <= indice < len(treinos):
            treino_removido = treinos.pop(indice)
            salvar_treinos(treinos)
            print(f"Treino '{treino_removido['nome']}' deletado com sucesso.")
        else:
            print("Número inválido.")

    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")


def cinco():
    treinos_filtrados = []
    if not treinos:
        print("Nenhum treino registrado")
  
    print("Escolha uma opção de filtro:")
    print("1 -> Filtragem por tempo")
    print("2 -> Filtragem por distância")
    while True:
        opcao_filtro = input("Insira a opção: ").strip()
        if opcao_filtro != "1" and opcao_filtro != "2":
            print("Insira uma opção válida")
        
        else:
            break
    
    while True:
        try:
            
            if opcao_filtro == "1":
                print("\n")
                temp_max = float(input("Insira o tempo máximo: ")).strip()
                temp_min = float(input("Insira o tempo mínimo: ")).strip()

                for treino in treinos:
                    if temp_min <= treino['tempo'] <= temp_max:
                        treinos_filtrados.append(treino)
                    

                if treinos_filtrados:
                    print("\n")
                    print("╒═══════════════════════════╕")
                    print("Treinos filtrados por tempo:")
                    print("╘═══════════════════════════╛")
                    print("\n")
                    
                    
                    for treino in treinos_filtrados:
                        for key, value in treino.items():
                            print(f"{key.capitalize()}: {value}")
                        print("------")
                        print("\n")
                    break
                else:
                    print("Nenhum treino encontrado nesse intervalo")

            elif opcao_filtro == "2":
                print("\n")
                dist_max = float(input("Insira a distância máxima: ")).strip()
                dist_min = float(input("Insira a distância mínima: ")).strip()

                for treino in treinos:
                    if dist_min <= treino['distancia'] <= dist_max:
                        treinos_filtrados.append(treino)

                if treinos_filtrados:
                    print("\n")
                    print("╒═══════════════════════════╕")
                    print("Treinos filtrados por tempo:")
                    print("╘═══════════════════════════╛")
                    
                    for treino in treinos_filtrados:
                        for key, value in treino.items():
                            print(f"{key.capitalize()}: {value}") 
                        print("------")
                        print("\n")
                    break

                else:
                    print("Nenhum treino encontrado nesse intervalo.")
                    break
                
                

        except ValueError:
            print("Insira uma entrada válida.")
            continue

def seis():
    metas = carregar_metas()

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
            tipo_de_meta = input("Escolha uma opção: ").strip()

            if tipo_de_meta == "1":
                distancia = float(input("Insira a meta de distância total (em km): ")).strip()
                metas.append({"tipo": "Distância", "valor": distancia, "unidade": "km"})
                print(f"Meta de distância definida: {distancia} km.")

            elif tipo_de_meta == "2":
                tempo = float(input("Insira a meta de tempo total (em minutos): ")).strip()
                metas.append({"tipo": "Tempo", "valor": tempo, "unidade": "minutos"})
                print(f"Meta de tempo definida: {tempo} minutos.")

            else:
                print("Opção inválida. Tente novamente.")
                continue
            
            salvar_metas(metas)

        elif opcao_metas == "2":
            verificar_metas_atingidas(metas, treinos)
            print("\n---- Metas ----")
            if metas:
                for meta in metas:
                    print(f"{meta['tipo']}: {meta['valor']} {meta['unidade']}")
                
                distancia_total = sum(float(treino["distancia"]) for treino in treinos)
                tempo_total = sum(int(treino["tempo"]) for treino in treinos)

                
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
                            salvar_metas(metas)
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

def sete():
    print("\n")
    print("╒═════════════════════════════════╕")
    print("  SUGESTÃO DE TREINOS ALEATÓRIOS ")
    print("╘═════════════════════════════════╛")
    print("\n")


    if treinos:
        treino_sugerido = random.choice(treinos)
        print("\n🎲 Treino sugerido com base no seu histórico:")
        for chave, valor in treino_sugerido.items():
            print(f"{chave.capitalize()}: {valor}")
    else:
        print("Não há treinos cadastrados para sugerir. Cadastre alguns treinos primeiro.")

def dieta():
    """Carrega as sugestões de treino ou dieta de um arquivo."""
    sugestoes = {}
    try:
        with open("oito.txt", "r", encoding="utf8") as file:
            conteudo = file.read()
            categorias = conteudo.strip().split("\n\n")
            for categoria in categorias:
                linhas = categoria.split("\n")
                chave = linhas[0].replace(":", "").strip()
                sugestoes[chave] = linhas[1:]
        return sugestoes
    except FileNotFoundError:
        print("Erro: O arquivo 'oito.txt' não foi encontrado.")
        return {}
    except Exception as e:
        print(f"Erro ao carregar as sugestões: {e}")
        return {}

def oito():
    try:
        peso = float(input("Digite o seu peso em Kg: ")).strip()
        altura = float(input("Digite sua altura em metros: ")).strip()
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")
        return

    sugestoes = dieta()

    if not sugestoes:
        return


    imc = peso / (altura ** 2)
    if imc < 18.5:
        print("Você está abaixo do peso.")
        estado = "abaixo_peso"
    elif 18.5 <= imc < 24.99:
        print("Você está na classificação normal.")
        estado = "peso_normal"
    elif 25 <= imc < 29.99:
        print("Você está com sobrepeso.")
        estado = "sobrepeso"
    elif imc >= 30:
        print("Você está com obesidade.")
        estado = "obesidade"
    else:
        print("Não conseguimos verificar seu IMC.")
        return

    print(f"Seu IMC é: {imc:.2f}")
    
    with open("funcionalidade.txt", "a", encoding="utf8") as file:
        file.write(f"Peso: {peso:.2f} Kg, Altura: {altura:.2f} m, IMC: {imc:.2f}, Estado: {estado}\n")

    while True:
        escolha = input("Deseja ver sugestões de treino e dieta? (s/n): ").strip().lower()
        if escolha == 's':
            if estado in sugestoes:
                print("\nSugestões para sua categoria:")
                for item in sugestoes[estado]:
                    print(f"- {item}")
                    
            else:
                print("Não foi possível encontrar sugestões para a sua categoria.")
        elif escolha == 'n':
            print("Ok, voltando ao menu principal...")
            break
        else:
            print("Opção inválida. Digite 's' para sim ou 'n' para não.")


def nove():
    print("Saindo do programa. Até mais!")


treinos = carregar_treinos()
def menu():
    while True:
        print('''

███████╗██╗██████╗░███████╗░██╗░░░░░░░██╗░█████╗░██╗░░░░░██╗░░██╗
██╔════╝██║██╔══██╗██╔════╝░██║░░██╗░░██║██╔══██╗██║░░░░░██║░██╔╝
█████╗░░██║██████╔╝█████╗░░░╚██╗████╗██╔╝███████║██║░░░░░█████═╝░
██╔══╝░░██║██╔══██╗██╔══╝░░░░████╔═████║░██╔══██║██║░░░░░██╔═██╗░
██║░░░░░██║██║░░██║███████╗░░╚██╔╝░╚██╔╝░██║░░██║███████╗██║░╚██╗
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

        ''')
        try:
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
            match opcao:
                case '1':
                    um()
                case '2':
                    dois()
                case '3':
                    tres()
                case '4':
                    quatro()
                case '5':
                    cinco()
                case '6':
                    seis()
                case '7':
                    sete()
                case '8':
                    oito()
                case '9':
                    nove()
                    break
                case _:
                    print("Opção inválida. Tente novamente.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

menu()