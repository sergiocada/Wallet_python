from flask import Flask,render_template, request, redirect, url_for,jsonify
import hashlib,datetime,os,json
from validacion import wallet
from Transaccion import transaccion

app = Flask(__name__)

def hash_read(datos):
    return hashlib.sha256(datos.encode('utf-8')).hexdigest()

@app.route("/wallet", methods=["GET", "POST"])
def ingreso():
    if os.stat("proyecto.txt").st_size == 0:
        print ("Vacio")
        return redirect(url_for('registro'))
    else:
        print("lleno")
        return redirect(url_for('transaccion'))

@app.route("/Registro_wallet", methods=["GET", "POST"])
def registro():
    if request.method == 'POST':
        palabras = request.form['name']
        correo = request.form['email']
        hora_actual = datetime.datetime.now().time()
        seed = str(palabras)+correo+str(hora_actual)
        hash_origen = hash_read(seed)
        seed = str(palabras)+correo+str(hora_actual)
        wallet = {
            "origen":"wallet",
            "operacion":"validar",
            "palabras":str(palabras),
            "email":str(correo),
            "hora_actual":str(hora_actual),
            "hash_origen":hash_origen
        }
        archivo = open("validacion.py","w")
        archivo.write("wallet = {}" .format(wallet) )
        archivo.close()
        archivo = open("proyecto.txt","w")
        archivo.write("{}" .format(seed) )
        archivo.close() 
        wallet_1 = {}
        wallet_1['datos'] = []
        wallet_1['datos'].append({
            "palabras":str(palabras),
            "email":str(correo),
            "hora_actual":str(hora_actual),
            "hash_origen":str(hash_origen)
        })
        with open('wallet.json', 'w') as file:
            json.dump(wallet_1, file, indent=4)
        return redirect(url_for('validacion'))
    return render_template("signup_form.html")

@app.route("/wallet_1", methods=["GET","POST"])
def validacion():
    r = requests.post('http://142.44.246.23:5596/coordinator',datos=jsonify({"wallet":wallet}))
    datos = request.get_json()
    respuesta = datos["respuesta"]
    print("La respuesta es "+respuesta)
    if respuesta.upper() == "TRUE":
        print("Datos correctos")
        return redirect(url_for('transaccion'))
    else:
        print("Datos incorrectos")
        return redirect(url_for('registro'))
        
@app.route("/datos_wallet2")
def datos_transaccion():
    return jsonify({"wallet":transaccion})

@app.route("/saldo",methods=["GET","POST"])
def saldo():
    r = requests.post('http://142.44.246.23:5596/coordinator',datos={"origen":"wallet","operacion":"consultarfondos"})
    datos = request.get_json()
    saldo = datos["saldo"]
    usuario = {'saldo':saldo}
    return render_template('Saldo.html', usuario = usuario)

@app.route("/validacion",methods=["GET","POST"])
def validacion_transaccion():
    r = requests.post('http://142.44.246.23:5596/coordinator',datos=jsonify({"wallet":transaccion}))
    datos = request.get_json()
    respuesta = datos["respuesta"]
    if respuesta.upper()=="TRUE":
        usuario = {'transaccion':"Existoso"}
        return render_template('inicio.html', usuario = usuario)
        return redirect(url_for('saldo'))
    else:
        usuario = {'transaccion':"Denegado"}
        return render_template('inicio.html', usuario = usuario)
        return redirect(url_for('transaccion'))

@app.route("/transaccion", methods=["GET","POST"])
def transaccion():
    if request.method == 'POST':
        dir1 = request.form['dir1']
        dir2 = request.form['dir2']
        dinero = request.form['dinero']
        transaccion = {
            "origen":"wallet",
            "operacion":"registrartransaccion",
            "dir1":str(dir1),
            "dir2":str(dir2),
            "dinero":str(dinero)
        }
        archivo = open("Transaccion.py","w")
        archivo.write("transaccion = {}" .format(transaccion) )
        archivo.close() 
        return redirect(url_for('validacion_transaccion'))
    with open('wallet.json') as contenido:
        datos_wallet = json.load(contenido)
        for dato in datos_wallet['datos']:
            verificacion = dato['hash_origen']
            print(verificacion)
    usuario = {'name':verificacion}
    return render_template('inicio.html', usuario = usuario)

if __name__ == '__main__':
    app.run(host="142.44.246.66",debug=True,port=4000)
