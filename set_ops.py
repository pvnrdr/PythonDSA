dict_1= {}
print(type(dict_1))

set_1 = set() #empty

set_of_cars = {"audi","bmw","volvo"}
another_set_of_cars = {"mahindra","maruti","tata","bmw"}

print(set_of_cars)

set_of_cars.add("skoda")

print(set_of_cars)

set_of_cars.remove("audi")
print(set_of_cars)

union_set_3 = set_of_cars.union(another_set_of_cars)
print(union_set_3)

intersection_set_4 = set_of_cars.intersection(another_set_of_cars)
print(intersection_set_4)

print(set_of_cars.difference(another_set_of_cars))

a = {1,2,3,4,5} # superset
b = {2,5} #subset

print(b.difference(a))

print(b.issubset(a))
print(a.issuperset(b))