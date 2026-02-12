import streamlit as st
import pandas as pd
from streamlit_extras.badges import badge
from países import dados, continents

st.link_button("Meu LinkedIn", "https://www.linkedin.com/in/leonardo-cs-silva/")

st.title("Calculadora de Custo de Capital (Modelo Damodaran)")

# --- INPUTS DO USUÁRIO ---
with st.container():
    st.subheader("Parâmetros de Valuation")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Damodaran costuma usar o Treasury de 10 anos como Risk-Free
        rf = st.number_input("Taxa Livre de Risco (Rf) %", value=4.25, help="Sugestão: US Treasury 10Y")
    
    with col2:
        beta = st.number_input("Beta do Ativo (β)", value=1.00, step=0.1, help="Medida de risco sistemático")
        
    with col3:
        # Buscamos os países únicos da sua planilha
        lista_paises = dados['Country'].unique()
        pais_selecionado = st.selectbox("País de Operação", lista_paises, index=20) # 20 costuma ser Brasil/EUA dependendo da ordem

# --- LÓGICA DE CÁLCULO ---
# Localizamos o ERP do país selecionado na sua base
erp_pais = dados.loc[dados['Country'] == pais_selecionado, 'Total Equity Risk Premium'].values[0]

erp = (erp_pais / 100)

# Cálculo do Ke (Cost of Equity)
# Fórmula: Rf + (Beta * ERP)
ke = (rf / 100) + (beta * erp)

# --- RESULTADO ---
st.divider()
st.markdown(f"### O Custo de Capital Próprio (Ke) para este ativo em **{pais_selecionado}** é:")
st.header(f"{ke:.2%}")

st.subheader("Análise de Sensibilidade (Impacto do Risco País)")

# Criamos variações de risco (ex: -2% até +2% do valor atual)
variacoes = [-0.02, -0.01, 0, 0.01, 0.02]
tabela_sensibilidade = []

for var in variacoes:
    erp_simulado = erp + var
    ke_simulado = (rf / 100) + (beta * erp_simulado)
    tabela_sensibilidade.append({
        "Variação no Risco": f"{var:+.0%}",
        "ERP Simulado": f"{erp_simulado:.2%}",
        "Novo Ke (Custo de Capital)": f"{ke_simulado:.2%}"
    })

df_sensibilidade = pd.DataFrame(tabela_sensibilidade)
st.table(df_sensibilidade)

st.caption("Nota: Veja como pequenas mudanças no risco país impactam drasticamente o retorno exigido pelo investidor.")

# --- EXPLICAÇÃO TÉCNICA (Estilo Damodaran) ---
with st.expander("Entenda o Cálculo"):
    st.write(f"""
    De acordo com a metodologia de Damodaran, o custo de capital próprio reflete o custo de oportunidade.
    No seu caso, estamos somando a taxa livre de risco de **{rf}%** ao prêmio de risco de mercado de **{erp:.2%}**, 
    ajustado pelo risco específico do ativo (Beta de **{beta}**).
    """)