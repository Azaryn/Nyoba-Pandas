import pandas as pd
import numpy as np

np.random.seed(0)
nilai_acak = list(np.random.randint(70, 91, size = 10)) #Menghasilkan 10 nilai acak antara 70 hingga 90 dan disimpan ke dalam list

status = [] #Menentukan status nilai dan disimpan ke dalam list
for nilai in nilai_acak:
    if nilai >= 75:
        status.append('Sangat memuaskan')
    else:
        status.append('Cukup')

data = {
    'nim': [f'NIM{i+1}' for i in range(10)], #perulangan membuat NIM1 hingga 10
    'nilai': nilai_acak,
    'status_nilai': status
} #membuat dataframe dari lsit

df = pd.DataFrame(data)

df_urut = df.sort_values(by='nilai', ascending=False) #Mengurutkan dataframe berdasarkan kolom nilai yang terbesar

print(df_urut)