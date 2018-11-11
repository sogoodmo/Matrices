'''Column = input('Enter the amount of columns in your matrix: ')
while not Column.isdigit():
    Column = input('Error: Invalid Input\nEnter the amount of columns in your matrix: ')
''' 



#Entering data for matrix. Ensuring its the correct amount of data.
'''Matrix_Val = str(input("Enter the values of your matrix in order. Seperate each value with a comma\n"))
        Matrix_Val = Matrix_Val.replace(' ','')
        Mat_List_Check = Matrix_Val.replace(',','')

        while len(Mat_List_Check) != (Column*Row):
            Matrix_Val = str(input("Error: Invalid Matrix\nEnter the values of your matrix in order. Seperate each value with a comma\n"))
            Matrix_Val = Matrix_Val.replace(' ','')
            Mat_List_Check = Matrix_Val.replace(',','')
        Mat_List = list(Mat_List_Check)
        Mat_Str = Mat_List_Check'''


'''
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
            '''
'''
class Matrix():
    num_of_matricies = 0
    main_matrix_list = []

    def __init__(self,column,row):
        self.column = column
        self.row = row
        Matrix.create_matrix(self,column,row)

    def create_matrix(self,column, row): #To use this function. Do Matrix.Create_Matrix(Column, Row)
        
        #Creating row amount of empty 2d lists 
        for x in range(self.row):
            Matrix.main_matrix_list.append([])

        #Entering value of each matrix one at a time, repeat this Row amount of times
            for i in range(self.column):
                mat_val = input('Enter the value of your matrix at row ' + str(x+1) + ' and at column ' + str(i+1) + ': ')
                while not mat_val.isdigit() :
                    mat_val = input('Error: Invalid Matrix\nEnter the value of your matrix at row ' + str(x+1) + ' and at column ' + str(i+1) + ': ')
                mat_val = int(mat_val)
                if Matrix.num_of_matricies >= 1:
                    Matrix.main_matrix_list[Matrix.num_of_matricies + x + 1].append(mat_val)
                else:
                    Matrix.main_matrix_list[x].append(mat_val)
        
        #For each value in the final list, join it in a string with a comma.
        for r in Matrix.main_matrix_list: 
            print(', '.join(str(x) for x in r))

        Matrix.num_of_matricies += 1


Matrix(2,2)
Matrix(2,2)
Matrix(2,2)
print(Matrix.main_matrix_list)

'''
    