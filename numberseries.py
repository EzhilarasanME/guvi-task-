n= int(input("How many terms? "))
a1, a2 = 0, 1
count = 0
print("Fibonacci sequence:")
while count < n:
    print(a1)
    nth = a1 + a2
    a1 = a2
    a2 = nth
    count +
