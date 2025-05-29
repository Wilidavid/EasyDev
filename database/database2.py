import json
from dotenv import load_dotenv
load_dotenv()
import os
import variables as v
from supabase import create_client 
url= os.environ.get("SUPABASE_URL")
key= os.environ.get("SUPABASE_KEY")
supabase= create_client(url, key)
import random
import guardar
def downloadall():
    problemas=(supabase.table("Problems").select("*").execute())
    temporal=[x['info'] for x in problemas.data]
    for ix,x in enumerate(temporal):
        v.archivos[ix][3:6]=x
        

    guardar.guardar()

    

def download():
    cuentas=(supabase.table("Users").select("*").execute())
    temporal=cuentas.data
    diccionario_usuarios = {registro["username"]: registro["Info"] for registro in temporal}
    
    with open('cuentas.json',"w") as f:
        f.write(json.dumps(diccionario_usuarios, indent=4))

def download_problem(id):
    respuesta = supabase.table("Problems").select("*").eq("id", id).execute()
    data = respuesta.data
    datos_nube = data[0] 
    nuevos_valores = datos_nube['info']
    with open("archivos.json", 'r') as f:
        problemas_locales = json.load(f)
    print(nuevos_valores)
    problemas_locales[id][3] = nuevos_valores[0]
    problemas_locales[id][4] = nuevos_valores[1]
    problemas_locales[id][5] = nuevos_valores[2]
        
    with open("archivos.json", 'w') as f:
        json.dump(problemas_locales, f, indent=4)
    
def change_usuario(usuario,change):
    response=supabase.table("Users").update({"Info":change}).eq("username", usuario).execute()
    
def register(user,info):
    response = (supabase.table("Users").insert({"username":user,"Info":info}).execute())

def change_problem(id,info):
    response=supabase.table("Problems").update({"info": info}).eq("id", id).execute()

def new(k):
    response = (supabase.table("Problems").insert({"id":k[-1],"info":k}).execute())

def wipeout(): ##NO USAR, REINICIA todO DE PROBLEMAS
    for ex in v.archivos:
        ex[3:6]=[0,[],[]]

    with open('archivos.json', 'w') as f:
        json.dump(v.archivos, f, indent=4)

def subir():
    for k in v.archivos:
        p = tuple([k[x] for x in range(3,6)])
        change_problem(k[-1],p)

# cuentasbot=['CrimsonFox', 'AzureWolf07', 'EmeraldHawk123', 'GoldenLionX', 'IndigoTigerPro', 'JadePumaGamer', 'LavenderJaguarYT', 'MagentaEaglePlays', 'OnyxSharkTV', 'OrchidSnakeXtreme', 'PeridotBear22', 'QuartzBadger007', 'RubyRabbitKnight', 'SapphireDeerLord', 'TealOwlQueen', 'TopazCatKing', 'UmberMouseLegend', 'VioletHorseAce', 'WhiteSquirrelOne', 'YellowCougarMax', 'AmberLeopardLite', 'BronzePandaPlus', 'CopperMonkeyUltra', 'DiamondHippoGod', 'GarnetGorillaXPro', 'MoonstoneRhinoYTMax', 'OpalGoatPrimeAce', 'PearlZebraGodOne', 'PlatinumSpiderMaxLite', 'SilverTurtlePlusUltra']



# vacio={}
# for i in cuentasbot:
#     vacio[i]=[1, 0, 0, [0, True], [random.randint(0,200) for _ in range(random.randint(1,10))], [random.randint(0,200) for _ in range(random.randint(1,10))], 0, ["", random.randint(2,40)]]

# with open('cuentas.json', 'w') as f:
#     json.dump(vacio, f, indent=4)

# for nombre, info in vacio.items():
#     supabase.table("Users").insert({
#         "username": nombre,
#         "Info": info
#     }).execute()