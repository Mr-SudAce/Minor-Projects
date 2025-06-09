import os

data_file = "ATM.txt"


def load_users():
    atm = []
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            for line in file:
                pin_, name, acc_number, balance = line.strip().split(" | ")
                atm.append({
                    "pin" :pin_,
                    "name" : name,
                    "accnumber" :acc_number,
                    "blnc" : float(balance)
                })
    return atm



def save_atmdetail(atm):
    with open(data_file, "w") as file:
        for user in atm:
            file.write(f"{user['pin']} | {user['name']} | {user['accnumber']} | {user['balance']}\n")


def create_account(atm):
    pin = input("Set 4-digit PIN:")
    name = input("Enter your name")
    acc_number = input("Enter account number: ")
    balance = float(input("Enter opening balance: "))
    
    atm.append({
        "pin": pin,
        "name": name,
        "accnumber": acc_number,
        "balance": balance
    })
    
    save_atmdetail(atm)
    print("Account created successfully!\n")
    
    
def find_user(atm, pin):
    for user in atm:
        if user['pin'] == pin:
            return user
        return None




def ATM():
    atm = load_users()
    while True:
        print("\n=== ATM Menu ===")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Withdraw Money")
        print("Type 'exit' to quit")
        
        
        
        choice = input("Enter any one:\t ")
        if choice == "1":
            create_account(atm)
        elif choice == "2":
            pin = input("Enter your PIN: ")
            user = find_user(atm, pin)
            if user:
                print(f"Hello {user['name']}! Your current balance is Rs.{user['balance']}")
            else:
                print("Invalid PIN!")
        elif choice == "3":
            pin = input("Enter your PIN: ")
            user = find_user(atm, pin)
            if user:
                amount = float(input("Enter amount to withdraw: "))
                if amount <= user['balance']:
                    user['balance'] -= amount
                    save_atmdetail(atm)
                    print(f"Withdrawal successful! New balance: Rs.{user['balance']}")
                else:
                    print("Insufficient balance!")
            else:
                print("Invalid PIN!")
        elif choice.lower() == "exit":
            print("Exiting... Bye!")
            break
        else:
            print("Invalid choice! Try again.")
            
ATM()
        
    