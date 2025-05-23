# copy dictionary

teman_teman = {
    "cans" : "ican surican",
    "tong" : "otong surotong",
    "dung" : "dudung surudung",
    "sep"  : "asep si kasyep", 
    "cuy"  : "ucuy surucuy"
}

friends = teman_teman.copy()

print(f"teman-teman: {teman_teman}\n")
print(f"teman-teman:{friends}\n")

teman_teman["cans"]="ican si kweren"
print(f"teman-teman: {teman_teman}\n")
print(f"teman-teman:{friends}\n")

# pop dictionary (berdasarkan key)
dataAsep = friends.pop("sep")
print(f"data asep = {dataAsep}\n")
print(f"friends = {friends}\n")

# popitem dictionary (yang terakhir ajah)
dataTerakhir = friends.popitem()
print(f"data terakhir = {dataTerakhir}\n")
print(f"friends = {friends}\n")

