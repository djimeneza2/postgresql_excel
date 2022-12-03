import os
import pandas as pd
import numpy as np
 
#'/config/workspace/proyecto_oswalk/root_inicio/ENOSA/2022/04_2022

path_root='/config/workspace/root_inicio'
path_client='/'+'ENOSA'
path_year='/'+'2022'
path_month= '/'+'04_2022'

path_final=path_root+path_client+path_year+path_month

#archive = '042022_ENG_DC_American_Quality_Sum10910500'+'.xlsx'
archive = 'mediciones_contratos_libre'+'.xlsx'

archive_final = archive

path_archive_final=path_final+'/'+archive_final

required_df_1 = pd.read_excel(path_archive_final, sheet_name='contrato_1')
required_df_2 = pd.read_excel(path_archive_final, sheet_name='contrato_2')
required_df_3 = pd.read_excel(path_archive_final, sheet_name='contrato_3')
required_df_4 = pd.read_excel(path_archive_final, sheet_name='contrato_stevia')

#required_df_1.to_excel(path_archive_final,sheet_name='paste_final')

#required_df = pd.read_excel(path_archive_final, usecols = [1, 2]).drop([0,2])

#m_array=np.delete(required_df.values,0,0)

#df_array=pd.DataFrame(m_array,columns=['pot','ener'])

##m_array=np.delete(required_df)

##df_array=pd.DataFrame(m_array,columns=['pot','ener'])

#print(required_df_2)

#print('###############')

#print(required_df_2.loc[0:2])

#print('###############')

#print(required_df_2['PIURA_60KV'].loc[[1]].values)

#print('###############')

#print(required_df_2.columns)

fecha_archives='042022'

archives_final_daniel=fecha_archives+'_'+required_df_2['PIURA_60KV'].loc[[1]].values+'.xlsx'

#print(archives_final_daniel)

print('###############')

#print(required_df_2['PIURA_60KV'])
'''
archivos_1=[]
for dd in required_df_2['NUEVA_ZORRITOS_60KV'].index:
    if type(required_df_2['NUEVA_ZORRITOS_60KV'].loc[[dd]].values[0]) == float:
            break
    else:
        m0=fecha_archives+'_'+required_df_2['NUEVA_ZORRITOS_60KV'].loc[[dd]].values+'.xlsx'
        archivos_1.append(m0[0]) 

    #m0=fecha_archives+'_'+required_df_2['PIURA_10KV'].loc[[dd]].values+'.xlsx'
    #archivos_1.append(m0[0])
#print(archivos_1)
'''
#dict_med_lib_enosa_1={}
#s=[]
#for ll in required_df_2.columns:
#    s.append(ll)
#    print(s)

#print(required_df_2.columns)
#print(np.shape(required_df_2.columns))
#print(required_df_2['PIURA_10KV'].loc[[2]].values)

#print(type(required_df_2['PIURA_60KV'].loc[[5]].values[0]))
'''
dict_med_lib_enosa_1={}
for ll in required_df_2.columns:
    archivos_1=[]
    for dd in required_df_2[ll].index:
        if type(required_df_2[ll].loc[[dd]].values[0]) == float:
            break
        else:
            m0=fecha_archives+'_'+required_df_2[ll].loc[[dd]].values+'.xlsx'
            archivos_1.append(m0[0])
    dict_med_lib_enosa_1[ll]=archivos_1

print(dict_med_lib_enosa_1)
'''

contratos=['contrato_1','contrato_2','contrato_3','contrato_stevia']

dict_med_lib_enosa_1={}
for cc in contratos:
    required_df_2 = pd.read_excel(path_archive_final, sheet_name=cc)
    dict_med_lib_enosa_1[cc]={}
    for ll in required_df_2.columns:
        archivos_1=[]
        for dd in required_df_2[ll].index:
            if type(required_df_2[ll].loc[[dd]].values[0]) == float:
                break
            else:
                m0=fecha_archives+'_'+required_df_2[ll].loc[[dd]].values+'.xlsx'
                archivos_1.append(m0[0])
        dict_med_lib_enosa_1[cc][ll]=archivos_1    


#rr=dict_med_lib_enosa_1['contrato_1']['PIURA_60KV']
#print(rr)


archivos=[]
for cc in dict_med_lib_enosa_1.keys():
    for ll in dict_med_lib_enosa_1[cc].keys():
        for mm in dict_med_lib_enosa_1[cc][ll]:
            archivos.append(mm)
print(archivos)





