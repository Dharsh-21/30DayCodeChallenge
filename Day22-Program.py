#Day22
# 1 Read a jpeg image and print the image file 
# from PIL import Image , ImageFilter
# img = Image.open('C:\\Users\\KISHORE\\Desktop\\Internship\\Python Internship\\30DayCodeChallenge\\ganesha.jpg')
# filter_img = img.convert('L')
# crooked  = filter_img.rotate(180)
# #resize = filter_img.resize((300,300))

# crooked.save("C:\\Users\\KISHORE\Desktop\\Internship\\Python Internship\\30DayCodeChallenge\\blur.jpg","png")
# print(img.format)

from PIL import Image , ImageFilter
img = Image.open('C:\\Users\\KISHORE\\Desktop\\Internship\\Python Internship\\30DayCodeChallenge\\ganesha.jpg')
filter_img = img.convert('L')
crooked  = filter_img.rotate(180)
#resize = filter_img.resize((300,300))

crooked.save("C:\\Users\\KISHORE\Desktop\\Internship\\Python Internship\\30DayCodeChallenge\\blur.jpg","png")
print(img.format)


#2.	Merge two pdf files using python script

import PyPDF2 
pdf1File = open('1.pdf', 'rb')
pdf2File = open('2', 'rb')
 
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
 

pdfWriter = PyPDF2.PdfFileWriter()
 

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
 

for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
 

pdfOutputFile = open('MergedFiles.pdf', 'wb')
pdfWriter.write(pdfOutputFile)

pdfOutputFile.close()
pdf1File.close()
pdf2File.close()


#3.	Scrape a website and store the data into DB.

import requests
import MySQLdb
from bs4 import BeautifulSoup


mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="Dhar",

)
dbse = mydb.cursor()

url_to_scrape = 'https://en.wikipedia.org/wiki/India'
plain_html_text = requests.get(url_to_scrape)
soup = BeautifulSoup(plain_html_text.text, "html.parser")

print(soup.prettify())