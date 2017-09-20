# for next 0 to 3
for steps in range(4):
    print("loop " + str(steps))
# for x = 1 to 10 by 2 
for steps in range(1,10,2):
    print("loop " + str(steps))

#answer='0'
#while answer != '42':
#    answer=input('what is the answer to the ultimate question of life, the universe and everyting? ')

print('correct')

guests=['a','b','c']
guests.append('d')
guests.append('e')
print(guests[-1])
print(guests)
guests[3]='f'
guests.append('h')
print(guests)
guests.remove('f')
print(guests)
del guests[1]
print(guests)
print(guests.index('e'))

