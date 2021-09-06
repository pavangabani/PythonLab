a=int(input("Enter any number 1 :"))
b=int(input("Enter any number 2 :"))

for i in range(a,b+1):
    t=0
    for j in range(2,i):
        if i%j==0:
            t=1
            break
    if t==0:
        print(i)
