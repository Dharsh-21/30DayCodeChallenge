import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="Dhar",
)

mycursor = mydb.cursor()
print(mydb)

dbse = mydb.cursor()

dbse.execute("CREATE DATABASE EmployeeManage")


dbse = mydb.cursor()

dbse.execute("SHOW DATABASES")

for x in dbse:
    print(x)

    mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="0712",
  database="employeemanage"
)
dbse = mydb.cursor()

dbse.execute("CREATE TABLE Employee (empid INT , empNAME VARCHAR(255),empSALARY DOUBLE )")

dbse = mydb.cursor()

dbse.execute("SHOW TABLES")

for j in dbse:
  print(j)

  dbse = mydb.cursor()

dbse.execute("SHOW COLUMNS FROM employee")

for j in dbse:
  print(j)

  dbse = mydb.cursor()

sql = "INSERT INTO employee (empid , empNAME , empSALARY) VALUES (%s,%s,%s)"
val = [
  ('1','suji','10000.0'),
    ('2','Ave','20000.0'),
    ('3','janani','50000.0'),
    ('4','jaya','60000.0'),
    ('5','vish','76200.0'),
    ('6','suja','82000.0'),
    ('7','divi','79000.0'),
    ('8','sivas','26000.0'),
    ('9','ek','28000.0'),
    ('10','kishore','9100.0'),
    ('11','dhar','50000.0'),
    ('12','vishika','20000.0'),
    
       
]


dbse.executemany(sql, val)

mydb.commit()

print(dbse.rowcount, "was inserted.")

#1	Write a query to get the maximum and minimum salary from employees table

mycursor = mydb.cursor()

mycursor.execute("SELECT empNAME,empSALARY FROM employee where empSALARY = (select max(empSALARY) from employee)")

myresult = mycursor.fetchall()

for i in myresult:
    print(i)

    mycursor = mydb.cursor()

mycursor.execute("SELECT empNAME,empSALARY FROM employee where empSALARY = (select min(empSALARY) from employee)")

myresult = mycursor.fetchall()

for i in myresult:
    print(i)

#2 write a query to get the number of employees working with the company

    mycursor = mydb.cursor()

mycursor.execute("SELECT COUNT(*) from employeedata")

myresult = mycursor.fetchall()

for i in myresult:
    print(i)
    
#3 Write a query to get the first 3 characters of first name from employees table

    mycursor = mydb.cursor()

mycursor.execute("SELECT * from employee WHERE empNAME LIKE('Ave%')")

myresult = mycursor.fetchall()

for i in myresult:
    print(i)