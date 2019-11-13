Latihan Tipe data
#Boolean
myvar=True          # Tipe data boolean
print(myvar)        # Cetak Data
True

#Complex
myvar =2+4j
print(myvar)
(2+4j)

#Long
myvar=888888888
print(myvar)
888888888

#None
myvar =None
print(myvar)
None

Latihan tipe data (Lanjutan 1)
#Hexadecimal
myvar=0xbb
print(myvar)
187

#Float
myvar= 20.43
print(myvar)
20.43

#integer
myvar =33
print(myvar+8)
41

#String
myvar ="ini string"
print(myvar)
ini string
print(myvar[0])
print(myvar[1])
n
print(myvar[-1])
g
print(myvar[1:])
ni string
print(myvar[:1])
i

Latihan tipe data (Lanjutan 2)

#List
myvar=[100, 200, 300, 400] # numerik
print(myvar)
[100, 200, 300, 400]
print(myvar[0])
100
print(myvar[1])
200
print(myvar[3])
400

myvar=["satu","dua","tiga","empat"] #string
print(myvar)
['satu', 'dua', 'tiga', 'empat']
print(myvar[0])
satu
print(myvar[1])
dua
print(myvar[3])
empat

myvar=[1, "dua", 3, "empat"] # numerik dan string
print(myvar)
[1, 'dua', 3, 'empat']
print(myvar[0])
1
print(myvar[1])
dua
print(myvar[3])
empat

Code 4.1 – Numerik (interger, fload)

# Simpan dengan nama : code41.py
# Pemrograman Game Praktikum 4
# latihan code 4.1 : Numerik (integer dan float) # buat variabel dan beri nilai
a = 4
b = 5
c = 6.3
# cetak variabel ke layar
print(a)
4
print(b)
5
print(c)
6.3
# cetak '*' sebanyak 50 kali
print('*'*50)
**************************************************
# cetak variabel dengan keterangan ke layar print("Variable A :", a )
print("Variable B : %d " % b )
Variable B : 5
print("Variable C : %f " % c )
Variable C : 6.300000
print('*'*50)
**************************************************
# cetak variabel dengan keterangan ke laya
# operasi + , * , / dan cetak ke layar
print("Variable A+B : ", a+b )
Variable A+B :  9
print("Variable A*B : ", a*b )
Variable A*B :  20
print("Variable C/3 : ", c/3 )
Variable C/3 :  2.1

Code 4.2 – String 
# Simpan dengan nama file : code42.py
# Pemrograman Game Praktikum 4
# latihan code 4.2 : string
myvar="Informatika UMMU"
print(myvar)
Informatika UMMU
# cetak colom 0 (pertama) dari variabel myvar
print(myvar[0])
I
# cetak colom 0 dengan keterangan
print("myvar  [0] : ", myvar[0])
myvar  [0] :  I
# cetak colom awal sampai colom ke 4
print(myvar[:3])
Inf
# cetak colom awal sampai colom ke 4 dengan keterangan print("myvar  [:3] : ", myvar[:3])
# cetak semua kecuali colom 0 (pertama)
print(myvar[1:])
nformatika UMMU
# cetak semua kecuali colom 0 (pertama) dengan keterangan print("myvar  [1:] : ", myvar[1:])
# cetak semua kecuali colom terakhir
print(myvar[:-1])
Informatika UMM
# cetak semua kecuali colom terakhir dengan keterangan print("myvar  [:-1] : ", myvar[:-1])

Code 4.3 – String (lanjutan)
# Simpan dengan nama : code43.py
# Pemrograman Game Praktikum 4
# latihan code 4.3 : string
# Buat variabel dan memberikan nilai
prodi = "Teknik Informatika"
konsen = "Jaringan"
mata_kuliah = "Pemrograman Game"
kampus = "UMMU"
lokasi = "Ternate"
tahun = 2019
# Menampilkan nilai variabel ke layar
print(prodi)
Teknik Informatika
print(konsen)
Jaringan
print(mata_kuliah)
Pemrograman Game
print(kampus)
UMMU
print(lokasi)
Ternate
# Cetak '-' sebanyak 40 kali
print( '*' * 40 )
****************************************
# Cetak nilai variabel ke layar dengan keterangan
print("Prodi : ", prodi)
Prodi :  Teknik Informatika
>>> print("Konsentrasi : ", konsen)
Konsentrasi :  Jaringan
print("Mata Kuliah : ", mata_kuliah)
Mata Kuliah :  Pemrograman Game
print("Kampus : %s " % kampus)
Kampus : UMMU
print("Lokasi : %s " % lokasi)
Lokasi : Ternate
print("Tahun  : %d " % tahun)
Tahun  : 2019
# Cetak '-' sebanyak 40 kali
... print( '*' * 40 )
****************************************
# Cetak variabel prodi dan kampus
print("Prodi & Kampus : ", prodi, ",", kampus)        # cara 1
Prodi & Kampus :  Teknik Informatika , UMMU
print("Prodi dan Kampus : ", prodi + ", " + kampus)   # cara 2
Prodi dan Kampus :  Teknik Informatika, UMMU
print("Prodi dan Kampus :  %s, %s " % (prodi, kampus))# cara 3
Prodi dan Kampus :  Teknik Informatika, UMMU

