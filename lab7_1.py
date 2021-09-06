#find number of vowel in string
s=input('Enter String :')
v={'a':0,'i':0,'e':0,'o':0,'u':0}
s.lower();
for i in s:
    if i in v.keys():
        v[i]+=1
print(v)


