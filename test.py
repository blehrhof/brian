my_string = "this is a string"

#for char in my_string:
#    print(char)
print(my_string[5],my_string[6])

fruits = ['banana', 'apple', 'pear']
for f in fruits:
    print(f)
for f, x in enumerate(fruits):
    print(f, x)
for f in fruits:
    if f == "banana":
        print("i like "+f+"!")
        break #stops for loop

my_list=[1,2,3,4,5,6,7,8,9,10]

for x in range(1, 5):  # range items 1 to 4 stop BEFORE 5
    print(x)

start_num=0
while start_num <5:
    print(my_list[start_num])
    start_num += 1 #increment
