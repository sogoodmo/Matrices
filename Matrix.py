
'''
Hello. This is my first project where I will be attempting to create a library that can be used to
find the inverse of a matrix, find the determantes of a matrix, and create a matrix with given numbers. 

Start Date: 4/10/2018
Author: Mohamed Boudjillouli
'''

#Creating a matrix given that the user has given me some values.
def Create_Matrix(Column, Row):
    Main_Matrix = []
    #Creating row amount of empty 2d lists 
    for x in range(Row):
        Main_Matrix.append([])
    #Entering value of each matrix one at a time 
        for i in range(Column):
            Mat_Val = input("Enter the value of your matrix at row " + str(x+1) + " and at column " + str(i+1) + ": ")
            while not Mat_Val.isdigit() :
                  Mat_Val = input("Error: Invalid Matrix\nEnter the value of your matrix at row " + str(x+1) + " and at column " + str(i+1) + ": ")
            Mat_Val = int(Mat_Val)
            Main_Matrix[x].append(Mat_Val)     
        print(Main_Matrix[x])

Create_Matrix(2,2)     
    