import csv
from prettytable import PrettyTable
# =====================================================================
#  FILE HANDLING (MEMBACA & MENULIS FILE)
# =====================================================================
# Python dapat membaca dan menulis file dalam berbagai mode:
#
# Mode File:
#   "r"  → read (membaca file)
#   "w"  → write (menulis file baru, akan menimpa file lama)
#   "a"  → append (menambah isi file tanpa menghapus)
#   "x"  → create (membuat file baru; error kalau file sudah ada)
#   "r+" → read + write
#
# File dapat berupa:
# - file teks (.txt)
# - file csv
# - file json
#
# Struktur dasar operasi file:
# ---------------------------------------------------------
# 1. Membuka file:
#       f = open("nama.txt", "mode")
# f = open("belajar\\data.txt", "a")
#
# 2. Membaca file:
#       f.read()       → membaca semua isi file
#       f.readline()   → membaca 1 baris
#       f.readlines()  → membaca semua baris menjadi list
# f.write("darurat \n")
#
# 3. Menulis file:
#       f.write("teks")
#
# 4. Menutup file:
#       f.close()
# f.close()
# ---------------------------------------------------------
#
#
# KONTEKS MANAGER "with" (Cara modern)
# ---------------------------------------------------------
# Cara terbaik untuk bekerja dengan file adalah:
#
#   with open("nama.txt", "r") as f:
#       isi = f.read()
#
# Karena otomatis menutup file tanpa perlu f.close()
# try:
#     with open("belajar\\data.txt", "r") as f:
#         isi = f.readlines()
#         jumlah = 0
#         for line in isi:
#             jumlah += int(line)
#         print(jumlah)
# except ValueError:
#     print("File mengandung data non-angka!")
# except FileNotFoundError:
#     print("File tidak ditemukan!")

# r
# w (list lain)

#data.csv
# 1
# 2
# 3

#simpan
# 1
# 2 
# 3

# list lain
# 1
# 4
# 3

# data_lain
# biodatalain

#digabung
# data + biodatalain

#
#
# JENIS HASIL YANG DIBACA:
# - read() menghasilkan string
# - readline() menghasilkan string 1 baris
# - readlines() menghasilkan list berisi baris
#
#
# MENULIS FILE:
# - write() hanya menerima string
# - jika ingin menulis angka → harus dirubah ke string dulu
#
# Contoh:
#   f.write(str(angka))
#
# APPEND (menambah data tanpa menghapus file):
#   with open("data.txt", "a") as f:
#       f.write("baris baru\n")
#
#
# KHUSUS FILE JSON (struktur data):
#   json.dump(data, file)   → simpan dictionary ke file JSON
#   json.load(file)         → baca file JSON menjadi dictionary
#
#
# KHUSUS FILE CSV (tabel data):
#   csv.writer()            → menulis baris
#   csv.reader()            → membaca baris
table = PrettyTable()
table.field_names = ["nama_depan", "nama_belakang", "Umur"]
with open("belajar\\data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        table.add_row([row["nama_depan"], row["nama_belakang"], row["usia"]])
print(table)
#
#
# File handling sangat penting untuk:
# - sistem login sederhana
# - penyimpanan database kecil
# - laporan hasil program
# - CRUD di terminal
#
# =====================================================================
