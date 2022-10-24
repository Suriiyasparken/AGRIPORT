
#register
#sign in
print("#WELCOME*to*AGRIPORT#")
option0=input("enter you are new user or old user for agriport:")
sheet = open('suriya2', "a+`")
print(sheet.write(f" {option0}\n"))
if option0 == 'new user' or option0 == 'old user' or option0 == 'olduser' or option0 == 'old' or option0 == 'new':
    print("you are new  sign up or sign in\n* sign up\n* sign in\n ")
    option=input("enter you are choice:")

    if option == 'sign up' or option == 'signup':
        agri = input("you r vendor or farmer:")
        if agri == 'vendor':

            name = input("enter you are name:")

            addr = input("enter you are district:")
            number = input("enter the your number:")
            shop_name = input("enter you are shop name or address:")

            file = open('suriya', "a+")
            file2a = file.write(f" 1)name is {name}\n")
            file3a = file.write(f" 2)district is {addr}\n")
            file4a = file.write(f" 3)phone number is {number}\n")
            file5a = file.write(f" 4)shop name or address is {shop_name}\n" )
            print(file2a)
            print(file3a)
            print(file4a)
            print("SUCCESSFULLY U R SIGN UP")

        else:
            name1 = input("enter you are name:")
            addr1 = input("enter you are district:")
            number1 = input("enter the your number:")
            harvest = input("harvest crop is:")
            file1 = open('suriya1', "a+")
            file2 = file1.write(f" 1)name is {name1}\n")
            file3 = file1.write(f" 2)district is {addr1}\n")
            file4 = file1.write(f" 3)phone number is {number1}\n")
            fileA = file1.write(f" 4){name1} harvest crop is {harvest}\n")
            print(file2)
            print(file3)
            print(file4)
            print(fileA)
            print("SUCCESSFULLY U R SIGN UP")

    if option == 'sign in' or option == 'signin':
        print("default username:suriya, password:admin123@")
        user_name=input("enter u r username:")
        passwd = input("enter ur passwoord:")

        if user_name == 'suriya' and passwd == 'admin123@':

            print("you r logged in")
            option2 = input("you r vendor or farmer:")
            if option2 == 'vendor':
                print("see u r farmers")
                file = open('suriya1', "r")
                print(file.read())
            elif option2 == 'farmer':
                print("see u r vendors")
                file1 = open('suriya', "r")
                print(file1.read())
        else:
            print("enter again username and password")


else:

    print("error mistake try again ")






















