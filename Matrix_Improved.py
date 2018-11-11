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
                Matrix.main_matrix_list[x].append(mat_val)
        
        #For each value in the final list, join it in a string with a comma.
        for r in Matrix.main_matrix_list: 
            print(', '.join(str(x) for x in r))

        Matrix.num_of_matricies += 1


matrix_to_add = Matrix(2,3)
print(Matrix.main_matrix_list)
print(Matrix.num_of_matricies)

            

