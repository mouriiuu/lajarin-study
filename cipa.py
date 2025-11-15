# tipe data integer
# umur = 18

# ini betul

# umur = 20              # int

# tinggi_badan = 165.5   # float

# sudah_makan = True     # bool

# nama = "Cipa"          # str

# inisial = 'C'          # char

# ini BETUL!

# umur = 50
# if umur > 50:
#     print("TUA WOY")
# elif 17 < umur <= 50:
#     print("dewasa tapi korupsi")
# else:
#     print("aku kecil dan aku masih bahagia")
    
# ini betul

print ("game madlibs")
text1 = input("text pertama: ")
text2 = input("text kedua: ")
text3 = input("text ketiga: ")
print("aku hidup dengan", text1)
print("aku jalan dengan", text2)
print("aku benci dengan", text3)

# mantab 100/100

print("DATA MAHASISWA")
username = input("masukkan username: ")
try:
    umur = int(input("masukkan umur: "))
    ipk = float(input("masukkan IPK: "))
except ValueError:
    print("ERROR: umur & IPK harus angka!")
    exit()
status_input = input("apakah mahasiswa aktif? (ya/tidak): ")
if status_input == "ya" :
    status = True
else:
    False
print("\n=== OUTPUT ===")
print(f"username: {username} | umur: {umur}")
print(f"IPK: {ipk}, status: {status}")
print(f"mahasiswa {username} berstatus aktif: {status}")
