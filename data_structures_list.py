list_of_fruits = [1,2,3,4,"shubham",True,False]

print(type(list_of_fruits))
print(list_of_fruits)

list_of_names = list()
print(type(list_of_names)) 

"""
which is faster [] or list()
"""

"""
Operations in list
append -
clear -
count
"""

list_of_players = []
list_of_players.append("Virat kohli")

list_of_players.append("Rohit Sharma")
list_of_players.append("Sir Jadeja")
print(list_of_players)

list_of_players.clear()
print(list_of_players)

list_of_nums = [11,2,3,4,4,5,6,7,7,8,7,8,8,10]
list_of_nums_new = [1,2,3,5,6,300,3000,10]
print(list_of_nums.count(8))

l = list_of_nums.extend(list_of_nums_new)
print(dir(list_of_nums_new))