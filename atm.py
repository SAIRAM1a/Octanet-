import time

print("Please insert your CARD")
time.sleep(1.5)

user_id = input("Enter your User ID: ")
password = 535
pin = int(input("Enter your PIN: "))

balance = 5000

trxn_history = []
if user_id == "21416" and pin == password:
    # ATM MENU

    while True:
        print(
            """ 
    1 == Balance
    2 == Withdraw
    3 == Deposit
    4 == Transfer
    5 == Transaction History
    6 == Quit 
    """
        )

        try:
            option = int(input("Please enter your choice:"))
        except:
            print("Invalid option")
            time.sleep(1)

        if option == 1:
            print("Your balance is: ", balance)
            print("===========================================================")
            time.sleep(1)

        if option == 2:
            while True:
                try:
                    withdraw_amt = int(
                        input("Please enter the amount to be withdrawn:")
                    )
                except:
                    print("Invalid amount")
                    time.sleep(1)
                    print("===========================================================")
                    continue

                if withdraw_amt > balance:
                    print("Insufficient balance")

                    print("Your current balance is: ", balance)
                    print("===========================================================")
                    time.sleep(1)
                else:
                    balance = balance - withdraw_amt
                    print(f"{withdraw_amt} is debited from your account.")

                    trxn_history.append(f"Withdraw: {withdraw_amt}")
                    print("Please collect your cash")

                    time.sleep(1)
                    print("Your current balance is: ", balance)
                    print("===========================================================")
                    time.sleep(1)
                    break

        if option == 3:
            while True:
                try:
                    deposit_amt = int(input("Please enter the amount to be deposited:"))
                except:
                    print("Invalid amount")
                    time.sleep(1)
                    print("===========================================================")
                    continue

                if deposit_amt < 0:
                    print("Invalid amount")
                    print("===========================================================")
                    time.sleep(1)
                else:
                    balance = balance + deposit_amt
                    trxn_history.append(f"Deposit: {deposit_amt}")
                    print(f"{deposit_amt} is credited to your account.")
                    print("Your current balance is: ", balance)
                    print("===========================================================")
                    time.sleep(1)
                    break
        if option == 4:
            while True:
                try:
                    transfer_amt=int(input("Please enter the amount to be transfer:"))
                except:
                    print("Invalid amount")
                    time.sleep(1)
                    print("===========================================================")
                if transfer_amt>balance:
                    print("Insufficient balance")
                    print("Your current balance is: ", balance)
                    print("===========================================================")
                    time.sleep(1)
                else:
                    transfer_act=int(input("enter id to transfer money:"))
                    balance=balance-transfer_amt
                    trxn_history.append(f"transferred: {transfer_amt} rupees to the Account ID {transfer_act}")
                    print(f"{transfer_amt} is debited from your account.")
                    print("Your current balance is: ", balance)
                    print("===========================================================")
                    time.sleep(1)
                    break
        if option == 5:
            print("Transaction History:")
            for trxn in trxn_history:
                print(trxn)
            print("===========================================================")

        if option == 6:
            print("Thanks for using the ATM")
            break

else:
    print("Invalid User ID or PIN")
