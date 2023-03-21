import timeit

print("TUPLE: ",round(timeit.timeit('x=(1,2,3,4,5)', number=1000000),7))
print("LIST: ",round(timeit.timeit('x=[1,2,3,4,5]', number=1000000),7))
