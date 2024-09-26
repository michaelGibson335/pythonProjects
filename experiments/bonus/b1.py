## ask a user for a password and check if the password is correct

#ask user for password input
password = input("Enter a password: ")

while password != "pass123":
    password = input("Enter a password: ")

print("Password was correct!")