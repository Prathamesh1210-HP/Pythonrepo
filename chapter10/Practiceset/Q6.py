# Can you change the self-parameter inside a class to something else (say "Patu"). Try changing self to "slf" or "Patu" and see effects.
from random import randint


class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"Train No: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")

t = Train(12399)
t.book("Rampur", "Delhi")
t.getstatus()
t.getFare("Rampur", "Delhi")

# NO there will be no changes occured by changing self to slf, its just not good practice that's it.