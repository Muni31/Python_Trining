# 1) Saurabh needs to withdraw X Rs. from an ATM. The transaction will succeed only if X is an odd number,
# and Saurabh's account balance has enough cash to perform the withdrawal transaction 
# (including bank charges). For each successful withdrawal the bank charges 10.50 Rs. Calculate 
# Saurabh's account balance after an attempted transaction. 

# Input: 
# - Saurabh's initial account balance 
# - Withdrawal amount 
# Output 
# - Amount present in Saurabh's account after withdrawal. 
# - Error message, if the withdrawal did not match transaction criteria. 

def withdraw(amount,balance):
    charges=10.50
    total=amount+charges
    if amount%2!=0 and balance>=total:
        
        balance-=total
        print(f"Amount your going to withdraw 'Rs.{amount}' + bank charges for withdrawal 'Rs.{charges} '= Total amount 'Rs.{total}'")
        print(f"Balance amount present in your account 'Rs.{balance}' after withdrawal ")
    else:
        print("Transaction failed ......")
        print("Insufficient money in your account (please add money in your bank accont) ")

balance=int(input("Enter your Account Balance : "))
amount=int(input("Enter the amount you want to withdraw : "))
withdraw(amount,balance)
    