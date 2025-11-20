import csv
from prettytable import PrettyTable

DATA_FILE = "crud/data.csv"

def read_csv(filename):
    data = []
    with open(filename, "r") as file:
        content = csv.DictReader(file)
        for bio in content:
            data.append(bio)
    return data


def read_data():
    table = PrettyTable()
    data = read_csv(DATA_FILE)
    table = PrettyTable()
    table.field_names = ["ID","Nama Depan", "Nama Belakang", "Usia"]
    for bio in data:
        table.add_row([bio["id"],bio["nama_depan"],bio["nama_belakang"],bio["usia"]])
    print(table)

def create_data():
    namaDepan = input("Nama depan: ")
    namaBelakang = input("Nama belakang: ")
    usia = int(input("Usia : "))
    data = read_csv(DATA_FILE)
    newOrang = {
        "id": len(data) + 1,
        "nama_depan": namaDepan,
        "nama_belakang": namaBelakang,
        "usia": usia
    }
    data.append(newOrang)

    with open("crud/data.csv","w") as writer:
        fieldNames = ["id","nama_depan","nama_belakang","usia"]
        alat = csv.DictWriter(writer,fieldnames=fieldNames)
        alat.writeheader()
        alat.writerows(data)
    print("data berhasil ditambahkan")

def delete_data():
    read_data()
    id = input("Masukkan ID yang ingin dihapus: ")
    content = read_csv(DATA_FILE)
    data = []
    for bio in content:
        if bio["id"] == id:
            print(f"Menghapus {bio["nama_depan"]}")
            continue
        data.append(bio)

    with open("crud/data.csv","w") as writer:
            fieldNames = ["id","nama_depan","nama_belakang","usia"]
            alat = csv.DictWriter(writer,fieldnames=fieldNames)
            alat.writeheader()
            alat.writerows(data)
    print("data berhasil dihapus") 



def update_data():
    read_data()
    id = input("Masukkan ID yang ingin diupdate: ")
    content = read_csv(DATA_FILE)
    data = []
    for bio in  content:
        if bio["id"] == id:
            bio["nama_depan"] = input(f"Nama Depan ({bio["nama_depan"]}) : ")
            bio["nama_belakang"] = input(f"Nama Belakang ({bio["nama_belakang"]}) : ")
            bio["usia"] = input(f"Usia ({bio["usia"]}) : ")
        data.append(bio)

    with open("crud/data.csv","w") as writer:
        fieldNames = ["id","nama_depan","nama_belakang","usia"]
        alat = csv.DictWriter(writer,fieldnames=fieldNames)
        alat.writeheader()
        alat.writerows(data)
    print("data berhasil di update") 
