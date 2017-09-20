area=0
height=10
width=20

#calc area of triangle
area=width * height /2

print("the area if the triangle would be %.0f" % area)

# number of decimals for floating point number, pct sign is the concat instead of plus
# right justified 6 spaces
print ("print %06d !" % 42)
print ("print % 6d !" % 42)  # blank space
print("i have {0:d} cats".format(6))
print("i have {0:.2f} cats".format(6))
print("i have {0:.2f} {1:.2f} {2:.2f} cats".format(6,10,16))
# "/" at end of line indicates that the next line is a continuation

print("i have {0:.2f} {1:.2f} {2:.2f} cats" \
.format(6,10,16))

#salary=input("please enter your salary: ")
#bonus=input("please enter your bonus: ")
salary=500
bonus=75
paycheck=salary+bonus
print(paycheck)
paycheck=float(salary)+float(bonus)
print(paycheck)

import datetime
currentdate=datetime.date.today()
print(currentdate)
print(currentdate.year)
print(currentdate.month)
print(currentdate.day)

