import pandas as pd
from datetime import datetime

# Defina a data para filtrar
filter_date = "2024-11-10"  # Data em formato YYYY-MM-DD
filter_date = datetime.strptime(filter_date, '%Y-%m-%d')

# Ler o arquivo CSV de entrada
input_csv = 'unique_activities_old.csv'  # Nome do arquivo CSV de entrada
output_csv = 'unique_activities.csv'  # Nome do arquivo CSV de saída

df = pd.read_csv(input_csv)

# Converta a coluna 'current_date' para datetime
# Supondo que o formato da data seja YYYY-MM-DD
# Caso o formato seja diferente, ajuste o formato no 'to_datetime'
df['current_date'] = pd.to_datetime(df['current_date'], format='%Y-%m-%d')

# Filtrar registros após a data especificada
df_filtered = df[df['current_date'] > filter_date]

# Salvar o conteúdo filtrado em outro CSV
df_filtered.to_csv(output_csv, index=False)

print(f"Registros filtrados salvos em '{output_csv}'")
