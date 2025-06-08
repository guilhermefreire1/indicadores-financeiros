# main.py

import subprocess
import os

from src.coleta_unificada import coletar_indicadores
from src.salva_sqlite import salvar_em_sqlite

def main():
    print("Iniciando pipeline de indicadores financeiros...")

    try:
        # Coleta de dados
        dados = coletar_indicadores()
        print(f"{len(dados)} registros coletados com sucesso.")

        # Salvando no SQLite
        salvar_em_sqlite(dados)
        print("Dados salvos no banco SQLite com sucesso.")

    except Exception as e:
        print(f"Erro na execução do pipeline: {e}")

if __name__ == "__main__":
    main()

# Caminho do script Streamlit
dashboard_path = os.path.join("dashboard", "dashboard_indicadores.py")

# Executar a dashboard
print("🚀 Iniciando a dashboard...")
subprocess.Popen(["streamlit", "run", dashboard_path])
