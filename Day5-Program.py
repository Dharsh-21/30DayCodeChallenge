# #Day 5 - – User Inputs, Other Important Datatypes
#Exercise
#1
#creating a list
basket =[1,2,3,4,5]
#appending value to list
print(basket.append(100))
print(basket)
#deletion of last element
basket.pop()
print(basket)
#pop= deletes last element
basket.pop()
print(basket)
#pop= deletes the element in 2nd index
basket.pop(2)
print(basket)
#finding max and min value from the list
big = max(basket)
small = min(basket)
print(big)
print(small)
#del-delets the ele in particular index
del basket[0]
print(basket)

#2 - Create a tuple and print the reverse of the created tuple
new_tuple = ('hello',45,'6',6)
rev_tuple = new_tuple[::-1]
print(rev_tuple)

#3 -Create a tuple and convert tuple into list
new_tuple = ('hello',45,'6',6)
print(list(new_tuple)






