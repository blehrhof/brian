

my_list = ["apple", "pear", "orange"]

print(len(my_list))

my_list.append("banana")

print(my_list)
print(len(my_list))

my_list.pop()  # remove last key from list - LIFO stack
                # pop(0) returns first element
print(my_list)
my_list.pop()
print(my_list)

                
my_list = ["apple", "pear", "orange"]

my_fruit = my_list[0]
print(my_fruit)
my_fruit = my_list[1]
print(my_fruit)
my_list.insert(0,"banana") # 0 inserts at beginning - number is  'before this index'
print(my_list)
my_list.insert(2,"shrimp") # insert into element
print(my_list)
my_list.remove("shrimp")
print(my_list)
my_list.extend(["plum", "grapefruit"])
print(my_list)

new_list = my_list[0:2]  # from 1 to 2
print(new_list)
new_list = my_list[1:-1]  # last element
print(new_list)

