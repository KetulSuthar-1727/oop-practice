class Account:

    def __init__(self , balance , accountNo):
        self.balance = balance
        self.accountNo = accountNo

    def debit(self):
        debitAmm = int(input("Enter the ammont to debit : "))
        self.balance = self.balance - debitAmm
        self.balancePrint()

    def credit(self):
        creditAmm = int(input("Enter the ammout to add : "))
        self.balance = self.balance + creditAmm
        self.balancePrint()
        

    def balancePrint(self):
        print("Final balance : " , self.balance)


customer1 = Account(10000 , 100)
customer2 = Account(15000 , 101)

customer1.credit()
customer1.debit()

print("Customer 2 data is showing")

customer2.credit()
customer2.debit()