import pandas as pd
import sqlite3
import os

def salvar_em_sqlite(df):
    os.makedirs("db", exist_ok=True)

    db_path = "db/indicadores.db"
    df["data"] = pd.to_datetime(df["data"])

    conn = sqlite3.connect(db_path)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS indicadores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data DATE,
        valor REAL,
        indicador TEXT
    )
    """)

    df.to_sql("indicadores", conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()

    print("✅ Dados salvos no banco SQLite com sucesso: db/indicadores.db")
