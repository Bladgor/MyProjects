from mysql.connector import connect, Error
from config_data import config


try:
    with connect(
        host="localhost",
        user='root',
        password=config.PASSWORD,
        database='shop'
    ) as connection:
        select_movies_query = "SELECT name, price FROM shop.good LIMIT 5"
        with connection.cursor() as cursor:
            cursor.execute(select_movies_query)
            result = cursor.fetchall()
            for row in result:
                print(row)
except Error as e:
    print(e)
