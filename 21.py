n=int(input('Enter number n:'))
matrix=[[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        matrix[i][j]=int(input('Enter Number'))
tmatrix=[[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        tmatrix[i][j]=matrix[j][i]
for i in range(n):
    for j in range(n):
        print(tmatrix[i][j],end=' ')
    print('')


        