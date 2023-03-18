from flask import Blueprint


direc = Blueprint('direc' , __name__)

@direc.route('/getDirec',methods=['GET'])
def getdirec():
    return {'key':'Directivos'}