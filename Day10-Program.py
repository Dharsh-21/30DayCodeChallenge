#Day10
#single inheritance
class Parent:
     def func1(self):
          print("this is example one")
class Child(Parent):
     def func2(self):
          print(" this is example 2 ")
ob = Child()
ob.func1()
ob.func2()

# #multiple inheritance
class Parent:
   def func1(self):
        print("this is example 1")
class Parent2:
   def func2(self):
        print("this is example 2")
class Child(Parent , Parent2):
    def func3(self):
        print("this is example 3")
 
ob = Child()
ob.func1()
ob.func2()
ob.func3()

# #multilevel inheritance
class Parent:
      def func1(self):
          print("this is example 1")
class Child(Parent):
      def func2(self):
          print("this is example 2")
class Child2(Child):
      def func3(self):
          print("this is example 3")
ob = Child2()
ob.func1()
ob.func2()
ob.func3()

#hierachical inheritance
class Parent:
      def func1(self):
          print("this is example 1")
class Child(Parent):
      def func2(self):
          print("this is example 2")
class Child2(Parent):
      def func3(self):
          print("this is example 3")
 
ob = Child()
ob1 = Child2()
ob.func1()
ob.func2()

# #hybrid inheritance
class Parent:
     def func1(self):
         print("this is example 1")
 
class Child(Parent):
     def func2(self):
         print("this is example 2")
 
class Child1(Parent):
     def func3(self):
         print(" this is example 3")
 
class Child3(Child1,Parent):
     def func4(self):
         print(" this is example 4")
 
ob = Child3()
ob.func1()

# #using super class
class Parent:
     def func1(self):
         print("this is example 1")
class Child(Parent):
     def func2(self):
          super().func1()
          print("this is example 2")
 
ob = Child()
ob.func2()
# #method overrding
class Parent:
    def func1(self):
        print("this is parent function")
 
class Child(Parent):
    def func1(self):
        print("this is child function")
 
ob = Child()
ob.func1()

#Exercise - Create a real time scenario for inheritance example Banking concept, ecommerce concept
class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
  
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
  
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
  
    def display(self):
        print("\n Net Available Balance=",self.balance)
  

s = Bank_Account()
s.deposit()
s.withdraw()
s.display()