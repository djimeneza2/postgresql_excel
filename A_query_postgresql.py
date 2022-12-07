from Z_data_base_query import *

class data_base_conection():

    def __init__(self,user,password,host,port,database):

        self.user=user

        self.password=password

        self.host=host

        self.port=port

        self.database=database
    

    def execute_query(self,query):

        try:

            connection = psycopg2.connect( user=self.user ,

                                        password=self.password ,

                                        host=self.host ,

                                        port=self.port ,

                                        database=self.database )


            cursor = connection.cursor()

            query_f=query

            cursor.execute(query_f) 

            data = cursor.fetchall()

            print(data)

            connection.commit()

        except (Exception, psycopg2.Error) as error :

            print ("Error while connecting to PostgreSQL", error)

        finally:

                if(connection):

                    cursor.close()

                    connection.close()

                    print("PostgreSQL connection is closed")


    def dataframe_to_postgresql(self,dataframe_df,table_df):

        engine=create_engine(url="postgresql://{0}:{1}@{2}:{3}/{4}".format(

                self.user, self.password, self.host, self.port, self.database

                ))

        dataframe_df.to_sql(table_df, con=engine, if_exists='replace', index=False)

        return 0


    def execute_query_insert_many(self,table_name,records):

        try:
            connection = psycopg2.connect( user=self.user ,

                                        password=self.password ,

                                        host=self.host ,

                                        port=self.port ,

                                        database=self.database )

            cursor = connection.cursor()

            sql_insert_query = """ INSERT INTO public.{table} (kwh, kvar_i, kvar_c, kw, kwh_i, id_facturacion, periodo) VALUES (%s,%s,%s,%s,%s,%s,%s) """

            result = cursor.executemany(sql_insert_query.format(table=table_name), records)

            connection.commit()

            print(cursor.rowcount, "Record inserted successfully")

        except (Exception, psycopg2.Error) as error :

            print ("Error while connecting to PostgreSQL", error)

        finally:

                if(connection):

                    cursor.close()

                    connection.close()

                    print("PostgreSQL connection is closed")


##################################################################
'''
M=data_base_conection("admin",
                    "secret",
                    "172.25.0.1",
                    "5432",
                    "mediciones_cliente"
                    )

path_prueba='/config/workspace/root_inicio/ENOSA/2022/05_2022/revision_libres/'+'12.csv'

df_prueba=pd.read_csv(path_prueba,index_col=[0])

records_to_insert=[]

for ro in df_prueba.index: 

    tuple_prueba=()

    for col in df_prueba.columns:

        tuple_data = df_prueba.loc[ro,col]

        if type(tuple_data) == str:

            tuple_prueba+=(df_prueba.loc[ro,col],)

        else:

            tuple_prueba+=(df_prueba.loc[ro,col].item(),)  

    records_to_insert.append(tuple_prueba)

M.execute_query_insert_many('medicion_eng_dc_agricola_el_arenal_sum12547590_cl',records_to_insert)
'''

'''
search_path_root='/config/workspace/root_inicio'
search_path_client='/'+'ENOSA'
search_path_year='/'+'2022'
search_path_month= '/'+'05_2022'
search_final_path=search_path_root+search_path_client+search_path_year+search_path_month
search_final_path_data=search_final_path+'/'+'intefase_postgresql.xlsx'
data_postgresql=pd.read_excel(search_final_path_data,sheet_name="nombre_data")

query_daniel_1="DELETE FROM public.medicion_eng_dc_altamar_sum12597027 WHERE id>=1;"
#query_daniel_1="SELECT * FROM public.medicion_eng_dc_american_quality_sum10910500 WHERE periodo='2022-05-01 08:00';"
#M=data_base_conection("admin","secret","172.25.0.1","5432","mediciones_cliente")
#M.execute_query(query_daniel_1)

for table_name in data_postgresql['mediciones_tabla_postgres']:
    print(table_name)
    #query=f"SELECT kw FROM public.{table_name} WHERE periodo='2022-05-01 08:00';"
    query=f"DELETE FROM public.{table_name} WHERE id>=1;"
    data_base_conection("admin",
                    "secret",
                    "172.25.0.1",
                    "5432",
                    "mediciones_cliente"
                    ).execute_query(query)
'''

