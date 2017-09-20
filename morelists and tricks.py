


a=['aaaa','bb','ccccc']

#example of list comprehsion syntax

[len(s)   for s in a   ]

a=[1,2,3,4]

print([num*num  for num in a])
print([num*num  for num in a  if num > 2])

import re

[f  for f in os.listdir('.')  if re.search(r'__\w+__', f)]


cities=['a','b','c','d']
# the bad way
i=0
for city in cities:
    print(i,city)
    i +=1

# the good way
for i,city in enumerate(cities):
    print(i,city)

x_list=[1,2,3]
y_list=[2,4,6]
# the bad way
for i in range(len(x_list)):
    x=x_list(i)
    y=y_list(i)
    print (x,y)

# the good way
for x,y in zip(x_list, y_list):
    print (x,y)

x=10
y=-10
print ('before: x = %d, y=%d' % (x,y))
# the bad way to swap variables
tmp = y
y=x
x=tmp
print ('before: x = %d, y=%d' % (x,y))
# the good way to swap variables using tuples
x,y = y,x
print ('before: x = %d, y=%d' % (x,y))


ages = {
        'mary'  : 31,
        'john'  : 28
}
# the bad way
if 'dick' in ages:
    age = ages['dick']
else
    age = 'unknown'
print ('dick is %s years old' % age)

# the good way
age = ages.get('dick','unknown')


needle = 'd'
haystack = ['a', 'b', 'c']
#the bad way
found = False
    if needle == letter:
        print('found')
        found = True
        break
if not found:
    print('not found')

# the good way
for letter in haystack:
    if needle == letter:
        print('found')
        break
else:
    print('not found')

# the bad way
f=open('pimpin-aint-easy.txt')
text=f.read()
for line in text.split('\n'):
    print(line)
f.close

#better way
f=open('pimpin-aint-easy.txt')
for line in f:
    print(line)
f.close

#best way
with open('pimpin-aint-easy.txt') as f:
for line in f:
    print(line)


print ('converting')
print(int('1')
print ('done')

# doesn't

print ('converting')
print(int('x')
print ('done')


print ('converting')
try:
    print(int('x')
except:
    print ('conversation failed')
else:
    print('conversion successful')
finally: # always
    print ('done')