Code 4.4 – List
# Simpan dengan nama : code44.py
# Pemrograman Game Praktikum 4
# latihan code 4.4 : List
# Buat variabel dan memberikan elemen
buah=["Durian","Mangga","Rambutan","Anggur","Pepaya"]
 # cetak list buah
print(buah)
['Durian', 'Mangga', 'Rambutan', 'Anggur', 'Pepaya']
# cetak elemen pertama list (elemen pertama adalah 0) print("Buah [0] ", buah[0])
# cetak elemen kedua list (elemen kedua adalah 1)
print("Buah [1] ", buah[1])
Buah [1]  Mangga
# cetak elemen ketiga list sampai akhir elemen
print("Buah [2:] ", buah[2:])
Buah [2:]  ['Rambutan', 'Anggur', 'Pepaya']
# cetak elemen terakhir list ( [-1] adalah elemen terakhir) print("Buah [-1] ", buah[-1])
Print("*"*35)
Traceback (most recent call last):
File "<stdin>", line 2, in <module>
NameError: name 'Print' is not defined
# Silahkan Simpan dulu lalu Jalankan script anda,
# Lanjutkan setelah melihat hasil
# Buat variabel list mylist dan memberikan elemen
mylist=["Ternate", 1000, 2000, "Tidore", "Maitara", 3000] # cetak list mylist
print("mylist : ", mylist)
mylist :  ['Ternate', 1000, 2000, 'Tidore', 'Maitara', 3000]
# cetak list elemen pertama sampai elemen ke 3
print("mylist [:3] : ", mylist[:3])
mylist [:3] :  ['Ternate', 1000, 2000]
# cetak list elemen ke 2 dan ke 3
print("mylist[1] : ", mylist[1])
mylist[1] :  1000
print("mylist[2] : ", mylist[2])
mylist[2] :  2000
# operasi antar elemen list : elemen ke 2 + elemen ke 3
print("mylist[1] + mylist[2] : ", mylist[1] + mylist[2])
mylist[1] + mylist[2] :  3000

Code 4.5 – List (lanjutan – Tambah dan Hapus elemen list)
# Simpan dengan nama : code45.py
# Pemrograman Game Praktikum 4
# latihan code 4.5 : List
# Buat variabel dan memberikan elemen
buah=["Durian","Mangga","Rambutan"]
# cetak list buah
print(buah)
['Durian', 'Mangga', 'Rambutan']
print("Sebelum ditambah :", buah)
Sebelum ditambah : ['Durian', 'Mangga', 'Rambutan']
# tambah elemen ke dalam list buah di bagian akhir buah.append("Anggur")
print("Setelah ditambah :", buah)
Setelah ditambah : ['Durian', 'Mangga', 'Rambutan']
# tambah elemen ke list sesuai posisi (0 adalah diawal) buah.insert(0, "Pepaya")
print("Setelah ditambah :", buah)
Setelah ditambah : ['Durian', 'Mangga', 'Rambutan']
# hapus elemen list yang ke 1 (1 adalah bagian ke 2) buah.remove(buah[1])
print("Setelah dihapus [1] :", buah)
Setelah dihapus [1] : ['Durian', 'Mangga', 'Rambutan']
# hapus elemen list yang bernilai "Anggur"
buah.remove("Anggur")
Traceback (most recent call last):
File "<stdin>", line 2, in <module>
ValueError: list.remove(x): x not in list
print("Setelah dihapus (Anggur) : ", buah)
Setelah dihapus (Anggur) :  ['Durian', 'Mangga', 'Rambutan']





