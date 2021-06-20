#Day8
#1 Write a Python script to merge two Python dictionaries

choco = {"milkybar":"white",
          "Diarymilk":"brown",
          "fruitplus":"purple",
           "katchamango":"green"}

cartoon = {"bheem":"raju",
            "shinchan":"kasama",
            "dora" : "buji",
             "dharshini" : "jayavarshini"}
sample_dict = choco.copy()
for key,value in cartoon.items():
    sample_dict[key] = value
print(sample_dict)

#2  Write a program to sort the value from descending to ascending in list and convert it in to a set.
height = [90,87,45,32,21,16,10,3,1]
print(height[::-1])
convert_set = set(height)
print(convert_set)

#3 Write a Python program to list number of items in a dictionary key and sort the list with the help of a function & without the function.
count = 0
for i in sample_dict.items():
    count = count +1
print(count)
print (sorted(sample_dict.keys()))
res = {key: val for key, val in sorted(sample_dict.items(), key = lambda ele: ele[1])}
print("Result dictionary sorted by values : " + str(res)) 

#4Write a Python program to get a string from a given string (user input) and change the first occurrence of the word to a user specified input
a=input("Enter the string :")
b=input("Enter the substring :")
c=input("String to be replaced :")
d=a.split()
for i in range(len(d)):
    if(d[i]==b):
        d[i]=c
        break
str=""
for i in d:
    str+=i
    str+=" "
print("After replacing : ",str)


#5 Write a Python program to get a string from a given string where all occurrences of its first char have been changed to capital letter
x=input("Enter the string: ")
y=x[0]
z=y.upper()
d=x.replace(y,z)
print("After replacing the first charcter:",d)


#6 Write a Python program to find the repeated items of a list
list=[1,4,5,1,9,5,4]
list1=[]
list2=[]
for i in list:
    if(i not in list1):
        list1.append(i)
    else:
        list2.append(i)
print("Repeated items :",list2)


#7 Write a Python program to check the sum of three elements and divided by a value which is given as an input by the user
a=2
b=0
c=9
sum=a+b+c
m=int(input("Enter number to be divide"))
print("The sum afters dividing  : ",sum/m)

#8 Write a Python program to find the Mean,median,mode among three given numbers
import statistics
a=10
b=20
c=30
mean=(a+b+c)/3
l=[a,b,c]
print("Mean  :",mean)
print("Median:  ",statistics.median(l))
print("Mode : ",statistics.mode(l))

#9 Write a Python program to swap cases of a given string
def swap(str1):
   str = ""   
   for i in str1:
       if i.isupper():
           str += i.lower()
       else:
           str += i.upper()           
   return str
print(swap("Hello"))
print(swap("PEOPLE"))	

#10 write a program to convert an integer to binary & octa decimal

x= int(input("enter the number"))
print(bin(x))
print(oct(x))