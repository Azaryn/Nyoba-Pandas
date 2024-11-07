import pandas as pd #memanggil library pandas
import random #memanggil library random

print(f"Pemilik Program\nNAMA: Rafi Hadianto Aribowo\nNIM:242410102006\nKELAS:ALGO D")
print(" ")

nilai_acak = [] #list kosong untuk menampung nilai acak
for _ in range(10): #perulangan untuk memanggil angka acak sebanyak 10
    nilai_acak.append(random.randint(70, 91))#memasukkan nilai acak dari 70 hingga 90 ke dalam list

#Menentukan status nilai dan disimpan ke dalam list
status = [] #list kosong untuk menampung status dari nilai
for nilai in nilai_acak: #perulangan untuk setiap nilai acak
    if nilai >= 75: #jika nilai lebih dari sama dengan 75 menambahkan 'Sangat Memuaskan' pada list
        status.append('Sangat memuaskan') 
    else: #jika nilai kurang dari 75 menambahkan 'Cukup' pada list
        status.append('Cukup')

#Data 
data = {} #dict kosong untuk menampung nim, nilai dan status
data['nim'] = [] #menambahkan key ke dalam dict data
for i in range(10): #membuat perulangan dalam range 10
    data['nim'].append(f'2424101020{i+1}') #memasukkan value ke dalam key nim dengan urut index ke i
data['nilai'] = nilai_acak #menambahkan key nilai dan value berupa nilai acak
data['status_nilai'] = status #menambahkan key status nilai dan value berupa status

#membuat dataframe dari list
df = pd.DataFrame(data) #membuat dataframe dari data
print("data frame:")
print(df) #mencetak dataframe
print(" ")

#Mengurutkan dataframe berdasarkan kolom nilai yang terbesar
df_sort = df.sort_values(by='nilai', ascending=False)  #mengurutkan dataframe dari nilai terbesar ke terkecil
print("data frame sorted")
print(df_sort) #mencetak dataframe
