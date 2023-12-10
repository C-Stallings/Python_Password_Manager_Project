import hashlib
import getpass


password_manager = {}


## function to ask user their username, password - hide it
## and store it in password_manager dictionary as a key-value pair
def create_account():
    username = input("Enter your desired username: ")
    password = getpass.getpass("Enter your desired password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print("Account created successfully!")


## function asking user if they want to create an account or login
def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if (
        username in password_manager.keys()
        and password_manager[username] == hashed_password
    ):
        print("Login successful!")
    else:
        print("Invalid username or password.")


## creating while loop function to prompt user to go through each choice until the break choice point
def main():
    while True:
        choice = input("Enter 1 to create an account, 2 to login, or 0 to exit: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")


## used to order the functions in the way it's told to
if __name__ == "__main__":
    main()
