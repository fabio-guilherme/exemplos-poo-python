class Staff:
    def __init__ (self, pPosition, pName, pPay):
        #self.__position = pPosition
        self.__position = pPosition
        self.name = pName
        self.pay = pPay
        print('Creating Staff object')

    def __str__(self):
        return "Position = %s, Name = %s, Pay = %d" %(self.__position, self.name, self.pay)
    
    def calculatePay(self):
        prompt = '\nEnter number of hours worked for %s: ' %(self.name)
        hours = input(prompt)
        prompt = 'Enter the hourly rate for {}: '.format(self.name)
        hourlyRate = input(prompt)
        self.pay = int(hours)*int(hourlyRate)
        return self.pay

#'''
    @property
    def position(self):
        print("Getter Method")
        return self.__position

    @position.setter
    def position(self, value):
        if value == 'Manager' or value == 'Basic':
            self.__position = value
        else:
            print('Position is invalid. No changes made.')
#'''

'''
officeStaff1 = Staff('Basic', 'Yvonne', 0)

print(officeStaff1.name)
print(officeStaff1.position)

#change variable position 
officeStaff1.position = 'Manager' 
#print position again 
print(officeStaff1.position)

print(officeStaff1.pay)

officeStaff1.calculatePay()
print(officeStaff1.pay)

print(officeStaff1)
'''