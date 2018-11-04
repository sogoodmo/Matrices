'''
Hello. This is my first project where I will be attempting to create a library that can be used to
find the inverse of a matrix, find the determantes of a matrix and calculate the dimensions of a given matrix

Start Date: 4/10/2018
Author: Mohamed Boudjillouli
'''
import os
import time
import random 
import Matrix

print("This program will allow you to calculate the dimensions of a matrix, determinates of matricies and inverse of a matrix")
def main()
    run_program = input("Press enter to continue...") 
    num_of_matrix = 0
    while num_of_matrix == 0:
        Matrix.Creat_Matrix()







    #Asking user if he wants to run the program again
    again = str(input("Do you want to run this program again? Y/N: ")).lower()
    if again == "no" or again == "n":
        print("Shutting Down...")
        time.sleep(3)
        quit()
    if again == "yes" or again == "y":
        main()
    #If the input isnt "Yes, Y, No or N" ask the user to input a valid input.   
    while (again != "y") or (again != "yes") or (again != "n") or (again != "no"):
        again = str(input("Error: Invalid input\nDo you want to run this program again? Y/N: ")).lower()
        if again == "no" or again == "n":
            print("Shutting Down...")
            time.sleep(3)
            quit()
        if again == "yes" or again == "y":
            main()
main()