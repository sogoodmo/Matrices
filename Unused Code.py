z = ('hello')
a = list(z)
print(a)



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