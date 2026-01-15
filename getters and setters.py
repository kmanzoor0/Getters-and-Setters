# Create a class BankAccount:
# Private variable _balance
# Getter balance
# Setter balance that does not allow negative value

class BankAccount:
    def __init__(self,balance):
        self._balance = balance
    def display(self):
        print(self._balance)
    @property
    def balance(self):
            return self._balance
    @balance.setter
    def balance(self,balance):
        if balance > 0:
            self._balance = balance
        else:
            print('Please enter a positive number')
acc = BankAccount(100)
acc.balance=-50
print(acc.balance)

#Create a class Student:
#Private variables _name and _marks
#Getter & setter for marks
#If marks < 0 or > 100 → print "Invalid marks"

class Student:
    def __init__(self,name,marks):
        self._name = name
        self._marks = marks
    def display(self):
        print(self._name)
        print(self._marks)
    @property
    def marks(self):
        return self._marks
    @marks.setter
    def marks(self,marks):
        if marks <0 or marks > 100:
            print('Invalid marks')
        else:
            self._marks = marks

a = Student('Ali',34)
a.marks = 54
a.display()


