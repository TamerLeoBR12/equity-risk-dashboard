import streamlit as st
import pandas as pd
import yfinance as yf
from streamlit_extras.badges import badge
from países import dados, continents

# O restante do seu código Home.py vem abaixo daqui...

st.link_button("Meu LinkedIn", "https://www.linkedin.com/in/leonardo-cs-silva/")

st.title("Estratégias e Performance Real")

# --- ENTRADA LIVRE DE TICKER ---
# O usuário pode digitar QUALQUER coisa aqui
ticker_input = st.text_input("Digite o Ticker do Ativo (ex: PETR4.SA, IVV, TSLA):", value="IVV")

periodo = st.select_slider("Período de Análise", options=["1mo", "6mo", "1y"])

# O .upper() garante que o ticker vá sempre em maiúsculas para o Yahoo Finance
ticker = ticker_input.upper()

if ticker:
    # Baixamos os dados conforme o que foi digitado
    hist = yf.download(ticker, period=periodo)

    if not hist.empty:
        # Puxamos apenas o fechamento
        # Usamos ['Close'] para garantir que pegamos o preço
        dados_plot = hist['Close']

# --- CÁLCULO DE RETORNO REAL ---
hist = yf.download(ticker, period=periodo)["Close"]
retorno_real = float(hist.iloc[-1] / hist.iloc[0]) - 1

# --- SEÇÃO 2: PARÂMETROS DE RISCO (Otimizado) ---
# Organizamos os seletores em uma linha só para não poluir
st.subheader("Configuração do Modelo (CAPM)")
col_rf, col_beta, col_pais = st.columns(3)

with col_rf:
    rf = st.number_input("Taxa Livre de Risco (Rf) %", value=4.25, step=0.25)
with col_beta:
    beta = st.number_input("Beta do Ativo (β)", value=1.00, step=0.1)
with col_pais:
    # Busca automática do índice para os EUA ou Brasil se existirem na lista
    lista_paises = sorted(dados['Country'].unique())
    try:
        idx_inicial = lista_paises.index("United States")
    except:
        idx_inicial = 0
    pais_ref = st.selectbox("País de Referência (ERP)", lista_paises, index=idx_inicial)

# --- LÓGICA DE CÁLCULO UNIFICADA ---
# Buscamos o ERP do país selecionado
erp_selecionado = dados.loc[dados['Country'] == pais_ref, 'Total Equity Risk Premium'].values[0]
erp = erp_selecionado / 100
# Cálculo do Ke esperado (Teoria)
ke_esperado = (rf / 100) + (beta * erp)

# --- DOWNLOAD E CÁLCULO REAL ---
hist_full = yf.download(ticker_input, period=periodo)

if not hist_full.empty:
    hist = hist_full["Close"]
    retorno_real = float(hist.iloc[-1] / hist.iloc[0]) - 1

    st.divider()

    # --- SEÇÃO 3: ANÁLISE E GRÁFICO ---
    st.subheader(f"Análise: {ticker_input} vs. Risco {pais_ref}")

    m1, m2 = st.columns(2)
    with m1:
        st.metric("Retorno Realizado (Mercado)", f"{retorno_real:.2%}")
    with m2:
        st.metric(f"Retorno Esperado (ERP {pais_ref})", f"{ke_esperado:.2%}")

    # Gráfico de Performance (Sem títulos duplicados)
    st.line_chart(hist)

    # --- CONCLUSÃO ANALÍTICA ---
    if retorno_real > ke_esperado:
        st.success(f"O ativo superou o prêmio de risco exigido para {pais_ref}! Houve geração de Alpha.")
    else:
        st.warning(f"O retorno foi abaixo do risco esperado para {pais_ref}. O prêmio de risco não compensou.")
else:
    st.error("Ativo não encontrado. Verifique o Ticker e tente novamente.")

with st.expander("Guia de Utilização e Fontes de Dados"):
    st.write("""
    ### **1. Tickers (Yahoo Finance)**
    Os nomes dos ativos devem seguir o padrão do **Yahoo Finance**. 
    * **Ações Brasileiras:** Adicione `.SA` ao final (ex: `PETR4.SA`, `VALE3.SA`).
    * **Ações Americanas:** Use o ticker direto (ex: `AAPL`, `IVV`).
    * **Criptomoedas:** Use o par com USD (ex: `BTC-USD`).

    ### **2. Taxa Livre de Risco (Risk-Free Rate)**
    A taxa livre de risco representa o retorno de um investimento com risco zero. 
    * **Onde encontrar:** O padrão de mercado é utilizar o rendimento dos títulos de 10 anos do governo americano (**US Treasury 10Y**). 
    * **Sugestão:** Você pode consultar o valor atualizado na **Página 2 (Calculadora)** deste dashboard ou em sites de notícias financeiras.

    ### **3. Beta do Ativo (β)**
    O Beta mede a sensibilidade de um ativo em relação ao mercado. 
    * **Onde encontrar:** Disponível na aba 'Summary' ou 'Statistics' de qualquer ativo no Yahoo Finance ou Investing.com.
    * **Dica:** Um Beta > 1 indica que o ativo é mais volátil que o mercado; Beta < 1 indica um ativo mais defensivo.

    ### **4. País de Referência (ERP)**
    Para uma análise precisa, selecione o país onde a empresa possui a maior parte de suas operações. 
    * **Importante:** Comparar uma ação brasileira com o prêmio de risco (ERP) dos EUA resultará em um custo de capital subestimado, pois não considera o **Risco País** adicional do Brasil.
    """)