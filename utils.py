# utils.py
from person import Person
from bank_account import BankAccount

def person_data():
    name = input("Enter the person's name:\n")
    account_number = int(input("Enter a 4-digit account number:\n")) 
    initial_balance = float(input("Enter the initial balance:\n"))

    person = Person(name)
    account = BankAccount(account_number, initial_balance)
    person.add_account(account)

    done = input("Are you done adding accounts? (yes/no):\n")

    while done != "yes":
        account_number = int(input("Enter a 4-digit account number:\n"))
        initial_balance = float(input("Enter the initial balance:\n"))

        account = BankAccount(account_number, initial_balance)
        person.add_account(account)

        done = input("Are you done adding accounts? (yes/no):\n")

    return person

def balance_summary(person_list):
    for person in person_list:
        total = 0

        for account in person.accounts:
            total += account.balance

        print(f"{person.name} : {total:.2f}")