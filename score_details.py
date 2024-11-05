import pandas as pd

# Carregar a planilha unique_activities
df = pd.read_csv("unique_activities.csv")

# Função para converter segundos para o formato "X horas e Y minutos"
def seconds_to_hours_minutes(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{int(hours)} horas e {int(minutes)} minutos"

# Função para determinar o fator de pontuação com base no tipo de atividade
def get_score_factor(activity_type):
    if activity_type in ["Walk", "Run"]:
        return 2
    elif activity_type == "Ride":
        return 1
    else:
        return 1  # Caso não seja nenhum dos tipos especificados, utiliza 1 como padrão

# Adicionando uma coluna de fator de pontuação ao DataFrame
df["score_factor"] = df["type"].apply(get_score_factor)

# Agrupar os dados por participante (firstname e lastname) e calcular as métricas
participant_scores = (
    df.groupby(["firstname", "lastname"])
    .agg(
        total_seconds=("moving_time", "sum"),                                  # Somando moving_time em segundos
        total_kilometers=("distance", lambda x: round(x.sum() / 1000, 2)),     # Convertendo distância para km e arredondando
        activity_count=("moving_time", "count"),                               # Contando o número de atividades
        total_score_factor=("score_factor", "sum")                             # Somando os fatores de pontuação
    )
    .reset_index()
)

# Adicionando uma coluna de horas no formato desejado
participant_scores["total_hours"] = participant_scores["total_seconds"].apply(seconds_to_hours_minutes)

# Calcular a pontuação com base em horas, quilômetros e o fator de pontuação, arredondando para duas casas
participant_scores["score"] = round((participant_scores["total_seconds"] / 3600 + participant_scores["total_kilometers"]) * participant_scores["total_score_factor"], 2)

# Ordenar por pontuação em ordem decrescente
participant_scores = participant_scores.sort_values(by="score", ascending=False)

# Salvar o resultado em um novo CSV
participant_scores.drop(columns=["total_seconds", "total_score_factor"], inplace=True)  # Removendo colunas desnecessárias para simplificar o CSV
participant_scores.to_csv("participant_scores_with_details.csv", index=False)

print("Pontuação dos participantes com horas, quilômetros e quantidade de atividades salva em 'participant_scores_with_details.csv' com sucesso.")
