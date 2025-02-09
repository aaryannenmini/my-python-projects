class Bank:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Amount deposited. New balance: {self.balance}")
        else:
            print("You must enter a positive number.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Amount withdrawn. New balance: {self.balance}")
        else:
            print("The amount you want to withdraw is more than your balance.")

    def get_balance(self):
        print(f"Current balance: {self.balance}")
def bank_talker():
    name = input("What is your name? ")
    balance = float(input("Enter your initial balance: "))
    customer = Bank(name, balance)

    while True:
        print("\nWhat would you like to do?")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Please enter the number of your choice: ")

        if choice == '1':
            amount = float(input("Enter the amount to deposit: "))
            customer.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter the amount to withdraw: "))
            customer.withdraw(amount)
        elif choice == '3':
            customer.get_balance()
        elif choice == '4':
            print("Thank you for banking with us. Bye")
            break
        else:
            print("Invalid choice. Please select a valid option.")
bank_talker()