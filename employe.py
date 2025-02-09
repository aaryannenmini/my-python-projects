
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Employee: {self.name}, Salary: {self.salary}"


class Manager(Employee):
    def manage(self):
        return f"{self.name} is managing the team."

class Developer(Employee):
    def code(self):
        return f"{self.name} is writing code."

class TechLead(Manager, Developer):
    def lead_project(self):
        return f"{self.name} is leading the project."

e1 = Employee("John", 50000)
print(e1.get_details())

m1 = Manager("Alice", 70000)
print(m1.get_details())
print(m1.manage())

d1 = Developer("Bob", 60000)
print(d1.get_details())
print(d1.code())

t1 = TechLead("Eve", 90000)
print(t1.get_details())
print(t1.manage())
print(t1.code())
print(t1.lead_project())
