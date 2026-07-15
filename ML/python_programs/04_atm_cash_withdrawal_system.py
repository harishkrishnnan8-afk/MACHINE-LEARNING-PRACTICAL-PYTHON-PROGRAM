"""
Question:
Check account balance, verify PIN, and perform withdrawal if sufficient balance exists.
"""

balance = 10000
pin = 1234

p = int(input("Enter PIN: "))

if p == pin:
    amount = float(input("Enter Withdrawal Amount: "))
    if amount <= balance:
        balance -= amount
        print("Transaction Successful")
        print("Remaining Balance =", balance)
    else:
        print("Insufficient Balance")
else:
    print("Invalid PIN")
