#Day7
#1.	Create a function getting two integer inputs from user & print the following:
#Addition of two numbers is +value
#Subtraction of two numbers is +value
#Division of two numbers is +value
#Multiplication of two numbers is +value

def cal(value1,value2):
   add = value1+value2
   print(add)
   sub = value1-value2
   print(sub)
   mul = value1*value2
   print(mul) 
   div = value1/value2
   return (div)

#fun call
final = cal(4,5)
print(final)

#Create a function covid( ) & it should accept patient name, and body temperature, by default the body temperature should be 98 degree
#to call fun that checks the patient 
def covid(name, tem):
    if(tem >98):
        print("Covid patient:" +name)
    

#to get names and temp
i = 10 
for x in range (0,i):
    nam =input()
    temp = float(input()) 
    patient = covid(nam,temp)

