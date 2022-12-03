import os
import pandas as pd
import numpy as np

 
#'/config/workspace/proyecto_oswalk/root_inicio/ENOSA/2022/04_2022
#"C:\Users\djimeneza\docker\proyecto_oswalk\volume\workspace\root_inicio\ENOSA\2022\05_2022\052022_ENG_DC\mediciones_ENOSA.xlsx"
#'/config/workspace/proyecto_oswalk\root_inicio\ENOSA\2022\05_2022\052022_ENG_DC\

print('###############')

path_root='/config/workspace/proyecto_oswalk/root_inicio'
path_client='/'+'ENOSA'
path_year='/'+'2022'
path_month= '/'+'04_2022'

path_archive_data='/'+'042022_ENG_DC'

path_final=path_root+path_client+path_year+path_month
print(path_final+path_archive_data)
data=[]

os.chdir(path_final+path_archive_data)
for root, dirs, files in os.walk('.', topdown = False):
    for name in files:
        data.append(name)
print(data)
