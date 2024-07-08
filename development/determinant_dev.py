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


def main():
    while True:
        print("\n---------- New Instance ----------")
        matrix = input_matrix()
        if matrix is None:
            break
        determinant = calc_determinant(matrix)
        print("\nDeterminant:", determinant)


if __name__ == '__main__':
    main()