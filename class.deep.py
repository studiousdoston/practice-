''' CLASS deep dive
  1. ENCAPSULATION
  2. INHERITANCE
  3. POLYMORPHISM
'''

print(" ===== ENCAPSULAION =====")
'''
C++ , JAVA      -> public,   private,   protected
PHP TypeScript  -> public,   private,   protected
PYTHON          -> public, __private,   _protected📌
'''


class Account():
  # state
  description = " The class is used to create new bank accounts"
  # constructor
  def __init__(self, owner, amount):
    self.__owner = owner
    self.__amount = amount

  # method
  def get_balance(self):
    print(f"The owner {self.__owner} has {self.__amount}$")

  def deposit(self,amount):
    print("deposit:", amount )
    self.__amount += amount
    
  def withdraw(self, amount):
    print("withdraw:" ,amount)
    self.__amount -= amount

  @property
  def holder(self):
    return self.__owner
  
  @holder.setter
  def holder(self, new_owner):
    self.__owner = new_owner

  
  
  def change_ownership(self,new_owner):
    print("change_ownership:", new_owner)
    self.__owner  = new_owner



my_account = Account("Deen", 1000)
my_account.get_balance()

print("---------")
my_account.deposit(3500)
my_account.withdraw(400)
my_account.get_balance()

print("---------")
my_account.amount = 1000000  # not executed
my_account.amount = 10000000  # not executed
my_account.get_balance()

print("---------")
#print(my_account.owner) 
try:
  result = my_account.__amount
  print("result:", result)
except Exception as err:
  print("No target state found:" , err)

# getter & setter
print("Previous owner: ",my_account.holder)  # Deen
# my_account.change_ownership("Joshua")
my_account.holder = "Joshua"

print("Current owner: ", my_account.holder)
