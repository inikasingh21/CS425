import mysql.connector
from mysql.connector import Error

def execute_query(host_name, user_name, user_password,db_name, query):
    connection = None
    cursor = None
    result = []
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name

        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
    except Error as e:
        print("Error executing query:", e)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    return result
