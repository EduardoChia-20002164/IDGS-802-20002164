import flask
from Alumnos.routes import alumnos
from Directivos.routes import direc
from Maestros.routes import maestros
from flask import Flask, redirect, render_template
from flask import request
from flask import url_for
import forms
from config import DevelopmenConfig
from flask_wtf.csrf import CSRFProtect
from models import db
from models import Alumnos

app= flask.Flask(__name__)
app.config.from_object(DevelopmenConfig)
app.register_blueprint(alumnos)
app.register_blueprint(direc)
app.register_blueprint(maestros)
csrf= CSRFProtect()
app.config['DEBUG']= True

@app.route("/",methods=['GET', 'POST'])
def home():
    btn = request.form.get("registra")

    if btn == 'Alumnos':
        return redirect((url_for('alumnos.getalum')))
    
    if btn == 'Maestros':
        return redirect((url_for('maestros.getmaes')))

    return render_template('main.html')

if __name__ =="__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
         db.create_all()
    app.run(debug=True, port=3000)