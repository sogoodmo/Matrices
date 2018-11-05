
'''This will be used to test the program, this program will also be used to hold code that I don't want to use yet

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



Matrix_A = []
        C_Value_List = []                                                                   
        for i in range(Column):
            C_Value = int(input("Enter the values for the columns of your matrix in order: "))
            C_Value_List.append(C_Value)
            Matrix_A.append(C_Value_List)
            C_Value_List.clear()
            print(Matrix_A)
            
        for o in range(Row-1):
            R_Value = int(input("Enter the values for the rows for your matrix in order: "))
            Matrix_A[0].append(R_Value)
            print(Matrix_A)
'''
