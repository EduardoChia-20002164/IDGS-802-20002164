from flask import Blueprint, redirect
import flask
from flask import Flask, render_template
from flask import request
from flask import url_for
import forms
from config import DevelopmenConfig
from models import db
from models import Maestros
from temApp import insertMaestro , getAllTabla, searchId

maestros = Blueprint('maestros' , __name__)

@maestros.route('/getMaes',methods=['GET','POST'])
def getmaes():
    btn = request.form.get("registrarMaes")
    btn2 = request.form.get("modificar")
    create_form = forms.UserForm(request.form)
    if request.method=='POST':
        if btn == 'Registrar Mestro':
            nombre= create_form.nombre.data
            apellido = create_form.apellidos.data
            email = create_form.email.data
            insertMaestro.insertM(nombre, apellido, email)
        if btn2 == 'modificar':
            return redirect(url_for('maestros.ABCompletoM'))
    return render_template('indexM.html',form=create_form)


@maestros.route('/ABCompletoM',methods=['GET','POST'])
def ABCompletoM():
    btn5 = request.form.get("buscarID")
    form = forms.UserForm(request.form)
    maestr = getAllTabla.getall()
    
    if request.method=='POST':
        if btn5 == 'Buscar':
            id= form.buscar.data
            if id != '':
                maestr = searchId.searchM(id)      
    return render_template('ABCompletoM.html',form=form,maestro = maestr)  


    
@maestros.route("/modificarM",methods=['GET','POST'])
def modificarM():
    create_fprm= forms.UserForm(request.form)
    if request.method == 'GET':
        id=request.args.get('id')
        alum1=db.session.query(Maestros).filter(Maestros.id == id).first()
        create_fprm.id.data=request.args.get('id')
        create_fprm.nombre.data= alum1.nombre
        create_fprm.apellidos.data= alum1.apellidos
        create_fprm.email.data= alum1.email
    if request.method == 'POST':
        id = create_fprm.id.data
        maes = db.session.query(Maestros).filter(Maestros.id==id).first()
        maes.nombre = create_fprm.nombre.data
        maes.apellidos = create_fprm.apellidos.data
        maes.email = create_fprm.email.data
        db.session.add(maes)
        db.session.commit()
        return redirect(url_for('maestros.ABCompletoM'))
    
    return render_template('modificarM.html',form=create_fprm)

@maestros.route("/eliminarM",methods=['GET','POST'])
def eliminarM():
    create_fprm= forms.UserForm(request.form)
    if request.method == 'GET':
        id=request.args.get('id')
        alum1=db.session.query(Maestros).filter(Maestros.id == id).first()
        create_fprm.id.data=request.args.get('id')
        create_fprm.nombre.data= alum1.nombre
        create_fprm.apellidos.data= alum1.apellidos
        create_fprm.email.data= alum1.email
    if request.method == 'POST':
        id = create_fprm.id.data
        maes = db.session.query(Maestros).filter(Maestros.id==id).first()
        maes.nombre = create_fprm.nombre.data
        maes.apellidos = create_fprm.apellidos.data
        maes.emal = create_fprm.email.data
        db.session.delete(maes)
        db.session.commit()
        return redirect(url_for('maestros.ABCompletoM'))
    return render_template('eliminarM.html',form=create_fprm)



   