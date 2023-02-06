import pandas as pd
import numpy as np

tablas = ['medicion_ENG_DC_PLAZA_CENTER_PAITA_Sum15540396',
'medicion_ENG_DC_PLAZA_CENTER_PIURA_Sum16907674',
'medicion_ENG_DC_PLAZA_CENTER_SULLANA_Sum15252775',
'medicion_ENG_DC_PLAZA_CENTER_TALARA3_Sum8704597',
'medicion_ENG_DC_PLAZA_CENTER_TUMBES_Sum17214405',
'medicion_ENG_DC_PROAGRO_Sum16303064',
'medicion_ENG_DC_SANTA_MONICA',
'medicion_ENG_DC_Turismo_Costa_del_Sol_Sum5037077',
'medicion_ENG_DC_UDEP',
'medicion_ENG_DC_EPS_GRAU_Sum5808079_Curumuy',
'medicion_ENG_DC_Seafrost',
'medicion_ENG_DC_Seafrost_Sum12316977',
'medicion_ENG_DC_EPS_GRAU_Sum5089681_SanMartin',
'medicion_ENG_DC_Hielos_y_Servicios_Sum6716374_Tumbes_CL',
'medicion_ENG_DC_Latimar_Sum6629386',
'medicion_ENG_DC_RAPEL',
'medicion_ENG_DC_Sucroalcolera',
'medicion_ENG_DC_HIELNORV_Sum10876015']


for i in tablas:
    print(f'''
    CREATE TABLE IF NOT EXISTS public."{i}"
    (
        id integer NOT NULL,
        kwh numeric,
        kvar_i numeric,
        kvar_c numeric,
        kw numeric,
        kwh_i numeric,
        id_facturacion integer,
        CONSTRAINT "{i}_pkey" PRIMARY KEY (id),
        CONSTRAINT facturacion_medicion_fkey FOREIGN KEY (id_facturacion)
            REFERENCES public.nombre_barra_facturacion (id) MATCH SIMPLE
            ON UPDATE CASCADE
            ON DELETE CASCADE
            NOT VALID
    )

    TABLESPACE pg_default;
    ''')

