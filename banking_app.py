
import os
import random
 

# USER_FILE = "User.txt"
# CUSTOMER_FILE = "Customer.txt"
# ACCOUNT_FILE = "Account.txt"
# TRANSACTION_HISTORY_FILE ="Transaction_History.txt"

# Create Account Function===========================================================================================

def create_account():
    print("======Customer Creation=====")
    customer_name = input("Enter your name:")
    customer_address = input("Enter your address:") 
    customer_phone_no = int(input("Enter your phone number:"))
    intial_balance = float(input("Enter the intial balance:$"))
    customer_NIC_no = int(input("Enter your N.I.C.No:"))
    return[customer_name,customer_address,customer_phone_no,intial_balance,customer_NIC_no]
   
        

#Fuction for Auto account number creation==========================================================================

def auto_account_number():
    return str(random.randint(2000, 12000))
    

def customer_id():
    existing = read_file(User.txt)
    return f"C_{3000 + len(existing) + 1}"
    

def user_id():
    existing = read_file(Customer.txt)
    return f"U_{5000 + len(existing) + 1}"
    


# Banking Files====================================================================================================

def file_creation(account_creation):
    with open("User.txt", "a") as user_info:
        user_info.write(f"{auto_account_number()} /**/ {user_id()} /**/ {account_cration[0]} /**/ {account_creation[1]} /**/{account_creation[2]} /**/ {account_creation[4]}\n")

    with open("Customer.txt", "a") as customer_info:
        customer_info.write(f"{auto_account_number()} /**/ {customer_id()} /**/ {account_creation[3]}\n")

    with open ("Account.txt","a") as acconut_info:
        acconut_info.write(f"{auto_account_number()} /**/ {account_creation[3]} \n")
    
    # with open ("Transaction_History.txt","w") as transaction_info:
    #     transaction_info.write(f"{account_creation[]}")
    
    auto_account_number()
    Customer_id()
    user_id()
#=================================================================================================================
def read_file(USER_FILE):

    with open("User.txt", "r") as user_info:
        user_info.write(f"{auto_account_number()} /**/ {user_id()} /**/ {account_cration[0]} /**/ {account_creation[1]} /**/{account_creation[2]} /**/ {account_creation[4]}\n")

def read_file(CUSTOMER_FILE):
    with open("Customer.txt", "r") as customer_info:
        customer_info.write(f"{auto_account_number()} /**/ {customer_id()} /**/ {account_creation[3]}\n")


# Deposit Money Function================================================================================================

def deposit_money():
    try:
        deposit = float(input("Enter amount to deposit: $"))
        if deposit <= 0:
            print("Enter  the positive numbers only!.")  
        else:    
            initial_balances[selected_account] += deposit
            print(f"Deposit successful. New balance: ${intial_balances[selected_account]}")

    except ValueError:
        print("Enter the numbers only!")
#============================================================================================================================

# Withdraw Money Function ====================================================================================================

def withdraw_money(): 
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

# def transaction_history():


# =============================================================================================================================


#Admin Login =======================================================================

correct_admin_name = "Admin"
correct_admin_password = "admin@123**" 
max_attempts = 3
attempts = 0

while attempts < max_attempts :
    print("======Admin Login======")
    admin_name = input("Enter the admin name:")
    admin_password = input("Enter the admin password: ")
    
    if admin_name == correct_admin_name and admin_password == correct_admin_password:
        print("Login Success Full!")
        break

    else:
        attempts += 1
        remaining = max_attempts - attempts
        print(f"Invalid Information.{remaining}attempt(s) left.")


if attempts == max_attempts:
        print("Too many failed attempts.Exiting program.")
        exit()
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
        data_save = file_creation(account_creation)
        print("Account Creation Success full!")
         
    elif choice == "2":
        deposit_money()

    elif choice == "3":
        withdraw_money()

    elif choice == "4":
        check_balance()

    elif choice =="5":
        transaction_history()

    elif choice == "6":
        print("Thank you for using this mini banking system!.")
        exit()
        break
    else:
        print("Enter the one to six numbers only!.")


#=========================================================================================


# Users Login ==============================================================================
print("/n=====Users Login======/n")
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
        transaction_history()

    elif choice == "5":
        print("Thank you for using this mini banking system!.")
        exit()
        break
    else:
        print("Enter the one to five numbers only!.")



