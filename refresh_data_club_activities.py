import csv

def copiar_csv(arquivo_origem, arquivo_destino):
    with open(arquivo_origem, 'r', newline='', encoding='utf-8') as csv_origem:
        leitor = csv.reader(csv_origem)
        
        with open(arquivo_destino, 'w', newline='', encoding='utf-8') as csv_destino:
            escritor = csv.writer(csv_destino)
            
            for linha in leitor:
                escritor.writerow(linha)

# Exemplo de uso
arquivo_origem = 'unique_activities_old.csv'
arquivo_destino = 'club_activities.csv'
copiar_csv(arquivo_origem, arquivo_destino)

print(f'Dados copiados de {arquivo_origem} para {arquivo_destino} com sucesso!')