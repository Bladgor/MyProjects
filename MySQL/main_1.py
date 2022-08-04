from config_data import config

import mysql.connector
from mysql.connector import Error


def create_connection(host_name, user_name, user_password, user_db):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=user_db
        )
        print("Подключение к базе данных MySQL прошло успешно")
    except Error as e:
        print(f"Произошла ошибка '{e}'")

    return connection


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Произошла ошибка '{e}'")


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Запрос выполнен успешно")
    except Error as e:
        print(f"Произошла ошибка '{e}'")


connection_test = create_connection("remotemysql.com", config.USER, config.PASSWORD, '7z5r4sXnHW')

select_users = "SELECT * from users"
users = execute_read_query(connection_test, select_users)

for elem in users:
    print(list(elem))

connection_test.close()
