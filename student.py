class student(object):
    """student"""
    number_of_students=0

    def __init__(self, name,index):
        self.name=name
        self.index=index
        student.number_of_students += 1
    def __del__(self):
        student.number_of_students -= 1



s1=student('fred',12345)
s2=student('dave',34567)
#print(student.number_of_students, s1.number_of_students, s2.number_of_students)

del s1
print(student.number_of_students)

x="the quick brown fox"
x.zfill()

