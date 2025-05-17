from dotenv import load_dotenv
load_dotenv()
import os
from supabase import create_client 
url= os.environ.get("SUPABASE_URL")
key= os.environ.get("SUPABASE_KEY")
supabase= create_client(url, key)

#---Funcion crea para ingresar nuevo problema, dificultad 0 para easy, 1 para medium, 2 para hard---(eso lo podemos configurar mejor)
def crea_problema(id,dificult):
     data=supabase.table("Problems").insert({"id":id,"dificult":dificult}).execute()



#---Funcion crea para ingresar nueva informacion, usar para registrar usuarios----, se especifica el nombre y contraseña el resto son default
def crea_usuario(user,contra):
     data=supabase.table("Users").insert({"name":user,"password":contra}).execute()
#Ejemplo crea("Wilson","Buenas")



#--Funcion entra para modificar informacion de usuario, se necesita id o usuario se puede cambiar puntaje,contraseña.
def entra(tabla,user,changed,change):
     data=supabase.table(tabla).update({changed:change}).eq("name", user).execute()
#Ejemplo:  entra("Users","Wilson","points",5)



#--Funcion sale para sacar información que necesite, parametros: que info sale y de quien sale
# (el id es el parametro identificador, de normal es el usuario para mas facilidad)
def sale(tabla,que,id,quien):
     response=supabase.table(tabla).select(que).eq(id, quien).execute()#Esta linea suelta un diccionario
     info=response.data[0][que]#Aqui obtengo el dato necesario nada mas
     return info #y aqui te retorno tu datico bro

#Ejemplo:saco los points del identificado con el name wilson
#sale("Users","points","name","Wilson"))