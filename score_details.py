import pandas as pd

# Carregar a planilha unique_activities
df = pd.read_csv("unique_activities.csv")

# Carregar a planilha de atividades inválidas
try:
    invalid_activities = pd.read_csv("invalid_activities.csv")
except pd.errors.EmptyDataError:
    invalid_activities = pd.DataFrame()

# Verificar se há registros em invalid_activities
if not invalid_activities.empty:
    # Filtrar atividades que estão na planilha de atividades inválidas
    # Utilizando as colunas 'firstname', 'lastname', 'name', 'distance', 'moving_time', 'elapsed_time', 'total_elevation_gain', 'type', 'sport_type'
    df = df.merge(invalid_activities, on=['firstname', 'lastname', 'name', 'distance', 'moving_time', 'elapsed_time', 'total_elevation_gain', 'type', 'sport_type'], how='left', indicator=True)
    df = df[df['_merge'] == 'left_only'].drop(columns=['_merge'])

# Função para converter segundos para o formato "X horas e Y minutos"
def seconds_to_hours_minutes(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{int(hours)} horas e {int(minutes)} minutos"

# Função para determinar o fator de pontuação com base no tipo de atividade
def get_score_factor(activity_type):
    if activity_type in ["Walk", "Run"]:
        return 3
    elif activity_type in ["Ride", "EBikeRide"]:
        return 1
    else:
        return 1  # Caso não seja nenhum dos tipos especificados, utiliza 1 como padrão

# Adicionando uma coluna de fator de pontuação ao DataFrame
df["fator_pontuacao"] = df["type"].apply(get_score_factor)

# Agrupar os dados por participante (firstname e lastname) e calcular as métricas
pontuacao_participantes = (
    df.groupby(["firstname", "lastname"])
    .agg(
        total_segundos=("moving_time", "sum"),                                  # Somando moving_time em segundos
        total_quilometros=("distance", lambda x: round(x.sum() / 1000, 2)),       # Convertendo distância para km e arredondando
        quantidade_atividades=("moving_time", "count"),                         # Contando o número de atividades
        quilometros_peso_1=("distance", lambda x: round(x[df["fator_pontuacao"] == 1].sum() / 1000, 2)),  # Somando quilômetros com peso 1
        quilometros_peso_3=("distance", lambda x: round(x[df["fator_pontuacao"] == 3].sum() / 1000, 2))   # Somando quilômetros com peso 3
    )
    .reset_index()
)

# Adicionando uma coluna de horas no formato desejado
pontuacao_participantes["total_horas"] = pontuacao_participantes["total_segundos"].apply(seconds_to_hours_minutes)

# Calcular a pontuação com base na regra especificada:
# 3 pontos por hora de qualquer atividade
# 3 pontos por quilômetro para Walk e Run
# 1 ponto por quilômetro para Ride
pontuacao_participantes["pontuacao"] = round(
    (pontuacao_participantes["total_segundos"] / 3600) * 3 +
    (pontuacao_participantes["quilometros_peso_3"] * 3) +
    (pontuacao_participantes["quilometros_peso_1"] * 1),
    2
)

# Reorganizar as colunas para que a pontuação fique ao lado do nome
colunas_ordenadas = ["firstname", "lastname", "pontuacao", "total_quilometros", "quilometros_peso_1", "quilometros_peso_3", "quantidade_atividades", "total_horas"]
pontuacao_participantes = pontuacao_participantes[colunas_ordenadas]

# Ordenar por pontuação em ordem decrescente
pontuacao_participantes = pontuacao_participantes.sort_values(by="pontuacao", ascending=False)

# Salvar o resultado em um novo CSV
pontuacao_participantes.to_csv("participant_scores_with_details.csv", index=False)

print("Pontuação dos participantes com horas, quilômetros e quantidade de atividades salva em 'participant_scores_with_details.csv' com sucesso.")
