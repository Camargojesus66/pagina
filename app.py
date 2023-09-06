from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import dbase as dbase  

db = dbase.dbConnection()

app = Flask(__name__)

#Rutas de la aplicación
@app.route('/')
def home():
    tennis = db['tennis']
    tennisrecivido = tennis.find()
    return render_template('index.html', tenniss = tennisrecivido)

@app.route('/tennisjc66/<string:tennis>')
def productos(tennis):
    producto = db['tennis']
    productosrecividos = producto.find({'name': tennis})
    return render_template('index.html', producto = productosrecividos)



