import pandas as pd

# Carregar o arquivo CSV
csv_file = "unique_activities.csv"
data = pd.read_csv(csv_file)

# Inicializa uma lista para armazenar as linhas que não passam nas validações
invalid_rows = []

# Função para calcular o pace (min/km)
def calculate_pace(moving_time, distance):
    if distance == 0:
        return float('inf')  # Retorna um valor infinito caso a distância seja zero
    pace = (moving_time / 60) / (distance / 1000)  # Pace em min/km
    return pace

# Validação 1: Verificar se por dia a atividade com o sport_type == 'WeightTraining' tem moving_time > 2h30min
# weight_training_daily = data[data['sport_type'] == 'WeightTraining'].groupby('current_date')['moving_time'].sum()
# for date, total_time in weight_training_daily.items():
#     if total_time > 2.5 * 3600:
#         excess_hours = (total_time - 2.5 * 3600) / 3600
#         invalid_rows.extend(data[(data['sport_type'] == 'WeightTraining') & (data['current_date'] == date)]
#                            .assign(validation_issue='Validação 1: WeightTraining com moving_time diário > 2h30min', excess_hours=excess_hours).to_dict('records'))

# Validação 2: Verificar se nas atividades do type == 'Walk' está tendo um pace maior que 15 ou menor que 8 min/km
for index, row in data.iterrows():
    if row['type'] == 'Walk':
        pace = calculate_pace(row['moving_time'], row['distance'])
        if pace > 20 or pace < 8:
            row['validation_issue'] = 'Validação 2: Walk com pace fora do intervalo [8, 20]'
            row['pace'] = pace
            invalid_rows.append(row)

# Validação 3: Verificar se nas atividades do type == 'Run' está tendo um pace maior que 12 ou menor que 4 min/km
for index, row in data.iterrows():
    if row['type'] == 'Run':
        pace = calculate_pace(row['moving_time'], row['distance'])
        if pace > 12 or pace < 4:
            row['validation_issue'] = 'Validação 3: Run com pace fora do intervalo [4, 12]'
            row['pace'] = pace
            invalid_rows.append(row)

# Criar um DataFrame com as linhas que não passaram nas validações
invalid_data = pd.DataFrame(invalid_rows)

# Salvar as linhas inválidas em um novo CSV
invalid_data.to_csv("invalid_activities.csv", index=False)

print("Validações concluídas e atividades inválidas salvas no arquivo 'invalid_activities.csv'")
