import pymysql
 
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='crud',
)
id=input("Input Id to be Deleted: ")

try:
    with connection.cursor() as cursor:
        sql = "DELETE FROM student WHERE id = %s"
        try:
            cursor.execute(sql, (id,))
            print("Successfully Deleted...")
        except Exception as e:
            print("Oops! Something wrong")
            print (e)
 
    connection.commit()
finally:
    connection.close()
