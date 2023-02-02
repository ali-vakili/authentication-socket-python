from pages.profile import generate_html
from pages.page404 import page_not_found
from pages.page401 import unauthorized_access
from database import check_login
from pathlib import Path
import json


session = {}

keys = ["id", "username", "password", "student_code", "first_name", "last_name",
        "grade", "field_of_study"]


def get_message(message):
    if isinstance(message, list):
        state, user = message
        # skip the password of user and make dictionary of keys and values
        user = {keys[i]: str(user[i]) for i in range(len(keys)) if i != 2}
        message = [state, user]
        return message
    elif isinstance(message, bool):
        return [message, None]


def get_paths(path):
    path_parts = path.split('/')
    if path_parts[1] == 'static':
        directory = path_parts[2]
        file = path_parts[3]
        return directory, file

    elif path_parts[1] == 'profile':
        username = path_parts[2]
        return username


def unauthorized():
    headers = b"HTTP/1.1 401 Unauthorized\r\n"
    headers += b"Access-Control-Allow-Origin: *\r\n"
    headers += b"Content-Type: text/html\r\n"
    response_body = unauthorized_access()
    # headers += b"Content-Type: application/json\r\n"
    # response_body = b'{"message": "Something went wrong!"}'
    return headers, response_body


def not_found(type):
    headers = b"HTTP/1.1 404 Not Found\r\n"
    headers += b"Access-Control-Allow-Origin: *\r\n"
    if type == 'page':
        headers += b"Content-Type: text/html\r\n"
        response_body = page_not_found()
    elif type == 'message':
        headers += b"Content-Type: application/json\r\n"
        response_body = b'{"message": "Path does not exist!"}'
    return headers, response_body


def handleRequests(method, path, body):
    if path == "/login":
        # Send a response
        if method == "OPTIONS":
            headers = b"HTTP/1.1 200 OK\r\n"
            headers += b"Access-Control-Allow-Origin: *\r\n"
            headers += b"Access-Control-Allow-Methods: POST\r\n"
            headers += b"Access-Control-Allow-Headers: Content-Type\r\n"
            headers += b"\r\n"
            return headers, None

        elif method == "POST":
            # Parse the body as JSON
            data = json.loads(body)
            username = data['username'].strip()
            password = data['password'].strip()
            print(
                f"Client Login reqeust message: username: {data['username']} , password: {data['password']}")
            result = check_login(username, password)
            state, user = get_message(result)
            session['user'] = user
            print(f"matching: {state}")

            if state:
                headers = b"HTTP/1.1 302 Found\r\n"
                headers += b"Access-Control-Allow-Origin: *\r\n"
                headers += b"Location: http://127.0.0.1:9000/profile\r\n"
                headers += b"Content-Type: application/json\r\n"
                headers += b"\r\n"
                response_body = json.dumps({"user": user}).encode()
                return [headers, response_body]

            elif not state:
                headers = b"HTTP/1.1 401 Unauthorized\r\n"
                headers += b"Access-Control-Allow-Origin: *\r\n"
                headers += b"Content-Type: application/json\r\n"
                headers += b"\r\n"
                if username == '' or password == '':
                    response_body = b'{"message": "Username and Password is required!"}'
                else:
                    response_body = b'{"message": "Username or Password is wrong!"}'
                return headers, response_body

    elif path == '/profile':
        if method == "OPTIONS":
            headers = b"HTTP/1.1 200 OK\r\n"
            headers += b"Access-Control-Allow-Origin: *\r\n"
            headers += b"Access-Control-Allow-Methods: POST\r\n"
            headers += b"Access-Control-Allow-Headers: Content-Type\r\n"
            headers += b"\r\n"
            return headers, None

        elif method == "GET":
            # username = get_paths(path)
            if 'user' in session:
                user = session['user']
                # if user['username'] == username:
                headers = b"HTTP/1.1 200 OK\r\n"
                headers += b"Access-Control-Allow-Origin: *\r\n"
                headers += b"Content-Type: text/html\r\n"
                headers += b"\r\n"
                response_body = generate_html(user)
                return headers, response_body

                # else:
                #     headers, response_body = unauthorized()
                #     return headers, response_body

            else:
                headers, response_body = unauthorized()
                return headers, response_body

    elif path.startswith("/static/"):
        if method == "GET":
            directory, file = get_paths(path)
            headers = b"HTTP/1.1 200 OK\r\n"
            headers += b"Access-Control-Allow-Origin: *\r\n"
            if directory == 'css':
                headers += b"Content-Type: text/css\r\n"
            elif directory == 'javascript':
                headers += b"Content-Type: application/javascript\r\n"
            elif directory == 'image':
                headers += b"Content-Type: image/png\r\n"
            else:
                headers, response_body = not_found('message')
                return headers, response_body
            headers += b"\r\n"
            with open(f"../../static/{directory}/{file}", "rb") as file:
                return headers, file.read()

    else:
        headers, response_body = not_found('page')
        return headers, response_body
