class Bank_Account:
  def_init_(self):
  self.balance=0
  print("hello!!!welcome to the Deposit& withdrawal Machine")
  def deposit(self):
    amount=float (input("enter amount to be deposited: "))
    self.balance +=amount 
    print("/n Amount
deposited:", amount")
Def withdraw(self):
amoun=float(input("enter amount to be withdrawn: "))
if self.balance>=amount:
self.balance-=amount
print("/n you withdrew:", amount)
else:
print("/n Insufficient balance")
def display(self):
print.("/n Net Available Balance=", self.balance)
s=Bank_Account()
s.deposit()
s.withdraw()
s. display()



      