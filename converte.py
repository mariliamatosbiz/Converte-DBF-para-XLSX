import pandas as pd
from dbfread import DBF
import os
import time

def dbf_to_excel(dbf_files):
    try:
        if not isinstance(dbf_files, list):
            raise ValueError("A entrada deve ser uma lista de arquivos DBF.")
        
        for dbf_file in dbf_files:
            if not os.path.isfile(dbf_file):
                print(f"Aviso: O arquivo DBF '{dbf_file}' não foi encontrado.")
                continue
            
            start_time = time.time()
            
            table = DBF(dbf_file)
            df = pd.DataFrame(iter(table))
            excel_file = os.path.splitext(dbf_file)[0] + ".xlsx"
            df.to_excel(excel_file, index=False)
            
            end_time = time.time()
            duration = end_time - start_time
            
            print(f"Arquivo DBF '{dbf_file}' convertido e salvo em '{excel_file}' com sucesso. Tempo decorrido: {duration:.2f} segundos.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

dbf_files = [
    r"C:\Users\Marilia\Documents\converte\OS.dbf",
    r"C:\Users\Marilia\Documents\converte\Caixa.dbf"
]  # Lista de arquivos DBF

dbf_to_excel(dbf_files)
