import streamlit as st
from streamlit_extras.badges import badge
from países import dados, continents

# O restante do seu código Home.py vem abaixo daqui...

st.link_button("Meu LinkedIn", "https://www.linkedin.com/in/leonardo-cs-silva/")

# Informações do Projeto

st.set_page_config(layout="wide", page_title="Equity Risk Premium e Country Risk Premium")

st.title("Global Equity Risk & Performance Analytics")
st.text("Dashboard de dados econômicos da Universidade de Nova York (NYU) - Aswalth Damodaran")
st.text("Equity Risk Premium e Country Risk Premium")
st.divider()

extra = st.toggle("País específico")


brazil = round(dados[dados["Country"] == "Brazil"]["Total Equity Risk Premium"])
usa = round(dados[dados["Country"] == "United States"]["Total Equity Risk Premium"])

delta1 = float(brazil) - float(usa)
delta2 = float(usa) - float(brazil)

# Gráficos

# extra = st.checkbox("País extra")
# st.radio("Países", ["Brazil", "USA","Finland"]) utilizar com poucas opções
# extra = st.toggle("País extra")
# st.multiselect("Escolha Um País", ["Brazil", "USA","Finland"])

if extra:

    country = st.selectbox("Escolha Um País", list(dados["Country"].unique()))
    pais_extra = round(dados[dados["Country"] == country]["Total Equity Risk Premium"])

    delta3 = round(float(pais_extra) - float(usa), 2)

    with st.container(border=True):

        col3, col4, col5 = st.columns(3)

        col3.metric(label='USA (%)', value=usa, delta=delta2, delta_color="inverse")
        col4.metric(label='Brazil (%)', value=brazil, delta=delta1, delta_color="inverse")
        col5.metric(label=f"{country} (%)", value=pais_extra, delta=delta3, delta_color="inverse")
        st.table(dados[dados["Country"] == country])
        

else:
    with st.container(border=True):

        col1, col2 = st.columns(2)

        col1.metric(label='USA (%)', value=usa, delta=delta2, delta_color="inverse")
        col2.metric(label='Brazil (%)', value=brazil, delta=delta1, delta_color="inverse")

st.text("Top 15 países mais seguros")       
st.table(dados.sort_values("Total Equity Risk Premium").head(15))

col1, col2 = st.columns(2)

col1.table(continents)
col2.bar_chart(continents, horizontal=True, height=400)

# st.sidebar.header("Título do Sibebar")

# with st.sidebar.container(border=True):
#     st.metric("Brazil", 10)

# st.sidebar.text("Área tb utilizavel")

st.divider()
with st.expander("Saiba mais sobre a metodologia e o intuito deste trabalho"):
    st.markdown(f"""
    ### **Sobre este Projeto**
    Este dashboard foi desenvolvido com o intuito de monitorar e comparar o **Risco de Patrimônio Líquido (ERP)** entre diferentes nações e continentes. 
    A análise é fundamental para decisões de alocação de capital e avaliação de empresas (Valuation).

    ### **Metodologia e Fonte**
    Os dados são extraídos das publicações do **Prof. Aswath Damodaran**, da **New York University (NYU Stern)**. 
    Damodaran é a maior referência mundial em avaliação de ativos, e seus dados fornecem uma base padronizada para comparar o custo de capital globalmente.

    ### **Conceitos Chave**
    * **Equity Risk Premium (ERP):** É o retorno adicional que um investidor exige para investir em ações (ativos de risco) em comparação com uma taxa livre de risco (como os títulos do Tesouro Americano).
    * **Country Risk Premium (CRP):** É o prêmio adicional que reflete o risco específico de investir em um determinado país, considerando fatores políticos, econômicos e financeiros (muitas vezes baseado no *Default Spread* da dívida soberana).
    """)