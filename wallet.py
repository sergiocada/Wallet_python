import hashlib,datetime,re,os,json

def cargar_datos():
    with open('coordinador.json') as contenido:
        Cordinadorcomprueba = json.load(contenido)
        for dato in Cordinadorcomprueba['Prueba']:
            verificacion = dato['comprobacion']
            print(verificacion)
    return verificacion

def hash_read(articulo):
    return hashlib.sha256(articulo.encode('utf-8')).hexdigest()

def agregar_articulo(articulo):
    archivo_lista = open("proyecto.txt","w")
    archivo_lista.write("{}" .format(articulo) )
    archivo_lista.close()
 
def Registro():
    dato = {}
    dato['WalletRegistro'] = []
    print("|-------Registro-------|")
    palabras = (input("Agregar palabras: "))
    correo = input("Agregar correo: ")
    hora_actual = datetime.datetime.now().time()
    seed = str(palabras)+correo+str(hora_actual)
    hashIni =hash_read(seed) 

    dato['WalletRegistro'].append({
        'palabras': palabras,
        'correo':correo,
        'tiempo':str(hora_actual),
        'Hash':hashIni
    })
    with open('dato.json', 'w') as file:
        json.dump(dato, file, indent=4)

    while True:
        if cargar_datos():
            agregar_articulo(seed)
            break
        else:
            print("Algo esta mal")
            cargar_datos()
            Registro()
def crear():
    saldo = {}
    saldo['SaldoWalet'] = []
    saldo['SaldoWalet'].append({
            'Ver_Saldo': True
        })
    with open('Contenidosaldo.json', 'w') as file:
        json.dump(saldo, file, indent=4)


def Mostrar_saldo():
    with open('Saldo.json') as contenido:
        saldoS = json.load(contenido)
        for dato in saldoS['Prueba1']:
            saldoTotal = dato['comprobacion']
            print(saldoTotal)
    return saldoTotal

    
def Hash_Bienvenida():
    if os.stat("proyecto.txt").st_size == 0:
        print ("Vacio")
        Registro()
    else:
        Dato_Transaccion = {}
        Dato_Transaccion['WalletEnvio'] = []
        file = open("proyecto.txt", "r")
        archivo = file.readline()
        file.close()
        Publica = hash_read(archivo)
        Privada = hash_read(Publica)
        print("Su hash es :" + Publica)
        dir2 = input("¿Cual es la dirreccion hash a la cual quieres enviar dinero?")
        dinero = input("¿Cuanto dinero quieres enviar?")
        

        Dato_Transaccion['WalletEnvio'].append({
            'DireccionHash_1': Publica,
            'DireccionHash_2':dir2,
            'dinero':dinero
        })
        with open('Dato_Transaccion.json', 'w') as file:
            json.dump(Dato_Transaccion, file, indent=4)

        while True:
            if cargar_datos():
                print("Transaccion exitosa")
                saldo = input("¿Deseas ver su saldo?")   
                if saldo.lower() == "si":
                    crear()
                    print("Saldo {}".format(Mostrar_saldo()))
                else:
                    break    
                break    
            else:
                print("Transaccion denegada")
                saldo = input("¿Desea ver su saldo ?")   
                if saldo.lower() == "si":
                    crear()
                    print("Saldo {}".format(Mostrar_saldo()))
                else:
                    Hash_Bienvenida()    

Hash_Bienvenida()