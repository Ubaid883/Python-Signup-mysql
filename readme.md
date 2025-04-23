## (Python + MySQL)

A simple command-line Signup, Login built using **Python** and **MySQL**. This project features user **Sign Up** and **Login** functionality with secure database integration via `pymysql`.

---

### ✨ Features

- 🔐 **User Authentication**
  - Sign up with unique usernames
  - Login with stored credentials from MySQL database
- 🗂️ **Modular Code Structure**
  - Authentication logic separated in `auth.py`
  - Main application logic in `main.py`
- 🖥️ **Command-line Interface**
  - Easy to use via terminal
  - Terminal screen clears between interactions for better UX

---

### 🧰 Tech Stack

- **Python 3**
- **MySQL**
- `pymysql` (Python library for MySQL)
- Optional: `os` module for terminal clearing

---

### 🚀 Getting Started

1. **Clone the repo**  
   ```bash
   git clone https://github.com/Ubaid883/Python-Signup-mysql.git
   cd pyhon_signup

2. **Install dependencies**
    ```bash
    pip install pymysql
3. **Set up MySQL database**
    ```bash
    CREATE DATABASE user_auth;
    USE user_auth;
    CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(255)
    )

4. **Update DB credentials in auth.py**
    ```bash
    DB_HOST = 'localhost'
    DB_USER = 'your_mysql_username'
    DB_PASSWORD = 'your_mysql_password'
    DB_NAME = 'user_auth'

5. **Run the project**
    ```bash
    python main.py

---

### 🔒 Future Improvements
- Password hashing with bcrypt

- Better error handling and logging

- Full CRUD operations (e.g., account management, balances)

- GUI version using tkinter or web version with Flask

---

### 📄 License

This project is open-source and available under the MIT License.