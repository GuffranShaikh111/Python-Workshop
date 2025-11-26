Balance=20000
n=int(input("enter a number:"))
if n>Balance:
    print("Entered amount exceeds the balanced amount")
elif n<Balance:
    NewBalance=Balance-n
    print("New Balance is",NewBalance)