import pkg

if __name__=='__main__':

    inicio = pkg.time.time()

    data_copy_paste=pkg.pd.read_excel('copy_paste_manttos.xlsx',sheet_name='COPY_PASTE_MANTTOS')

    array_execute=pkg.np.array(data_copy_paste['execute'])

    array_copy_final_path=pkg.np.array(data_copy_paste['copy_final_path'])
    array_copy_workbook=pkg.np.array(data_copy_paste['copy_workbook'])
    array_copy_sheet=pkg.np.array(data_copy_paste['copy_sheet'])
    array_copy_startRow=pkg.np.array(data_copy_paste['copy_startRow'])
    array_copy_startCol=pkg.np.array(data_copy_paste['copy_startCol'])
    array_copy_endRow=pkg.np.array(data_copy_paste['copy_endRow'])
    array_copy_endCol=pkg.np.array(data_copy_paste['copy_endCol'])

    array_paste_final_path=pkg.np.array(data_copy_paste['paste_final_path'])
    array_paste_workbook=pkg.np.array(data_copy_paste['paste_workbook'])
    array_paste_sheet=pkg.np.array(data_copy_paste['paste_sheet'])
    array_paste_startRow=pkg.np.array(data_copy_paste['paste_startRow'])
    array_paste_startCol=pkg.np.array(data_copy_paste['paste_startCol'])
    array_paste_endRow=pkg.np.array(data_copy_paste['paste_endRow'])
    array_paste_endCol=pkg.np.array(data_copy_paste['paste_endCol'])

    array_parametros = list(zip(array_execute,
                                array_copy_final_path,
                                array_copy_workbook,
                                array_copy_sheet,
                                array_copy_startRow,
                                array_copy_startCol,
                                array_copy_endRow,
                                array_copy_endCol,
                                array_paste_final_path,
                                array_paste_workbook,
                                array_paste_sheet,
                                array_paste_startRow,
                                array_paste_startCol,
                                array_paste_endRow,
                                array_paste_endCol))
    

    for c0,c1,c2,c3,c4,c5,c6,c7,p1,p2,p3,p4,p5,p6,p7 in array_parametros:

        if c0==1:
            copied_data=pkg.ClassCopyPaste.copy_excel_data(c1,c2,c3,c4,c5,c6,c7).activate_workbook_to_copy()
            pkg.ClassCopyPaste.paste_excel_data(p1,p2,p3,p4,p5,p6,p7,copied_data).activate_workbook_to_paste()
    
    df_mantenimientos=pkg.pd.read_excel('./manttos_final.xlsx',sheet_name='manttos_final')

    df_names_coes=pkg.pd.read_excel('./manttos_final.xlsx',sheet_name='unidades_coes')

    df_hidros_coes_plexos=pkg.pd.read_excel('./manttos_final.xlsx',sheet_name='bd_hidros')

    df_hidros_coes_plexos=df_hidros_coes_plexos[df_hidros_coes_plexos['codigo_coes']>0]

    array_grupos_coes=pkg.np.array(df_names_coes['grupos_coes'])

    array_hidros_coes=pkg.np.array(df_names_coes['hidroelectricas_coes'])

    array_termicas_coes=pkg.np.array(df_names_coes['termicas_coes'])

    array_rer_eolicas_coes=pkg.np.array(df_names_coes['rer_eolicas_coes'])

    array_rer_solares_coes=pkg.np.array(df_names_coes['rer_solares_coes'])

    df_mantenimientos_dropduplicate=df_mantenimientos.drop_duplicates(subset=['codigo'],keep='last')

    df_coes_hidros=df_mantenimientos[(df_mantenimientos['equipo'].isin(array_grupos_coes)) & 
                                        (df_mantenimientos['ubicacion'].isin(array_hidros_coes))]

    df_coes_termicas=df_mantenimientos[(df_mantenimientos['equipo'].isin(array_grupos_coes)) & 
                                        (df_mantenimientos['ubicacion'].isin(array_termicas_coes))]

    df_coes_eolicas=df_mantenimientos[(df_mantenimientos['equipo'].isin(array_grupos_coes)) & 
                                        (df_mantenimientos['ubicacion'].isin(array_rer_eolicas_coes))]

    df_coes_solares=df_mantenimientos[(df_mantenimientos['equipo'].isin(array_grupos_coes)) & 
                                        (df_mantenimientos['ubicacion'].isin(array_rer_solares_coes))]
    
    df_mantenimientos_dropduplicate.to_csv('./manto_sin_duplicado.csv',encoding='latin1')

    df_coes_hidros['value_replace']=pkg.np.zeros(pkg.np.shape(df_coes_hidros['codigo']),dtype=int)

    df_coes_hidros['unit']=pkg.np.zeros(pkg.np.shape(df_coes_hidros['codigo']),dtype=int)

    for i in df_coes_hidros.index:
        if pkg.np.shape(df_hidros_coes_plexos[df_hidros_coes_plexos['codigo_coes']==df_coes_hidros.loc[i,'codigo']])[0]>0:
            df_coes_hidros.loc[i,'value_replace']=100*pkg.np.array(df_hidros_coes_plexos[df_hidros_coes_plexos['codigo_coes']==df_coes_hidros.loc[i,'codigo']]['porcentaje'].to_list())[0]           
            df_coes_hidros.loc[i,'unit']=pkg.np.array(df_hidros_coes_plexos[df_hidros_coes_plexos['codigo_coes']==df_coes_hidros.loc[i,'codigo']]['central_plexos'].to_list())[0]

    df_coes_hidros['unit']=df_coes_hidros['unit'].replace(0,pkg.np.nan)
    df_coes_hidros=df_coes_hidros[['unit','fecha_inic','fecha_fin','value_replace']].dropna(subset=['unit','value_replace'])

    df_coes_hidros['date_init']=df_coes_hidros['fecha_inic'].apply(lambda x: '('+str(x.year)+','+str(x.month)+','+str(x.day)+','+str(x.hour)+','+'0'+')')
    df_coes_hidros['date_end']=df_coes_hidros['fecha_fin'].apply(lambda x: '('+str(x.year)+','+str(x.month)+','+str(x.day)+','+str(x.hour)+','+'0'+')')

    df_coes_hidros.to_csv('./manto_hidros.csv',index=False)
    #df_coes_termicas.to_csv('./manto_termicas.csv',encoding='latin1')
    #df_coes_eolicas.to_csv('./manto_eolicas.csv',encoding='latin1')
    #df_coes_solares.to_csv('./manto_solares.csv',encoding='latin1')

    final=pkg.time.time()
   
    print(f'ejecucion finalizada de copy and paste en {final-inicio} segundos')
