import json
from dotenv import load_dotenv
load_dotenv()
import os
from supabase import create_client 
url= os.environ.get("SUPABASE_URL")
key= os.environ.get("SUPABASE_KEY")
supabase= create_client(url, key)

def download():
    cuentas=(supabase.table("Users").select("*").execute())
    temporal=cuentas.data
    diccionario_usuarios = {registro["username"]: registro["Info"] for registro in temporal}
    with open('cuentas.json',"w") as f:
        f.write(json.dumps(diccionario_usuarios, indent=4))

def upload_problem(id,tochange):
    response=supabase.table("Problems").select(tochange).eq("id",id).execute()
    valorprevio=int(response.data[0][tochange])
    response=supabase.table("Problems").update({tochange: valorprevio+1}).eq("id", id).execute()

def download_problem(id):
    response=supabase.table("Problems").select("*").eq("id",id).execute()
    valorprevio=(response.data[0])
    print(valorprevio)
    
def change_usuario(usuario,change):
    response=supabase.table("Users").update({"Info":change}).eq("username", usuario).execute()
    
def register(user,info):
    response = (supabase.table("Users").insert({"username":user,"Info":info}).execute())

def new(name,info):
    response = (supabase.table("Problems").insert({"username":name,"Info":info}).execute())

h=open("ar.json")
archivos=json.load(h)
h.close()

print(archivos)