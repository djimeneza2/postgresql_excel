import pkg

if __name__=='__main__':

    inicio = pkg.time.time()

    data_copy_paste=pkg.pd.read_excel('factura_python.xlsx',sheet_name='FTE_PY',encoding='latin-1')

    '''
    execute 

    copy_final_path	
    copy_workbook	
    copy_sheet	
    copy_startRow	
    copy_startCol	
    copy_endRow	
    copy_endCol	

    paste_final_path	
    paste_workbook	
    paste_sheet	
    paste_startRow	
    paste_startCol	
    paste_endRow	
    paste_endCol
    '''

    array_copy_final_execute=pkg.np.array(data_copy_paste['execute'])

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

    array_parametros = list(zip(array_copy_final_execute,
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

    final=pkg.time.time()

    print(f'ejecucion finalizada de copy and paste en {final-inicio} segundos')





