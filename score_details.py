import pandas as pd

# Carregar a planilha unique_activities
df = pd.read_csv("unique_activities.csv")

# Agrupar os dados por participante (firstname e lastname) e calcular as métricas
participant_scores = (
    df.groupby(["firstname", "lastname"])
    .agg(
        total_hours=("moving_time", lambda x: round(x.sum() / 3600, 2)),       # Convertendo moving_time para horas e arredondando
        total_kilometers=("distance", lambda x: round(x.sum() / 1000, 2)),    # Convertendo distância para km e arredondando
        activity_count=("moving_time", "count")                                # Contando o número de atividades
    )
    .reset_index()
)

# Calcular a pontuação com base em horas e quilômetros, arredondando para duas casas
participant_scores["score"] = round(participant_scores["total_hours"] + participant_scores["total_kilometers"], 2)

# Ordenar por pontuação em ordem decrescente
participant_scores = participant_scores.sort_values(by="score", ascending=False)

# Salvar o resultado em um novo CSV
participant_scores.to_csv("participant_scores_with_details.csv", index=False)

print("Pontuação dos participantes com horas, quilômetros e quantidade de atividades salva em 'participant_scores_with_details.csv' com sucesso.")
