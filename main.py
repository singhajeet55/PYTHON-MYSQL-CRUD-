import mysql.connector

def connect_db():
    conn = mysql.connector.connect(host="localhost", user="root", password="admin", database="db1")
    cursor = conn.cursor()
    return conn, cursor

def disconnect_db(conn_tuple: tuple):
    conn_tuple[1].close()
    conn_tuple[0].close()


q1, q2, conn_tuple = "DROP TABLE IF EXISTS student;", "Create table student(roll_no integer(4) PRIMARY KEY,first_name varchar(20),last_name varchar(20))", connect_db()
conn_tuple[1].execute(q1)
conn_tuple[1].execute(q2)
conn_tuple[0].commit()
disconnect_db(conn_tuple=conn_tuple)



def insert_Data():
    roll_no = int(input("Enter roll_no: "))
    first_name = input("Enter first_name: ")
    last_name = input("last_name :")
    insert_query = f"INSERT INTO student (roll_no,first_name,last_name ) VALUES ('{roll_no}','{first_name}','{last_name}');"
    conn, cursor = connect_db()
    cursor.execute(insert_query)
    conn.commit()
    disconnect_db(conn_tuple)
    print("Data inserted successfully!")
def search_data():
    search_name = input("Enter the name or roll_no to search:")
    search_query = "SELECT * FROM student WHERE first_name LIKE %s OR last_name LIKE %s OR CONCAT(first_name, ' ', last_name) LIKE %s OR roll_no = %s;"
    conn, cursor = connect_db()
    cursor.execute(search_query,('%' + search_name + '%', '%' + search_name + '%', '%' + search_name + '%', search_name))
    results = cursor.fetchall()
    disconnect_db(conn_tuple)
    if results:
        for row in results:

            print(f"roll_no: {row[0]}, first_name: {row[1]}, last_name: {row[2]}")

    else:

        print("No matching data found.")

def update_data():

    print("Press 1 to update roll_no")
    print("Press 2 to update first_name")
    print("Press 3 to update last_name")
    print("Press 4 to exit")

    sel=int(input('enter the value:'))

    if sel==1:
        new_roll_no,old_roll_no = input('Enter the old roll_no:'), input('Enter the new roll_no:')
        update_new_name=f"UPDATE student SET roll_no='{new_roll_no}'WHERE roll_no='{old_roll_no}'"
        conn, cursor = connect_db()
        cursor.execute(update_new_name)
        conn.commit()
        disconnect_db(conn_tuple)
        print("Data updated successfully!")


    if sel==2:

        first_name,first_name_new=input('Enter the old first name'),input('Enter the new first name')
        update_new_name=f"UPDATE student SET first_name='{first_name_new}'WHERE first_name='{first_name}'  "
        conn, cursor = connect_db()
        cursor.execute(update_new_name)
        conn.commit()
        disconnect_db(conn_tuple)
        print("Data updated successfully!")

    elif sel==3:

        last_name,last_name_new = input('Enter the old last name:'),input('Enter the new last name:')
        update_last_name = f"UPDATE student SET last_name='{last_name_new}'WHERE last_name='{last_name}'"
        conn,cursor = connect_db()
        cursor.execute(update_last_name)
        conn.commit()
        disconnect_db(conn_tuple)
        print("Data updated successfully!")


def delete_data():

    roll_no = int(input("Enter the roll_no of the student to delete: "))
    delete_query = f"DELETE FROM student WHERE roll_no = {roll_no};"
    conn, cursor = connect_db()
    cursor.execute(delete_query)
    conn.commit()
    disconnect_db(conn_tuple=conn_tuple)
    print("Data deleted successfully!")

def main():
    while True:
        print("Options:")
        print("1. Insert data")
        print("2. Search data")
        print("3. Update data")
        print("4. Delete data")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            insert_Data()
        elif choice == 2:
            search_data()
        elif choice == 3:
            update_data()
        elif choice == 4:
            delete_data()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()






