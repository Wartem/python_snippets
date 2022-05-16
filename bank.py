import sys

class BankAccount:
    
    DESC = "Bank Account"
    
    def __init__(self, name):
        self._balance = 0
        self._guest_list = set()

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount: int):
        self._balance = amount

    def deposit(self, amount: int):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount: int):
        if amount > 0:
            self.balance -= amount

    def __str__(self):
        return self._balance
    
    @property
    def guest_list(self):
        return self._guest_list
    
    @guest_list.setter
    def guest_list(self, list_of_guests):
        self._guest_list = list_of_guests
        
    def add_guest(self, name):
        self._guest_list.add(name)
        
    def print_guests(self):
        print(sorted(self.guest_list))
        for guest in sorted(self._guest_list):
            print(guest)

def welcome():
    welcome_str = "Welcome"
    for x in welcome_str.upper():
        print(x, end=' ')
    print("To", BankAccount.DESC)
    
def main():
    welcome()
    bank_account = BankAccount("Karl")
    try:
        bank_account.deposit(100)
        bank_account.withdraw(50)
        print(bank_account.__str__())
    except TypeError:
        print("Wrong input by user!")
        sys.exit()
        
    bank_account.add_guest("John")
    bank_account.add_guest("Marie")
    bank_account.add_guest("Soran")
    bank_account.add_guest("John")
    bank_account.add_guest("Karl")
    bank_account.add_guest("John")
    bank_account.add_guest("John")
    
    bank_account.print_guests()

if __name__ == "__main__":
    main()
