# Strava Club Activity Data Processor

Este projeto contém scripts em Python que acessam a API do Strava para buscar atividades de um clube, processar esses dados e gerar pontuações para cada participante. O projeto salva os resultados em diferentes arquivos CSV conforme descrito abaixo.

## Arquivos

- **unique_activities.csv**: Este arquivo contém as 200 atividades mais recentes de um clube Strava, incluindo a data em que foram recuperadas. Ele é o primeiro passo do processamento e armazena dados brutos.

- **participant_scores.csv**: Este arquivo contém a pontuação de cada participante, calculada a partir das atividades no `unique_activities.csv`. A pontuação é baseada no tempo em movimento e na distância percorrida.

- **participant_scores_with_details.csv**: Este arquivo inclui informações detalhadas sobre cada participante, incluindo a pontuação, o total de horas, quilômetros e a quantidade de atividades realizadas.

## Scripts

### 1. Baixar e Salvar Atividades do Clube
Este script app.py acessa a API do Strava e salva as atividades do clube no arquivo `unique_activities.csv` com a data de recuperação dos dados. Para usar este script, forneça um token de acesso válido e o ID do clube Strava.

### 2. Calcular Pontuação de Participantes
Este script score.py processa o arquivo `unique_activities.csv` e gera uma pontuação baseada em horas (1 ponto por hora) e distância (1 ponto por quilômetro) para cada participante, salvando o resultado no `participant_scores.csv`.

### 3. Gerar Pontuação com Detalhes
Este script score_details.py calcula a pontuação, total de horas, total de quilômetros e quantidade de atividades para cada participante e salva os dados em `participant_scores_with_details.csv`. A pontuação é arredondada para duas casas decimais e o arquivo é ordenado por pontuação.

## Exemplo de Uso

1. Execute o script app.py para baixar as atividades do clube Strava e salve-as no `unique_activities.csv`.
2. Em seguida, execute o script score.py de cálculo de pontuação para gerar o `participant_scores.csv`.
3. Por fim, execute o script score_details.py para gerar o `participant_scores_with_details.csv`, que inclui pontuação, horas, quilômetros e contagem de atividades.

## Dependências

- `pandas`
- `requests` (para acesso à API do Strava)

Instale as dependências com:

```bash
pip install pandas requests
