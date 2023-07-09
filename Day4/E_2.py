# Encapsulation Eg-2
class ATM:
    def __init__(self, acc_no, pin, balance):
        self.__acc_no = acc_no
        self.__pin = pin
        self.__balance = balance

    def get_acc_no(self):
        return self.__acc_no

    def validate_pin(self, pin):
        return pin == self.__pin

    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful.")
            print("Remaining balance:", self.__balance)
        else:
            print("Insufficient balance.")


acc_no = input("Enter the account number: ")
pin = input("Enter the PIN: ")
balance = float(input("Enter the account balance: "))

my_account = ATM(acc_no, pin, balance)
print("Account Details:")
print("Account Number:", my_account.get_acc_no())

input_pin = input("Enter your PIN to validate: ")
if my_account.validate_pin(input_pin):
    withdrawal_amount = float(input("Enter the withdrawal amount: "))
    my_account.withdraw(withdrawal_amount)
else:
    print("Invalid PIN. Access denied.")
