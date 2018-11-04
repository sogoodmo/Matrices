
'''
Hello. This is my first project where I will be attempting to create a library that can be used to
find the inverse of a matrix, find the determantes of a matrix, and create a matrix with given numbers. 

Start Date: 4/10/2018
Author: Mohamed Boudjillouli
'''
class Matrices:
    #Creating a matrix given that the user has given me some values.

    def Create_Matrix():
        while True:
            try:
                Column = int(input("Enter the amount of columns in your matrix: "))
            except ValueError:
                print("Error: Enter only whole numbers")
            else:
                break

        while True:
            try:
                Row = int(input("Enter the amount of rows in your matrix: "))
            except ValueError:
                print("Error: Enter only whole numbers")
            else:
                break
        Matrix_A = [[]]
        C_Value_List = []
        for i in range(Column):
            C_Value = int(input("Enter the values for the columns of your matrix in order: "))
            C_Value_List.append(C_Value)
            Matrix_A.append(C_Value_List)
            print(Matrix_A)
            for o in range(Row):
                R_Value = int(input("Enter the values for the rows for your matrix in order: "))
                Matrix_A[len(Matrix_A)-1].append(R_Value)
                print(Matrix_A)




        

    Create_Matrix()




