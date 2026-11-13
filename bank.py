class BankAccount:
    def __init__(self,acc_no,name,acc_type,balance=0):
        self.acc_no=acc_no
        self.name=name
        self.acc_type=acc_type
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposited{amount}.New balance: {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
            print(f"withdrew{amount}.New balance: {self.balance}")
acc=BankAccount(101,"Anjali","Savings",5000)
acc.deposit(2000)
acc.withdraw(1000)