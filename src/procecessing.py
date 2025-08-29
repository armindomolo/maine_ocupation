import pandas as pd
import polars as pl
import seaborn
import json
import numpy as np
import os
import utils

"""
Data clenear: Verificando as qualidades dos dados obtidos
"""
#1 Pegar os dados
path_data = 'data/raw/dados_ocupation.json'

data_ocupation = utils.dataFrame(path_data,'data')
# informacoes sobre os dados
print(data_ocupation.info())
        

    
        
        
    
    









