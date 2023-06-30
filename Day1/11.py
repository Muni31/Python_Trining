# Write a program a function for ATM machine which takes amount as input and 
# output should be number of notes of each denomination. 
# The ATM has notes in following denomination : 2000, 500, 100.  
# Note that the ATM machine rarely gives all	 notes of a single amount.
# If you enter 4000, it will give 1 2000rs, 3 500rs and 5 100rs	 notes for even distribution. 
def atm(amount):
    denominations = [2000, 500, 100]
    notes = []

    for count in denominations:
        note = amount // count
        notes.append(note)
        amount %= count

    return notes


requested_amount = int(input("Enter the amount: "))
result = atm(requested_amount)
print(f"Number of notes for {requested_amount} are :")
print("2000 rupee notes:", result[0])
print("500 rupee notes:", result[1])
print("100 rupee notes:", result[2])

