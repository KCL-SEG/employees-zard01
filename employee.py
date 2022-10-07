"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract,pay, hasCommission):
      self.name = name
      self.contract = contract
      self.pay=pay
      self.hasCommission=hasCommission
      self.commissionType=""
      self.hours=0
      self.numContracts=0
      self.perContract=0
      self.bonusPay=0
      self.totalPay=0


     def set_pay(self):
         self.totalPay=self.pay


    def get_pay(self):
        self.set_pay()
        return self.totalPay


    def __str__(self):
        return self.name



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 'monthly',4000, False)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 'hourly',25, False)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 'monthly',3000, True)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan','hourly',25,True)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie','monthly',2000,True)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel','hourly',30,True)
