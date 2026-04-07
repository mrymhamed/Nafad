balanc = 500
username = 0
password = 0

while username !="" and password !="":
    username = input("Enter Your username: ")
    password = input("Enter Your password :")
    if username =='admin' and password =='1234' :
        print("Login successful!")
        
        servesic = input("Chose number of srevesic :1.check balance 2. Withdraw money 3. Deposit money  :")
        

        if servesic == "1":
            print("Your balance is ", balanc, "OMR")
            break

        elif servesic == "2":
            d = float(input("Enter amount of money you want to deposit or withdraw: "))
            if balanc >= d:
                n = 500 - d
                print("Your balance is:", n, "OMR")
                break
            else:
                print(f"Insufficient Balance \nYour current balance is: {balanc} OMR ")
                break

        else:
            d = float(input("Enter amount of money you want to deposit or withdraw: "))
            n = 500 + d
            print("Your balance is:", n, "OMR")
            break
    else :
        print("Access Denied")
        
    
        
        
        
        
        