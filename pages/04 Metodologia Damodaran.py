import streamlit as st

st.title("Embasamento Teórico e Metodologia")

st.markdown("""
### **A Referência: Aswath Damodaran**
Este projeto foi desenvolvido utilizando as bases de dados e metodologias do **Prof. Aswath Damodaran** (NYU Stern), amplamente reconhecido como o 'Papa do Valuation'. 

### **Por que esta ferramenta é útil?**
No mercado financeiro, o **Custo de Capital Próprio (Ke)** é o pilar para decisões de investimento. No entanto, calcular o prêmio de risco país (CRP) e o prêmio de risco de mercado (ERP) de forma integrada costuma ser uma tarefa manual e lenta. 

**Este dashboard automatiza:**
* **Extração de Dados:** Coleta em tempo real de ERP e Rating de Crédito de mais de 150 países.
* **Aplicação do Modelo CAPM:** Integração da Taxa Livre de Risco (Rf) com Betas setoriais.
* **Geração de Alpha:** Comparativo instantâneo entre o retorno exigido pela teoria e o retorno entregue pelo mercado (via Yahoo Finance).
""")

st.info("Os dados de risco país são atualizados anualmente com base nos levantamentos publicados pelo Prof. Damodaran em seu portal oficial.")