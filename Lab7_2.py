#Python function to multiply all the numbers in a list
def mul(a):
    ans=1
    for i in a:
        ans*=i
    return ans
l=[1,2,3]
print(mul(l))