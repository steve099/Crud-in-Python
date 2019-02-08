import pymysql
 
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='crud',
)
 
fname = input("Enter your First Name: ")
lname = input("Enter your Last Name:  ")
age = input("Enter your Age: ")

try:
    with connection.cursor() as cursor:
        sql = "INSERT INTO student (`first`, `last`, `age`) VALUES (%s, %s, %s)"
        try:
            cursor.execute(sql, (fname, lname, age))
            print("Task added successfully")
        except Exception as e:
            print("Oops! Something wrong")
            print (e);
 
    connection.commit()
finally:
    connection.close()
