class Student:

    def __init__(self,name,maths,science,physics):

        self.name = name
        self.maths =  maths
        self.science = science
        self.physics = physics

    def avg(self):

        totalSum  = self.maths + self.science + self.physics

        return totalSum / 3
    

s1 = Student("Ketul" , 80 ,70 , 60)
s2 = Student("Maulik" , 70 , 50 , 80)
print(s1.avg())
print(s2.avg())




class stack:

    def __init__(self):
        self.values = []

    def push(self,number):
        self.values.append(number)
        print(f"{number} is pushed")


    def is_empty(self):
        return len(self.values) == 0
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print(f"{self.values.pop()} is popped from the stack")

    def peek(self):
        if self.is_empty():
            print("Stack is empty there is not top element")
            return None
        print(self.values[-1])

    def size(self):
        print(len(self.values))
    
    def display(self):
        print(self.values[::-1])

    def min_Stack(self):
        if self.is_empty():
            print("Stack is empty")

        minimum = self.values[0]

        for val in self.values:
            if val < minimum:
                minimum = val

        print(minimum)

stack = stack()

stack.push(10)
stack.push(20)
stack.pop()
stack.peek()
stack.size()
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.push(3)
stack.display()
stack.pop()
stack.display()
stack.min_Stack()