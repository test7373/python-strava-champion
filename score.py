import pandas as pd

# Carregar a planilha unique_activities
df = pd.read_csv("unique_activities.csv")

# Agrupar os dados por participante (firstname e lastname) e calcular a pontuação
participant_scores = (
    df.groupby(["firstname", "lastname"])
    .apply(lambda x: round(
        (x["moving_time"].sum() / 3600) +  # Convertendo moving_time para horas e somando os pontos
        (x["distance"].sum() / 1000),      # Convertendo distância para km e somando os pontos
        2                                  # Arredondando o score para duas casas decimais
    ))
    .reset_index(name="score")             # Renomeando a coluna de pontuação
)

# Ordenar por pontuação em ordem decrescente
participant_scores = participant_scores.sort_values(by="score", ascending=False)

# Salvar o resultado em um novo CSV
participant_scores.to_csv("participant_scores.csv", index=False)

print("Pontuação dos participantes salva em 'participant_scores.csv' com sucesso.")
