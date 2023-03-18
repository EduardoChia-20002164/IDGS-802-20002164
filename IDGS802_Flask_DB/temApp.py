from db import get_connection
'''
try:
    connection  = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call verRegistrosTabla()')
        resutset = cursor.fetchall()
        cursor.close()
        for row in resutset:
            print(row)
except Exception as ex:
    print('ERROR')

'''

'''
try:
    connection  = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call verRegistrosTablaId(%s)',(2,))
        resutset = cursor.fetchall()
        cursor.close()
        for row in resutset:
            print(row)
except Exception as ex:
    print('ERROR')

    '''

try:
    connection  = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call InsertRegistrosTabla(%s,%s,%s)',('Nadia','Juarez','nad@gmail.com'))
    connection.commit()
    connection.close()
except Exception as ex:
    print(ex)