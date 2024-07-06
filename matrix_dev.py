from decimal import getcontext, Decimal, InvalidOperation


getcontext().prec = 5


def input_matrix():
    while True:
        try:
            print("\n[Enter 0 to exit]")
            dim = int(input("Enter matrix dimension: "))
            if dim < 0:
                raise ValueError
            if dim == 0:
                return None
            break
        except ValueError:
            print("Error: Enter positive integer.")
    matrix = []
    print("\nInput matrix elements row-by-row:")
    for _ in range(dim):
        while True:
            try:
                row = list(map(Decimal, input().split()))
                if len(row) != dim:
                    raise ValueError
                matrix.append(row)
                break
            except ValueError:
                print(f"Error: Enter exactly {dim} elements.")
            except InvalidOperation:
                print("Error: Enter numerical elements separated by spaces.")
    print("\nInput Matrix:")
    display_matrix(matrix)
    return matrix


def display_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))


def get_submatrix(matrix, i, j):
    return [row[:j] + row[j+1 :] for row in (matrix[:i] + matrix[i+1 :])]


def calc_determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    matrix_det = Decimal(0)
    for j in range(len(matrix)):
        sign = (-1) ** j
        element = matrix[0][j]
        submatrix_det = calc_determinant(get_submatrix(matrix, 0, j))
        matrix_det += sign * element * submatrix_det
    return matrix_det


def calc_cofactor(matrix):
    cofactor_matrix = []
    for i in range(len(matrix)):
        cofactor_row = []
        for j in range(len(matrix)):
            sign = (-1) ** i+j
            submatrix_det = calc_determinant(get_submatrix(matrix, i, j))
            cofactor_row.append(sign * submatrix_det)
        cofactor_matrix.append(cofactor_row)
    return cofactor_matrix


def get_transpose(matrix):
    transpose = []
    for i in range(len(matrix)):
        transpose_row = []
        for j in range(len(matrix)):
            transpose_row.append(matrix[j][i])
        transpose.append(transpose_row)
    return transpose


def calc_adjugate(matrix):
    return get_transpose(calc_cofactor(matrix))


def calc_inverse(matrix):
    inverse = []
    determinant = calc_determinant(matrix)
    adjugate = calc_adjugate(matrix)
    if determinant == 0:
        raise ZeroDivisionError("Cannot invert singular matrix.")
    for i in range(len(matrix)):
        inverse_row = []
        for j in range(len(matrix)):
            inverse_row.append(adjugate[i][j] / determinant)
        inverse.append(inverse_row)
    return inverse


def main():
    print("\n---------- New Instance ----------")
    matrix = input_matrix()
    if matrix is None:
        exit()
    while True:
        print(
            "\n1 - Determinant"
            "\n2 - Transpose"
            "\n3 - Cofactor Matrix"
            "\n4 - Adjugate Matrix"
            "\n5 - Inverse Matrix"
            "\nE - Exit"
            "\nN - New matrix"
        )
        choice = input("\nEnter number of operation: ")
        if choice not in ('1','2','3','4','5','E','N'):
            print("Error: Enter a valid choice.")
            continue
        if choice.upper() == 'E':
            break
        if choice.upper() == 'N':
            main()
        if choice == '1':
            print("\nDeterminant:", calc_determinant(matrix))
        elif choice == '2':
            print("\nTranspose Matrix:")
            display_matrix(get_transpose(matrix))
        elif choice == '3':
            print("\nCofactor Matrix:")
            display_matrix(calc_cofactor(matrix))
        elif choice == '4':
            print("\nAdjugate Matrix:")
            display_matrix(calc_adjugate(matrix))
        elif choice == '5':
            try:
                inverse = calc_inverse(matrix)
                print("\nInverse Matrix:")
                display_matrix(inverse)
            except ZeroDivisionError as exception:
                print(exception)
        else:
            print("Invalid input. Please enter a valid number.")


if __name__ == '__main__':
    main()