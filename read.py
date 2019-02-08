import pymysql
 
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='crud',
)
 
try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM student "
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
 
            print("Id\t\t First Name\t\tLast Name\t\tAge")
            for row in result:
                print(str(row[0]) + "\t\t" + row[1] + "\t\t\t" + row[2] + "\t\t\t" + str(row[3]))
 
        except Exception as e:
            print("Oops! Something wrong")
            print (e)
 
    connection.commit()
finally:
    connection.close()
