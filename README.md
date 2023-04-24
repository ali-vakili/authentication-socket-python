# authentication-socket-python

HTTP user authentication using socket

## Guide

### Requirements

```tsx
python -m venv env
```

**First, setup a virtual environment and activate it**.

```tsx
pip install -r requirements.txt
```

**Then install the requirements.txt in the file**.

### Database

    .
    ├── ...
    ├── server
    │   ├── databases           # Create databases folder
    │   │    ├── db.sqlite      # This can be created in database.py in the socket folder
    │   │
    │   ├── socket
    │   │    ├── database.py
    │   │    └── ...
    │   └── ...
    └── ...

You need to create a folder called **databases** in the shown path.

#### Working with database

```tsx
python database.py
```

**this will run the special variable `__name__` in file**.

###

```tsx
'database.py'

if __name__ == "__main__":
    create_table("students", username='TEXT NOT NULL', password='TEXT NOT NULL', student_code='INTEGER',
                 firstname='TEXT NOT NULL', lastname='TEXT NOT NULL', grade='INTEGER', field='TEXT NOT NULL')
```

**to create a database in the databases folder and also create a table called student**.

###

```tsx
'database.py'

if __name__ == "__main__":
    insert_row("{table_name}", "{username}", "{password}", {"student_code(number)"},
               "{first_name}", "{last_name}", {"grade(number)"}, "{field}")
```

**for inserting a row in your database, Don't forget to fill in the values in insert_row**.

### Start server

```tsx
python server.py
```

**it's essential first to make sure that the server is running for waiting connections from the client**.

### Start client

for running the client side and making authentication requests to the server, open the **login.html** file in html folder with **Live Server** and you are ready to go.
