n1=int(input('Enter number 1:'))
n2=int(input('Enter number 2:'))
for i in range(n1,n2+1):
    sum=0
    s=list(map(int,list(str(i))))
    for j in s:
        sum=sum+j**3
    if sum==i:
        print(i)
    sum=0
