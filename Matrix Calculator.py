#import Matrix

print("Welcome to that matrix calculator!\nThis program will you allow to create matrix..(Will add more features in the future) ") 

def main():
    To_do = str(input("What would you like to do\nEnter 1 to: Create a matrix\nEnter 2 to: Find the determinates of a matrix\nEnter 3 to: Find the inverse of a matrix\nEnter 4 to: Perform calculations with matricies\n"))

    while To_do != '1' and To_do != '2' and To_do != '3' and To_do != '4':
        To_do = str(input('Error: Invalid Input\nEnter 1 to: Create a matrix\nEnter 2 to: Find the determinates of a matrix\nEnter 3 to: Find the inverse of a matrix\nEnter 4 to: Perform calculations with matricies\n'))
        print(type(To_do))
    if To_do == '1':
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
        Matrix_Val = str(input("Enter the values of your matrix in order. Seperate each value with a comma\n"))
        Matrix_Val = Matrix_Val.replace(' ','')
        Mat_List_Check = Matrix_Val.replace(',','')
        while len(Mat_List_Check) != (Column*Row):
            Matrix_Val = str(input("Error: Invalid Matrix\nEnter the values of your matrix in order. Seperate each value with a comma\n"))
            Matrix_Val = Matrix_Val.replace(' ','')
            Mat_List_Check = Matrix_Val.replace(',','')
            Mat_List = list(Mat_List_Check)
        print(Mat_List_Check)
        #Matrix.Create_Matrix(Column, Row, Mat_List)




    


main()
#To use this function. Do Matrix.Create_Matrix(Column, Row, List of Data)
