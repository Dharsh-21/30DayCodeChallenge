#day6
#exercise
#1 To merge two Python dictionaries
dict1 = {"hello" : "Hello",
      "How are you?" : "Im fine!",
      "tongue" : "taste",
      "eyes":"to see"}

dict2 = {"web" : "Flask",
          "game": "Pygame",
          "ear":"to hear",
          "leg":"walk"}

print(dict1)
print(dict2)
#items in dict1 are copied to dict3
dict3 = dict1.copy()
#each item in dict 2 are changed to item in dict3
for key,value in dict2.items():
    dict3[key] = value
print(dict3)

#2 to remove a key from a dictionary
#deleting item by specifing the key
dict1.pop('hello')
print(dict1)
#last key will be deleted using del 
del dict2[key]
#deleting the specified key using del
del dict2["game"]
print(dict2)

#3 to map two lists into a dictionary
list1 = ['chemistry','maths','physics']
list2 = ['98','95','91']
#zip - collects both the list 
d4 = zip(list1,list2)
#converting to dictionary
new_dict = dict(d4)
print(new_dict)

#4  Python program to find the length of a set
set1 = {"bean", "bheem", "dora","ninja"}
print(len(set1))

#5  to remove the intersection of a 2nd set from the 1st set
set2 = {"bheem","shinchan","Doremon","dora"}
#difference_update - method that provide diff btw sets
set1.difference_update(set2)
print(set1)
print(set2)
#-=   -method that provide diff btw sets
set1-=set2
print(set1)
print(set2)

