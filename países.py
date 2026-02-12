import pandas as pd, yfinance as yf


dados = pd.read_excel(r"C:\Users\RICARDO\Downloads\Damodaran.xls", sheet_name="ERPs by country", skiprows=7)
dados = dados.iloc[:157, :6]
dados = dados.astype({"Rating-based Default Spread": float,
              "Total Equity Risk Premium": float,
                      	"Country Risk Premium": float})

#dados["Country Risk Premium"] = pd.to_numeric(dados["Country Risk Premium"])

dados = pd.read_excel(r"C:\Users\RICARDO\Downloads\Damodaran.xls", sheet_name="ERPs by country", skiprows=7)
dados = dados.iloc[:157, :6]
dados = dados.astype({"Rating-based Default Spread": float,
              "Total Equity Risk Premium": float,
                      	"Country Risk Premium": float})

#dados["Country Risk Premium"] = pd.to_numeric(dados["Country Risk Premium"])

colunas_financeiras = ["Rating-based Default Spread", "Total Equity Risk Premium", "Country Risk Premium"]
dados[colunas_financeiras] = dados[colunas_financeiras] * 100

dados

continents = dados.groupby("Continents")["Total Equity Risk Premium"].mean()
continents = continents.to_frame()
continents.sort_values(by="Total Equity Risk Premium", inplace=True)

continents.style.format('{:,.2%}'. format)