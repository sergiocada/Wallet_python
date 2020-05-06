from flask import Flask,render_template, request, redirect, url_for,jsonify
import hashlib,datetime,os,json
from validacion import wallet
from Transaccion import transaccion

app = Flask(__name__)

@app.route("/wallet", methods=["GET", "POST"])
def ingreso():
    datos = jsonify({"wallet":transaccion})
    return datos

if __name__ == '__main__':
    app.run(debug=True,port=5000)