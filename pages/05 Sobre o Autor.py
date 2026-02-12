import streamlit as st

st.title("Sobre o Autor")

col1, col2 = st.columns([1, 2])


st.markdown("""
### **Perfil Profissional**
Sou **Leonardo Costa Silva**, economista formado pela Universidade Anchieta, entusiasta de Finanças Quantitativas e tecnologia. Este projeto nasceu da minha paixão pelo mercado financeiro.

Atualmente, foco meus estudos no em **Valuation, Gestão de Risco e Análise Macroeconômica** utilizando Python. Acredito que a união entre o rigor teórico (como as metodologias do Prof. Damodaran) e a automação via programação é o que define o futuro da análise de investimentos.

### **Dedicatória e Propósito**
Dedico este trabalho à nova geração de economistas brasileiros e o mercado global como o caminho para um mercado financeiro mais transparente, técnico e eficiente. 

Este projeto é fruto de um estudo profundo sobre as metodologias do **Prof. Aswath Damodaran**, visando democratizar o acesso a análises de prêmio de risco e custo de capital que, muitas vezes, ficam restritas a grandes terminais financeiros de alto custo.

### **Visão de Carreira**
Meu objetivo é atuar no desenvolvimento de modelos quantitativos que auxiliem na tomada de decisão em **Equity Research, Asset Management e Gestão de Risco**.
""") # Fechamento obrigatório das aspas triplas

# Os elementos abaixo devem ficar fora da indentação da coluna ou alinhados conforme seu layout
st.divider()
st.info("Sinta-se à vontade para se conectar comigo no LinkedIn e trocar insights sobre o mercado!")

# Botões de contato
col_btn1, col_btn2 = st.columns(2) # Opcional: colocar os botões lado a lado
with col_btn1:
    st.link_button("Meu LinkedIn", "https://www.linkedin.com/in/leonardo-cs-silva/")
with col_btn2:
    st.link_button("Meu GitHub", "https://github.com/leonardo-cs-silva")