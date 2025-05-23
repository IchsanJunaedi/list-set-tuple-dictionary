# operator dictionary

data_dict = {
    'cans' : 'ican surican',
    'tg' : 'otong surotong',
    'dg' : 'dudung surudung'
}

# panjang dictionary
lendict = len(data_dict)
print(f"panjang dictionary : {lendict}")

# mengecek key exist atau tidak
key = 'cans'
checkkey = key in data_dict
print(f"apakah {key} ada di data_dict: {checkkey}")

# mengakses value (read) dengan get
print(data_dict["cans"])
print(data_dict.get("cans"))
print(data_dict.get("cas", "cas tidak ditemukan")) # cek key dengan message tidak ditemukan

# mengupdate data
data_dict["cans"] = "ican si ganteng"
print(data_dict)
data_dict["rung"] = "karung si god"
print(data_dict)

data_dict.update({"cans":"ican surican"})
print(data_dict)
data_dict.update({"no":"sandiaga uno"})
print(data_dict)

# mendelete data pada dictionary
del data_dict["no"]
print(data_dict)