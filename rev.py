from datetime import datetime


class Bank:

    def __init__(self,name,userId,phoneNumber):
        self.name=name
        self.userId=userId
        self.phoneNumber=phoneNumber
        self.balance=0
        self.loan=0
        self.loan_limit=40000
        self.transaction_fee=200
        self.interestRate_fee=0.5
        self.transactions=[]
    #  self.account=[]

    def deposit(self,amount):
        if amount<0:
            return f"Dear customer please Enter valid amount"
        else:
            self.balance+=amount
                
            return f"Hello{self.name}  with {self.userId}  your phoneNumber is  {self.phoneNumber} you have deposited{amount} and your balance is {self.balance}"
    def withdraw(self,amount):
        if amount<0:
            return f" Dear {self.name} Please enter valid amount"
        elif amount>self.balance:
            return f"Dear{self.name}  you can't withdraw , your balance is less than amount"

        else:
            amount<=self.balance
            amount+self.transaction_fee<=self.balance 
            self.balance-=amount+self.transaction_fee

            return f"Hello{self.name} with {self.userId} your phoneNumber is  {self.phoneNumber}  you have withdrawed{amount} and your balance is  {self.balance}" 
    def borrow(self,amount):  
        if amount<0:
            return f"Dear{self.name}   you can't borrow amount which is less than zero"
        elif amount>self.loan_limit:
            return f"Dear{self.name}   your expectations is beyond loan limit"
        #    elif self.loan>0:
        #        return f" Dear{self.name}  you have an existing loan, you should pay first"
        else:
            self.balance+=amount
            self.loan+=(amount*self.interestRate_fee)+amount
            transaction={f"amount":amount,"balance":self.balance,"narration":"you have borrowed","time":datetime.now()}
            self.transactions.append(transaction)
            return f"Hello{self.name}with you have borrowed successfully and your balance is  {self.balance} the payback amount will be{self.loan} " 

    def repayment(self,amount):

        interest = self.interestRate_fee * amount
        payable= amount+interest

        if amount<=0:
            return f"Dear {self.name}  enter valid amount"
        elif amount<payable:
            self.loan-=amount
            remains=self.loan-amount
            return f"Hello your outstanding loan is {remains}"  

        else:
        #  amount>payable

            excess=amount-payable
            self.balance+=excess
            self.loan=0
            transaction={f"amount":amount,"balance":self.balance,"narration":"you have repaid your loan","time":datetime.now()}
            self.transactions.append(transaction)
            return f"Hello {self.name} your have repaid your loan  your new balance is {self.balance}"

    def transfer(self,amount,account):
        transMoney=amount+self.transaction_fee
        if transMoney<0:
                return f" Please enter valid amount" 
        elif transMoney>self.balance:
                return f"Hello you have insufficient amount"    

        else:
                
                self.balance-=transMoney
                account.deposit(amount)
                transaction={"amount": amount,"balance":self.balance,"narration":"you have transfered money ","time":datetime.now()}
                self.transactions.append(transaction)
                return f"Hello you have successful transfered money{amount} to {account.name} and your new balance is {self.balance}"

    def  get_statement(self):
        for transaction in self. transactions:
            amount=transaction["amount"] 
            narration=transaction["narration"]   
            balance=transaction["balance"] 
            time=transaction["time"]   
            date=time.strftime("%D")
            print(f"{date}....{narration}.... {amount}... balance{balance}....{date}")

class MobileMoneyAccount(Bank): 
    def __init__(self, name, userId,phoneNumber,service_provider):
        Bank.__init__(self,name,userId,phoneNumber)
        self.service_provider=service_provider

    def buy_airtime(self,amount):
        try:
            amount+4
        except TypeError:
            return f"please enter amount in figures"
               
        if amount<0:
            return f"please enter valid amount"  
        elif amount>self.balance:
            return f"Hello you have insufficient balance"
        else:

             self.balance-=amount
             transaction={"amount":amount,"balance":self.balance,"narration":"you have bought airtime","time":datetime.now()}
             self.transactions.append(transaction)
             return f"Hello you have successful bought airtime{amount} and your new balance is{self.balance}"
            






      
