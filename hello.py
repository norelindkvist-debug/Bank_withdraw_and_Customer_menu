bank_account = 10000

while True:
    card_code = int(input("Welcome to Swedbank, please insert your card and type in your 4 digit code: "))
    
    if card_code == 1234: # if you type in code 1234 you will get this message under
        print(f"Succsessful, you have {bank_account} SEK.") 
        break # break is so that the messedge don't repeat itself you will continue from the next loop
    else: 
        print("Wrong code please try again.") 
        # if you type in the wrong code it will restart again until you put in the right code

while True:
    amount = int(input("Amount to withdraw: "))

    if amount > bank_account:
        print(f"You can't withdraw {amount}, you can withdraw a maximum of {bank_account}") 
        # if you try to take out more money than u have you will get an error messedge and need to type in a new value

    else:
        bank_account -= amount
        print(f"You have withdrawn {amount}, you have {bank_account} left on your account")
        break 
    # when u have typed in an amount that isn't more than you have you will get this messedge 
    # break is there to continue with the code that comes next, if break is not here u will continue forever

answer = input("Would you like a receipt? (yes/no): ").lower() 
# .lower() so you can type yes however you want and the code will still function if you don't have this command you will get the else statement even if you answer Yes. You need to answer exactly yes to get to the if statement 
if answer == "yes":
    print("Your receipt is printed, Thank you")

else: 
    print("Thank you for being eco friendly!")
    

    