"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
      self.name = name
      self.contract = ''
      self.pay=0
      self.hasCommission=False
      self.commissionType=""
      self.hours=0
      self.numContracts=0
      self.perContract=0
      self.bonusPay=0
      self.totalPay=0

    def set_contract(self, contract):
      self.contract=contract

    def set_pay(self, pay):
      self.pay= pay

    def set_hasCommission(self, val):
      self.hasCommission=val

    def set_commissionType(self, type):
      self.commissionType = type

    def set_commission_contracts(self, numContr, perContr):
      self.numContracts=numContr
      self.perContract=perContr

    def set_bonusPay(self, bPay):
      self.bonusPay=bPay

    def set_hours(self, num):
      self.hours=num

      '''

    def calculate_pay_hourly():
      self.totalPay=self.pay*self.hours

    def calculate_pay_monthly():
      self.totalPay=self.pay

    def calculate_pay_contract():
      self.totalPay+=self.numContracts*self.perContract

    def calculate_pay_bonus():
      self.totalPay+=self.bonusPay

      '''

    def set_totalPay(self):
      if self.contract=="hourly":
        #calculate_pay_hourly()
        self.totalPay=self.pay*self.hours
      elif self.contract=="monthly":
        self.totalPay=self.pay
      else:
        print("Invalid contract type")
      if self.hasCommission:
        if self.commissionType == "contract":
          #calculate_pay_contract()
          self.totalPay+=self.numContracts*self.perContract
        elif self.commissionType=='bonus':
          #calculate_pay_bonus()
          self.totalPay+=self.bonusPay
        else:
          print("Invalid commission type")

    def get_pay(self):
      self.set_totalPay()
      return self.totalPay

    def __str__(self):
      returnString = "{} works on a".format(self.name)
      if self.contract == "monthly":
        returnString+=" monthly salary of {}".format(self.pay)
      elif self.contract=="hourly":
        returnString+=" contract of {} hours at {}/hour".format(self.hours, self.pay)

      if self.hasCommission:
        if self.commissionType == "contract":
          returnString+=" and receives a commission for {} contract(s) at {}/contract".format(self.numContracts,self.perContract)
        elif self.commissionType == 'bonus':
          returnString+=" and receives a bonus commission of {}".format(self.bonusPay)

      returnString+=". Their total pay is {}.".format(self.totalPay)
      return returnString

#name, contract,pay, hasCommission

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')
billie.set_contract('monthly')
billie.set_pay(4000)
billie.set_hasCommission(False)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')
charlie.set_contract('hourly')
charlie.set_pay(25)
charlie.set_hasCommission(False)
charlie.set_hours(100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')
renee.set_contract('monthly')
renee.set_pay(3000)
renee.set_hasCommission(True)
renee.set_commissionType('contract')
renee.set_commission_contracts(4,200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')
jan.set_contract('hourly')
jan.set_pay(25)
jan.set_hasCommission(True)
jan.set_hours(150)
jan.set_commissionType('contract')
jan.set_commission_contracts(3,220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')
robbie.set_contract('monthly')
robbie.set_pay(2000)
robbie.set_hasCommission(True)
robbie.set_commissionType('bonus')
robbie.set_bonusPay(1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
ariel.set_contract('hourly')
ariel.set_pay(30) 
ariel.set_hasCommission(True)
ariel.set_hours(120)
ariel.set_commissionType('bonus')
ariel.set_bonusPay(600)