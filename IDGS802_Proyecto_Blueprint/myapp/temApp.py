from db import get_connection

class getAllTabla:
    def getall():
        try:
            connection  = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call VerRegistrosTablaMaestros()')
                resutset = cursor.fetchall()
                cursor.close()
                    
        except Exception as ex:
            print('ERROR')
        
        return resutset

class searchId:
    def searchM(id):
        try:
            connection  = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call VerRegistrosTablaIdMaestros(%s)',(id,))
                resutset = cursor.fetchall()
                cursor.close()  
        except Exception as ex:
                print('ERROR')
        return resutset

class insertMaestro:
    def insertM(nombre,apellido,email):
        try:
            connection  = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call InsertRegistrosTablaMestros(%s,%s,%s)',(nombre,apellido,email))
            connection.commit()
            connection.close()
        except Exception as ex:
            print(ex)

