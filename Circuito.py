#-*- coding : utf-8 -*-

#Coded ----------: Python3.9.0
#Author --------: Stephano Bravo
#Git Repository : https://github.com/Superlasek/Circuit-Calc--OHM-LAW-

import time, math, os
import Calcsimple as s

_Parallel = s.Circuito_Paralelo()
_Serie = s.Serie()
circuit = 0

def sum_resistors(type):
    if  type == 1:
        circuit = _Parallel
    else:
        circuit = _Serie
    
    added_resistors = int(input("Resistors to add: "))
    for i in range(added_resistors):
        circuit.__add__(int(input("Add the resistor: ")))
    print(circuit.__RT__())

# Simple calc
def simple():
    print("\n_________________")
    print("   Simple Calc")
    print("_________________")
    while True:
        print("\nType of circuit: ")
        print("1 | Series")
        print("2 | Parallel")
        choice = get_number("\nEnter your choice: ")
        if choice == 1:
            print("\nSeries")
            sum_resistors(1)
            print("\n...")
            #Clear terminal screen
            os.system('cls' if os.name == 'nt' else 'clear')
            circuit = _Serie

            break


#TODO: For advanced calcs
def advanced():
    pass


#!TESTING
# Get the user input for validate that the input is a number
def get_number(prompt):
    while True:
        try:
            # Return the input as an integer
            return int(input(prompt))
        except ValueError:
            print("Please enter a number")


# Main function...
def main():
    print("""\n
 ██████╗ ██╗  ██╗███╗   ███╗█╗ ███████╗   ██████╗ █████╗ ██╗      ██████╗
██╔═══██╗██║  ██║████╗ ████║╚╝ ██╔════╝  ██╔════╝██╔══██╗██║     ██╔════╝
██║   ██║███████║██╔████╔██║   ███████╗  ██║     ███████║██║     ██║     
██║   ██║██╔══██║██║╚██╔╝██║   ╚════██║  ██║     ██╔══██║██║     ██║     
╚██████╔╝██║  ██║██║ ╚═╝ ██║   ███████║  ╚██████╗██║  ██║███████╗╚██████╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝   ╚══════╝   ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝                                                     
    \n""")
    while True:
        while True:
            print("1 | Simple Calculations")
            print("2 | Advanced Calculations")

            choice = get_number("\nEnter your choice: ")
            if choice == 1:
                print("\nEntering Simple Calculations mode...")
                time.sleep(0.5)
                print("\n...")
                #Clear terminal screen
                os.system('cls' if os.name == 'nt' else 'clear')
                simple()
                break
            elif choice == 2:
                print("\nAdvanced")
                break


if __name__ == '__main__':
    main()