import datetime

#multikey

mahasiswa1 = {
    'nama' : 'Ican Surican',
    'nim' : '2901022',
    'sks_lulus' :130,
    'beasiswa' : False,
    'lahir' :datetime.datetime(2004,4,15)
}

mahasiswa2 = {
    'nama' : 'otong surotong',
    'nim' : '2901032',
    'sks_lulus' :140,
    'beasiswa' : True,
    'lahir' :datetime.datetime(2002,10,10)
}

mahasiswa3 = {
    'nama' : 'Asep Kasyep',
    'nim' : '2901222',
    'sks_lulus' :100,
    'beasiswa' : False,
    'lahir' :datetime.datetime(2000,2,25)
}

data_mahasiswa = {
    'MAH001':mahasiswa1,
    'MAH002':mahasiswa2,
    'MAH003':mahasiswa3 
}

print(f"{'KEY':<6} {'Nama':<17} {'SKS':<5} {'Beasiswa':<9} {'Lahir':<10}")
print("-"*50)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

    print(f"{KEY:<6} {NAMA:<17} {SKS:<5} {BEASISWA:^9} {LAHIR:<10}")