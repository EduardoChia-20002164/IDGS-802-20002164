from flask import Blueprint


maestros = Blueprint('maestros' , __name__)

@maestros.route('/getMaes',methods=['GET'])
def getalum():
    return {'key':'Maestros'}