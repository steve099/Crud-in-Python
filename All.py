import pymysql
connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='mycrud',
        )
    

def create():
        fname = input("Enter your First Name: ")
        lname = input("Enter your Last Name: ")
        age = input("Enter your Age: ")

        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO student (`first_name`, `Last_name`, `Age`) VALUES (%s, %s, %s)"
                try:
                    cursor.execute(sql, (fname, lname, age))
                    print("Task added successfully")
                except Exception as e:
                    print("Something wrong")
                    print (e);
     
                connection.commit()
        finally:
                return

def read():
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
                print("Something wrong")
                print (e)
     
            connection.commit()
    finally:
        return

def update():
        
    studid=input("Input Id to Edit: ")
    print("What to Update\n1. Fname\n2. Lname\n3. Age\n")
    choice=int(input())

    if choice==1:
        new=input("Enter your First Name:  ")
        sql = "UPDATE student SET first_name=%s WHERE `id` = %s"
    elif choice==2:
        new=input("Enter your Last Name:  ")
        sql = "UPDATE student SET Last_name=%s WHERE `id` = %s"
    elif choice==3:
        new=input("Enter your Age:  ")
        sql = "UPDATE student SET Age=%s WHERE `id` = %s"
    else:
        print("Invalid Input")



    try:
        with connection.cursor() as cursor:
                
            try:
                cursor.execute(sql, (new,studid))
                print("Successfully Updated...")
            except Exception as e:
                print("Something wrong")
                print (e)
         
        connection.commit()
    finally:
            return
def delete():
    id=input("Input Id to be Deleted: ")

    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM student WHERE id = %s"
            try:
                cursor.execute(sql, (id,))
                print("Successfully Deleted...")
            except Exception as e:
                print("Something wrong")
                print (e)
     
        connection.commit()
    finally:
            return
def main():
    while True:    

        print("----------CRUD program in Python-----------");
        print("1. Create\n2. Read\n3. Update\n4. Delete\n5. Exit");

        choice=int(input("Enter Your Choice:"))

        if choice==1:
            create()
        elif choice==2:
            print("List of Student: ")
            read()
        elif choice==3:
        
            update()
        elif choice==4:
        
            delete()
        elif choice == 5:
            break
        else:
            print("Invalid Input ");
        
main()

        
