from flask import Blueprint, redirect
import flask

from flask import Flask, render_template
from flask import request

from flask import url_for
import forms

from config import DevelopmenConfig

from models import db
from models import Alumnos




alumnos = Blueprint('alumnos' , __name__)



@alumnos.route('/getAlum',methods=['GET','POST'])
def getalum():
    btn = request.form.get("registrarAlum")
    btn2 = request.form.get("modificar")
    create_form = forms.UserForm(request.form)
    if request.method=='POST':
        if btn == 'Registrar Alumno':
            alum = Alumnos(nombre= create_form.nombre.data,
                        apellidos = create_form.apellidos.data,
                        email = create_form.email.data)
            db.session.add(alum)
            db.session.commit()
        if btn2 == 'modificar':
            return redirect(url_for('alumnos.ABCompleto'))
    return render_template('index.html',form=create_form)


@alumnos.route('/ABCompleto',methods=['GET','POST'])
def ABCompleto():
    
    form = forms.UserForm(request.form)
    alumno = Alumnos.query.all()
    return render_template('ABCompleto.html',form=form,alumno = alumno)  


    
@alumnos.route("/modificar",methods=['GET','POST'])
def modificar():
    create_fprm= forms.UserForm(request.form)
    if request.method == 'GET':
        id=request.args.get('id')
        alum1=db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_fprm.id.data=request.args.get('id')
        create_fprm.nombre.data= alum1.nombre
        create_fprm.apellidos.data= alum1.apellidos
        create_fprm.email.data= alum1.email
    if request.method == 'POST':
        id = create_fprm.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum.nombre = create_fprm.nombre.data
        alum.apellidos = create_fprm.apellidos.data
        alum.email = create_fprm.email.data
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('alumnos.ABCompleto'))
    
    return render_template('modificar.html',form=create_fprm)

@alumnos.route("/eliminar",methods=['GET','POST'])
def eliminar():
    create_fprm= forms.UserForm(request.form)
    if request.method == 'GET':
        id=request.args.get('id')
        alum1=db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_fprm.id.data=request.args.get('id')
        create_fprm.nombre.data= alum1.nombre
        create_fprm.apellidos.data= alum1.apellidos
        create_fprm.email.data= alum1.email
    if request.method == 'POST':
        id = create_fprm.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum.nombre = create_fprm.nombre.data
        alum.apellidos = create_fprm.apellidos.data
        alum.emal = create_fprm.email.data
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for('alumnos.ABCompleto'))
    return render_template('eliminar.html',form=create_fprm)



   
