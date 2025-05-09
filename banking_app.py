
import os
import random
import datetime




USER_FILE = "User.txt"
CUSTOMER_FILE = "Customer.txt"
ACCOUNT_FILE = "Account.txt"
TRANSACTION_HISTORY_FILE ="Transaction_History.txt"

 



# Create Account Function===========================================================================================

def create_account():
    print("======Customer Creation=====")
    customer_name = input("Enter your name:")
    customer_address = input("Enter your address:") 
    customer_phone_no = int(input("Enter your phone number:"))
    intial_balances = float(input("Enter the intial balance:$"))
    customer_NIC_no = int(input("Enter your N.I.C.No:"))
    return(customer_name,customer_address,customer_phone_no,intial_balances,customer_NIC_no)

    
    
# ================================================================================================================

#=================================================================================================================
#  Function for read file ========================================================================================

def read_user():
    try:
        with open("User.txt", "r") as user_info:
            lines = file.readlines()
        return lines

    except FileNotFoundError:
        return[]
        
        

def read_customer():
    try:
        with open("Customer.txt", "r") as customer_info:
           lines = file.readlines()
        return lines

    except FileNotFoundError:
        return[] 
        


def read_account():
    try:
        with open("Account.txt", "r") as account_info:
            lines = file.readlines()
        return lines

    except FileNotFoundError:
        return[]
        
        
# =================================================================================================================== 

# Fuction for Auto account number creation==========================================================================

def auto_account_number():
    return str(random.randint(2000, 12000))
    

def customer_id():
    existing = read_customer()
    return f"C_{3000 + len(existing) + 1}"
    

def user_id():
    existing = read_user()
    return f"U_{5000 + len(existing) + 1}"
    
# Banking Files====================================================================================================

def file_creation(account_creation):

    acc_no = auto_account_number()
    u_id = user_id()
    c_id = customer_id()

    with open("User.txt", "a") as user_info:
        user_info.write(f"{acc_no}  {u_id}   {account_creation[0]}   {account_creation[1]}   {account_creation[2]}   {account_creation[4]}\n")

    with open("Customer.txt", "a") as customer_info:
        customer_info.write(f"{acc_no}  {c_id}   {account_creation[3]}\n")

    with open ("Account.txt","a") as acconut_info:
        acconut_info.write(f"{acc_no}   {account_creation[3]} \n")
    
    # with open ("Transaction_History.txt","w") as transaction_info:
    #     transaction_info.write(f"{account_creation[]}")
    
    



# Deposit Money Function================================================================================================

def deposit_money(selected_account, intial_balances):
    with open ('Account.txt','r') as file: 
        text = file.read()
        words = text.split("    ")
        selected_account = "words"

    global initial_balances
    try:
        if deposit >"0":
            deposit = float(input("Enter amount to deposit: $"))
            initial_balances[selected_account] += deposit
            print(f"Deposit successful. New balance: ${intial_balances[selected_account]}") 
        if selected_account not in intial_balances:
            print(f"Account'{selected_account}'not found.")
            return  
        else:    
            deposit < "0"
            print("Enter the positive numbers only!.")
            return


    except ValueError:
        print("Enter the numbers only!")
#============================================================================================================================

# Withdraw Money Function ====================================================================================================

def withdraw_money(selected_account,initial_balances): 
    with open ('Account.txt','r') as file: 
        text = file.read()
        words = text.split("    ")
        selected_account = "words"

    initial_balances
    try:
        amount = float(input("Enter amount to withdraw: $"))
        if amount <= initial_balances[selected_account]:
            initial_balances[selected_account] -= amount
            print(f"Withdrawal successful. New balance: ${account_balances[selected_account]}")

        else:
            print("Insufficient funds!")

    except ValueError:
        print("Enter the numbers only!")


#     ==================================================


# # Check Balance Function==================================================================================================

def check_balance():
    print(f"Account {selected_account + 1} Balance: ${intial_balances[selected_account]}")
    
#========================================================================================================================    


# Transaction History Function============================================================================================

def add_transaction(filename, auto_account_number, amount, description):
    
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    transaction = f"{auto_account_number()}, {current_time}, {amount}, {description}\n"
    
    with open("filename",'a') as file:
        file.write(transaction)
    
    print("Transaction added successfully!")


def view_transactions(filename):
    try:
        with open("filename", 'r') as file:
            transactions = file.readlines()
            
            if not transactions:
                print("No transactions found.")
            else:
                print("Transaction History:")
                print("ID | Date & Time | Amount | Description")
                for transaction in transactions:
                    print(transaction.strip())
    
    except FileNotFoundError:
        print("Transaction history file not found")
    
    
# =============================================================================================================================


#Admin Login =======================================================================

# correct_admin_name = "Admin"
# correct_admin_password = "admin@123**" 
# max_attempts = 3
# attempts = 0

# while attempts < max_attempts :
#     print("======Admin Login======")
#     admin_name = input("Enter the admin name:")
#     admin_password = input("Enter the admin password: ")
    
#     if admin_name == correct_admin_name and admin_password == correct_admin_password:
#         print("Login Success Full!")
#         break

#     else:
#         attempts += 1
#         remaining = max_attempts - attempts
#         print(f"Invalid Information.{remaining}attempt(s) left.")


# if attempts == max_attempts:
#         print("Too many failed attempts.Exiting program.")
#         exit()
#===================================================================================


#ATM MENU ===========================================================================

while True:

    print("====ATM MENU====")
    print("1.Create Account")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Check Balance")
    print("5.Transcation History")
    print("6.Exit")
    
    choice = input("Enter Your choice(1-5):")

    if choice == "1":
        account_creation = create_account()
        file_creation(account_creation)
        print("Account Creation Success full!")
         
    elif choice == "2":
        acc_num = input("Enter your Account_no:")
        deposit_money(selected_account,intial_balance)

    elif choice == "3":
        acc_num = input("Enter your Account_no:")
        withdraw_money(selected_account,intial_balance)

    elif choice == "4":
        acc_num = input("Enter your Account_no:")
        check_balance()

    elif choice =="5":
        acc_num = input("Enter your Account_no:")
        add_transaction(filename, 1, 100.50, "Deposit")
        view_transactions(filename)


    elif choice == "6":
        print("Thank you for using this mini banking system!.")
        exit()
        break
    else:
        print("Enter the one to six numbers only!.")


#=========================================================================================


# Users Login ==============================================================================
print("=====Users Login======")
user_name = input("Enter the users_name:")
user_id = input("Enter your user id :")

#============================================================================================


# ATM MENU ===================================================================================

while True:
    print("====ATM MENU====")
    print("1.Deposit Money")
    print("2.Withdraw Money")
    print("3.Check Balance")
    print("4.Transcation History")
    print("5.Exit")

    choice = input("Enter Your choice(1-5):")

    if choice == "1":
        deposit_money()


    elif choice == "2":
        withdraw_()

    elif choice == "3":
        check_balance()

    elif choice =="4":
        add_transaction(filename, 1, 100.50, "Deposit")
        view_transactions(filename)



    elif choice == "5":
        print("Thank you for using this mini banking system!.")
        exit()
        break
    else:
        print("Enter the one to five numbers only!.")



