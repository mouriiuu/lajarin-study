import csv
import os

def read_csv(filename):
    try:
        if not os.path.exists(filename):
            return [] 
        with open(filename,'r') as file:
            content = csv.DictReader(file) 
            return list(content)
    except FileNotFoundError:
        print("File tidak ditemukan")
    except Exception as e:
        print(f"Error : {e}")


def login():
    username = input("Username : ")

    if not username:
        print("username nya diboleh kosong woy")

    password = input("password : ")

    if not password:
        print("password tidak boleh kosong woy")

    data = read_csv('login/users.csv')
    if not data:
        print("list kosong!")
    else:
        for user in data:
            if user["username"] == username and user["password"] == password:
                return user["role"]
            else:
                print("login gagal")
