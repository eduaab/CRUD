import os
os.system('cls')
import random
from datetime import datetime, timedelta

historico = {
    "agachamento": [datetime(2024, 10, 28), datetime(2024, 10, 25)],
    "flexão": [datetime(2024, 10, 29)],
    "abdominal": [datetime(2024, 10, 30)],
    "corrida": [datetime(2024, 10, 24)],
}

exercicios_disponiveis = [
    "agachamento",
    "flexão",
    "abdominal",
    "corrida",
    "burpee",
    "prancha",
    "jumping jacks",
]

def sugerir_treino(historico, exercicios, dias_para_evitar=7):
    data_limite = datetime.now() - timedelta(days=dias_para_evitar)
    
    exercicios_sugeridos = [
        exercicio for exercicio in exercicios
        if exercicio not in historico or all(data < data_limite for data in historico[exercicio])
    ]

    treino_sugerido = random.sample(exercicios_sugeridos, k=min(3, len(exercicios_sugeridos)))
    return treino_sugerido

treino = sugerir_treino(historico, exercicios_disponiveis)
print("Treino sugerido:", treino)