#Function 1:
#Creating a matrix with given rows, columns, and a list of values
def create_matrix(row,column,list_of_values):
    result_matrix = []

    for i in range(row):
        result_matrix.append([])
        for j in range(column):
            result_matrix[i].append(list_of_values[(column*i)+j])

    for k in result_matrix: 
       print(', '.join(str(i) for i in k))
    print('\n')

    return result_matrix

matrix_1 = create_matrix(2,2,[1,2,3,4])
matrix_2 = create_matrix(2,2,[1,2,3,4])

#Function 2:
#Addition with matricies returning a third matrix.
def add_matrix(matrix_1,matrix_2):
    addition_result_matrix = []

    for i in range(len(matrix_1)):
        addition_result_matrix.append([])
        for j in range(len(matrix_1[0])):
            addition_result_matrix[i].append(matrix_1[i][j]+matrix_2[i][j])

    return addition_result_matrix


#Function 3:
#Subtrasction with matricies returning 
def sub_matrix(matrix_1,matrix_2):
    subtraction_result_matrix = []

    for i in range(len(matrix_1)):
        subtraction_result_matrix.append([])
        for j in range(len(matrix_1[0])):
            subtraction_result_matrix[i].append(matrix_1[i][j]-matrix_2[i][j])

    return subtraction_result_matrix


#Function 4:
#Sclar multiplication of a matrix
def scalar_multi(matrix_1,scale_factor):
    scalar_multi_result_matrix = []

    for i in range(len(matrix_1)):                                              
        scalar_multi_result_matrix.append([])                                    
        for j in range(len(matrix_1[0])):                                      
            scalar_multi_result_matrix[i].append((matrix_1[i][j])*4)

    return scalar_multi_result_matrix


#Function 5:
#Multiplying matricies together
def matrix_multiply(matrix_1,matrix_2):
    multi_result_matrix = []

    matrix_1_row = len(matrix_1)
    matrix_2_column = len(matrix_2[0])

    for i in range(matrix_1_row):
        for j in range(matrix_2_column):
            element_value = 0
            for l in range(matrix_2_column):
                element_value += (int(str(matrix_1[i][l]))*int(str(matrix_2[l][j])))
            multi_result_matrix.append(element_value)
    print(multi_result_matrix)

matrix_multiply(matrix_1,matrix_2) 
        

