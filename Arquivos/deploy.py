# OBS.:  Este arquivo não pode ser jupyter notebook, pois é necessário que seja um arquivo .py para a biblioteca streamlit ser exeutada

# CRIANDO MICROSITE COM CAMPOS DE PREENCHIMENTO COM OS DADOS DO AIRNBN PARA CALCULAR VALOR

import streamlit as st
import pandas as pd
import joblib

# dados iniciais de cada campo = 0
dados_numericos = {'host_total_listings_count': 0, 'latitude': 0, 'longitude': 0, 'accommodates': 0, 'bathrooms': 0, 'bedrooms': 0, 'beds': 0, 'extra_people': 0, 'minimum_nights': 0, 'number_of_reviews': 0, 'mes': 0, 'ano': 0, 'qntd_amenities': 0}

dados_bool = {'host_is_superhost': 0, 'instant_bookable': 0}

dados_classificatorios = {'property_type': ['Apartment', 'Bed and breakfast', 'Condominium', 'Guest suite', 'Guesthouse', 'Hostel', 'House', 'Loft', 'Outros', 'Serviced apartment'], 'room_type': ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room'], 'bed_type': ['Airbed', 'Couch', 'Futon', 'Pull-out Sofa', 'Real Bed'], 'cancellation_policy': ['Estritos', 'flexible', 'moderate', 'strict_14_with_grace_period']}

# Criando dicionário auxiliar dos dados_classificatorios para encontrar o valor das variáveis dummie
dic_aux = {}
for item in dados_classificatorios:
    for valor in dados_classificatorios[item]:
        # será criado um dict juntando a chave de 'dados_classificatorios' e cada item da lista que se refere, inserindo a essa nova chave o valor 0. Resultado: {'property_type_Apartment': 0, 'property_type_Bed and breakfast': 0, ...}
        dic_aux[f'{item}_{valor}'] = 0

# CRIANDO CAMPOS DE PREENCHIMENTO E BOTÃO

# Armazenar preenchimento dos campos numéricos com os novos dados para execução
for item in dados_numericos:

    # Tratando valores para 5 casas decimais de preenchimento
    if item == 'latitude' or item == 'longitude':  # caso este item seja selecionado, seu valor será alterado para o valor inserido no input
        valor = st.number_input(f'{item}', step=0.00001, value=0.0, format='%.5f')
        # .number_imput(rotulo do campo) -> campo numérico
        # step -> variação ao clicar para aumentar ou diminuir valor no campo
        # value -> valor padão de início (ex: 0 valores inteiro, 0.0 valores float)
        # format -> será usado para dizer quantas casa decimais deverá ter o valor no campo (código de formatação diferente do convencional)
    
    # Tratando valores para 2 casas decimais de preenchimento
    elif item == 'extra_people': # caso este item seja selecionado, seu valor será alterado para o valor inserido no input
        valor = st.number_input(f'{item}', step=0.01, value=0.0)

    # Tratando valores inteiros de preenchimento
    else:  # caso este item seja selecionado, seu valor será alterado para o valor inserido no input
        valor = st.number_input(f'{item}', step=1, value=0)


# Armazenar preenchimento dos campos booleanos com os novos dados para execução
for item in dados_bool:
    valor = st.selectbox(f'{item}', ('Sim', 'Não'))
    # .selectbox(rotulo do campo, tupla com os valores selecionaveis) -> campo de seleção de valores

    if valor == 'Sim': # caso este item seja selecionado, seu valor será alterado para 1
        dados_bool[item] = 1
    elif valor == 'Não': # caso este item seja selecionado, seu valor será alterado para 0
        dados_bool[item] = 0 


# Armazenar preenchimento dos campos de classificação com os novos dados para execução

for item in dados_classificatorios:
    valor = st.selectbox(f'{item}', dados_classificatorios[item])
    dic_aux[f'{item}_{valor}'] = 1 # caso este item seja selecionado, seu valor será alterado para 1

botao = st.button('Prever Valor do Imóvel')

# CRIANDO FUNCIONALIDADE DO BOTÃO

if botao: # Caso o botão receba a ação do click
    # Juntando todos os dicionários com os valores alterados/inseridos nos campos em um df
    dic_aux.update(dados_numericos)
    dic_aux.update(dados_bool)
    eixo_x = pd.DataFrame(dic_aux, index=[0]) # index necessário, além de ser uma lista, então colocamos 0 pq so terá uma linha esse df

    # A ordem das colunas do df eixo_x deve ser a mesma do df exportado em .csv no final do arquivo de dessafio, então:

    # Criando lista com o nome das colunas do arquivo .csv
    dados_finais = pd.read_csv('DadosFinais.csv')
    colunas = list(dados_finais.columns)[1:] # Não irei incluir a priemira coluna, pois se trata do índice criado ao ler o arquivo .csv

    # Reordenando colunas do df eixo_x respectivamente com a lista de clunas do arquivo .csv
    eixo_x = eixo_x[colunas] # já que as colunas são as mesmas, nenhuma alteração será feita nesta linha, apenas acontecerá a reordenação
    # caso as colunas não estiverem na mesma ordem a ferramenta de aplicação não funcionará

    # Inserindo modelo para prever o preço
    modelo = joblib.load('modelo.joblib') # selecionando modelo na pasta

    # Gerando a previsão do preço
    preço = modelo.predict(eixo_x)

    # Imprimindo a previsão na tela
    st.write(preço[0])


# Rodar arquivo no Anaconda Prompt

# PASSO A PASSO: abrir AnacondaPrompt > navegar até a pasta deste arquivo > executar 'streamlit run NomeDoArquivo.py' 