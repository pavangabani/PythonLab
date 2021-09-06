s=str(input())

t=s.lower()
print('lowercase :',t)

t1=t.split(' ')
print('Split :',t1)

t2=''.join(t1)
print('join :',t2)

t3=t2.find('gabani')
print('Find :',t3)

t4=t2.replace('gabani','donda')
print('Replace :',t4)

