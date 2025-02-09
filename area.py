class rectangle:
    def __init__(self, width, lenght):
        self.lenght = lenght
        self.width=width

    def area(self):
        return self.width * self.lenght
    
    def peri(self):
        return self.width*2 + self.lenght*2 

x = float(input("Enter a lenght: "))
y = float(input("Enter a width: "))
rec1 = rectangle(x,y)   


print(f"rectangle 1 area = {rec1.area()} and rectangle 1 perimeter = {rec1.peri()}")
print("__________________________________________________________________")

class employe:
    def __init__(self, name , position, salary):
        self.name= name
        self.position = position
        self.salary = salary

    def anual_salary(self):
        return self.salary * 12
    
    def display(self):
        print(f"Employe name: {self.name}, Position: {self.position}, Salary: {self.salary}, Anual salary: {self.anual_salary()} ")

e = input("What is your Name: ")

p = input("What is your position: ")

s = float(input("What is your monthly salary: "))

e1 = employe(e,p,s)

e1.display()
 
print("______________________________________________")

class student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.scores = []

    def add_grade(self, score):  
        self.scores.append(score)

    def average(self):
        return sum(self.scores)/len(self.scores)

    def display(self):
        print(f"Student: {self.name}, Grade: {self.grade}, and has a average score of {self.average()}")

n = input("What is your name: ")

g = input("What grade are you in: ")

sc1 = int(input("What is your first subjects grade: "))

sc2 = int(input("What is your second subjects grade: "))

sc3 = int(input("What is your third subjects grade: "))

sc4 = int(input("What is your four subjects grade: "))

s1 = student(n,g)

s1.add_grade(sc1)

s1.add_grade(sc2)

s1.add_grade(sc3)

s1.add_grade(sc4)

s1.display()

class bank:
    def __init__(self,name, balance=0):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        if amount > 0:
            self.balance+=amount
            print(f"Amount deposited. New balance: {self.balance}")
        else:
            print("You must enter a positive number")
    
    def widthdraw(self,amount):
        if 0 < amount <=self.balance:
            self.balance-=amount
            print(f"Amount widthdrawen. New balance: {self.balance}")
        else:
            print("The amount you want to widthdraw is over your balance")

c1=bank("Aaryan",1020030)

c1.deposit(50000)
c1.widthdraw(500000)



    