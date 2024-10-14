a = int(input())
b = []
d = []
for i in range(2,a):
    c = 0
    for j in range(2,i):
        if(i%j == 0):
            c = c + 1
    if(c >= 1):
        print(i,"is a not a prime number")
        b.append(i)
    else:
        print(i,"is a prime numbeer")
        d.append(i)  

print(d," are prime numbers",b,"---are not prime numbers----- aknc")
print(d)  
print(a)            