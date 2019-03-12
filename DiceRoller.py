"""Imports"""
###############################################################################
import random
###############################################################################


"""The Class"""
###############################################################################
class Dice(object):

    """The Functions"""
    ###########################################################################
    def __init__(self, min, max):
        self.min= min
        self.max = max

    ###########################################################################
    def welcome(self):
        print('\n\nWELCOME TO THE DICE ROLLER!')
        print('The default range of the dice is set from 1-6. \n')

    ###########################################################################
    def setDiceRange(self):
        statement = "Do you want to set your own dice range? Enter [yes] or [no]\n"
        Yesresult = "Setting your own range!"
        noResult = "Going with the previous set range then"

        return self.continuer(statement, Yesresult, noResult)

    ###########################################################################
    def diceRange(self):
        print('Set the range of your dice!')

        while True:

            while True:
                try:
                    self.min = int(input('Enter minimum range:\n'))
                    break
                except ValueError:
                    print("You didn't enter a number!")

            print('\nYour minimum range is:', self.min, '\n')

            while True:
                try:
                    self.max = int(input('Enter maximum range:\n'))
                    break
                except ValueError:
                    print("You didn't enter a number!")

            print('\nYour maximum range is:', self.max, '\n')

            if self.min > self.max:
                print("Your minimum range is bigger than your maximum range!")
                print("Set the min and max range again.")
            else:
                break

    ###########################################################################
    def rollDice(self):
        number = random.randint(self.min, self.max)
        print('\nYOUR RANDOM NUMBER WAS: ', number, '\n')

    ###########################################################################
    def rollAgain(self):
        statement = "Roll another dice? Enter [yes] or [no]\n"
        Yesresult = "Still going, woohoo!"
        noResult = "Aww, sad :("

        return self.continuer(statement, Yesresult, noResult)

    ###########################################################################
    def farewell(self):
        print('Farewell for now!')

    ###########################################################################
    def continuer(self, statement, Yesresult, noResult):
        while True:

            yesno = input(statement)

            if yesno.lower() == 'yes':
                print(Yesresult, '\n')
                return True
                break

            elif yesno.lower() == 'no':
                print(noResult, '\n')
                return False
                break

            else:
                print('Invalid input, try again')

###############################################################################

"""Main Application"""
###############################################################################
def main():
    p1 = Dice(1, 6)
    p1.welcome()
    while True:
        setDice = p1.setDiceRange()
        if setDice == True:
            p1.diceRange()
        p1.rollDice()
        reroll = p1.rollAgain()
        if reroll == False:
            p1.farewell()
            break

###############################################################################

"""Runnable"""
###############################################################################
main()
