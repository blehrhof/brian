# open to create and open the file
# myfile=open(filename, accessmode)
# file will be created in folder where program is unless you specify a path
# r - read , w - write (OVER) , a - append,  b - binary r+  w+
filename='C://Users//bl11749//Documents//My Projects//demo.txt'
mode="r"
#myfile=open(filename,mode)
#myfile.write("hi there\n")
#myfile.write("how are you")
#myfile.close()

#data=input('please enter file info')
with open(filename) as file:

#fullfile=file.read()
#print( fullfile)
#exit
#eachline=file.readline()
#i=0
    for each in file:
    
        print(each)



#file.write(data)
file.close()
