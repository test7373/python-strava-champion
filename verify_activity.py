import pandas as pd

# Carregar o arquivo CSV
csv_file = "unique_activities.csv"
data = pd.read_csv(csv_file)

# Converter moving_time de segundos para horas e minutos
def convert_moving_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{hours}h {minutes}min"

# Converter distance de metros para quilômetros (arredondado para duas casas decimais)
def convert_distance(distance):
    return round(distance / 1000, 2)

# Inicializa uma lista para armazenar as linhas que não passam nas validações
invalid_rows = []

# Função para calcular o pace (min/km)
def calculate_pace(moving_time, distance):
    if distance == 0:
        return float('inf')  # Retorna um valor infinito caso a distância seja zero
    pace = (moving_time / 60) / (distance / 1000)  # Pace em min/km
    return round(pace, 2)

# Validação 2: Verificar se nas atividades do type == 'Walk' está tendo um pace maior que 20 ou menor que 8 min/km
for index, row in data.iterrows():
    if row['type'] == 'Walk':
        pace = calculate_pace(row['moving_time'], row['distance'])
        if pace > 20 or pace < 8:
            row['validation_issue'] = 'Validação 2: Walk com pace fora do intervalo [8, 20]'
            row['pace'] = pace
            row['moving_time_converted'] = convert_moving_time(row['moving_time'])
            row['distance_converted_km'] = convert_distance(row['distance'])
            invalid_rows.append(row)

# Validação 3: Verificar se nas atividades do type == 'Run' está tendo um pace maior que 12 ou menor que 4 min/km
for index, row in data.iterrows():
    if row['type'] == 'Run':
        pace = calculate_pace(row['moving_time'], row['distance'])
        if pace > 12 or pace < 4:
            row['validation_issue'] = 'Validação 3: Run com pace fora do intervalo [4, 12]'
            row['pace'] = pace
            row['moving_time_converted'] = convert_moving_time(row['moving_time'])
            row['distance_converted_km'] = convert_distance(row['distance'])
            invalid_rows.append(row)

# Criar um DataFrame com as linhas que não passaram nas validações
invalid_data = pd.DataFrame(invalid_rows)

# Salvar as linhas inválidas em um novo CSV
invalid_data.to_csv("invalid_activities.csv", index=False)

print("Validações concluídas e atividades inválidas salvas no arquivo 'invalid_activities.csv'")
