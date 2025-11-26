user_name=input("Enter the user_name:")
if user_name=="user":
    print("user_name is valid")
    password=input("Enter password:")
    if password=="user@123":
        print("Login successful")
    else:
        print("Login failed")
else:
    print("user_name is not valid")