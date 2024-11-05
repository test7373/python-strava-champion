# Exportar relatórios do Strava Clubs

## Descrição
Este repositório contém scripts para interagir com a API do Strava, coletando e processando dados de atividades de um clube. Utilizamos o GitHub Actions para automatizar a execução dos scripts em intervalos regulares e salvar os resultados como artefatos. Este projeto é útil para criar relatórios detalhados sobre as atividades do clube e gerar pontuações para os participantes.

## Funcionalidades
- Coleta de atividades do clube utilizando a API do Strava.
- Atualização automática de dados através do GitHub Actions a cada hora.
- Geração de relatórios detalhados sobre as atividades e pontuações dos participantes.
- Salvamento automático dos arquivos gerados no repositório.

## GitHub Actions
O workflow do GitHub Actions definido no projeto é responsável pela execução periódica dos scripts. Abaixo está uma descrição de cada etapa:

1. **Workflow Dispatch e Cron Job**
   - O workflow pode ser iniciado manualmente ou é executado automaticamente a cada hora, conforme definido no cron (`0 * * * *`).

2. **Checkout do Repositório**
   - Faz o checkout do repositório para garantir que todos os arquivos estejam acessíveis.

3. **Configuração do Python**
   - Configura o ambiente Python utilizando a versão `3.x`.

4. **Instalação de Dependências**
   - Atualiza o `pip` e instala as dependências necessárias, incluindo `pandas` e `requests`.

5. **Execução dos Scripts**
   - **Buscar Dados do Strava**: Executa o script `app.py` para buscar as atividades do clube utilizando o token de acesso do Strava.
   - **Definir Data de Início da Competição**: Executa o script `start_competition.py` para definir o início da competição.
   - **Calcular Pontuação Detalhada**: Executa o script `score_details.py` para calcular e gerar relatórios detalhados das pontuações dos participantes.

6. **Upload dos Arquivos Gerados**
   - Os arquivos CSV gerados são salvos como artefatos no GitHub, incluindo detalhes das atividades e pontuações.

7. **Commit e Push dos Arquivos CSV**
   - Os arquivos CSV são adicionados, commitados e enviados para o repositório automaticamente, garantindo que os dados estejam sempre atualizados.

## Configuração
### Variáveis de Ambiente
Para que o workflow funcione corretamente, é necessário configurar os seguintes segredos no repositório:
- `STRAVA_CLIENT_ID`: ID do cliente do Strava.
- `STRAVA_CLIENT_SECRET`: Segredo do cliente do Strava.
- `STRAVA_REFRESH_TOKEN`: Token de atualização para obter novos tokens de acesso.
- `GITHUB_TOKEN`: Token automático fornecido pelo GitHub para realizar commits no repositório.

## Como Utilizar
1. Clone o repositório:
   ```sh
   git clone https://github.com/Strava-Amigos-com-Proposito/python-strava-champion.git
   ```
2. Configure as variáveis de ambiente no GitHub (Secrets).
3. Ajuste os scripts conforme necessário.
4. O GitHub Actions cuidará da execução periódica dos scripts e da atualização dos arquivos CSV no repositório.

## Scripts Disponíveis
- **app.py**: Busca e salva as atividades do clube.
- **start_competition.py**: Define a data de início da competição.
- **score_details.py**: Gera pontuação detalhada dos participantes.

## Artefatos Gerados
- `unique_activities.csv`: Atividades únicas coletadas do Strava.
- `unique_activities_old.csv`: Atividades anteriores.
- `participant_scores_with_details.csv`: Pontuação detalhada dos participantes.
- `strava_tokens.csv`: Tokens do Strava utilizados.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request para melhorias ou correções.

## Contato
Para quaisquer dúvidas, entre em contato através do [LinkedIn](https://www.linkedin.com/in/natanielpaiva/).

