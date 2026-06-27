# Day 10 � Error Handling & Exceptions
# Date: July 03, 2026
#
# Learning Goals:
# TODO: Fill in what you learned today, code exercises, and notes.

import requests


try:
    response=requests.get("https://jsonplaceholder.typicode.com/users/1" ,timeout=5)
    response.raise_for_status()
except requests.exceptions.Timeout:
    print("Request timed out ⏳")
except requests.exceptions.ConnectionError:
    print("No Internet connection")
except requests.exceptions.HTTPError as e:
    print("Http Error Ocurred" , e)
except Exception as e:
    print("Unexpected Error",e)
else:
    data=response.json()
    print(f"Name: {data['name']}")
    print(f"Email: {data['email']}")
    print(f"Phone: {data['phone']}")
finally:
    print("APi Request Completed")



# class ATM:
#     def __init__(self):
#         self.balance=1000
        
    
#     def check_balance(self):
#         print(f'Your balance is {self.balance}')
#     def deposit(self,amount):
#         if amount<0:
#             raise ValueError("Deposit amount cannot be negative")
#         self.balance+=amount
#         print(f"Your balance has been increased by {amount} : Current balance: {self.balance}")
#     def withdraw(self,amount):
#         if amount<=0:
#             raise ValueError("Withdraw amount must be greater than zero")
#         if amount>self.balance:
#             raise ValueError("You have insufficent balance")
#         self.balance=self.balance-amount
#         print(f"your remaining balanace is {self.balance}")
    
    
    
# atm = ATM()


# while True:
#     print("\n--- ATM MENU ---")
#     print("1. Check Balance")
#     print("2. Deposit")
#     print("3. Withdraw")
#     print("4. Exit")
    
#     try:
#         choice=int(input("Choose an option: "))
        
#         if choice==1:
#             atm.check_balance()
#         elif choice==2:
#             try:
#                 amount=int(input("Enter Amount to deposit: "))
#             except ValueError:
#                  print("Enter a valid number")
#             else:
#                 atm.deposit(amount)
#         elif choice==3:
#             try:
#                 amount=int(input("Enter Amount to withdraw: "))
#             except ValueError:
#                 print("Enter a valid number")
#             else:
#                 atm.withdraw(amount)
#         elif choice==4:
#             print("THANK YOU FOR USING OUR ATM")
#             break
#     except ValueError as e:
#         print("Error:", e)
#     finally:
#         print("Transaction completed.\n")
        
        



