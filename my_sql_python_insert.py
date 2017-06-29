import mysql.connector
from mysql.connector import errorcode
import time

def insert(name, password):
    try:
        cnx = mysql.connector.connect(user='root', password='toor',
                                      host='127.0.0.1',
                                      database='new_DB')
        cursor = cnx.cursor()


        query = 'INSERT INTO `new_DB`.`test`(`name`, `pass`) VALUES ("{name}", "{password}");'.format(name=name,password=password)

        cursor.execute(query)

        cnx.commit()
        cursor.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()