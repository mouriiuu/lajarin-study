# #umur = 12, 23, 33
# #int

# # ini kelebihan angkanya

# nama = "arum"
# # str

# phi = 3.14
# # float

# i = "a"
# # char
# # HARUSNYA CHAR PAKE TANDA PETIK 1

# laper = True
# # bool

# umur = 12
# if umur >50:
#     print('woy tua')
# elif umur <50 and umur >17:
#     print('dewasa korupsi')
# else:
#     print('aku kecil')
    
#     # lumayan lah

# print('game madlids')
# nama = input('nama : ')
# nama2 = input('nama2: ')
# nama3 = input('nama3: ')
# print('aku hidup dengan', nama)
# print('aku benci dengan', nama2)
# print('aku jalan dengan', nama3)

# walau input yang diminta salah tapi okelah 90 / 100

nama = input('masukkan username: ')
umur = ''
ipk = ''
try:
    umur = int(input('masukkan umur: '))
    ipk = float(input('masukkan ipk: '))
    status = input('apakah mahasiswa aktif (iya/tdk): ')
    if status == 'iya':
        akstif = True
    else:
        akstif = False
    print('===== OUTPUT ====')
    print('username : ', nama ,'| umur : ', umur)
    print('ipk : ', ipk, ', Status : ', akstif)
    print('mahasiswa', nama, 'berstatus aktif: ', akstif)
except ValueError:
    print('input harus angka')
    exit


