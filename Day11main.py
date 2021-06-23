#Day11

#1 Create a python module with list and import the module in another .py file(Day11hello.py) and change the value in list
import Day11hello 
Day11hello.my_function(9)

#2 Install pandas package (try to import the package in a python file
import pandas as pd
import numpy as np
df = pd.DataFrame({
    "State": ['Andhra Pradesh', 'Maharashtra', 'Karnataka', 'Kerala', 'Tamil Nadu'],
    "Capital": ['Hyderabad', 'Mumbai', 'Bengaluru', 'Trivandrum', 'Chennai'],
    "Literacy %": [89, 77, 82, 97,85],
    "Avg High Temp(c)": [33, 30, 29, 31, 32 ]
})
print(df)

#3 Import a module that picks random number and write a program to fetch a random number from 1 to  100 on every run
#method1
import random
print (random.randint(0, 100))
#method2
import random
print(random.random() * 100)

#4 Import sys package and find the python path
import sys
print(sys.path)

#5 here,package-name = itsdangerous 
# pip install <package-name>
# pip uninstall <package-name>
