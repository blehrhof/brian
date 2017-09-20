#open(filename, access mode,buffering)

# escape the slashes in the file name

file= open("C:\\Users\\bl11749\\Desktop\\FACT_CHACCO_D15B.sef", "r")
print ("FileName: "+file.name)
print("is closed: "+str(file.closed))
print("Mode: "+file.mode)
#number is number of characters
print (file.read(4))
#steaming functions
print (file.tell) # current position of stream
file.seek(5)
print(file.tell())



linenum=0
for line in file:
    linenum=linenum+1
    print(linenum, line)

file.close()


file.