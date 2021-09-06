# call by reference
def add_more(list):
    list.append(50)
    print("Inside Function", list)
mylist = [10,20,30,40]
add_more(mylist)
print("Outside Function:", mylist)

# call by value
string = "Pavan"
def test(string):	
	string = "PAvanGabani"
	print("Inside Function:", string)	
test(string)
print("Outside Function:", string)
