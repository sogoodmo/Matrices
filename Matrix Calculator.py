import Matrix

#Introduction
print("Welcome to that matrix calculator!\nThis program will you allow to create matrix..(Will add more features in the future) ") 

def main():
    To_do = str(input("\nWhat would you like to do\nEnter 1 to: Create a matrix\nEnter 2 to: Find the determinates of a matrix\nEnter 3 to: Find the inverse of a matrix\nEnter 4 to: Perform calculations with matricies\n"))

    #Spahgetti while loop to ensure they don't enter anything other than the avalible options
    while To_do != '1' and To_do != '2' and To_do != '3' and To_do != '4':
        To_do = str(input('Error: Invalid Input\nEnter 1 to: Create a matrix\nEnter 2 to: Find the determinates of a matrix\nEnter 3 to: Find the inverse of a matrix\nEnter 4 to: Perform calculations with matricies\n'))
        print(type(To_do))
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
        #Creating empty matrix to add my values to.
        
main()
#To use this function. Do Matrix.Create_Matrix(Column, Row, List of Data)
