import hashlib

def hash_read(articulo):
    return hashlib.sha256(articulo.encode('utf-8')).hexdigest()

def agregar_articulo(articulo):
    archivo_lista = open("C:\python\Archivos_Python\proyecto.txt","a")
    archivo_lista.write("{}\n " .format(articulo) )
    archivo_lista.close()



seed = input("Agregar Semilla: ")
agregar_articulo(seed)
hash_read(seed)
print("Hexa : " + hash_read(seed))