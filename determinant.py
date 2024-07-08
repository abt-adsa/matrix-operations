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


def main() -> None:
    '''Entry point for program that runs all other functions.'''
    while True:
        print("\n---------- New Instance ----------")
        matrix: list[list[Decimal]] = input_matrix()
        if matrix is None:
            break
        determinant: Decimal = calc_determinant(matrix)
        print("\nDeterminant:", determinant)


if __name__ == '__main__':
    main()
