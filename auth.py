# Create Login and Signup classes to handle user authentication
# using a MySQL database.
# first install pymysql using pip
# pip install pymysql
import pymysql as sql

# Database connection details
def connect():
    return sql.connect( host='localhost',user='root',password='',database='auth_user')
    

# Create User Login
def signup(username, password):
    """
    Registers a new user in the database.
    """
    conn = connect()
    cursor = conn.cursor()

    # Check if the username already exists
    cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    if cursor.fetchone():
        conn.close()
        return "Username already exists."

    # Insert new user
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    conn.close()
    return "Signup successful!"

def login(username, password):
    """
    Logs in a user by checking credentials.
    """
    conn = connect()
    cursor = conn.cursor()

    # Check if credentials match
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    result = cursor.fetchone()
    conn.close()

    if result:
        return "Login successful!"
    else:
        return "Invalid username or password."