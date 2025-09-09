class Student:

    clg = "Sal"
    # this is the default constructor
    def __init__(self):
        pass

    # this is parametrized constructor
    def __init__(self,name,enrollment,dept):
        self.name = name
        self.enrollment = enrollment
        self.dept = dept
        
    
s1 = Student("Ketul" , 231263116019 , "IT")
s2 = Student("Maulik" , 231263116008 , "CE")
print(s1.name,s1.enrollment,s1.dept,s1.clg)
print(s2.name,s2.enrollment,s2.dept,s2.clg)
