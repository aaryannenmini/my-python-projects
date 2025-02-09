class bank:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.__balance=balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"You Deposited {amount}")
 
    def width(self,amount): 
        if 0<amount<=self.__balance: 
            self.__balance -= amount 
            print(f"You have widthdrawen {amount}") 
 
        else: 
            print("Insufficient funds or Invalid amount") 
 
    def get_balance(self):
        return self.__balance
    
a1 = bank("Lewis Hamilton",50000000000000000000000000000000000000000000000000000000000000000000000000000)
a1.deposit(50000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
a1.width(900000000000000000000000000000000000000000000000000000)
print(a1.get_balance())


print(a1.owner)
#print(a1.__balance) it will gen a attr error

class book:
    def __init__(self,title,author):
        self.__title=title
        self.__author=author 
        self.__isbarowed=False        

    def boroww(self):
        if not self.__isbarowed:
            self.__isbarowed=True
            print(f"You have borowwed {self.__title}")

        else:
            print( f"{self.__title} is already borrowed")

    def return_book(self):
        if self.__isbarowed:
            self.__isbarowed=False
            print(f"Yu have returned {self.__title}")

    def get_details(self):
        status='Available'if not self.__isbarowed else "Borrowed"




        return f"Title: {self.__title} Author:{self.__author} Status: {status}"
    
ob = book("Max Verstappen", " Goddzilla Is Very Big")

print(ob.get_details())
ob.boroww()
print(ob.get_details())
ob.return_book()
print(ob.get_details())


























    