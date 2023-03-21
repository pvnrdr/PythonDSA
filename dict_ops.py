d1 = {}   #dict init empty

d2 = dict()  #create empty dict

my_dict = {
    "name":"shubham",
    "role":"developer",
    "city":"pune"
}

print(my_dict['name']) # method 1

print(my_dict.get('role')) #method 2


my_dict['salary'] = 2000
my_dict['name'] = "Shubham Londhe"
print(my_dict)

my_dict.update({"hobby":"teaching"})
print(my_dict)


# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())

# iteration

for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)

for key,value in my_dict.items():
    print(key,value)
