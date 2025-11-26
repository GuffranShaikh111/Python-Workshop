for i in range(1,11):
    for j in range(1,11):
        result=i*j
        print(f"{i}*{j}={result}")
        print()

n=[25,30,54,60,67,79]
print("Odd numbers in the list are:")
for num in n:
    if num%2!=0:
        print(num)