import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

#function to create connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        return connection

    except mysql.connector.Error as error:
        print("database connection error:", error)
        return None


#function to create account
def create_account():
    connection=create_connection()
    cursor=connection.cursor()
    account_holder=input("enter the account holder name:")
    balance=int(input("enter the opening balance:"))
    query="""insert into accounts(account_holder,balance)
    values(%s,%s)"""
    cursor.execute(query,(account_holder,balance))
    account_id=cursor.lastrowid
    account_number=f"ACC{1000+account_id}"
    update_query="""
    update accounts
    set account_number=%s
    where account_id=%s
    """
    cursor.execute(update_query,(account_number,account_id))
    connection.commit()
    print("account created successfully.")
    print(f"your account number:{account_number}")
    cursor.close()
    connection.close()

#function to deposit
def deposit():
    connection=create_connection()
    cursor=connection.cursor()
    account_number=input("enter your account number:")
    try:
        connection.start_transaction()
        cursor.execute("select balance from accounts where account_number=%s",(account_number,))
        account=cursor.fetchone()
        if account:
            balance=account[0]
            amount=int(input("enter amount to deposit:"))
            new_balance=balance+amount
            cursor.execute("UPDATE accounts SET balance = %s WHERE account_number = %s",(new_balance, account_number))
            query=""" insert into transactions(account_number,transaction_type,amount)
            values(%s,%s,%s)"""
            cursor.execute(query,(account_number,"deposit",amount))
            connection.commit()
            print("Amount deposited successfully.")
        else:
            print("Account not found.")     
    except mysql.connector.Error as error:
        connection.rollback()
        print("Transaction failed:", error)     
    cursor.close()
    connection.close()


#function to withdraw
def withdraw():
    connection=create_connection()
    cursor=connection.cursor()
    account_number=input("enter your account number:")
    try:
        connection.start_transaction()
        cursor.execute("select balance from accounts where account_number=%s",(account_number,))
        account=cursor.fetchone()
        if account:
            balance=account[0]
            amount=int(input("enter amount to withdraw:"))
            if amount>balance:
                print("insufficient balance.")
            else:
                new_balance=balance-amount
                cursor.execute("UPDATE accounts SET balance = %s WHERE account_number = %s",(new_balance, account_number))
                query=""" insert into transactions(account_number,transaction_type,amount)
                values(%s,%s,%s)"""
                cursor.execute(query,(account_number,"withdraw",amount))
                connection.commit()
                print("Amount withdrawn successfully.")
        else:
            print("account not found.") 
                      
    except:
        connection.rollback()   
        print("transaction failed.")
    cursor.close()
    connection.close()    

#function to check balance
def check_balance():
    connection=create_connection()
    cursor=connection.cursor()
    account_number=input("enter account number:")
    cursor.execute("select account_number,account_holder,balance from accounts where account_number=%s",(account_number,))
    account=cursor.fetchone()
    if account:
        print("\n-------- ACCOUNT DETAILS --------")
        print(f"Account Number : {account[0]}")
        print(f"Account Holder : {account[1]}")
        print(f"Balance        : {account[2]}")
    else:
        print("Account not found.")
    cursor.close()
    connection.close()

#function to transaction history
def transaction_history():
    connection = create_connection()
    cursor = connection.cursor()
    account_number = input("enter account number:")
    cursor.execute( """select transaction_id,transaction_type,amount,transaction_date from transactions where account_number=%s order by transaction_date""",(account_number,))
    transactions = cursor.fetchall()
    if transactions:
        print("\n --------- TRANSACTION HISTORY --------")
        print(f"{'ID':<8}{'type':12}{'amount':12}{'date'}")
        for transaction in transactions:
            transaction_id=transaction[0]
            transaction_type=transaction[1]
            amount=transaction[2]
            transaction_date=transaction[3]
            print(f"{transaction_id:<8}{transaction_type:<12}{amount:<12}{transaction_date}")
    else:
        print("No transactions found") 
    cursor.close()
    connection.close()

#main menu
while True:
    print("\n======= BANK MANAGEMENT SYSTEM =========")
    print("1.create account")
    print("2.deposit amount")
    print("3.withdraw amount")
    print("4.check balance")
    print("5.transaction history")
    print("6.exit")
    print("=========================================")
    choice=input("choose your choice:")
    if choice=="1":
        create_account()
    elif choice=="2":
        deposit()
    elif choice=="3":
        withdraw()
    elif choice=="4":
        check_balance()
    elif choice=="5":
        transaction_history()
    elif choice=="6":
        print("exit.")
        break
    else:
        print("invalid choice.")                        


    
               
    





    
    

