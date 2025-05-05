# Create Account Function===========================================================================================


def create_account():
    customer_name = input("Enter your name:")
    customer_address = input("Enter your address:") 
    intial_balance = input("Enter the intial balance:$")
    return[customer_name,customer_address,intial_balance]
    

account_creation = create_account()
print(account_creation)

#==================================================================================================================

# function for User_creation=========================================================================================

with open ("user.txt","a") as file:
    file.write("account_creation[0]" + " " + "account_cretion[1]")     
print(account_creation.readlines())



#===================================================================================================================

# Deposit Money Function=============================================================================================

def deposit_money():
    deposit = input("Enter the deposit money:$")
     
    if deposit > 0:
        deposit += intial_balance
        print(f"Deposit Successfull. Now your balance is:${intial_balance}.")

    elif deposit < 0:
        print("Enter the positive numbers only!.")
    
    else:
        print ("Enter the numbers only!.")

#=======================================================================================================================  

# Withdarw Money Function================================================================================================

def withdraw_money():
    withdraw = input("Enter the withdraw money:$")
    if withdraw < intial_balance :
        withdraw -= intial_balance
        print(f"Withdraw Successfull. Now your balance is:${intial_balance}")
        
    elif withdraw > intial_balance: 
        print("Enter the correct money.")

    else:
        print ("Enter the numbers only!.")
        
#======================================================================================================================


# Check Balance Function==================================================================================================

def check_balance():
    check_balance = intial_balance
    print(f"Your balance is:$")

#========================================================================================================================    


#Transaction History Function============================================================================================

def transaction_history():


#=============================================================================================================================


# Admin Login =======================================================================

correct_admin_name = "Admin"
correct_admin_password = "admin@123**" 
max_attempts = 3
attempts = 0

while attempts < max_attempts :
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


# ATM MENU ===========================================================================

while True:

    print("====ATM MENU====")
    print("1.Create Account")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Check Balance")
    print("5.Transcation History")
    print("6.Exit")
    break
    choice = input("Enter Your choice(1-5):")

    if choice == "1":
        create_account()

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

    else:
        print("Enter the one to six numbers only!.")


#=========================================================================================


# Users Login ==============================================================================

users_name = input("Enter the users_name:")
users_id = 

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

    else:
        print("Enter the one to five numbers only!.")



