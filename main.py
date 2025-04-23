# main.py

from auth import signup, login

def main():
    print("Welcome! Choose an option:")
    print("1. Sign Up")
    print("2. Login")
    choice = input("Enter 1 or 2: ")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if choice == '1':
        message = signup(username, password)
    elif choice == '2':
        message = login(username, password)
    else:
        message = "Invalid choice."

    print(message)

if __name__ == "__main__":
    main()
