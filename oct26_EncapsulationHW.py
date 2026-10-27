
# Encapsulation 

class BankAccount:
    def __init__(self, name, account_no, bank_name, balance):
        self.name = name
        self.__account_no = account_no
        self.bank_name = bank_name
        self.__balance = balance

    # Getter methods
    def get_name(self):
        return self.name

    def get_account_no(self):
        return self.__account_no

    def get_bank_name(self):
        return self.bank_name

    def get_balance(self):
        return self.__balance

    # Setter method
    def set_balance(self, balance):
        self.__balance = balance


user_1 = BankAccount("Rohit Sharma", 12345, "SBI", 5000)

print("Name:", user_1.get_name())
print("Account No:", user_1.get_account_no())
print("Bank Name:", user_1.get_bank_name())
print("Old Balance:", user_1.get_balance())

user_1.set_balance(8000)
print("Updated Balance:", user_1.get_balance())