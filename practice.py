class Circle:

    def __init__(self,radius):
        self.radius = radius

    def Area(self):
        return (22/7) * self.radius ** 2

    def Perimeter(self):
        return 2 * (22/7) * self.radius
    
c1 = Circle(21)
print(c1.Area())
print(c1.Perimeter())



class Employee:

    def __init__(self,role,department,salary):
        self.role = role
        self.departmenet = department
        self.salary = salary
    

    def showDetails(self):
        print(self.role , self.departmenet , self.salary)

class Engineer(Employee):

    def __init__(self,name ,age):
        self.name = name
        self.age = age
        super().__init__("Engineer" , "IT" , 50000)

    def allDetails(self):
        print(self.name,self.age,self.role,self.departmenet,self.salary)

emp1 = Employee("HR" , "Finance" , '50000')
emp1.showDetails()

eng1 = Engineer("Ketul Suthar",20)
eng1.allDetails()


class Order:

    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,ord2):
        return (self.price > ord2.price)

ord1 = Order("nachos" , 150)
ord2 = Order("Chips" , 130)

print(ord1 > ord2)