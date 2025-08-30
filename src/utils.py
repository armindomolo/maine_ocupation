import json
import pandas as pd
import polars as pl
import numpy as np
import os
"""
Pastas de funcoes para o uso do programa:

"""

# decorador de print:
def printAll(func):
    
    return func
# Carregar Json:
def loarding_json(path: str, key: str = None):
    with open(path, 'r', encoding='utf-8') as f:
        datajson = json.load(f)
    if key:
        return datajson[key]
    return datajson  

# funcao que recebe os dados do formato csv e json:
def dataFrame(path:str ,key:str= None):
    type = path[path.find(".")+1:].lower()
    if type == 'json':
        dataJson = loarding_json(path=path, key=key)
        data = pd.DataFrame(dataJson)
        print('Dados carregados:')
        [print(x) for x in data.columns ]
        return data
    elif type == "csv":
        data = pd.read_csv(path)
        print('Dados carregados:')
        [print(x) for x in data.columns ]
        return data
    else:
        print("Tipo de dados invalidos verifique o 'directorio'")

# Numero de registo por catetoria:s
def print_numero_registro(df:dataFrame, *args) -> None:
   print(df.groupby(*args).size().sort_values(ascending=False))



if __name__== "__main__":
  pass
        