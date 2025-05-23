data_angka = [1,5,1,4,3,2,3,1,4,7,8,9,6,2]

print(f"data angka = \n{data_angka}")

# count data

jumlah_data_4 = data_angka.count(1)
jumlah_data_3 = data_angka.count(3)

print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

# ambil posisi data (index)

data = ["ican", "ekel", "karung"]

print(f"data = {data}")

index_ican = data.index("ican")
index_ekel = data.index("ekel")
print(f"index si ican = {index_ican}")
print(f"index si ekel = {index_ekel}")

# mengurutkan list 
print(f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print(f"data angka sort = \n{data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

# balik listnya
data_angka.reverse()
data.reverse()
print(f"data di reserve = \n{data_angka} \n{data}")

