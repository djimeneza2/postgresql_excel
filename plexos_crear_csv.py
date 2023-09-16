import pandas as pd
import numpy as np
import datetime
import ast
import pkg_copy_paste 


class ArrayMonthDaysPeriods():

    def __init__(self,year,month,periodsperdays):
        self.year=year
        self.month=month
        self.periodsperdays=periodsperdays

    def funcNumberOfDaysInMonth(self):
        if self.month in np.array([1,3,5,7,8,10,12]):
            self.number_days_in_month=31
        elif self.month in np.array([4,6,9,11]):
            self.number_days_in_month=30
        elif self.month in np.array([2]):
            if self.year%4==0 and (self.year%100 !=0 or self.year%400==0):
                self.number_days_in_month=29
            else:
                self.number_days_in_month=28
        return self.number_days_in_month

    def funcArrayOfPeriodsInDay(self):
        self.array_of_periods_in_day=np.arange(1,self.periodsperdays+1,dtype=int)
        return self.array_of_periods_in_day
    
    def funcArrayOfPeriodsInMonth(self):
        self.array_of_periods_in_month=np.tile(self.funcArrayOfPeriodsInDay(),self.funcNumberOfDaysInMonth()).astype(int)
        return self.array_of_periods_in_month
    
    def funArrayOfDaysInMonth(self):
        self.array_of_days_in_month=np.array([])
        for i in np.arange(1,self.funcNumberOfDaysInMonth()+1):
            array=np.tile(np.array([i]),np.shape(self.funcArrayOfPeriodsInDay())[0])
            self.array_of_days_in_month=np.append(self.array_of_days_in_month,array).astype(int)
        return self.array_of_days_in_month

    def funcArraysOfMonthInMonth(self):
        self.array_of_month_in_month=self.month*np.ones_like(self.funArrayOfDaysInMonth())
        return self.array_of_month_in_month
    
    def funcArrayYearsInMonth(self):
        self.array_of_year_in_month=self.year*np.ones_like(self.funArrayOfDaysInMonth()).astype(int)
        return self.array_of_year_in_month
    
    def funcArrayMonthDaysPeriods(self):
        self.array_month_day_periods=np.stack((self.funcArrayYearsInMonth(),
                                                self.funcArraysOfMonthInMonth(),
                                                self.funArrayOfDaysInMonth(),
                                                self.funcArrayOfPeriodsInMonth()),axis=1).astype(int)
        return self.array_month_day_periods
    

class CreateDataframeOfMonth(ArrayMonthDaysPeriods):

    def __init__(self,
                 year,
                 month,
                 periodsperdays,
                 array_columns,
                 data_complete_blanks):
        
        super().__init__(year,month,periodsperdays)
        self.array_columns=array_columns
        self.data_complete_blanks=data_complete_blanks

    def funcDfOfIndexes(self):

        df_indexes=pd.DataFrame(self.funcArrayMonthDaysPeriods(),columns=['YEAR','MONTH','DAY','PERIOD'])
        data_DF=self.data_complete_blanks*np.ones((np.shape(self.funcArrayMonthDaysPeriods())[0],np.shape(self.array_columns)[0]))      
        df_data=pd.DataFrame(data_DF,columns=self.array_columns)
        self.DF_final=df_indexes.join(df_data)
        return self.DF_final
    

class CreateDataframeOfMultiMonths(CreateDataframeOfMonth):

    def __init__(self,
                 year,
                 month_init,
                 month_end,
                 periodsperdays,
                 array_columns,
                 data_complete_blanks):

        super().__init__(year,month_init,periodsperdays,array_columns,data_complete_blanks)
        self.month_init=month_init
        self.month_end=month_end

    def funcmultimonth(self):

        self.DF_final_multimonth=CreateDataframeOfMonth(self.year,self.month_init,self.periodsperdays,self.array_columns,self.data_complete_blanks).funcDfOfIndexes()
        for month_loop in np.arange(self.month_init+1,self.month_end+1):
            prueba=CreateDataframeOfMonth(self.year,month_loop,self.periodsperdays,self.array_columns,self.data_complete_blanks).funcDfOfIndexes()
            self.DF_final_multimonth=pd.concat([self.DF_final_multimonth,prueba])
        return self.DF_final_multimonth
    
