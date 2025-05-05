master_pwd = input("What is your master password? ")

def add():
    name = input("Enter your name: ")
    pwd = input("Enter your password: ")

    with open("password.txt","a") as f:
        f.write(name + "|" + pwd + "\n")

def view():
    with open("password.txt","r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ", user, "| Password: ", passw)
            
while True:
    mode = input("Would you like to add new password or view password? \n "
                 "click (add) for add new password \n "
                 "click (view) for view password \n "
                 "click (Q) for exit: ").lower()

    if mode == "q":
        break
    elif mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Your typing is valid!")

print("Good Bye!")