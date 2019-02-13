import os
import sys
def product_Menu():
    """Menu for slecting Fuel product type, returns a value from dictionary 'options'."""
    os.system('clear')
    print(':-----------:-----------: FUEL TYPES AVAILABLE :-----------:-----------:\n')
    print('1:91 Petrol, 2:95 Unleaded, 3:98 unleaded, 4:Diesel, 5:LPG, 6:E85, 7:Quit')
    while True:
        Base_url = 'https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?'
        options = {1:1, 2:2,
                3:6, 4:4,
                5:5, 6:10,
                7:7, 8:8}
        try:
            piked = int(input('\n\nPlease select which fuel type you desire: '))
        except ValueError:
            print('Value Error: Please select 1 - 7')
            continue
        chosen = options.get(piked)
        if chosen == 7:
            sys.exit(0)
        elif chosen == None:
            print('Value Error: Please select 1 - 7')
            continue
        return chosen