class CreateDataframeOfMultiYears(CreateDataframeOfMultiMonths):

    def __init__(self,
                 year_init,
                 year_end,
                 periodsperdays,
                 array_columns,
                 data_complete_blanks):
        
        super().__init__(year_init,
                        1,
                        12,
                        periodsperdays,
                        array_columns,
                        data_complete_blanks)
        
        self.year_init=year_init
        self.year_end=year_end

    def funcmultiyear(self):

        self.DF_final_multiyear=CreateDataframeOfMultiMonths(self.year_init,1,12,self.periodsperdays,self.array_columns,self.data_complete_blanks).funcmultimonth()
        for year_loop in np.arange(self.year_init+1,self.year_end+1):
            prueba=CreateDataframeOfMultiMonths(year_loop,1,12,self.periodsperdays,self.array_columns,self.data_complete_blanks).funcmultimonth()
            self.DF_final_multiyear=pd.concat([self.DF_final_multiyear,prueba])
        
        indices=pd.Series(np.arange(0,np.shape(self.DF_final_multiyear)[0]))
        self.DF_final_multiyear=self.DF_final_multiyear.set_index(indices)

        return self.DF_final_multiyear

class ModifyDataFrameMultiYears(CreateDataframeOfMultiYears):

    def __init__(self,
                 year_init,
                 year_end,
                 periodsperdays,
                 array_columns,
                 data_complete_blanks,
                 dataframe_modif):
        
        super().__init__(year_init,
                         year_end,
                         periodsperdays,
                         array_columns,
                         data_complete_blanks)

        self.dataframe_modif=dataframe_modif

    def parse_tuple(self,string):
            try:
                s = ast.literal_eval(str(string))
                if type(s) == tuple:
                    return s
                return
            except:
                return
            
    def funCalcDifDates(self):

        iterate=np.shape(self.dataframe_modif)[0]
        range_iterate=np.arange(0,iterate)
        data_diff_dates=np.array([])
        data_periods_init=np.array([])
        data_periods_end=np.array([])

        for i in range_iterate:
            date_from=self.parse_tuple(self.dataframe_modif['date_init'].loc[i])
            date_to=self.parse_tuple(self.dataframe_modif['date_end'].loc[i])
            date_from_i=datetime.datetime(date_from[0],date_from[1],date_from[2],date_from[3],date_from[4])
            date_to_i=datetime.datetime(date_to[0],date_to[1],date_to[2],date_to[3],date_to[4])
            diff_date_to_from=date_to_i-date_from_i
            periods_changed=divmod(diff_date_to_from.days*24*60*60+diff_date_to_from.seconds,3600/(self.periodsperdays/24)) 
            data_diff_dates=np.append(data_diff_dates,int(periods_changed[0]))
            
            period_from_p=date_from[3]*self.periodsperdays/24+date_from[4]/(60/(self.periodsperdays/24))+1
            tuple_string_from= "("+str(date_from[0])+","+str(date_from[1])+","+str(date_from[2])+","+str(int(period_from_p))+")"
            data_periods_init=np.append(data_periods_init,tuple_string_from)
           
            period_to_p=date_to[3]*self.periodsperdays/24+date_to[4]/(60/(self.periodsperdays/24))+1
            tuple_string_to= "("+str(date_to[0])+","+str(date_to[1])+","+str(date_to[2])+","+str(int(period_to_p))+")"
            data_periods_end=np.append(data_periods_end,tuple_string_to)

        self.dataframe_modif['periods_change']=data_diff_dates
        self.dataframe_modif['date_init_p']=data_periods_init
        self.dataframe_modif['date_end_p']=data_periods_end

        return self.dataframe_modif
    
    def funChangeDataInDataframeColumn(self):

        iterate=np.shape(self.funCalcDifDates())[0] #2850
        range_iterate=np.arange(0,iterate) #0-2849

        dataframe_fin=CreateDataframeOfMultiYears(self.year_init,
                                                    self.year_end,
                                                    self.periodsperdays,
                                                    self.array_columns,
                                                    self.data_complete_blanks).funcmultiyear()

        for i in range_iterate:

            print('mantenimiento '+str(i)+' para la central '+str(self.funCalcDifDates()['unit'].loc[i])+' a la hora inicial '+str(self.funCalcDifDates()['date_init'].loc[i]))

            date_from=self.parse_tuple(self.funCalcDifDates()['date_init_p'].loc[i])

            index_inicio=dataframe_fin.index[(dataframe_fin['YEAR']==date_from[0]) &
                                                (dataframe_fin['MONTH']==date_from[1]) &
                                                (dataframe_fin['DAY']==date_from[2]) &
                                                (dataframe_fin['PERIOD']==date_from[3])].to_list()
            
            dataframe_fin.loc[index_inicio[0]:index_inicio[0]+self.funCalcDifDates()['periods_change'].loc[i],self.funCalcDifDates()['unit'].loc[i]]+=self.funCalcDifDates()['value_replace'].loc[i]
                    
            self.data_frame_fin_mod=dataframe_fin

        return self.data_frame_fin_mod
        

