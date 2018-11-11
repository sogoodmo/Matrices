#Function 1:
#Creating a matrix with given rows, columns, and a list of values
def create_matrix(row,column,list_of_values):
    result_matrix = []

    for x in range(row):
        result_matrix.append([])
        for y in range(column):
            result_matrix[x].append(list_of_values[(column*x)+y])

    for z in result_matrix: 
       print(', '.join(str(x) for x in z))

    return result_matrix

matrix_1 = create_matrix(2,2,[1,2,3,4])
matrix_2 = create_matrix(2,2,[1,2,3,4])

#Function 2:
#Addition with matricies returning a third matrix.
def add_matrix(matrix_1,matrix_2):
    addition_result_matrix = []

    for t in range(len(matrix_1)):
        addition_result_matrix.append([])
        for u in range(len(matrix_1[0])):
            addition_result_matrix[t].append(matrix_1[t][u]+matrix_2[t][u])

    return addition_result_matrix

print(add_matrix(matrix_1,matrix_2))

#Function 3:
#Subtrasction with matricies returning 
def sub_matrix(matrix_1,matrix_2):
    subtraction_result_matrix = []

    for w in range(len(matrix_1)):
        subtraction_result_matrix.append([])
        for v in range(len(matrix_1[0])):
            subtraction_result_matrix[w].append(matrix_1[w][v]-matrix_2[w][v])

    return subtraction_result_matrix
print(sub_matrix(matrix_1,matrix_2))

#Function 4:
#Sclar multiplication of a matrix
def scalar_multiplicaton(matrix_1,scale_factor):
    scalar_mult_result_matrix = []
    print(len(matrix_1))
    print(len(matrix_1[0]))

    for s in range(len(matrix_1)):                                              #FIX FIX FIX 
        scalar_mult_result_matrix.append([])                                    #FIX FIX FIX 
        for r in range(len(matrix_1[0])):                                       #FIX FIX FIX
            scalar_mult_result_matrix[s].append(matrix_1[r])

    return scalar_mult_result_matrix
print(scalar_multiplicaton(matrix_1,4))