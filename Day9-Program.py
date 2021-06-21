#Day9
#1 	Write a program to loop through a list of numbers and add +2 to every value to elements in list
numbers= [1,2,3,4,5,6,7,8]
for i in numbers:
    i = i+2
    print(i)


#2 Write a program to get the below pattern
# 54321
# 4321
# 321
# 21
# 1

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()
#same o/p in list
# new_num = [1,2,3,4,5]
# while True:
#     print(new_num[::-1])  
#     new_num.pop()


#3	Python Program to Print the Fibonacci sequence
nterms = int(input("How many terms? "))
n1 = 0
n2 = 1
count = 2
if nterms <= 0:
   print("Plese enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence:")
   print(n1)
else:
   print("Fibonacci sequence:")
   print(n1,",",n2,end=', ')
   while count < nterms:
       nth = n1 + n2
       print(nth,end=' , ')
       # update values
       n1 = n2
       n2 = nth
       count += 1


#4  Explain Armstrong number and write a code with a function
def  getSum (num):
    if num==0:
        return num
    else:
        return pow ((num%10), order) +getSum (num//10)
num =int(input("enter the number:"))
order=len (str (num))
sum=getSum (num)
if sum ==int (num):
    print(num,"is an Armstrong Number.")
else:
    print(num,"is not an Armstrong Number")


#5 Write a program to print the multiplication table of 9
n = int(input("enter the terms for 9 table"))
count =1
while (count != n):
    mul = 9 * count
    count = count +1
    print(mul)


#6 Check if a program is negative or positive
digit = int(input("enter to check pos or negative"))
if (digit > 0):
    print("positive")
else:
    print("negative")


#7	Write a program to convert the number of days to ages
days = int(input())
if (days < 0):
    print("imposiible")
else:
    age = float(days/365)
    print(age,"is ur age")


#8	Solve Trigonometry problem using math function write a program to solve using math function   
import math
a = math.pi/6
print(math.tan(a))
print(math.sin(a))
print(math.cos(a))


#9  Create a calculator only on a code level by using if condition (Basic arithmetic calculation)
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y


print("Select the ooperation\n 1.Addition \n2. Subtraction \n3. Multiplication \n4.Division \n5.Armstrong")

while True:
    choice = input("Enter choice 1/2/3/4")
    if choice in ('1','2','3','4'):
        num1 = float(input("enter the value1"))
        num2 = float(input("enter the value2"))

        if choice == '1':
            print(num1, "+" ,num2, "=" , add(num1, num2))

        elif choice == '2':
            print(num1, "-" ,num2, "=" , sub(num1, num2))

        elif choice == '3':
            print(num1, "*" ,num2, "=" , mul(num1, num2))

        elif choice == '4':
            print(num1, "/" ,num2, "=" , div(num1, num2))

        break
    
    else:
        print("Invalid Input")