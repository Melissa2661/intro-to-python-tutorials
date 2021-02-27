
a = int(input("Please enter a number: "))
result = 1

if a == 1 or a == 0:
    print(a)
else:
    while(a > 1):
        result *= a
        a-=1

print(result) 


