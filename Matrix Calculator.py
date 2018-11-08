import Matrix

#Introduction
print("Welcome to that matrix calculator!\nThis program will you allow to create matrix..(Will add more features in the future) ") 

def main():
    Matrix_Num = 0
    To_do = str(input("\nWhat would you like to do\nEnter 1 to: Create a matrix\nEnter 2 to: Find the determinates of a matrix\nEnter 3 to: Find the inverse of a matrix\nEnter 4 to: Perform calculations with matricies\n"))

    #Spahgetti while loop to ensure they don't enter anything other than the avalible options
    while To_do != '1' and To_do != '2' and To_do != '3' and To_do != '4':
        To_do = str(input('Error: Invalid Input\nEnter 1 to: Create a matrix\nEnter 2 to: Find the determinates of a matrix\nEnter 3 to: Find the inverse of a matrix\nEnter 4 to: Perform calculations with matricies\n'))

    if To_do == '1':
        #This is to ensure when they enter the amount of rows and columns that its only a whole number
        #Can't have a matrix with 2.3 rows
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
        Matrix.Create_Matrix(Column, Row)
        Matrix_Num += 1

        #Matrix.PlayAgain()

    #Next function. Operations with matricies.    
    elif To_do == '2':
        if Matrix_Num == 0:
            To_do = 1
        else:
            Op = str(input("What operation would you like to perform\nEnter 1 to: For Addtion\nEnter 2 for: Subtraction\nEnter 3 for: Multiplication\nEnter 4 for: Division\n"))   
            while Op != '1' and Op != '2' and Op != '3' and Op != '4':
                Op = str(input('Error: Invalid Input\nEnter 1 to: For Addtion\nEnter 2 for: Subtraction\nEnter 3 for: Multiplication\nEnter 4 for: Division\n'))
                print(type(Op))
            if Op == '1':
                print('DO SOME WORK!!!')


        
main()

