import sqlite3
import bcrypt


path = '../databases/db.sqlite3'
connection = sqlite3.connect(path)
cursor = connection.cursor()


def close_database():
    cursor.close()
    connection.close()


def hash_password(password):
    # Generate a salt
    salt = bcrypt.gensalt(10)

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password


# Checks requested user
def check_login(username, password):
    query = f"SELECT * FROM students WHERE username = '{username}'"
    cursor.execute(query)
    result = cursor.fetchone()
    # print(result)
    try:
        if result:
            hashed_password = result[2]
            client_password = password.encode()
            match = bcrypt.checkpw(client_password, hashed_password)
            context = [True, result] if match else False
            # print(context)
            return context
        else:
            return False

    finally:
        print("Authentication checked")


# Create Table
def create_table(table_name, *args, **kwargs):
    # Create the CREATE TABLE statement
    table = f"CREATE TABLE {str(table_name)} ( id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL, student_code INTEGER, firstname TEXT NOT NULL, lastname TEXT NOT NULL, grade INTEGER, field TEXT NOT NULL )"
    print("\n"+table+"\n")

    # Execute the statement
    cursor.execute(table)
    connection.commit()
    close_database()


# Insert Row To Table
def insert_row(table_name, username, password, student_code, firstname, lastname, grade, field):
    # Hash the password
    hashed_password = hash_password(password)

    # Create the list of column names and values
    row = f"INSERT INTO {table_name} (username, password, student_code, firstname, lastname, grade, field) VALUES ('{username}', '{hashed_password}', '{student_code}', '{firstname}', '{lastname}', '{grade}', '{field}')"
    query = f"INSERT INTO {table_name} (username, password, student_code, firstname, lastname, grade, field) VALUES (?, ?, ?, ?, ?, ?, ?)"
    print(row)

    # Create the INSERT INTO statement
    cursor.execute(query, (username, hashed_password,
                   student_code, firstname, lastname, grade, field))
    connection.commit()
    close_database()


if __name__ == "__main__":
    create_table("students", username='TEXT NOT NULL', password='TEXT NOT NULL', student_code='INTEGER',
                 firstname='TEXT NOT NULL', lastname='TEXT NOT NULL', grade='INTEGER', field='TEXT NOT NULL')

    # insert_row("{table_name}", "{ussername}", "{password}", {"student_code(number)"},
    #         "{first_name}", "{last_name}", {"grade(number)"}, "{field}")
