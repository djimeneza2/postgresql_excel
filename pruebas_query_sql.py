# direccion window para volumes docker \\wsl$\docker-desktop-data\data\docker\volumes
from datetime import datetime

date_time_str = '18/09/19 01:55:19'

date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')


print ("The type of the date is now",  type(date_time_obj))
print ("The date is", date_time_obj)

tabla='medicion_eng_dc_eps_grau_sum10491118_pt'
inicio='2022-07-01 00:15'
final='2022-08-01 00:00'


query_f=f'''
            SELECT id, kwh, kvar_i, kvar_c, kw, kwh_i, id_facturacion, periodo
            FROM public.{tabla}
            WHERE periodo >= '{inicio}'
            AND periodo <= '{final}';
        '''

print(query_f)
