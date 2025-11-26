balance=10000
while True:
    choice=str(input("Enter ur choice"))
    if choice=="stop":
        break
    elif choice=="debit":
        n = int(input("Enter a amount to be debited"))
        current_balance=balance-n
        print("Current Balance is",current_balance)
    elif choice=="credit":
        n = int(input("Enter a amount to be credited"))
        current_balance=balance+n
        print("Current Balance is",current_balance)