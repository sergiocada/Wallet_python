import hashlib
import re

def hash_read(usuario):
    return hashlib.sha256(usuario.encode('utf-8')).hexdigest()

def agregar_usuario(usuario):
    archivo_lista = open("proyecto.txt","w")
    archivo_lista.write("{}\n " .format(usuario) )
    archivo_lista.close()

def Registro():
    print("|-------Registro-------|")
    palabras = input("Agregar palabras: ")
    correo = input("Agregar correo: ")
    contraseña = input("Agregar contraseña: ")
    saldo = input("Agregar Saldo: ")
    seed = palabras+" "+correo+" "+contraseña+ " "
    seedPawword = hash_read(seed) + " " + contraseña + " " +saldo
    agregar_usuario(seedPawword)
    print("Hexa : " + hash_read(seed))

def cuentaLogin():
    while True:
        cuenta = input("Tienes cuenta? \n")
        if cuenta.upper() =="SI":
            file = open("proyecto.txt", encoding="utf-8")
            archivo = file.read()
            file.close()
            dir1 = input("Agregar hash: ")
            if re.search((dir1), archivo):
                print("Encontrada")
                contraseñaN = input("Agregar contraseña: ")
                if re.search((contraseñaN), archivo):
                    print("Encontrada")
            else:
                print("No se encuentra el hash\n Gracias Hasta la proxima")
        elif cuenta.upper() == "NO":
            Registro()        

cuentaLogin()