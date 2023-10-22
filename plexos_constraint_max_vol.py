import pkg
import pandas as pd
import numpy as np
import datetime
import ast

inicio = pkg.time.time()

#data a copiar

df_data_constraints=pkg.pd.read_csv('./Vol_Max_Hydro.csv')

#embalse_prueba='Max_vol_Junin Lago'

embalse_prueba='Max_vol_LagunasEP Em'

df_data_constraints=df_data_constraints.loc[df_data_constraints['NAME']==embalse_prueba]

#data_historical=df_data_constraints.reindex(np.arange(np.shape(df_data_constraints)[0]))

data_historical=pkg.pd.DataFrame(df_data_constraints.to_numpy(),index=np.arange(np.shape(df_data_constraints)[0]),columns=df_data_constraints.columns.to_numpy())

#data a pegar

data_columnas=[embalse_prueba]

data_embalses_days=pkg.plexos_crear_csv.CreateDataframeOfMultiYears(2023,2030,48,data_columnas,0)

plantilla_embalses=data_embalses_days.funcmultiyear()

#transformar periodos a horas

periods_to_hours=pkg.pd.read_csv('./transform_periods_hour.csv')

#copiar pegar por fecha

indice_j=0

for i in range(np.shape(data_historical)[0]):

    hour_d=periods_to_hours[periods_to_hours['PERIOD']==data_historical.loc[i,'PERIOD']]['HOUR'].to_list()[0]

    minute_d=periods_to_hours[periods_to_hours['PERIOD']==data_historical.loc[i,'PERIOD']]['MINUTE'].to_list()[0]

    date_historical=datetime.datetime(data_historical.loc[i,'YEAR'],data_historical.loc[i,'MONTH'],data_historical.loc[i,'DAY'],hour_d,minute_d)

    for j in range(indice_j,np.shape(plantilla_embalses)[0]):

        hour_f=periods_to_hours[periods_to_hours['PERIOD']==plantilla_embalses.loc[j,'PERIOD']]['HOUR'].to_list()[0]

        minute_f=periods_to_hours[periods_to_hours['PERIOD']==plantilla_embalses.loc[j,'PERIOD']]['MINUTE'].to_list()[0]

        date_embalses=datetime.datetime(plantilla_embalses.loc[j,'YEAR'],plantilla_embalses.loc[j,'MONTH'],plantilla_embalses.loc[j,'DAY'],hour_f,minute_f)

        if date_historical>=date_embalses:

            for k in data_columnas:

                plantilla_embalses.loc[j,k]=data_historical.loc[i,'VALUE']
        
        else:

            indice_j=j

            break
        
        print(f'date_historical= {i} / date_embalses= {j}')


plantilla_embalses.to_csv('./data_plantilla_vol_max.csv',index=False)
