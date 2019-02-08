import pymysql
 
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='crud',
)

id=input("Input Id to Edit: ")
print("What to Update\n1. Fname\n2. Lname\n3. Age\n")
choice=int(input())

if choice==1:
    new=input("Enter The New First Name:  ")
    sql = "UPDATE student SET first=%s WHERE `id` = %s"
elif choice==2:
    new=input("Enter The New Last Name:  ")
    sql = "UPDATE student SET last=%s WHERE `id` = %s"
elif choice==3:
    new=input("Enter The New Age:  ")
    sql = "UPDATE student SET age=%s WHERE `id` = %s"
else:
    print("Invalid Input")



try:
    with connection.cursor() as cursor:
        
        try:
            cursor.execute(sql, (new,id))
            print("Successfully Updated...")
        except Exception as e:
            print("Oops! Something wrong")
            print (e)
 
    connection.commit()
finally:
    connection.close()
