#Day15 - edube.org (registered and few problems are done)
#Day16
#1 Create a lambda function that multiplies argument x with argument y
r = lambda x, y : x * y
print(r(12, 4))

#2 Write a Python program to create Fibonacci series to n using Lambda
from functools import reduce
 
fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
                                range(n-2), [0, 1])
 
print("Fibonacci series upto 2:")
print(fib_series(2))
print("\nFibonacci series upto 5:")
print(fib_series(5))
print("\nFibonacci series upto 6:")
print(fib_series(6))
print("\nFibonacci series upto 9:")
print(fib_series(9))

#3  Write a Python program that multiply each number of given list with a given number 
nums = [2, 4, 6, 9 , 11]
n = 2
print("Original list: ", nums)
print("Given number: ", n)
filtered_numbers=list(map(lambda number:number*n,nums))
print("Result:")
print(' '.join(map(str,filtered_numbers)))

#4 Write a Python program to find numbers divisible by 9 from a list of numbers
nums = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
print("Orginal list:")
print(nums) 
result = list(filter(lambda x: (x % 19 == 0 or x % 13 == 0), nums)) 
print("\nNumbers of the above list divisible by nineteen or thirteen:")
print(result)

#5 	Write a Python program to count the even numbers in a given list of integers 
# Python program to count Even
# and Odd numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93, 1]

even_count, odd_count = 0, 0

# iterating each number in list
for num in list1:
	
	# checking condition
	if num % 2 == 0:
		even_count += 1

	else:
		odd_count += 1
		
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)
