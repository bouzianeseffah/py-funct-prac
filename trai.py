#max number
def max_num(a, b, c):
    if(a > b ) and (a > c):
        max = a
    elif(b > a ) and (b > c):
        max = b  
    else:
        max = c
    return max     
a = 14
b = 16 
c = 4  


print(max_num(a, b, c))  


# multiply all the numbers in a list 
def mult_list(mylist):
    result = 1
    for num in mylist:
        result = result * num
    return result


list1 = [3, 3, 3]
list2 = [3, 4, 6]        
print(mult_list(list1))
print(mult_list(list2))


#reverse a string
def rev_string(myStr):
    return myStr[::-1]
print(rev_string("hello"))
print(rev_string("this is my life"))    

#number falls in given range
def num_within(x,a,b):
  return x in range(a,b+1)
     
print(num_within(7,3,5))     
print(num_within(3,1,3))     
print(num_within(5,2,5))
#pascal's triangle

# Print Pascal's Triangle in Python
from math import factorial

# input n
n = 5
print(range(n))
for i in range(n):
	for j in range(n-i+1):

		# for left spacing
		print(end=" ")

	for j in range(i+1):

		# nCr = n!/((n-r)!*r!)
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

	# for new line
	print()