tablas_1=[
'medicion_ENG_DC_American_Quality_Sum10910500',
'medicion_ENG_DC_CbC_Peruana1_Sum10491010',
'medicion_ENG_DC_CbC_Peruana2_Sum10491280',
'medicion_ENG_DC_Limagro_Sum10889686',
'medicion_ENG_DC_SunshineExport1_Sum11845200',
'medicion_ENG_DC_SunshineExport2_Sum10889004',
'medicion_ENG_DC_Grupo_Camposur_CL',
'medicion_ENG_DC_Negocios _Del_Sur_Del_Peru_CL',
'medicion_ENG_DC_Musterion_Sum15602345_CL',
'medicion_ENG_DC_Musterion_Sum15783189_CL',
'medicion_ENG_DC_Koricancha_Sum16079100_CL',
'medicion_ENG_DC_Agricola_El_Arenal_Sum12547590_CL',
'medicion_ENG_DC_Agroindustrias_Del_Chira_S.R.L._Sum10878332_CL',
'medicion_ENG_DC_Greenway_Sum16210081_CL',
'medicion_ENG_DC_Depositos_Sum12546000_CL',
'medicion_ENG_DC_Medlog_Paita_Sum17165991_CL',
'medicion_ENG_DC_Macromar_Sum17217668_CL',
'medicion_ENG_DC_Medlog_Paita_Sum16959447_CL',
'medicion_ENG_DC_Hielos_y_Servicios_Sum15526673_Piura_CL',
#'medicion_ENG_DC_Agricola_Del_Chira(La Huaca)_Sum12557756',
'medicion_ENG_DC_Agricola_Del_Chira_La Huaca_Sum12557756',
'medicion_ENG_DC_Complejo_Agroindustrial_Beta_Sum16289448',
'medicion_ENG_DC_SunshineExport3_Sum17230679',
'medicion_ENG_DC_Altamar_Sum12597027',
'medicion_ENG_DC_ASJ_Sum11105870',
'medicion_ENG_DC_ASJ_Sum15362436',
'medicion_ENG_DC_CONSORCIO_FEGURRI_STA_REGINA',
'medicion_ENG_DC_DonPacking_Sum10843050',
'medicion_ENG_DC_EMPAFRUIT',
'medicion_ENG_DC_EPS_GRAU_Sum10491118_PT',
'medicion_ENG_DC_EPS_GRAU_Sum12517643_EB1',
'medicion_ENG_DC_EPS_GRAU_Sum12517652_EB2',
'medicion_ENG_DC_EPS_GRAU_Sum12517661_PCAP',
'medicion_ENG_DC_HIELO_POLAR',
'medicion_ENG_DC_PERUPEZ',
'medicion_ENG_DC_PLAZA_CENTER_PAITA_Sum15540396',
'medicion_ENG_DC_PLAZA_CENTER_PIURA_Sum16907674',
'medicion_ENG_DC_PLAZA_CENTER_SULLANA_Sum15252775',
'medicion_ENG_DC_PLAZA_CENTER_TALARA3_Sum8704597',
'medicion_ENG_DC_PLAZA_CENTER_TUMBES_Sum17214405',
'medicion_ENG_DC_PROAGRO_Sum16303064',
'medicion_ENG_DC_SANTA_MONICA',
'medicion_ENG_DC_Turismo_Costa_del_Sol_Sum5037077',
'medicion_ENG_DC_UDEP',
'medicion_ENG_DC_EPS_GRAU_Sum5808079_Curumuy',
'medicion_ENG_DC_Seafrost',
'medicion_ENG_DC_Seafrost_Sum12316977',
'medicion_ENG_DC_EPS_GRAU_Sum5089681_SanMartin',
'medicion_ENG_DC_Hielos_y_Servicios_Sum6716374_Tumbes_CL',
'medicion_ENG_DC_Latimar_Sum6629386',
'medicion_ENG_DC_RAPEL',
'medicion_ENG_DC_Sucroalcolera',
'medicion_ENG_DC_HIELNORV_Sum10876015',
'medicion_Promotora_Inmobiliaria_In dustrial_De_Piura_SAC_CL'
]

a=''
for i in tablas_1:
    b=f'''ALTER TABLE public."{i}" ADD COLUMN periodo timestamp without time zone;'''
    a+=b
print(a)


path_prueba='/config/workspace/root_inicio/ENOSA/2022/05_2022/revision_libres/'+'1.csv'

df_prueba=pd.read_csv(path_prueba)

print(np.shape(df_prueba))

print(np.array(df_prueba.iloc[0])[:])

array_medicion=[]
for i in range(np.shape(np.array(df_prueba.iloc[0]))[0]):
    array_medicion.append(np.array(df_prueba.iloc[0])[i])
query_prueba_daniel = f'''INSERT INTO public."medicion_ENG_DC_ASJ_Sum11105870" (kwh, kvar_i, kvar_c, kw, kwh_i, id_facturacion, periodo) VALUES ({float(array_medicion[1])}, {float(array_medicion[2])}, {float(array_medicion[3])}, {float(array_medicion[4])}, {float(array_medicion[5])}, {int(array_medicion[6])}, '{array_medicion[7]}');'''
print(query_prueba_daniel)



