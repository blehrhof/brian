lass Person:


    def __init__(self, name, hair_color, height):
        self.name=name
        self.hair_color=hair_color
        self.height=height
    def print_name(self):
        print(self.name)
    def print_hair_color(self):
        print(self.hair_color)
    def print_height(self):
        print(self.height)

class Employee(Person):
    def __init__(self, employee_id):
        self.employee_id = employee_id
    def print_employee_id(self):
        print(self.employee_id)
    

brian = Person("Brian","brown","5-7")

billy_the_employee = Employee("a123")

billy_the_employee.print_employee_id()


