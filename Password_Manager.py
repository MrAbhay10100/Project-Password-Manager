print("*****************************************************************************************")
print("*****************************************************************************************")

print("\n\n\t\t\t\tWelcome to the Secure Password Manager\n\n")

print("*****************************************************************************************")
print("*****************************************************************************************\n")

def add_new():
    new_acc = input("Enter Account Name : ")
    pass_of_acc = input("Enter Pass : ")
    with open(f"pass.txt","a") as file:
        file.write((f"{new_acc} : {pass_of_acc}\n"))
        
def view_pass():
    acc_name = input("Enter your account name here : ")
    with open(f"Secure_Password_Manager\pass.txt","r") as file:
        print(file.read())
        
Main_passwd = input("Enter Main Password here : ")
    
if (Main_passwd == "123"): 

    while True:

        print('''\nChoose your options from here : 
        1 --> Add new password
        2 --> View stored password 
        3 --> QUIT? The Process ''')

        User_mode = input("\nWhat would you like to do Sir/Mam? ")
        
        if User_mode == "3":
            break
        elif User_mode == "1":
            add_new()
        elif User_mode == "2":
            view_pass()

        else:
            print("your option is wrong choose option from here :")
            continue

            print("*****************************************************************************************")
            print("*****************************************************************************************")

else:
    print("Wrong password")
    



















