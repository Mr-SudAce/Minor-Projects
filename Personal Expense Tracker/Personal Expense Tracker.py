###################################################### Personal Expense Tracker #####################################################


import os                                                                   # check if file exist
from datetime import datetime                                               # get date and time



data_file = 'expense_detail.txt'                                            # save file name where transaction will be save

print("\tWelcome\nPersonal Expense Traceker")


def load_data():
    transaction = []                                                        # Empty list to store all transaction
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            for line in file:
                date, type_, amount, desc = line.strip().split(" | ")       # Each line has 4 parts separated by '|'
                transaction.append({
                    "date" : date,
                    "type" : type_,
                    "amount" : float(amount),
                    "desc" : desc
                })
    return transaction                                                      # Return the list of transactions


# This function saves a new transaction to the file
def save_transaction(type_, amount, desc):
    print(f"DEBUG: Saving transaction to file: {data_file}")
    with open(data_file, "a") as file:                                      # Open the file in append mode
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")                 # get current time
        file.write(f"{type_} | {amount} | {desc} | {date}\n ")              # write  data







# This function calculates and shows your current balance
def show_balance(transactions):
    balance = 0                                                             #start with zero
    for txn in transactions:
        if txn["type"] == "income":
            balance = balance + txn["amount"]                               #add income
        else:
            balance = balance - txn["amount"]                               #subtract expense
    
    print(f"\n Current Balance: Rs. {balance:.2f}")







# This function displays all past transactions
def view_transactions(transactions):
    print("\nTransaction History:")
    if not transactions:
        print("No transactions yet.")
    else:
        for txn in transactions:
             print(f"{txn['type'].title()} - Rs. {txn['amount']:.2f} - {txn['desc']} - {txn['date']}")
             
             







# This function asks the user to add a new transaction
def add_transaction():
    type_ = input("Type (income/expense): ").lower()                        # Ask for type
    if type_ not in ["income", "expense"]:                                  # Check if input is valid
        print("Invalid type! Try again.")
        return
    try:
        amount = float(input("Amount (Rs.): "))                             # Ask for amount
        desc = input("Description: ")                                       # Ask for description
        save_transaction(type_, amount, desc)                               # Save the transaction
        print("Transaction added successfully!")
    except ValueError:
        print("Invalid amount!")                                            # If user types a wrong number





# Main function that runs the program
def main():
    while True:                                                             # Infinite loop until user chooses to exit
        print("\nChoose an option:")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Show Balance")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ")                              # User selects option
        transactions = load_data()                                          # Load latest transactions every time

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions(transactions)
        elif choice == "3":
            show_balance(transactions)
        elif choice == "4":
            print("Exiting... Your data is saved.")
            break
        else:
            print("Invalid choice. Try again!")

# This ensures that main() runs only when the script is executed directly
if __name__ == "__main__":
    main()             
             
             
             
             
             
             
             
             
             