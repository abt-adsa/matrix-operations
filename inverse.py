from typing import List


def input_matrix() -> List[List[float]]:
    """Prompts user to input a matrix."""

    while True:
        try:
            n: int = int(input("\n[Enter '0' to exit]"
                               "\nMatrix dimension (nxn): "))
            if n < 0:
                raise ValueError("Dimension must be a positive integer")
            elif n == 0:
                return None
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid dimension.")

    matrix: List[List[float]] = []
    print("Input matrix row by row:")
    for _ in range(n):
        while True:
            try:
                row: List[float] = list(map(float, input().split()))
                if len(row) != n:
                    raise ValueError(f"Row must have {n} elements.")
                matrix.append(row)
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter the row again.")
    return matrix


def display_matrix(matrix: List[List[float]]) -> None:
    """Prints the given matrix."""
    for row in matrix:
        print(' '.join(map(str, row)))


def calc_determinant(matrix: List[List[float]]) -> float:
    """Calculates the determinant of a matrix."""
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det: float = 0.0
        for j in range(len(matrix[0])):
            sign: int = (-1) ** j
            det += sign * matrix[0][j] * calc_determinant(get_minor(matrix, 0, j))
    return det


def get_minor(matrix: List[List[float]], i: int, j: int) -> List[List[float]]:
    """Generates the minor of a matrix by removing the specified row and column."""
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]


def calc_cofactor(matrix: List[List[float]]) -> List[List[float]]:
    """Calculates the cofactor matrix."""
    cof_matrix: List[List[float]] = []
    for i in range(len(matrix)):
        cof_row: List[float] = []
        for j in range(len(matrix)):
            sign: int = (-1) ** (i + j)
            cof_row.append(sign * calc_determinant(get_minor(matrix, i, j)))
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
    while True:
        matrix: List[List[float]] = input_matrix()
        if matrix == None:
            break
        print("\nInput Matrix:")
        display_matrix(matrix)
        try:
            inv = calc_inverse(matrix)
            print("\nInverse Matrix:")
            display_matrix(inv)
        except ZeroDivisionError as e:
            print(e)


if __name__ == '__main__':
    main()