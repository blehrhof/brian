# open to create and open the file
# myfile=open(filename, accessmode)
# file will be created in folder where program is unless you specify a path
# r - read , w - write (OVER) , a - append,  b - binary r+  w+
filename='C://Users//bl11749//Documents//My Projects//demo.txt'
mode="w"
#myfile=open(filename,mode)
#myfile.write("hi there\n")
#myfile.write("how are you")
#myfile.close()

data=input('please enter file info')
file=open(filename,mode)
file.write(data)
file.close()

#file=open(filename,mode)
#entire.file.contents=file.read()
#each.line=file.readline()