##################################################################################################################################################################

inicio = pkg_copy_paste.time.time()
#data_columnas=['unit1','unit2','unit3']


#read_data_columnas=pd.read_excel('./manttos_final.xlsx',sheet_name='bd_hidros')

#read_data_columnas=read_data_columnas.drop_duplicates(subset=['central_plexos'],keep='last')

#read_data_columnas=read_data_columnas.dropna(subset=['central_plexos'])

#data_columnas=np.array(read_data_columnas['central_plexos'].to_list())
'''
data_columnas= ['00057_ch_01018_pariac'
,'00260_ch_00055_cahua'
,'00261_ch_00018_callahuanca'
,'00264_ch_00061_carhuaquero'
,'00267_ch_00073_canhon_del_pato'
,'00269_ch_00100_gallito_ciego'
,'00270_ch_00026_huampani'
,'00272_ch_00022_huinco'
,'00276_ch_00039_malpaso'
,'00277_ch_00001_mantaro'
,'00280_ch_00028_matucana'
,'00282_ch_00030_moyopampa'
,'00283_ch_00043_oroya'
,'00285_ch_00046_pachachaca'
,'00286_ch_00008_restitucion'
,'00291_ch_00050_yaupi'
,'00978_ch_00108_yanango'
,'01191_ch_00109_chimay'
,'01195_ch_00111_charcani_1'
,'01196_ch_00113_charcani_2'
,'01197_ch_00116_charcani_3'
,'01198_ch_00118_charcani_4'
,'01199_ch_00121_charcani_5'
,'01200_ch_00188_charcani_6'
,'01201_ch_00124_aricota_1'
,'01203_ch_00126_machupicchu'
,'01206_ch_00190_san_gaban_2'
,'10609_ch_00193_huanchor'
,'11116_ch_00199_yuncan'
,'11842_ch_00205_canha_brava'
,'11877_ch_11878_santacruz_1'
,'12193_ch_12194_poechos_2'
,'12201_ch_12202_la_joya'
,'12600_ch_12601_el_platanal'
,'12652_ch_12650_santacruz_2'
,'12722_ch_12760_roncador'
,'13368_ch_13411_imperial'
,'13513_ch_13514_yanapampa'
,'13574_ch_13575_las_pizarras'
,'14005_ch_14006_huanza'
,'14844_ch_14845_santa_teresa'
,'14909_ch_00204_carhuaquero_4'
,'14964_ch_14965_cheves'
,'14970_ch_14971_chaglla'
,'15210_ch_15211_cerro_del_aguila'
,'17492_ch_17493_maranhon'
,'17551_ch_00055_yarucaya'
,'18186_ch_18187_la_virgen'
,'18949_ch_18952_angel_1'
,'18950_ch_18955_angel_2'
,'18951_ch_18956_angel_3'
]


'''


