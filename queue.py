class queue:

    def __init__(self):
        self.values = []

    def enqueue(self,value):
        self.values.append(value)
        print(f"{value} is added to the queue")

    def dequeue(self):
        self.values.pop[0]
        print(f"{self.values[0]} is removed from the queue")

    def show(self):
        print(self.values)


queue = queue()
queue.enqueue(10)
queue.enqueue(20)
queue.dequeue()
queue.show()