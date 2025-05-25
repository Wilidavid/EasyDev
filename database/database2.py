import json
from dotenv import load_dotenv
load_dotenv()
import os
from supabase import create_client 
url= os.environ.get("SUPABASE_URL")
key= os.environ.get("SUPABASE_KEY")
supabase= create_client(url, key)

def bajar_infonube():
    cuentas=(supabase.table("Users").select("*").execute())
    temporal=cuentas.data
    with open('cuentas.json',"w") as f:
        f.write(json.dumps(temporal, indent=4))

def upload_problem(id,tochange):
    response=supabase.table("Problems").select(tochange).eq("id",id).execute()
    valorprevio=int(response.data[0][tochange])
    response=supabase.table("Problems").update({tochange: valorprevio+1}).eq("id", id).execute()

def download_problem(id):
    response=supabase.table("Problems").select("*").eq("id",id).execute()
    valorprevio=(response.data[0])
    print(valorprevio)
    
def change_usuario(usuario,tochange,thechange):
    response=supabase.table("Users").update({tochange: thechange}).eq("name", usuario).execute()
    
def crea_usuario(user):
    response = (supabase.table("Users").insert({"name":user,"password":user[0],"points":user[1]}).execute())

download_problem(4)