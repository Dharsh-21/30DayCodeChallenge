#DAY 2 : STRING

#How to print a value
print("hello,hope you are good!")
print('hopeyou are good')

# Assigning String to Variable
Hours= "thirty"
print(Hours)

#Indexing using String:
Days = "Thirty days"
print(Days[0])
print(Days[6])
print(Days[8])

#How to print the particular character from certain text
Challenge = "I will win"
print(Challenge[8:10])

#Print the length of Character:
Challenge = "I will win"
print(len(Challenge))

#Convert String into lower character
Challenge = "I will win"
print(Challenge.lower())

#string Concatenation – Joining two strings
a = "30 Days"
b = "30 hours"
c = a + b
print(c)

#Adding space during concatenation 
a = "30 Days"
b = "30 hours"
c = a + " " + b
print(c)

#casefold() - Usage
text = "Thirty days and Thirty hours"
x = text.casefold()
print(x)



#Assignment - Replace casefold with above values and execute it
#1 capitalize() - Capitalize every first letter of a sentence
text = "Thirty days and Thirty hours"
x = text.capitalize()
print(x)

#2 find() - returns index number f the letter is present in the string
text = "Thirty days and Thirty hours"
#here, 'e' is not present so returns -1
x = text.find('e')
print(x)
#here, 'y' is present in 5th position
x = text.find('y')
print(x)

#3 isalpha() - If all the characters in the string are alphabets, it returns True.No numbers, No special chanracter
#here, we have space bw words so, o/p is False
text = "Thirty days and Thirty hours"
x = text.isalpha()
print(x)

#4 isalnum() - Returns True if alphabet+numbers are present.No special character or space
# here, the string doesnot have numbers and there is space
text = "Thirty days and thirty hours"
x = text.isalnum()
print(x)
#here, we have no space but have num+alphabet
check = "Thirtydaysand30hours"
x = check.isalnum()
print(x)