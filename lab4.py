print('')
print('Pattern 1')
for i in range(1,6):
    for j in range(i):
        print('*',end=' ')
    print('')
for i in range(6,0,-1):
    for j in range(i):
        print('*',end=' ')
    print('')

print('')
print('Pattern 2')
t=6
for i in range(1,7):
    for j in range(i):
        print(i-j,end=' ')
    print('')

print('')
print('Pattern 3')
t=1
for i in range(1,5):
    for j in range(5-i):
        print(' ',end=' ')
    for j in range(i):
        print(chr(64+t),end=' ')
        t+=1
    print('')

print('')
print('Pattern 4')
for i in range(1,5):
    for j in range(i):
        print(chr(65+j),end=' ')
    print(' ')

print('')
print('Pattern 5')
t=1
for i in range(1,6):
    for j in range(6-i):
        print(' ',end=' ')
    for j in range(i):
        print(' *',end='  ')
    print(' ')
for i in range(1,5):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(5-i):
        print(' *',end='  ')
    print('')

print('')
print('Pattern 6')
for i in range(6):
    for j in range(5,i,-1):
        print(i+1,end=' ')
    print(' ')