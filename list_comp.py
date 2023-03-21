list_of_items = []  #normal list

for i in range(1,11):

    list_of_items.append(i)

print(list_of_items)

list_comp_new = [i for i in range(1,11)]  #list comprehension

print(list_comp_new)


list_comp_odd = [i for i in range(1,11,2)]  # odd list comp

print(list_comp_odd)