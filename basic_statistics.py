# -*- coding: utf-8 -*-
"""P02-19921122.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JAgOHzjsdDStzGOaYb5LqW1ltTul6tKl
"""

# Nama      : Salma Sari JUliani
# NIM       : 19921122
# Deskripsi : Praktikum Pengenalan Komputasi 2

"""Soal 1"""

# Membuat array untuk harga barang
harga_barang = [0 for i in range(4)]

harga_barang[0] = int(input('Masukkan harga barang ke-1 :'))
harga_barang[1] = int(input('Masukkan harga barang ke-2 :'))
harga_barang[2] = int(input('Masukkan harga barang ke-3 :'))
harga_barang[3] = int(input('Masukkan harga barang ke-4 :'))

jumlah_barang = [0 for i in range(4)]

jumlah_barang[0] = int(input('Masukkan jumlah barang ke-1 :'))
jumlah_barang[1] = int(input('Masukkan jumlah barang ke-2 :'))
jumlah_barang[2] = int(input('Masukkan jumlah barang ke-3 :'))
jumlah_barang[3] = int(input('Masukkan jumlah barang ke-4 :'))

diskon_barang = [0 for i in range(4)]

diskon_barang[0] = int(input('Masukkan diskon barang ke-1 (dalam persen):'))
diskon_barang[1] = int(input('Masukkan diskon barang ke-2 (dalam Persen):'))
diskon_barang[2] = int(input('Masukkan diskon barang ke-3 (dalam Persen):'))
diskon_barang[3] = int(input('Masukkan diskon barang ke-4 (dalam persen):'))

import numpy as np

# Nilai diskon
diskon_barang_satu = harga_barang[0]*diskon_barang[0]/100
diskon_barang_dua = harga_barang[1]*diskon_barang[1]/100
diskon_barang_tiga = harga_barang[2]*diskon_barang[2]/100
diskon_barang_empat = harga_barang[3]*diskon_barang[3]/100

# Harga jual setelah dikurangi diskon
harga_barang_satu = harga_barang[0]-diskon_barang_satu
harga_barang_dua = harga_barang[1]-diskon_barang_dua
harga_barang_tiga = harga_barang[2]-diskon_barang_tiga
harga_barang_empat = harga_barang[3]-diskon_barang_empat

# Harga jual setelah didiskon dikali jumlah barang

harga_akhir_satu = harga_barang_satu*jumlah_barang[0]
harga_akhir_dua = harga_barang_dua*jumlah_barang[1]
harga_akhir_tiga = harga_barang_tiga*jumlah_barang[2]
harga_akhir_empat = harga_barang_empat*jumlah_barang[3]

print("Tagihan total adalah :", harga_akhir_satu + harga_akhir_dua + harga_akhir_tiga + harga_akhir_empat)

"""Soal 2"""

tarif_per_km = [0 for i in range(1)]

tarif_per_km[0] = int(input('Masukkan tarif per km :'))

jarak_perjalanan = [0 for i in range(4)]

jarak_perjalanan[0] = int(input('Masukkan jarak perjalanan ke-1 (dalam km):'))
jarak_perjalanan[1] = int(input('Masukkan jarak perjalanan ke-2 (dalam km):'))
jarak_perjalanan[2] = int(input('Masukkan jarak perjalanan ke-3 (dalam km):'))
jarak_perjalanan[3] = int(input('Masukkan jarak perjalanan ke-4 (dalam km):'))

diskon_voucher = [0 for i in range(4)]

diskon_voucher[0] = int(input('Masukkan diskon voucher 1 (dalam persen):'))
diskon_voucher[1] = int(input('Masukkan diskon voucher 2 (dalam persen):'))
diskon_voucher[2] = int(input('Masukkan diskon voucher 3 (dalam persen):'))
diskon_voucher[3] = int(input('Masukkan diskon voucher 4 (dalam persen):'))

# Mencari tarif harga yang sudah dikurangi diskon

# Perjalanan 1
potongan_1 = diskon_voucher[0]/100*jarak_perjalanan[0]*tarif_per_km[0]
batas_1 = 1500

if potongan_1 <= batas_1:
  diskon_1=potongan_1
else:
  diskon_1=batas_1

# Karena potongan 1 > 1.500, maka potongan perjalanan 1 adalah 1500
tarif_final_1 = tarif_per_km[0]*jarak_perjalanan[0]-diskon_1


# Perjalanan 2 
potongan_2 = diskon_voucher[1]/100*jarak_perjalanan[1]*tarif_per_km[0]
batas_2 = 4000

if potongan_2 <= batas_2:
  diskon_2=potongan_2
else:
  diskon_2=batas_2

# Karena potongan 2 < 4.000, maka potongan perjalanan 2 adalah potongan_2
tarif_final_2 = int(tarif_per_km[0]*jarak_perjalanan[1]-diskon_2)


# Perjalanan 3
potongan_3 = diskon_voucher[2]/100*jarak_perjalanan[2]*tarif_per_km[0]
batas_3 = 3500

if potongan_3 <= batas_3:
  diskon_3=potongan_3
else:
  diskon_3=batas_3
# Karena potongan 3 > 3.500, maka potongan perjalanan 3 adalah 3500
tarif_final_3 = tarif_per_km[0]*jarak_perjalanan[2]-diskon_3


# Perjalanan 4
potongan_4 = diskon_voucher[3]/100*jarak_perjalanan[3]*tarif_per_km[0]
batas_4 = 5000

if potongan_4 <= batas_4:
  diskon_4=potongan_4
else:
  diskon_4=batas_4
# Karena potongan 4 < 5.000, maka potongan perjalanan 4 adalah potongan_4
tarif_final_4 = tarif_per_km[0]*jarak_perjalanan[3]-diskon_4

# Array tarif final

tarif_final = [0 for i in range(4)]

tarif_final[0] = tarif_final_1
tarif_final[1] = tarif_final_2
tarif_final[2] = tarif_final_3
tarif_final[3] = tarif_final_4

print("Tarif-tarif final adalah:")
print(tarif_final)

# Import data
import numpy as np

# Pendefinisian range
nilai_max = max(tarif_final)
nilai_min = min(tarif_final)
range = nilai_max - nilai_min

# Mencari mean
print("Mean:", np.mean(tarif_final))

# Mencari median
print("Median:", np.median(tarif_final))

# Mencari range
print("Range:", float(range))