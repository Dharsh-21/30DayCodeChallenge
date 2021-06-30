#Day17
#1 Create a connection for DB and print the version using a python program

import mysql.connector

mydb=mysql.connector.connect(host='Local Host',
                             user='root',
                             password="Dhar"
                            )
print(mydb)

#Create a multiple tables & insert data in table

mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="0712",
  database="database11"
)
dbse = mydb.cursor()

dbse.execute("CREATE TABLE office (Employee_name VARCHAR(255), Employee_id int,Employee_dep VARCHAR(255))")

dbse = mydb.cursor()

dbse.execute("CREATE TABLE custom (name VARCHAR(255), id int ,city VARCHAR(255))")

dbse =mydb.cursor()
dbse.execute("CREATE TABLE Student(reg INT(24) , name VARCHAR(255) , dob INT(19))")


dbse = mydb.cursor()

dbse.execute("SHOW TABLES")

for i in dbse:
  print(i)

#Create a employee table and read all the employee name in the table using for loop

import mysql.connector
mydb = mysql.connector.connect(
                               host="localhost",
                               database = "database12",
                               user ="root",
                               password="0712"
                               )

dbse = mydb.cursor()
dbse.execute("CREATE TABLE Employee1 ( EMP_name VARCHAR(255), EMP_no int , EMP_age int, EMPdept VARCHAR(255))")
dbse.execute("INSERT INTO Employee ( EMP_name, EMP_no, EMP_age, EMPdept) VALUES  ('Tina',1001,27,'CS')")
mydb.commit()

dbse.execute("SHOW TABLES")
for i in dbse:
    print(i)

dbse.execute("SELECT * FROM Employee")

for i in dbse:
    print(i)