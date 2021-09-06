#Python program to access a function inside a function.
def first_function(a):
    print('first function')
    print(a)

def second_function(a):
    print('second function')
    first_function(a)

print(second_function('Pavan'))
