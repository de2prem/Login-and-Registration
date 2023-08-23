import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
regexp= "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"




def register():
    username = (input("Enter emailid "))

    def check(username):
        if (re.fullmatch(regex, username)):
            return username

        else:
            username=(input("Please enter a valid mail id"))
            check(username)

    check(username)
    password = (input("Please input your desired password "))
    def checkpass(password):
        if (re.match(regexp, password)):
            return password
        else:
           password= (input("Please reenter password, it must have minimum one special character,one digit,one uppercase & one lowercase character"))
           checkpass(password)
    checkpass(password)
    file = open(r"C:\Users\Deepak\Desktop\Register.txt", "w")
    file.write(username)
    file.write(" ")
    file.write(password)
    file.write("\n")
    file.close()
    if login():
        print("You are now logged in...")
    else:
        print("You aren't logged in!")

def login():
    username = input("Please enter your email id")
    def check(username):
        if (re.fullmatch(regex, username)):
            return username

        else:
            username=(input("Please enter a valid mail id"))
            check(username)

    check(username)
    password = input("Please enter your password")

    def reset_password():
        # Prompt user for email/username
        email = input("Enter email: ")

        # Open file for reading
        with open(r"C:\Users\Deepak\Desktop\Register.txt", "r") as file:
            # Read lines from file
            lines = file.readlines()

            # Check if email/username exists in file
            for line in lines:
                record = line.strip().split(",")
                if email == record[0]:
                    # Prompt user for new password
                    new_password = input("Enter new password: ")

                    # Validate new password
                    if not validate(email, new_password):
                        print("Invalid password")
                        return
    def checkpass(password):
        if (re.match(regexp, password)):
            return password
        else:
           password= (input("Please reenter password, it must have minimum one special character,one digit,one uppercase & one lowercase character"))
           checkpass(password)
    checkpass(password)
    for line in open(r"C:\Users\Deepak\Desktop\Register.txt", "r").readlines(): # Read the lines
        login_info = line.split() # Split on the space, and store the results in a list of two strings
    if username == login_info[0] and password == login_info[1]:
            print("Correct credentials!")
            return True
    else:

        choice = input("Email/username or password is incorrect. Do you want to (R)egister or (F)orgot password? or R(E)try")
        if choice.lower() == "r":
            register()
        elif choice.lower() == "f":
            reset_password()
        elif choice.lower() == "e":
            login()
        else:
            print("Invalid choice")
        register()
        return False


login()
