# OBS.:  Este arquivo não pode ser jupyter notebook, pois é necessário que seja um arquivo .py para a biblioteca streamlit ser exeutada

import streamlit as st

# dados iniciais de cada campo = 0
dados_numericos = {'host_total_listings_count': 0, 'latitude': 0, 'longitude': 0, 'accommodates': 0, 'bathrooms': 0, 'bedrooms': 0, 'beds': 0, 'extra_people': 0, 'minimum_nights': 0, 'number_of_reviews': 0, 'mes': 0, 'ano': 0, 'qntd_amenities': 0}

dados_bool = {'host_is_superhost': 0, 'instant_bookable': 0, 'is_business_travel_ready': 0}

dados_classificatorios = {'property_type': ['Apartment', 'Bed and breakfast', 'Condominium', 'Guest suite', 'Guesthouse', 'Hostel', 'House', 'Loft', 'Outros', 'Serviced apartment'], 'room_type': ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room'], 'bed_type': ['Airbed', 'Couch', 'Futon', 'Pull-out Sofa', 'Real Bed'], 'cancellation_policy': ['Estritos', 'flexible', 'moderate', 'strict_14_with_grace_period']}

# Criando Botões

for item in dados_numericos:

    # Armazenar preenchimento dos campos com os novos dados para execução

    # Tratando valores para 5 casas decimais de preenchimento
    if item == 'latitude' or item == 'longitude':
        valor = st.number_input(f'{item}', step=0.00001, value=0.0, format='%.5f')
        # .number_imput(rotulo do campo) -> campo numérico
        # step -> variação ao clicar para aumentar ou diminuir valor no campo
        # value -> valor padão de início (ex: 0 valores inteiro, 0.0 valores float)
        # format -> será usado para dizer quantas casa decimais deverá ter o valor no campo (código de formatação diferente do convencional)
    
    # Tratando valores para 2 casas decimais de preenchimento
    elif item == 'extra_people':
        valor = st.number_input(f'{item}', step=0.01, value=0.0)

    # Tratando valores inteiros de preenchimento
    else:
        valor = st.number_input(f'{item}', step=1, value=0)


for item in dados_bool:
    valor = st.selectbox(f'{item}', ('Sim', 'Não'))
    # .selectbox(rotulo do campo, tupla com os valores selecionaveis) -> campo de seleção de valores

    # Armazenar preenchimento dos campos para execução com os novos dados
    if valor == 'Sim':
        dados_bool[item] = 1
    elif valor == 'Não':
        dados_bool[item] = 0

for item in dados_classificatorios:
    valor = st.selectbox(f'{item}', dados_classificatorios[item])

botao = st.button('Prever Valor do Imóvel')


# Rodar arquivo no Anaconda Prompt

# PASSO A PASSO: entrar no anacondaPrompt > navegar até a pasta deste arquivo > executar 'streamlit run NomeDoArquivo.py' 