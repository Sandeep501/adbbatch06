# encapsulation

class BankAccount():
    def __init__(self, account_number, balance):
        self.__account_number = account_number # private variable
        self.__balance = balance # private variable
    
    
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}, new balance is {self.__balance}")
    
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"withdrawn {amount} from account, new balance is {self.__balance}")
        else:
            print("insufficient funds")
    
    
    def __get_balance(self):
        return self.__balance
    
    
    def show_balance(self):
        return self.__get_balance()
    

account = BankAccount("1234", 10000)
print("Intial Balance")
# print(account.get_balance())
account.deposit(3000)
account.withdraw(1000)
# print(account.get_balance())
print(account.show_balance())
