import socket
import re

#archivo = open("registro.txt", encoding="utf-8")


""" file=open("registro.txt","r")
contenido=file.readlines()
ejemplo = "1233" 

comparacion = contenido[0].find("1233")
print(comparacion)
if ejemplo == comparacion:
    print("Si esta")

lista = contenido.split(",")

print(lista)  """

file = open("registro.txt", encoding="utf-8")
archivo = file.read()
file.close()
dir1=("14087dcc233c8301c651467e9981332170653f5d50f7242e85aecd6cf3624153")

if re.search((dir1), archivo):
    print("Encontrada")
""" 
if buscar == True:
    print("Se encuentra")
 """