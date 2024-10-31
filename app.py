import requests
import csv
import os
from datetime import datetime
import pandas as pd

# Configurações da API do Strava
CLIENT_ID = os.getenv("STRAVA_CLIENT_ID")
CLIENT_SECRET = os.getenv("STRAVA_CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("STRAVA_REFRESH_TOKEN")
CLUB_ID = '1304613'  # Substitua pelo seu ID do clube

# Função para buscar o access token automaticamente
def get_access_token():
    token_url = "https://www.strava.com/oauth/token"
    payload = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'refresh_token': REFRESH_TOKEN,
        'grant_type': 'refresh_token'
    }
    response = requests.post(token_url, data=payload)
    response_data = response.json()
    return response_data.get('access_token')

# Obtém o access token
ACCESS_TOKEN = get_access_token()
# Substitua pelo seu token de acesso
CLUB_ID = '1304613'  # Substitua pelo seu ID do clube

# Endpoint da API do Strava
API_URL = f'https://www.strava.com/api/v3/clubs/{CLUB_ID}/activities'
HEADERS = {'Authorization': f'Bearer {ACCESS_TOKEN}'}

# Busca atividades do clube
response = requests.get(API_URL, headers=HEADERS, params={'per_page': 138})
activities = response.json()

# Verifica se a resposta é uma lista de atividades
if not isinstance(activities, list):
    print("Erro: resposta inesperada da API do Strava")
    activities = []

# Salva as atividades em um CSV com a data atual, adicionando ao arquivo se ele já existir
csv_file_1 = 'club_activities.csv'
current_date = datetime.now().strftime('%Y-%m-%d')

file_exists = os.path.isfile(csv_file_1)

with open(csv_file_1, mode='a', newline='') as file:
    writer = csv.writer(file)
    # Cabeçalho (somente se o arquivo não existir)
    if not file_exists:
        writer.writerow([
            'firstname', 'lastname', 'name', 'distance', 'moving_time',
            'elapsed_time', 'total_elevation_gain', 'type', 'sport_type', 'current_date'
        ])
    # Registros
    for activity in activities:
        writer.writerow([
            activity.get('athlete', {}).get('firstname', ''),
            activity.get('athlete', {}).get('lastname', ''),
            activity.get('name', ''),
            activity.get('distance', 0),
            activity.get('moving_time', 0),
            activity.get('elapsed_time', 0),
            activity.get('total_elevation_gain', 0),
            activity.get('type', ''),
            activity.get('sport_type', ''),
            current_date
        ])

# Lê o CSV e salva em outro arquivo apenas registros não repetidos
csv_file_2 = 'unique_activities.csv'

# Carrega os dados no Pandas
df = pd.read_csv(csv_file_1)

# Remove registros duplicados considerando os campos especificados
filtered_df = df.drop_duplicates(subset=[
    'firstname', 'lastname', 'name', 'distance', 'moving_time',
    'elapsed_time', 'total_elevation_gain', 'type', 'sport_type'
])

# Salva o DataFrame filtrado em um novo CSV
filtered_df.to_csv(csv_file_2, index=False)

print(f'Atividades salvas em: {csv_file_1}')
print(f'Atividades filtradas e salvas em: {csv_file_2}')
