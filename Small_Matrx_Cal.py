def MatrixSum(matrix1, matrix2, rows, columns, result):
    for i in range(rows): 
        for j in range(columns): 
            result[i][j] = matrix1[i][j] + matrix2[i][j]

def MatrixDif(matrix1, matrix2, rows, columns, result):
    for i in range(rows): 
        for j in range(columns): 
            result[i][j] = matrix1[i][j] - matrix2[i][j]
            
def MatrixProduct(matrix1, matrix2, rows, columns, result):
    for i in range(rows):  
        for j in range(columns):
            for k in range(len(matrix2)):  
                result[i][j] += matrix1[i][k] * matrix2[k][j]
                
def MatrixTranspose(matrix1, rows, columns, result):
    for i in range(rows):
        for j in range(columns):
            result[j][i] = matrix1[i][j]
                
def MatrixScalMul(matrix1, num, rows, columns, result):
    for i in range(rows):
        for j in range(columns):
            result[i][j] = num * matrix1[i][j]
            
def MatrixDet(matrix):
    if len(matrix) == 2 and len(matrix[0]) == 2:
        det = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
        return det
    
    elif len(matrix) == 3 and len(matrix[0]) == 3:
        a, b, c = matrix[0]
        d, e, f = matrix[1]
        g, h, i = matrix[2]
        
        det = a * (e * i - h * f) - b * (d * i - f * g) + c * (d * h - e * g)
        return det
    else:
        return None
    
def MatrixInverse(matrix):
    if len(matrix) == 2 and len(matrix[0]) == 2:
        a, b = matrix[0]
        c, d = matrix[1]
        det = (a * d) - (b * c)
        
        if det == 0:
            print("Inverse doesn't exist, determinant is 0!")
            return None
        
        inverse = [
            [d / det, -b / det],
            [-c / det, a / det]
            ]
        
        print("Inverse of Matrix (2x2):")
        for r in inverse:
            print(r)
        return inverse

    elif len(matrix) == 3 and len(matrix[0]) == 3:
        a, b, c = matrix[0]
        d, e, f = matrix[1]
        g, h, i = matrix[2]
        
        det = MatrixDet(matrix)
        if det == 0:
            print("Inverse doesn't exist")
            return None
        
        adjoint = [
            [e * i - f * h, c * h - b * i, b * f - c * e],
            [f * g - d * i, a * i - c * g, c * d - a * f],
            [d * h - e * g, b * g - a * h, a * e - b * d]
        ]
        
        # Divide by determinant
        inverse = [[adjoint[i][j] / det for j in range(3)] for i in range(3)]
        
        print("Inverse of Matrix (3x3):")
        for r in inverse:
            print(r)
        return inverse
    else:
        print("Matrix size not supported for inversion!")
        return None
            
def Search(matrix, rows, columns):
    target = int(input("Enter the target element: "))
    
    for i in range(rows):
        for j in range(columns):
            if(matrix[i][j] == target):
                print(f"Element {target} is found at index [{i}][{j}].")
                return
    print("Element not found in matrix.")

def Sum_Rows_Columns(matrix, rows, columns):
    for i in range(rows):
        sumrow = 0
        for j in range(columns):
            sumrow += matrix[i][j]
        print(f"The sum of row[{i + 1}]: {sumrow}")

    for i in range(columns):
        sumcol = 0
        for j in range(rows):
            sumcol += matrix[j][i]
        print(f"The sum of column[{i + 1}]: {sumcol}")
        
def MatrixDiagSum(matrix):
    size = len(matrix)
    diag_sum = 0
    for i in range(size):
        diag_sum += matrix[i][i] + matrix[i][size - i - 1]
    if size % 2 == 1: 
        diag_sum -= matrix[size // 2][size // 2]
    print(f"Diagonal Sum: {diag_sum}")
    return diag_sum
    
def main():
    print("Matrix Calculator (2x2 to 3x3):")
    
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))

    matrix1 = []
    matrix2 = []
    result = [[0] * columns for _ in range(rows)]
    
    print("Enter elements for Matrix 1:")
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        matrix1.append(row)

    print("Enter elements for Matrix 2:")
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        matrix2.append(row)
        
    while True:
        print("Select what to calculate:")
        print("1. Sum\n2. Difference\n3. Product\n4.Transpose\n5. Scalar Multiplication")
        print("6. Determinant\n7. Inverse\n8. Search element\n9. Sum of Row & Column\n10. Diagonal Sum")
        choice = int(input("Your Choice: "))
        
        if choice == 1:
            MatrixSum(matrix1, matrix2, rows, columns, result)
            print("Result: ")
            for r in result:
                print(r)
                
        elif choice == 2:
            MatrixDif(matrix1, matrix2, rows, columns, result)
            print("Result: ")
            for r in result:
                print(r)
                
        elif choice == 3:
            if len(matrix1[0]) != len(matrix2):
                print("Matrix multiplication is not possible!")
            else:
                result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
                MatrixProduct(matrix1, matrix2, rows, len(matrix2[0]), result)
                print("Result:")
                for r in result:
                    print(r)
                    
        elif choice == 4:
            MatrixTranspose(matrix1, rows, columns, result)
            print("Result:")
            for r in result:
                print(r)
        
        elif choice == 5:
            num = int(input("Enter scalar value: "))
            MatrixScalMul(matrix1, num, rows, columns, result)
            print("Result:")
            for r in result:
                print(r)
                
        elif choice == 6:
            det = MatrixDet(matrix1)
            if det is not None:
                print(f"Determinant: {det}")
            else:
                print("Matrix size not supported for calculation!")
                
        elif choice == 7:
            inverse = MatrixInverse(matrix1)
            if inverse is not None:
                print("Inverse Matrix:")
                for r in inverse:
                    print(r)
                    
        elif choice == 8:
            Search(matrix1, rows, columns)
            
        elif choice == 9:
            Sum_Rows_Columns(matrix1, rows, columns)
            
        elif choice == 10:
            MatrixDiagSum(matrix1)
            
        elif choice == 0: 
            print("Thank you")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()