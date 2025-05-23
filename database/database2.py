import json
from dotenv import load_dotenv
load_dotenv()
import os
from supabase import create_client 
url= os.environ.get("SUPABASE_URL")
key= os.environ.get("SUPABASE_KEY")
supabase= create_client(url, key)
def cargar_infonube():
    cuentas=(supabase.table("Users").select("*").execute())
    temporal=cuentas.data
    archivo_temporal=open('cuentas.json',"w")
    archivo_temporal.write(json.dumps(temporal, indent=4))
    archivo_temporal.close()

def subir_infonube():
    archivo_temporal=open('cuentas.json',"r")
    cuentas=json.load(archivo_temporal)
    archivo_temporal.close()
    for cuenta in cuentas:
        consulta=supabase.table("Users").select("id").eq("id",cuenta["id"]).execute()
        if consulta.data:  
            supabase.table("Users").update(cuenta).eq("id", cuenta["id"]).execute()
        else:  # Si no existe, inserta
            supabase.table("Users").insert(cuenta).execute()
    archivo_temporal2=open('archivos.json',"r")
    archivos=json.load(archivo_temporal2)
    archivo_temporal2.close()
    for archivo in archivos:
        consulta=supabase.table("Problems").select("id").eq("id",archivo["id"]).execute()
        if consulta.data:  
            supabase.table("Problems").update(archivo).eq("id", archivo["id"]).execute()
        else:  # Si no existe, inserta
            supabase.table("Problems").insert(archivo).execute()



cargar_infonube()

# archivo_temporal2=open('archivos.json',"r")
# archivos=json.load(archivo_temporal2)
# archivo_temporal2.close()


# for i, archivo in enumerate(archivos, start=1):
#     registrar = {
#         "id": i,
#         "name": archivo[0],
#         "numerin": archivo[1],
#         "bool": archivo[2],
#         "numerin2": archivo[3]
#     }
#     supabase.table("Problems").insert(registrar).execute()



