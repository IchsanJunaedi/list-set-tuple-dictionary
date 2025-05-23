## operasi

# index  0(-3)       1(-2)          2 (-1)
data = ["ican", "asep", "jungkirk"]

# mengambil data dari list ini
data_0 = data[0]
print(f"data pertama(index 0) = {data_0}")

data_last = data[-1]
print(f"data terakhir adalah = {data_last}")

data_ican = data[-3]
print(f"data ican = {data_ican}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

## manipulasi data list

# menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")

data.insert(1,"rocky")
print(f"data sesudah ditambah = \n{data}")

# menambahkan di akhir list
data.append("janksi")
print(f"data ditambah lagi =\n{data}")

# menambahkan list dengan list
data_baru = ["sen", "riki" , "ekel"]
data.extend(data_baru)
print(f"data gabungan =\n{data}")

# merubah data
#kita ubah data ke 2 menjadi oding
data[2] = "oding"
print(f"data rubah = {data}")

# meremove data

data.remove("rocky")
print(f"data remove = \n{data}")
# data.remove ("ricky") akan error karena hurufnya salah 

# meremove data paling belakang
data_akhir = data.pop()
print(f"data akhir = {data}")

print(data_akhir)