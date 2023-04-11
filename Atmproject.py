accounts = []
balance=500
pin="1234"

def create_account():
    name = input("Enter name: ")
    account_number = input("Enter account number: ")
    balance = int(input("Enter initial balance: "))
    account = {
        "name": name,
        "account_number": account_number,
        "balance": balance
    }
    accounts.append(account)
    print("Account created successfully")

def remove_account():
    account_number = input("Enter account number: ")
    for account in accounts:
        if account["account_number"] == account_number:
            accounts.remove(account)
            print("Account removed successfully")
            return
    print("Account not found")

def update_account():
    account_number = input("Enter account number: ")
    for account in accounts:
        if account["account_number"] == account_number:
            print(f"Name: {account['name']}, Account Number: {account['account_number']}, Balance: {account['balance']}")
            balance = int(input("Enter new balance: "))
            account["balance"] = balance
            print("Account updated successfully")
            return
    print("Account not found")

def view_account():
    account_number = input("Enter account number: ")
    for account in accounts:
        if account["account_number"] == account_number:
            print(f"Name: {account['name']}, Account Number: {account['account_number']}, Balance: {account['balance']}")
            return
    print("Account not found")

def view_all_accounts():
    for account in accounts:
        print(f"Name: {account['name']}, Account Number: {account['account_number']}, Balance: {account['balance']}")

def generate_pin():
    global pin
    import random
    pin = str(random.randint(1000, 9999))
    print(f"New PIN: {pin}")

def change_pin():
    global pin
    current_pin = input("Enter current PIN: ")
    if current_pin != pin:
        print("Invalid PIN")
    else:
        new_pin = input("Enter new PIN: ")
        confirm_new_pin = input("Confirm new PIN: ")
        if new_pin != confirm_new_pin:
            print("PINs do not match")
        else:
            pin = new_pin
            print("PIN changed successfully")

def check_balance():
    print(f"Your current balance is {balance}")

while True:
    print("1. Create account")
    print("2. Remove account")
    print("3. Update account")
    print("4. View account")
    print("5. View all accounts")
    print("6. Generate Pin")
    print("7. Change Pin")
    print("8. Balance Enquiry")
    print("9. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        create_account()
    elif choice == 2:
        remove_account()
    elif choice == 3:
        update_account()
    elif choice == 4:
        view_account()
    elif choice == 5:
        view_all_accounts()
    elif choice == 6:
        generate_pin()
    elif choice == 7:
        change_pin()
    elif choice == 8:
        check_balance()
    elif choice == 9:
        print("Thank you for using our banking system")
        break
    else:
        print("Invalid choice. Please try again.")
