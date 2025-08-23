# Obtencao dos dados
import os
import requests
import polars as pl
import pandas as pd
import json

## Criacao da classe para obter os dados:
class DataClient:
    def __init__(self, url: str):
        self.url = url
        self.data = None
        self.df = None

    # criando metodo de busca da informacao
    def source_data(self):
        """fazer aquisicao da API"""
        response = requests.get(self.url)
        if response.status_code == 200:
            self.data = response.json()
            print("dados baixados com sucesso")
            return self.data
        else:
            raise Exception(f"Erro ao consultat os dados {response.status_code}")

    # busca os dados e salva os dados brutos:
    def save_json(self,path):
        """fazer aquisicao da API"""
        response = requests.get(self.url)
        if response.status_code == 200:
            print("dados acessados com sucesso")
            self.data = response.json()
            with open(path, "w", encoding= "utf-8") as r:
                json.dump(self.data,r , indent=4, ensure_ascii=False)
            print("dados baixados com sucesso")
            #return self.datas
        else:
            raise Exception(f"Erro ao consultat os dados {response.status_code}")
        

    def to_dataframe(self):
        columns = []
        """Converter os valores em dataFrame"""
        if not self.data:
            raise Exception("dados nao baixados.execute o source data para obtelas")
        elif self.data:
            self.df = pd.DataFrame(self.data["data"])
            [columns.append(x) for x in self.df.columns]
            print("columns name")
            print(columns)
            return self.data
        else:
            raise Exception("Estrutura de dados inesperada")
        
if __name__ =="__main__":
     pass 