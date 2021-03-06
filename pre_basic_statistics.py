# -*- coding: utf-8 -*-
"""TP02-19921122.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WVfvzRLL2u45doXtORXPtWYZvTh1iQCL

Identitas Diri
"""

# Nama      : Salma Sari Juliani
# NIM       : 19921122
# Deskripsi : TP Modul 2 (Pengenalan Python, Array, dan Statistik Dasar)

"""Code"""

# Membuat list kosong untuk menyimpan data tinggi badan masing-masing anak
tinggi_badan = [0 for i in range(15)]

# Pengguna dapat memasukkan data tinggi badan masing-masing anak dalam list
tinggi_badan[0] = int(input('Masukkan tinggi badan anak ke-1 :'))
tinggi_badan[1] = int(input('Masukkan tinggi badan anak ke-2 :'))
tinggi_badan[2] = int(input('Masukkan tinggi badan anak ke-3 :'))
tinggi_badan[3] = int(input('Masukkan tinggi badan anak ke-4 :'))
tinggi_badan[4] = int(input('Masukkan tinggi badan anak ke-5 :'))
tinggi_badan[5] = int(input('Masukkan tinggi badan anak ke-6 :'))
tinggi_badan[6] = int(input('Masukkan tinggi badan anak ke-7 :'))
tinggi_badan[7] = int(input('Masukkan tinggi badan anak ke-8 :'))
tinggi_badan[8] = int(input('Masukkan tinggi badan anak ke-9 :'))
tinggi_badan[9] = int(input('Masukkan tinggi badan anak ke-10 :'))
tinggi_badan[10] = int(input('Masukkan tinggi badan anak ke-11 :'))
tinggi_badan[11] = int(input('Masukkan tinggi badan anak ke-12 :'))
tinggi_badan[12] = int(input('Masukkan tinggi badan anak ke-13 :'))
tinggi_badan[13] = int(input('Masukkan tinggi badan anak ke-14 :'))
tinggi_badan[14] = int(input('Masukkan tinggi badan anak ke-15 :'))

# Mendefinisikan nilai maksimum dan nilai minimum dari list data
nilai_maksimum = max(tinggi_badan)
nilai_minimum = min(tinggi_badan)
range = nilai_maksimum - nilai_minimum

# Import data
import numpy as np

# Output statistik dasar dari data di dalam list
print('Rata-Rata : ', np.mean(tinggi_badan))
print('Standar Deviasi : ', np.std(tinggi_badan, ddof=1))
print('Range : ', range)
print('Kuartil Bawah : ', np.quantile(tinggi_badan, q=0.25))
print('Kuartil Tengah : ', np.quantile(tinggi_badan, q=0.50))
print('Kuartil Atas : ', np.quantile(tinggi_badan, q=0.75))

#Selesai