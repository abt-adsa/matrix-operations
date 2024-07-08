'''Import standard decimal module to avoid rounding errors'''
from decimal import getcontext, Decimal, InvalidOperation


getcontext().prec = 5  # Set precision to 5 decimal places


def input_matrix() -> list[list[Decimal]]:
    '''Prompts user input for matrix dimension and elements.'''
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

    matrix: list[list[Decimal]] = []
    print("\nInput matrix elements row-by-row:")
    for _ in range(dim):
        while True:
            try:
                # Convert input string of space-separated values to a list of Decimals
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


def display_matrix(matrix: list[list[Decimal]]) -> None:
    '''Prints the matrix row-by-row'''
    for row in matrix:
        print(' '.join(map(str, row)))


def get_submatrix(matrix: list[list[Decimal]], i: int, j: int) -> list[list[Decimal]]:
    '''Generates submatrix by removing the indexed row and column'''
    return [row[:j] + row[j+1 :] for row in (matrix[:i] + matrix[i+1 :])]


def calc_determinant(matrix: list[list[Decimal]]) -> Decimal:
    '''Calculates the determinant of the matrix.'''
    if len(matrix) == 1:
        return matrix[0][0]  # Determinant of 1x1 matrix is its only element
    
    matrix_det = Decimal(0)
    for j in range(len(matrix)):
        sign: int = (-1) ** j
        element: Decimal = matrix[0][j]
        submatrix_det: Decimal = calc_determinant(get_submatrix(matrix, 0, j))
        matrix_det += sign * element * submatrix_det  # Laplace Expansion
    return matrix_det


def calc_cofactor(matrix: list[list[Decimal]]) -> list[list[Decimal]]:
    '''Calculates the cofactor matrix.'''
    cofactor_matrix: list[list[Decimal]] = []
    for i in range(len(matrix)):
        cofactor_row: list[Decimal] = []
        for j in range(len(matrix)):
            sign: int = (-1) ** i+j
            submatrix_det: Decimal = calc_determinant(get_submatrix(matrix, i, j))
            cofactor_row.append(sign * submatrix_det)
        cofactor_matrix.append(cofactor_row)
    return cofactor_matrix


def get_transpose(matrix: list[list[Decimal]]) -> list[list[Decimal]]:
    '''Generates transpose by swapping row and column elements.'''
    transpose: list[list[Decimal]] = []
    for i in range(len(matrix)):
        trans_row: list[Decimal] = []
        for j in range(len(matrix)):
            trans_row.append(matrix[j][i])  # Swaps row and column indices
        transpose.append(trans_row)
    return transpose


def calc_adjugate(matrix: list[list[Decimal]]):
    '''Calculates the matrix adjugate'''
    return get_transpose(calc_cofactor(matrix))


def main() -> None:
    '''Entry point for program that runs all other functions.'''
    while True:
        print("\n---------- New Instance ----------")
        matrix: list[list[Decimal]] = input_matrix()
        if matrix is None:
            break
        adjugate: list[list[Decimal]] = calc_adjugate(matrix)
        print("\nAdjugate:")
        display_matrix(adjugate)


if __name__ == "__main__":
    main()
