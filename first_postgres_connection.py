import psycopg2
print("daniel")

try:
    connection = psycopg2.connect(user = "admin",
                                  password = "secret",
                                  host = "172.25.0.1",
                                  port = "5432",
                                  database = "mediciones_cliente")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

    #query="SELECT * FROM nombre_barra_facturacion;"
    #query="SELECT * FROM pg_catalog.pg_tables;"
    query="SELECT table_name FROM information_schema.tables WHERE table_schema='public' "
    cursor.execute(query) 
    data = cursor.fetchall()
    print(data)

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
