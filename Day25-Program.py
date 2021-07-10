#Day 25
#1	Write a Python program to convert a string to datetime 
from datetime import datetime
date_object = datetime.strptime('Jul 1 2014 2:43PM', '%b %d %Y %I:%M%p')
print(date_object)

#2 Write a Python program to subtract five days (last working day) from current date
from datetime import date, timedelta
dt = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date :',dt) 

#3 Write a Python program to convert the date to datetime using a function 
import datetime 
      
# using now() to get current time 
current_time = datetime.datetime.now() 
      
# Printing value of now. 
print ("Time now at greenwich meridian is : ", end = "") 
print (current_time) 

#4 	Write a Python program to print next 7 days (week) starting from today
import datetime
base = datetime.datetime.today()
for x in range(0, 5):
      print(base + datetime.timedelta(days=x))