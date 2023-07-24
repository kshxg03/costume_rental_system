from functions import *


def main_function():
    
    Input = False

    while Input == False:
        try:
            Input = int(input('Enter an option: '))
        except:
            print()
            print("Please enter values from above options only!!!")
            print()
        if Input == 1: 
            rent_costume()
                
        elif Input == 2:
            return_costume()                    
          
        elif Input == 3:
            exit_system()
            break

title()
options()
main_function()

            



