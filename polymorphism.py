class Polyorphism:

    def __init__(self,real,img):
        self.real = real
        self.img = img

    def show(self):
        print(self.real,"i +" ,self.img,"j")

    def __add__(self,number2):
        real = self.real + number2.real
        img = self.img + number2.img
        return Polyorphism(real,img)

number1 = Polyorphism(3,5)
number2 = Polyorphism(4,6)

number1.show()
number2.show()

number3 = number1 + number2
number3.show()