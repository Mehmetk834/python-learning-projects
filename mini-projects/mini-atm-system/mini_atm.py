balance = 0
correct_username = "Mehmet"
correct_password = 12345
login_attempts = 3
transaction_history = []


while login_attempts > 0:
    entered_username = input("Enter your username: ")

    try:
        entered_password = int(input("Enter your password: "))
    except ValueError:
        print("Password must be numeric.")
        continue

    if entered_username == correct_username and entered_password == correct_password:
        print("Login successful.")

        while True:
            print("\n--- ATM MENU ---")
            print("1 - View Balance")
            print("2 - Deposit Money")
            print("3 - Withdraw Money")
            print("4 - Transaction History")
            print("5 - Exit")

            choice = input("Your choice: ")

            if choice == "1":
                print("Your current balance:", balance)

            elif choice == "2":
                try:
                    deposit_amount = int(input("Enter amount to deposit: "))
                    if deposit_amount > 0:
                        balance += deposit_amount
                        transaction_history.append(f"{deposit_amount} TL deposited")
                        print("Money deposited. Current balance:", balance)
                    else:
                        print("Amount must be greater than 0.")
                except ValueError:
                    print("Please enter numbers only.")

            elif choice == "3":
                try:
                    withdraw_amount = int(input("Enter amount to withdraw: "))
                    if withdraw_amount > 0 and withdraw_amount <= balance:
                        balance -= withdraw_amount
                        transaction_history.append(f"{withdraw_amount} TL withdrawn")
                        print("Money withdrawn. Current balance:", balance)
                    else:
                        print("Insufficient balance or invalid amount.")
                except ValueError:
                    print("Please enter numbers only.")

            elif choice == "4":
                if len(transaction_history) == 0:
                    print("No transactions yet.")
                else:
                    print("\nTransaction History:")
                    for transaction in transaction_history:
                        print("-", transaction)

            elif choice == "5":
                print("Exiting.")
                break

            else:
                print("Invalid selection.")

        break

    else:
        login_attempts -= 1
        print("Incorrect username or password.")
        print("Remaining attempts:", login_attempts)

        if login_attempts == 0:
            print("Your account has been blocked.")
