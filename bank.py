
from datetime import datetime
class Account:

    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        self.transaction_fee=20  
        self.balance=0
        self.loan=0
        self.loan_limit=50000
        self.transactions=[]
    def deposit(self,amount):
        try:
            amount+10
        except  TypeError : 
            return f"Please enter amount in figures"

        if amount<=0:
            print ("Please deposit a valid amount")
        else:
            self.balance+=amount
            transaction={"amount":amount,"balance":self.balance,"narration":"you deposited","time":datetime.now()}
            self.transactions.append(transaction)
            return f"Hello {self.name} you have deposited {amount} your new balance is {self.balance}"

    def borrow(self,amount):
        try:
            amount+10
        except TypeError:
            return f"Please enter amount in figures"   
        if amount>=self.loan_limit:
           return "you are not allowed to borrow"  
        elif amount<0:
            return "you can't borrow"   

        elif self.loan>0:
            return "You  have an existing loan"

    def get_statement(self):   
        for transaction in self.transactions:
            amount=transaction["amount"] 
            narration=transaction["narration"]   
            balance=transaction["balance"] 
            time=transaction["time"]   
            date=time.strftime("%D")

            print(f"{date}....{narration}.... {amount}... balance{balance}....{date}")


    def repayment (self,amount):

        try:
            amount+4
        except TypeError:
            return f"Please enter amount in figures"   
        if amount<0: 
            return "enter valid amount"
        elif amount>self.loan:
            remainder=amount-self.loan
            self.balance+=remainder
            transaction={"amount":amount,"balance":self.balance,"narration":"repayment","time":datetime.now()}
            self.transactions.append(transaction)
            return f"Hello, you have repayed {amount} , your remainder{remainder} has been added to your {self.balance}"
        else: 
            self.balance+=amount  
            transaction={"amount":amount,"balance":self.balance,"narration":"you have repay","time":datetime.now()}
            self.transactions.append(transaction)
            return f"Hello, you have repayed {amount}, your new balance is{self.balance}"

    def transfer(self,amount): 
        try:
            amount+2
        except TypeError:
            return f"Please enter amount in figures"
        fee=amount*0.05
        total=amount+fee
        if total>self.balance:
            return f"Your balance is{self.balance} you need {total}  in order to transfer{amount}"        

        else:
            self.balance=total
            Account.deposit(amount)
            return f"you have transfered money successful"

class MobileMoneyAccount(Account): 
    def  __init__(self,name,phone,service_provider):
             Account.__init__( self,name,phone)
             self.service_provider=service_provider
    def buy_airtime(self,amount):
        try:
            amount+1
        except TypeError:
            return f"Please Enter amount in figures"   
        if  amount<0:
            return f"Please enter valid amount"
        elif amount>self.balance: 
            return f"You have insufficient amount" 
        else: 
            
            self.balance -=amount
            transaction={"amount":amount,"balance":self.balance,"narration":"you have bought airtime","time":datetime.now()}      
            self.transactions.append(transaction)
            return f"Hello you have bought airtime{amount} your new balance is{self.balance}"