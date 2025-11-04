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
