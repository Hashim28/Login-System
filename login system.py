import re

def register():
    db = open("database","r")
    u = []
    p = []
    for i in db:
        a,b = i.split(", ")
        b = b.strip()
        u.append(a)
        p.append(b)
    login_data = dict(zip(u,p))
    user_name = create_username(u)
    pass_word = create_password()
    db = open("database", "a")
    db.write(user_name +", "+ pass_word+"\n")
    print("Registration success")

def create_username(u):
##Creating username
    #Fisrt letter should be alphabet
    #Username should contain '@' and '.'
    #There should not be any '.' immediate next to '@'
    db = open("database","r")
    username = input("Create a username:")
    if(username[0].isalpha()==False):
        print("Fisrt character should be alphabet")
        create_username(u)
    if("@." in username or username[-1] == "."):
        print("Invalid username")
        create_username(u)
    if("@" not in username or "." not in username):
        print("Invalid username")
        create_username(u)
    if(username in u):
        print("Username exist.Try different username")
        create_username(u)
    return username

def create_password():
##Creating password

    password = input("Create a password:")

    if(len(password)>5 and len(password)<16):

        check1 = re.search("[@_!#$%^&*()<>?/\|}{~:]",password)
        if(check1 == None):
            print("Password should contain minimum one special character")
            create_password()

        check2 = re.search("[0-9]",password)
        if(check2 == None):
            print("Password should contain minimum one digit")
            create_password()

        check3 = re.search("[A-Z]",password)
        if(check3 == None):
            print("Password should contain minimum one uppercase character")
            create_password()

        check4 = re.search("[a-z]",password)
        if(check4 == None):
            print("Password should contain minimum one lowercase character")
            create_password()
    else:
        print("Password length should be greater than 5 and less than 16")
        create_password()

    password1 = input("Confirm password:")

    if password != password1:
        print("Password not matched.Try again.")
        create_password()

    return password


def access():
    db = open("database","r")
    username = input("Enter your username:")
    if(len(username)<1):
        print("Please enter your username")
        access()

    u = []
    p = []
    for i in db:
        a, b = i.split(", ")
        b = b.strip()
        u.append(a)
        p.append(b)
    login_data = dict(zip(u, p))

    try:
        if(username in u):
            password = input("Enter your password:")
            if(login_data[username]==password):
                print("Hi, ",username,"\nWelcome")
            else:
                print("Incorrect Password")
                f = input("Forgot your password?(Press Y to retrieve your password):")
                if(f=="Y" or f=="y"):
                    fp = forgetpassword()
                    print(f"Your password is {fp}")
                else:
                    home()
        else:
            print("Username doesn't exist")
            i = input("Do yo want to register?(Press Y to register):")
            if(i=="Y" or i=="y"):
                register()
            else:
                home()
    except:
        print("Login error")

def forgetpassword():
    db = open("database", "r")
    u = []
    p = []
    for i in db:
        a, b = i.split(", ")
        b = b.strip()
        u.append(a)
        p.append(b)
    login_data = dict(zip(u, p))
    username = input("Enter your username:")
    return login_data[username]



def home():
    ch = int(input("1.Login \n2.Register \nEnter your choice:"))
    if(ch == 1):
        access()
    elif(ch == 2):
        register()
    else:
        print("Invalid choice")
        home()
home()