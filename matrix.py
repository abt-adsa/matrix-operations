from typing import List


def input_matrix() -> List[List[float]]:
    """Prompts user to input a matrix."""
    while True:
        try:
            n: int = int(input("\n[Enter '0' to exit]"
                               "\nMatrix dimension (nxn): "))
            if n < 0:
                raise ValueError("Must be a positive integer")
            elif n == 0:
                return None
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Enter a valid dimension.")

    matrix: List[List[float]] = []
    print("Input matrix row by row [Ex. -2 0 3.14]:")
    for _ in range(n):
        while True:
            try:
                row: List[float] = list(map(float, input().split()))
                if len(row) != n:
                    raise ValueError(f"Row must have {n} elements")
                matrix.append(row)
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Enter the row again.")
    return matrix


def display_matrix(matrix: List[List[float]]) -> None:
    """Prints the given matrix."""
    for row in matrix:
        print(' '.join(map(str, row)))


def get_submatrix(matrix: List[List[float]],
                  i: int, j: int) -> List[List[float]]:
    """Generates a submatrix by removing row and column indices i and j"""
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]


def calc_determinant(matrix: List[List[float]]) -> float:
    """Calculates the determinant of a matrix."""
    if len(matrix) == 1:
        return matrix[0][0]
    else:
        det: float = 0.0
        for j in range(len(matrix[0])):
            sign: int = (-1) ** j
            element: float = matrix[0][j]
            submatrix: List[List[float]] = get_submatrix(matrix, 0, j)
            det += sign * element * calc_determinant(submatrix)
    return det


def calc_cofactor(matrix: List[List[float]]) -> List[List[float]]:
    """Calculates the cofactor matrix."""
    cof_matrix: List[List[float]] = []
    for i in range(len(matrix)):
        cof_row: List[float] = []
        for j in range(len(matrix)):
            sign: int = (-1) ** (i + j)
            cof_row.append(sign * calc_determinant(get_submatrix(matrix, i, j)))
        cof_matrix.append(cof_row)
    return cof_matrix


def transpose(matrix: List[List[float]]) -> List[List[float]]:
    """Transposes the given matrix."""
    transposed: List[List[float]] = []
    for i in range(len(matrix)):
        trans_row: List[float] = []
        for j in range(len(matrix)):
            trans_row.append(matrix[j][i])
        transposed.append(trans_row)
    return transposed


def calc_adjugate(matrix: List[List[float]]) -> List[List[float]]:
    """Calculates the adjugate of the matrix."""
    return transpose(calc_cofactor(matrix))


def calc_inverse(matrix: List[List[float]]) -> List[List[float]]:
    """Calculates the inverse of the matrix."""
    det: float = calc_determinant(matrix)
    if det == 0:
        raise ZeroDivisionError("Matrix is singular and cannot be inverted.")
    adj: List[List[float]] = calc_adjugate(matrix)
    inv_matrix: List[List[float]] = []
    for i in range(len(matrix)):
        inv_row: List[float] = []
        for j in range(len(adj)):
            inv_row.append(adj[i][j] / det)
        inv_matrix.append(inv_row)
    return inv_matrix


def main() -> None:
    """Main function to run the matrix operations."""
    matrix: List[List[float]] = input_matrix()
    print("\nInput Matrix:")
    display_matrix(matrix)

    while True:
        print(
            "\n1 - Determinant"
            "\n2 - Transpose"
            "\n3 - Cofactor Matrix"
            "\n4 - Adjugate Matrix"
            "\n5 - Inverse Matrix"
            "\n0 - Exit"
        )

        try:
            choice: int = int(input("\nWhat to calculate? Enter the number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if choice == 0:
            break
        if choice == 1:
            print("\nDeterminant:", calc_determinant(matrix))
        elif choice == 2:
            print("\nTranspose Matrix:")
            display_matrix(transpose(matrix))
        elif choice == 3:
            print("\nCofactor Matrix:")
            display_matrix(calc_cofactor(matrix))
        elif choice == 4:
            print("\nAdjugate Matrix:")
            display_matrix(calc_adjugate(matrix))
        elif choice == 5:
            try:
                inv = calc_inverse(matrix)
                print("\nInverse Matrix:")
                display_matrix(inv)
            except ZeroDivisionError as e:
                print(e)
        else:
            print("Invalid input. Please enter a valid number.")


if __name__ == '__main__':
    main()