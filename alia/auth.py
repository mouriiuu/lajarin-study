import os
def login():
    while True:
        os.system("cls || clear")
        username = input("username : ").strip()
        password = input("password : ")
        if username == "admin" and password == "admin123":
            role = "admin"
        elif username == "staff" and password == "staff123":
            role = "staff"
        else:
            print("SALAHHHHHH")
            enter = input("tekan enter kalo mau login ulang")
        # return role
