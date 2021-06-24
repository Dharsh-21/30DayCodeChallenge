#Day12
# file1 = open("myfile.txt","w") 
# L = ["This is Delhi \n","This is Paris \n","This is London \n"] 

# # \n is placed to indicate EOL (End of Line) 
# file1.write("Hello \n") 
# file1.writelines(L) 
# file1.close() #to change file access modes 

# file1 = open("myfile.txt","r+") 

# print ("Output of Read function is ")
# print (file1.read() )
# print (file1.seek(0))

# # seek(n) takes the file handle to the nth 
# # bite from the beginning. 
 

# print ("Output of Readline function is ")
# print (file1.readline()) 
# print (file1.seek(0)) 

# # To show difference between read and readline 
# print ("Output of Read(9) function is ")
# print (file1.read(9))
# print (file1.seek(0)) 

# print ("Output of Readline(9) function is ")
# print (file1.readline(9)) 

# file1.seek(0) 
# # readlines function 
# print ("Output of Readlines function is ")
# print (file1.readlines()) 

# file1.close()

# # Python program to illustrate 
# # Append vs write mode 
# file1 = open("myfile.txt","w") 
# L = ["This is Delhi \n","This is Paris \n","This is London \n"] 
# file1.close() 

# # Append-adds at last 
# file1 = open("myfile.txt","a")#append mode 
# file1.write("Today \n") 
# file1.close() 

# file1 = open("myfile.txt","r") 
# print ("Output of Readlines after appending")
# print (file1.readlines())
# print
# file1.close() 

# # Write-Overwrites 
# file1 = open("myfile.txt","w")#write mode 
# file1.write("Tomorrow \n") 
# file1.close() 

# file1 = open("myfile.txt","r") 
# print ("Output of Readlines after writing")
# print (file1.readlines()) 
# print
# file1.close()

file_Day12 = open("30days30houroperations.txt","w")
file_Day12.write("I have completed 10 days coding successfully \n")
file_Day12.close()

file_Day12 = open("30days30houroperations.txt","a")#append mode 
file_Day12.write("Dharshini S \n") 
file_Day12.close() 
