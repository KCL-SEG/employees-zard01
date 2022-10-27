"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class _Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

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



    def setCommissionType(self, type):
      self.commissionType = type;

    def setCommissionContracts(self, numContr, perContr):
      self.numContracts=numContr
      self.perContract=perContr

    def setBonusPay(self, bPay):
      self.bonusPay=bPay

    def setHours(self, num):
      self.hours=num

    def set_pay(self):
      if self.contract=="hourly":
        self.totalPay=self.pay*self.hours
      elif self.contract=="monthly":
        self.totalPay=self.pay
      else:
        print("Invalid contract type")
      if self.hasCommission:
        if self.commissionType == "contract":
          self.totalPay+=self.numContracts*self.perContract
        elif self.commissionType=='bonus':
          self.totalPay+=self.bonusPay
        else:
          print("Invalid commission type")

    def get_pay(self):
      self.set_pay()
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


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = _Employee('Billie')
billie = Employee('Billie', 'monthly',4000, False)


# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = _Employee('Charlie')
charlie = Employee('Charlie', 'hourly',25, False)
charlie.setHours(100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = _Employee('Renee')
renee = Employee('Renee', 'monthly',3000, True)
renee.setCommissionType('contract')
renee.setCommissionContracts(4,200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = _Employee('Jan')
jan = Employee('Jan','hourly',25,True)
jan.setHours(150)
jan.setCommissionType('contract')
jan.setCommissionContracts(3,220)



# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = _Employee('Robbie')
robbie = Employee('Robbie','monthly',2000,True)
robbie.setCommissionType('bonus')
robbie.setBonusPay(1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = _Employee('Ariel')
ariel = Employee('Ariel','hourly',30,True)
ariel.setHours(120)
ariel.setCommissionType('bonus')
ariel.setBonusPay(600)
