## List 

# kumpulan data numbers
data_angka = [1,2,3]
print(data_angka)

# kumpulan data string 
data_string = ["ican,","cans", "jeje"]
print(data_string)

# kumpulan data boolean
data_boolean = [True, False, True, True]
print(data_boolean)

# kumpulan campuran
data_campuran = [1,"mobil",2,"motor","ican",True,"ocep",False]
print(data_campuran)

## cara alternatif membuat list
data_range = range(0,10,2) #range (start,stop,step)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comprehension
list_pake_for = [i for i in range(0,10)] ## kalo pengen kuadrat pake **2
print(list_pake_for)

# membuat list pake for pake if
list_pake_for_if = [i for i in range(0,10) if i != 5]
print(list_pake_for_if) 

list_pake_for_if = [i for i in range(0,10) if i%2 ==0]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i%2 !=0]
print(list_pake_for_if) 