from getData import DataClient
import pandas as pd
import polars as pl
import os

# Conectando com API:

api = "https://honolulu-api.datausa.io/tesseract/data.jsonrecords?cube=pums_5&include=State:04000US23&measures=Total%20Population,Average%20Wage,Average%20Wage%20Appx%20MOE,Record%20Count&drilldowns=Year,Detailed%20Occupation&parents=true&debug=true&Workforce+Status=true"

while True:
    print("Carrendo os dados ....")
    apiData = DataClient(api)
    apiData.source_data()
    resposta_input = input("Deseja atualizar a base de dados json?[y, n] ")
    if resposta_input.lower() == 'y':
        apiData.save_json(path='data/raw/dados_ocupation.json')
    apiData.to_dataframe()
    resposta_input = input("Deseja atualizar a base de dados csv?[y, n] ")
    if resposta_input.lower() == 'y':
        apiData.save_csv(path='data/processed/dados_ocupation.csv')
    saida = input("Deseja parar o programa?[y, n] ")
    if saida.lower() == 'y':
        break
        
    
        
    


