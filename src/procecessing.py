import pandas as pd
import polars as pl
import seaborn
import json
import numpy as np
import os
import utils
from getData import DataClient


"""
Data clenear: Verificando as qualidades dos dados obtidos
"""
#1 Pegar os dados
path_data = 'data/raw/dados_ocupation.json'
data_ocupation = utils.dataFrame(path_data,'data')
print()
# informacoes sobre os dados
utils.print_numero_registro(data_ocupation, 'Minor Occupation Group')
        

    
        
        
    
    









