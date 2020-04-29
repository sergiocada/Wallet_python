import hashlib,datetime,re,os,json

register = True

def hash_read(articulo):
    return hashlib.sha256(articulo.encode('utf-8')).hexdigest()

def agregar_articulo(articulo):
    archivo_lista = open("proyecto.txt","w")
    archivo_lista.write("{}" .format(articulo) )
    archivo_lista.close()
 
def Registro():
    dato = {}
    dato['Wallet'] = []
    print("|-------Registro-------|")
    palabras = (input("Agregar palabras: "))
    correo = input("Agregar correo: ")
    hora_actual = datetime.datetime.now().time()
    seed = str(palabras)+correo+str(hora_actual)
    hashIni =hash_read(seed) 

    dato['Wallet'].append({
        'palabras': palabras,
        'correo':correo,
        'tiempo':str(hora_actual),
        'Hash':hashIni
    })
    with open('dato.json', 'w') as file:
        json.dump(dato, file, indent=4)
    
    while True:
        if register:
            agregar_articulo(seed)
            #print("Su hash es :" + hashIni)
            break
        else:
            print("Algo esta mal")
            Registro()
   

def Hash_Bienvenida():
    if os.stat("proyecto.txt").st_size == 0:
        print ("Vacio")
        Registro()
    else:
        file = open("proyecto.txt", "r")
        archivo = file.readline()
        file.close()
        print("Su hash es :" + hash_read(archivo))

        
        
Hash_Bienvenida()