# ============================================
# PENGENALAN FUNCTION DI PYTHON
# ============================================

# Function adalah blok kode yang hanya akan dijalankan saat dipanggil.
# Tujuan function:
# - Menghindari penulisan kode berulang
# - Membuat program lebih rapi dan terstruktur
# - Bisa menerima input (parameter)
# - Bisa mengembalikan output (return)



# ------------------------------------------------
# 1. Function Sederhana
# ------------------------------------------------
def salam():
    # Fungsi ini tidak menerima parameter
    # dan hanya menampilkan teks ke layar
    print("Halo, ini function sederhana!")


# ------------------------------------------------
# 2. Function dengan Parameter
# ------------------------------------------------
def sapa(nama):
    # Fungsi ini menerima 1 parameter 'nama'
    # sehingga output dapat menyesuaikan input
    print(f"Halo {nama}, selamat datang!")


# sapa("zidan")
# sapa("pirlo")
# sapa("yoga")

# ------------------------------------------------
# 3. Function dengan Return Value
# ------------------------------------------------
def tambah(a, b):
    # Fungsi ini menerima dua nilai (a dan b)
    # kemudian mengembalikan hasil penjumlahan
    return a + b


# ------------------------------------------------
# 4. Function dengan Nilai Default Parameter
# ------------------------------------------------
def cetak_kelas(nama, kelas="X RPL 1"):
    # Jika parameter 'kelas' tidak diberikan,
    # maka otomatis menggunakan nilai default
    print(f"{nama} dari kelas {kelas}")


# ------------------------------------------------
# 5. Function dengan Multiple Return Value
# ------------------------------------------------
def operasi(a, b):
    # Fungsi ini mengembalikan dua nilai sekaligus,
    # yaitu hasil tambah dan hasil kali
    return a + b, a * b


# ------------------------------------------------
# 6. Function dengan *args
# ------------------------------------------------
def total(*angka):
    # *args digunakan untuk menerima jumlah parameter tidak terbatas
    # Parameternya otomatis berbentuk tuple
    return sum(angka)


# ------------------------------------------------
# 7. Function dengan **kwargs
# ------------------------------------------------
def biodata(**data):
    # **kwargs menerima banyak data dalam bentuk key=value
    # Parameternya menjadi dictionary
    for key, value in data.items():
        print(f"{key} : {value}")


# =================================================
# PEMANGGILAN FUNCTION (CONTOH)
# =================================================

# if __name__ == "__main__":
#     salam()
#     sapa("Budi")
#     print("Hasil tambah:", tambah(5, 3))
#     cetak_kelas("Ani")
#     print("Hasil operasi:", operasi(4, 2))
#     print("Total semua angka:", total(1, 2, 3, 4, 5))

#     biodata(
#         nama="Rahmat",
#         umur=17,
#         kelas="XI TKJ"
#     )
