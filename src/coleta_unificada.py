import requests
import pandas as pd
from datetime import datetime
import os

def coletar_indicadores():
    def coletar_sgs(codigo_serie, data_inicio, data_fim):
        url = (
            f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_serie}/dados"
            f"?formato=json&dataInicial={data_inicio}&dataFinal={data_fim}"
        )
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        df = pd.DataFrame(dados)
        df["data"] = pd.to_datetime(df["data"], dayfirst=True)
        df["valor"] = df["valor"].str.replace(",", ".").astype(float)
        return df

    indicadores = {
        "selic": 1178,
        "ipca": 433,
        "dolar": 1
    }

    data_inicio = "01/01/2022"
    data_fim = datetime.today().strftime("%d/%m/%Y")
    os.makedirs("data", exist_ok=True)

    tabela_unificada = []

    for nome, codigo in indicadores.items():
        print(f"🔄 Coletando {nome.upper()}...")
        try:
            df = coletar_sgs(codigo, data_inicio, data_fim)
            df["indicador"] = nome
            tabela_unificada.append(df)
        except Exception as e:
            print(f"❌ Erro ao coletar {nome}: {e}")

    df_final = pd.concat(tabela_unificada, ignore_index=True)
    df_final.to_csv("data/indicadores.csv", index=False)
    print("✅ Arquivo unificado salvo em 'data/indicadores.csv'")
    return df_final
