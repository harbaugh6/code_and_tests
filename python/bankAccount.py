class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
  
  def __repr__(self):
    return "%s's account.  Balance: $%.2f" % (self.name, self.balance)
  
  def show_balance(self):
    print("The balance is $%.2f" % (self.balance))

  def deposit(self, amount):
    if amount <= 0:
      print("Cannot deposit $0 amount")
      return
    else:
      print("You have deposited $%.2f" % (amount))
      self.balance += amount
      self.show_balance()
    
  def withdraw(self, amount):
    if amount > self.balance:
      print("The amount is greater than the available balance")
      return
    else:
      print("You have withdrawn $%.2f" % (amount))
      self.balance -= amount
      self.show_balance()

my_account = BankAccount("Kyle")

print(my_account)
print(my_account.show_balance())
my_account.deposit(2000)
my_account.withdraw(1000)
my_account.deposit(350.55)
my_account.withdraw(177.94)
print(my_account)