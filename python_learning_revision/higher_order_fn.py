# writing function as an argument called higher order function
def hello(name):
	return name + '!!'

def who(func, val):
	return func(val)

hi = who(hello,'R')
#print(hi)

## map ##

## using map(function, iterable)
int_lst = range(1,11)
def double(x):
	return x*2

# doubled = map(double, int_lst)
# print(list(doubled))

# another way to write
doubled = map(lambda x: x*2, int_lst)
#print(list(doubled))

# merge and sort list
l1 = [3,5,55,34,33,46]
l2 = [2,4,55,66,77,98,99]
print(sorted((l1+l2)))