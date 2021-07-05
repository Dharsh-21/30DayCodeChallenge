#Day21
#1 Write a program using zip() function and list() function,
#  create a merged list of tuples from the two lists given.
list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]
list(zip(list_a, list_b))
[(1, 5), (2, 6), (3, 7), (4, 8)]

#2 First create a range from 1 to 8. Then using zip, 
# merge the given list and the range together to create a new list of tuples.
lst1=["Energy", "Agriculture", "Industry", "Technology", "Finance", "Forestry", "Transport"]
rng1=(1,8)
lst=zip(lst1,rng1)
print(lst)

#3 Using sorted() function, sort the list in ascending order.
a = (1, 11, 2)
x = sorted(a)
print(x)

#4 Write a program using filter function, 
# filter the even numbers so that only odd numbers are passed to the new list.
numbers = [1,2,6,7,13,14,12,17,16,53,67,34,75,48]
def odd_numbers(num):
    if(num%2 != 0):
        return True
    else:
        return False

oddNums = filter(odd_numbers, numbers)
print('odd Numbers are:')
new_list =[]
for num in oddNums:
    new_list.append(num)
print(new_list)