tabla_2 = [
'medicion_eng_dc_american_quality_sum10910500',
'medicion_eng_dc_cbc_peruana1_sum10491010',
'medicion_eng_dc_cbc_peruana2_sum10491280',
'medicion_eng_dc_limagro_sum10889686',
'medicion_eng_dc_sunshineexport1_sum11845200',
'medicion_eng_dc_sunshineexport2_sum10889004',
'medicion_eng_dc_grupo_camposur_cl',
'medicion_eng_dc_negocios_del_sur_del_peru_cl',
'medicion_eng_dc_musterion_sum15602345_cl',
'medicion_eng_dc_musterion_sum15783189_cl',
'medicion_eng_dc_koricancha_sum16079100_cl',
'medicion_eng_dc_agricola_el_arenal_sum12547590_cl',
'medicion_eng_dc_agroindustrias_del_chira_srl_sum10878332_cl',
'medicion_eng_dc_greenway_sum16210081_cl',
'medicion_eng_dc_depositos_sum12546000_cl',
'medicion_eng_dc_medlog_paita_sum17165991_cl',
'medicion_eng_dc_macromar_sum17217668_cl',
'medicion_eng_dc_medlog_paita_sum16959447_cl',
'medicion_eng_dc_hielos_y_servicios_sum15526673_piura_cl',
'medicion_eng_dc_agricola_del_chira_la_huaca_sum12557756',
'medicion_eng_dc_complejo_agroindustrial_beta_sum16289448',
'medicion_eng_dc_sunshineexport3_sum17230679',
'medicion_eng_dc_altamar_sum12597027',
'medicion_eng_dc_asj_sum11105870',
'medicion_eng_dc_asj_sum15362436',
'medicion_eng_dc_consorcio_fegurri_sta_regina',
'medicion_eng_dc_donpacking_sum10843050',
'medicion_eng_dc_empafruit',
'medicion_eng_dc_eps_grau_sum10491118_pt',
'medicion_eng_dc_eps_grau_sum12517643_eb1',
'medicion_eng_dc_eps_grau_sum12517652_eb2',
'medicion_eng_dc_eps_grau_sum12517661_pcap',
'medicion_eng_dc_hielo_polar',
'medicion_eng_dc_perupez',
'medicion_eng_dc_plaza_center_paita_sum15540396',
'medicion_eng_dc_plaza_center_piura_sum16907674',
'medicion_eng_dc_plaza_center_sullana_sum15252775',
'medicion_eng_dc_plaza_center_talara3_sum8704597',
'medicion_eng_dc_plaza_center_tumbes_sum17214405',
'medicion_eng_dc_proagro_sum16303064',
'medicion_eng_dc_santa_monica',
'medicion_eng_dc_turismo_costa_del_sol_sum5037077',
'medicion_eng_dc_udep',
'medicion_eng_dc_eps_grau_sum5808079_curumuy',
'medicion_eng_dc_seafrost',
'medicion_eng_dc_seafrost_sum12316977',
'medicion_promotora_inmobiliaria_industrial_de_piura_sac_cl',
'medicion_eng_dc_eps_grau_sum5089681_sanmartin',
'medicion_eng_dc_hielos_y_servicios_sum6716374_tumbes_cl',
'medicion_eng_dc_latimar_sum6629386',
'medicion_eng_dc_rapel',
'medicion_eng_dc_sucroalcolera',
'medicion_eng_dc_hielnorv_sum10876015',
'medicion_eng_dc_dominus_sum11210267_cl',
'medicion_eng_dc_dominus_sum16079146_cl',
'medicion_eng_dc_pachamama_sum5883322_cl',
'medicion_eng_dc_plaza_center_talara',
'medicion_eng_dc_proagro_sum17165258',
'medicion_eng_dc_stevia',
'medicion_eng_dc_unimar_sum12317105_sum12317105'
]

for i in tabla_2:
    print(f'''
    CREATE TABLE IF NOT EXISTS public.{i}
    (
        id serial NOT NULL,
        kwh numeric,
        kvar_i numeric,
        kvar_c numeric,
        kw numeric,
        kwh_i numeric,
        id_facturacion integer,
        periodo timestamp without time zone,
        CONSTRAINT {i}_pkey PRIMARY KEY (id),
        CONSTRAINT facturacion_medicion_fkey FOREIGN KEY (id_facturacion)
            REFERENCES public.nombre_barra_facturacion (id) MATCH SIMPLE
            ON UPDATE CASCADE
            ON DELETE CASCADE
            NOT VALID
    )

    TABLESPACE pg_default;
    ''')


for i in tabla_2:
    print(f'''
    ALTER TABLE IF EXISTS public.{i}
    ADD CONSTRAINT {i}_uq_per
    UNIQUE (periodo);
    ''')

# medicion_eng_dc_agroindustrias_del_chira_srl_sum10878332_cl_uq_
# medicion_promotora_inmobiliaria_industrial_de_piura_sac_cl_uq_p
