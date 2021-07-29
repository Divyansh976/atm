import random

class Atm(object):
    def __init__(self, pin_number, card_number):
        self.pin_number = pin_number
        self.card_number = card_number
    
    def atmActions(self):
        actionInput = input("Do you want to withdraw or you need balance enquiry: ")
        if(actionInput == "withdraw"):
            print("Cash withdrawl")
        if(actionInput == "balance enquiry"):
            print("This is your bank balance")
                
Atm1 = Atm( 798712318, 879854321 )
Atm1.atmActions()
print(Atm1)