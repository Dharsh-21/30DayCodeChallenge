#Day14

#1 List down all the error types and check all the errors using a python program for all errors
# KeyboardInterrupt : when an unrequired key is pressed by the user
name=input('enter your name')
# ValueError : when built-in function receives a wrong argument
int('xyz')
# The IndexError is thrown when trying to access an item at an invalid index.
L1=[1,2,3]
L1[3]
# ImportError : if it is unable to find the module
from math import cube
# ModuleNotFoundError
import notamodule


#2	Design a simple calculator app with try and except for all use cases
def calculator():
    '''
    This is our main function which entails the flow of our calculator program
    '''

    validMenuOptions = ["+", "-", "*", "/", "e"]
    while True:
        displayMenu()

        menuSelection = input("Enter your Option: ")

        # Handling user's menu input
        if menuSelection not in validMenuOptions:
            print("[-] Error: Invalid Input!")
        elif menuSelection == "e":
            print("[+] Program Terminated!")
            break
        else:
            # Asking user to enter numbers
            try:
                firstNumber = float(input("Enter 1st Number: "))
                secondNumber = float(input("Enter 2nd Number: "))

                result = 0

                # Checking each possibility and storing the output in 'result' variable
                if menuSelection == "+":
                    result = firstNumber + secondNumber
                    print("[+] Answer: ", result)
                elif menuSelection == "-":
                    result = firstNumber - secondNumber
                    print("[+] Answer: ", result)
                elif menuSelection == "*":
                    result = firstNumber * secondNumber
                    print("[+] Answer: ", result)
                elif menuSelection == "/":
                    if secondNumber == 0:
                        print("[-] Error: Cannot divide by zero")
                    else:
                        result = firstNumber / secondNumber
                        print("[+] Answer: ", result)
            except:
                print("[-] Error: Invalid Input! Only numerical input is allowed.")



def displayMenu():
    print("----------------------------")
    print("        Menu        ")
    print("Enter (+) for Addition")
    print("Enter (-) for Subtraction")
    print("Enter (*) for Multiplication")
    print("Enter (/) for Division")
    print("Enter (e) to Exit")
    print("----------------------------")


if __name__ == "__main__":
    calculator()


#3 print one message if the try block raises a NameError and another for other errors
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

#4 When try-except scenario is not required?
print("The try -except scenario is not required when there is no need to raise exception / check error within the code")

#5 Try getting an input inside the try catch block
try:
    user_input = input() 
    if not user_input:
        raise ValueError('empty string')
except ValueError as e:
    print(e)