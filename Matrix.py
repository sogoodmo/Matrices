
'''
Hello. This is my first project where I will be attempting to create a library that can be used to
find the inverse of a matrix, find the determantes of a matrix, and create a matrix with given numbers. 

Start Date: 4/10/2018
Author: Mohamed Boudjillouli
'''
class Matrices:
    #Creating a matrix given that the user has given me some values.

    def Create_Matrix(Column, Row, Data):
        for x in range(Row):
            Main_Matrix.append([])
            for i in range(Column):
                Main_Matrix[x].append(Mat_Str[(Column*x)+i])
                print(i) 
        print(Main_Matrix)     