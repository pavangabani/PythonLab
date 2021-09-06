a=int(input("Enter any number 1 :"))
b=int(input("Enter any number 2 :"))
c=int(input("Enter any number 3 :"))
if a>b and a>c:
    print("largest number is :",a)
elif b>c:
    print("largest number is :",b)
else:
    print("largest number is :",c)