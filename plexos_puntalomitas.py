import pandas as pd
import numpy as np
import pkg.pkg_plexos.PlexosClassCrearCsv as pkg
import pkg.pkg_plexos.PlexosClassCrearFirst as pkg2

'''
object_df_horario=pkg.CreateDataframeOfMultiYears(2023,2030,24,['1'],0)
df_punta_lomitas_horario=object_df_horario.funcmultiyear()
df_punta_lomitas_horario.to_csv('./data_excel_csv/horario_punta_lomitas.csv',index=False)
'''

df_punta_lomitas_horario=pd.read_csv('./data_excel_csv/horario_punta_lomitas.csv')
#print(df_punta_lomitas_horario)

object_df_mediohorario=pkg.CreateDataframeOfMultiYears(2023,2030,48,['1'],0)
df_punta_lomitas_mediohorario=object_df_mediohorario.funcmultiyear()
#print(df_punta_lomitas_mediohorario)


for i in df_punta_lomitas_horario.index:
    df_punta_lomitas_mediohorario.loc[[2*i,2*i+1],'1']=df_punta_lomitas_horario.loc[i,'1']
    #df_punta_lomitas_mediohorario.loc[,'1']=df_punta_lomitas_horario.loc[i,'1']
    print(i)


df_punta_lomitas_mediohorario.to_csv('./data_excel_csv/mediohorario_punta_lomitas.csv',index=False)

object_first=pkg2.copyfirstyear(2027,2030,'./data_excel_csv/','mediohorario_punta_lomitas.csv')

df_punta_lomitas_mediohorario_mod=object_first.copy_first_in_other_years_improve()

df_punta_lomitas_mediohorario_mod.to_csv('./data_excel_csv/mediohorario_punta_lomitas_mod.csv',index=False)


