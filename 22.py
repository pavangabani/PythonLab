def multiply(m1, m2, mat1,
             n1, n2, mat2):
 
    res = [[0 for x in range(n2)]
              for y in range (m1)]
     
    for i in range(m1):
        for j in range(n2):
            res[i][j] = 0
            for x in range(m2):           
                res[i][j] += (mat1[ i][x] *
                              mat2[ x][j])
            
    for i in range(m1):
        for j in range(n2):     
            print (res[i][j],
                   end = " ")       
        print ()

n1=int(input('Enter number n:'))
m1=int(input('Enter number m:'))
matrix=[[0 for i in range(m1)] for j in range(n1)]
for i in range(n1):
    for j in range(m1):
        matrix[i][j]=int(input('Enter Number'))
n2=int(input('Enter number n:'))
m2=int(input('Enter number m:'))
matrix2=[[0 for i in range(m2)] for j in range(n2)]
for i in range(n2):
    for j in range(m2):
        matrix2[i][j]=int(input('Enter Number'))
print(matrix,matrix2)
multiply(n1, m1, matrix,n2, m2, matrix2)

