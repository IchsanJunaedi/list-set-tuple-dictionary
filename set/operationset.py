# sets

data_sets = {10,4,3,2,4,5,6,7,5}
print(data_sets)

# add item
data_sets.add(11)
print(data_sets)

#remove item
data_sets.remove(3)
print(data_sets)

# gabungan
set_a = {1,2,3}
set_b = {3,4,5}
print(set_a.union(set_b)) # gabung tanpa duplikat

# intersection
print(set_a.intersection(set_b)) #cari yang sama

# difference
print(set_a.difference(set_b)) # sisa di a yang gaada di b