data_columnas= ['00258_ct_00209_aguaytia_tg1'
,'00258_ct_00210_aguaytia_tg2'
,'00275_ct_00271_malacas2_tg4'
,'00289_ct_00221_santarosa1_uti5d'
,'00289_ct_00223_santarosa1_td7h'
,'00289_ct_00240_santarosa1_uti6d'
,'00289_ct_00278_santarosa1_tg7h'
,'00289_ct_00279_santarosa1_tg7'
,'00289_ct_00280_santarosa1_uti5g'
,'00289_ct_00281_santarosa1_uti6g'
,'00290_ct_00205_ventanilla_td3'
,'00290_ct_00207_ventanilla_td4'
,'00290_ct_00274_ventanilla_tg3'
,'00290_ct_00275_ventanilla_tg4'
,'00290_ct_00286_ventanilla_tg3tv'
,'00290_ct_00287_ventanilla_tg4tv'
,'00290_ct_00288_ventanilla_tg3tg4tv'
,'00290_ct_00289_ventanilla_tg3tvfd'
,'00290_ct_00290_ventanilla_tg4tvfd'
,'00290_ct_00291_ventanilla_tg3tg4tvfd'
,'00987_ct_00236_san_nicolas_tv1'
,'00987_ct_00237_san_nicolas_tv2'
,'00987_ct_00238_san_nicolas_tv3'
,'00987_ct_00272_san_nicolas_td'
,'01066_ct_00303_santarosa2_tg8'
,'01205_ct_00241_chilina_sulz'
,'01205_ct_00355_chilina_td'
,'01214_ct_00346_mollendo_td'
,'11513_ct_00292_chilca1_tg1'
,'11513_ct_00295_chilca1_tg2'
,'11513_ct_00302_chilca1_tg3'
,'11513_ct_00327_chilca1_tg1tv'
,'11513_ct_00328_chilca1_tg2tv'
,'11513_ct_00329_chilca1_tg3tv'
,'11513_ct_00330_chilca1_tg1tg2tv'
,'11513_ct_00331_chilca1_tg2tg3tv'
,'11513_ct_00332_chilca1_tg1tg3tv'
,'11513_ct_00333_chilca1_tg1tg2tg3tv'
,'11571_ct_00296_kallpa_tg1'
,'11571_ct_00305_kallpa_tg2'
,'11571_ct_00306_kallpa_tg3'
,'11571_ct_00320_kallpa_tg1tv'
,'11571_ct_00321_kallpa_tg2tv'
,'11571_ct_00322_kallpa_tg3tv'
,'11571_ct_00323_kallpa_tg1tg2tv'
,'11571_ct_00324_kallpa_tg2tg3tv'
,'11571_ct_00325_kallpa_tg1tg3tv'
,'11571_ct_00326_kallpa_tg1tgtg3tv'
,'11883_ct_00298_oquendo_tg1'
,'11883_ct_03418_oquendo_tv1'
,'11883_ct_03424_oquendoi_tg1tv'
,'12720_ct_00304_las_flores_tg1'
,'12720_ct_03375_las_flores_tg1tv'
,'12781_ct_00312_independencia_tg'
,'12815_ct_00309_paramonga_tg'
,'13417_ct_00317_maple_tv'
,'13549_ct_00339_rf_ilo_td1'
,'13549_ct_00340_rf_ilo_td2'
,'13549_ct_00341_rf_ilo_td3'
,'13601_ct_00344_fenix_tg12'
,'13601_ct_00345_fenix_tg12tv'
,'13601_ct_00347_fenix_tg11'
,'13601_ct_00348_fenix_tg11tv'
,'13601_ct_00349_fenix_tg11tg12tv'
,'13601_ct_00553_fenix_td11tv'
,'13601_ct_00554_fenix_td11'
,'13601_ct_00555_fenix_td12tv'
,'13601_ct_00556_fenix_td12'
,'13601_ct_00605_fenix_tg11tg12tv'
,'13656_ct_00318_olleros_tg1tv'
,'13656_ct_00343_olleros_tg1'
,'14908_ct_00338_rf_talara_td5'
,'14908_ct_00543_rf_talara_tg5'
,'14927_ct_00353_rf_eten_td1'
,'14927_ct_00354_rf_eten_td2'
,'15107_ct_00843_recka_td1'
,'15214_ct_00358_puerto_bravo_td1'
,'15214_ct_00359_puerto_bravo_td2'
,'15214_ct_00360_puerto_bravo_td3'
,'15214_ct_00361_puerto_bravo_td4'
,'15785_ct_00606_chilca2_tg41'
,'15785_ct_00919_chilca2_tg41tv'
,'16290_ct_00372_rf_puerto_maldonado_td'
,'16291_ct_00373_rf_pucallpa_td'
,'16327_ct_00611_nepi_td41'
,'16327_ct_00612_nepi_td42'
,'16327_ct_00613_nepi_td43'
,'16926_ct_00672_malacas_tg6'
,'20510_ct_00573_canha_brava_tv1'
,'20510_ct_00574_canha_brava_tv2'
,'20510_ct_00575_canha_brava_tv1tv2'
]

#print(data_columnas)

dataframe_manttos=pd.read_csv('./manto_thermal.csv') 

prueba4=ModifyDataFrameMultiYears(2023,2024,48,data_columnas,0,dataframe_manttos)

#dataframe_final=prueba4.funcmultiyear()

#dataframe_final.to_csv('./plantilla-data-final.csv')

#df_calcdifdates=prueba4.funCalcDifDates()

#df_calcdifdates.to_csv('./plantilla-calcdifdate-final.csv')

dataframe_fin_mod=prueba4.funChangeDataInDataframeColumn()

dataframe_fin_mod.to_csv('./plexos_mantto_hidros.csv')

final=pkg_copy_paste.time.time()
   
print(f'ejecucion finalizada de copy and paste en {final-inicio} segundos')
