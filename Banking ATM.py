acnumber=int(input("accountnumber"))
global balance
balance=1000


if acnumber==45678:
    print("valid acc no")
    password=int(input("password"))
    if password==1234:
        print("login success")
        print()
        while True:
            print("1.balance")
            print("2.deposit")
            print("3.withdraw")
            print("4.exit")
            print()
            s=int(input("select input"))
            
            if s==1:
                
                print("balance is",balance)

            elif s==2:
                deposit=int(input("enter deposit amt "))
                balance=balance+deposit
                print('current balance',balance)

            elif s==3:
                withdraw=int(input("enter amt to withdraw "))
                balance=balance-withdraw
                print('current balance',balance)

            else:
                print('thank you')
                    
                break

            
    else:
        print("incorrect pswd")
       
else:
    print("invalid acc no")
    


    

