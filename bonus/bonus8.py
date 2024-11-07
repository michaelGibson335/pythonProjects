#journal app

date = input("Enter today's date: ")
mood = input("How do you rate today's mood from 1 to 10? ")
journal = input("Let your thoughts flow:\n")

with open(f"bonus/journal/{date}.txt", "w") as file:
    file.write(mood + 2 * '\n')
    file.write(journal)