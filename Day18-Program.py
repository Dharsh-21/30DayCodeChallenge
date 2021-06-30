#Day 18
#1 Create a DB with doctor and doctor ID & patients visited

mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="0712",
  database="Database13"
)
dbse = mydb.cursor()

dbse.execute("CREATE TABLE Doctors (dr_name VARCHAR(255),dr_id VARCHAR(255), Patient VARCHAR(255))")

dbse = mydb.cursor()

sql = "INSERT INTO Doctors (dr_name,dr_id , Patient) VALUES (%s,%s,%s)"
val = [('Tina','d5',5),('Jane','d6',8),('Jack','d7',21)]
dbse.executemany(sql, val)

mydb.commit()

print(dbse.rowcount, "was inserted.")




#2 Get the doctor(s) who have more than 5 patients visited
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Doctors where Patient >5")

myresult = mycursor.fetchall()

for a in myresult:
  print(a)

#3 Get the doctors with no patients visit
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Doctors where Patient =0")

myresult = mycursor.fetchall()

for a in myresult:
  print(a)