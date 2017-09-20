import cs50
import csv
from cs50student import Student

students=[]
for i in range(3):
    print("name: ",end="")
    name=cs50.get_string()

    print("dorm: ", end="")
    dorm=cs50.get_string()

    students.append(Student(name,dorm))

#for student in students:
#    print("{} is in {}.".format(student.name, student.dorm))

file=open("C://Users//bl11749//Documents//My Projects//students.csv","w")
writer=csv.writer(file)
for student in students:
    writer.writerow((student.name,student.dorm))
file.close