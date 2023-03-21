"""
By Siddhesh

"""

x = int(input("Enter value of x"))  # 1
y = int(input("Enter value of y"))  # 1
z = int(input("Enter value of z"))  # 1
n = int(input("Enter value of n"))  # 2

final_list_comp = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c !=n]

print(final_list_comp)
