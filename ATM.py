class ATM:
    def __init__(self,acctype,no,bal):
        self.acctype=acctype
        self.no =no
        self.bal=bal
        
    def change_pin(self):  
        self.pin=int(input("Enter New PIN:"))
        print("New PIN set successfully...!")
        
    def deposite(self):
        self.deposite=int(input("enter amount to deposit:"))
        self.bal += self.deposite
        print("Deposite successfully....!")
        print("updated balance:",self.bal)
        
    def withdrawal(self):
        self.withdrawal=int(input("enter amount to withdrawal:"))
        
        if(self.withdrawal<=self.bal): 
            self.bal-=self.withdrawal 
            print("withdrawal successfully....!")
            print("updated balance:",self.bal)
        else:
            print("insuffitient amount")
            print("available balance in your account is :",self.bal)
            
detail=ATM("saving account",883011976751,5000)
detail.pin=123

chance=0
while chance<3:
    userpin=int(input("Enter PIN :-"))
    
    if userpin==detail.pin:
        print("account type  :",detail.acctype)
        print("account number:",detail.no)
        print("accoun balance:",detail.bal)
        
        print("1.change PIN ")
        print("2.deposite amount ")
        print("3.withdrawal amount ")
        print("4.exit ")
    
        choice=int(input("Enter your choice :  "))
        
        if choice==1:
            detail.change_pin()
            
        elif choice==2:
            detail.deposite()
            
        elif choice==3:
            detail.withdrawal()
            
        elif choice==4:
            print("THANK YOU FOR USING ATM......!")
            break
            
        else:
            print("invalid choice")
    else:
        chance+=1

        print("Try Again")
            
if chance==3:
    s="\U0001F600"
    print("your card id blocked")
    print("try again after 24 Hours",s)           

    
            
        
            

            
            
        

        
    
    

    
    
        
    
    