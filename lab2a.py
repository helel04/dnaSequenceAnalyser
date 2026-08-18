import time

# Function to show expected input format and take matrix input
def input_matrix(rows, cols, name):

    print("\n==================================================")
    print(f"MATRIX INPUT FORMAT for Matrix {name} ({rows}x{cols})")
    print("--------------------------------------------------")

    for i in range(rows):
        format_row = " ".join([f"[{i}][{j}]" for j in range(cols)])
        print(f"Row {i}: {format_row}")

    print("==================================================")

    matrix = []

    print(f"\nEnter elements of Matrix {name} ROW-WISE:")
    print("----------------------------------------")

    for i in range(rows):

        while True:
            row = input(f"Row[{i}] → ").split()

            if len(row) != cols:
                print(f"Error: Please enter exactly {cols} elements.")
            else:
                matrix.append([int(x) for x in row])
                break

    return matrix


# Function to display matrix
def display_matrix(matrix, name):

    print(f"\nMatrix {name}:")
    print("----------------")

    for row in matrix:
        print(" ".join(map(str, row)))


# Conventional matrix multiplication
def multiply_matrix(A, B, r1, c1, r2, c2):

    if c1 != r2:
        print("\nMultiplication not possible.")
        print("Condition: Columns of Matrix A must equal Rows of Matrix B.")
        return None, 0

    result = [[0 for _ in range(c2)] for _ in range(r1)]

    start_time = time.perf_counter()

    # Conventional triple nested loop
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += A[i][k] * B[k][j]

    end_time = time.perf_counter()

    time_taken = end_time - start_time

    return result, time_taken


# Main menu program
def main():

    A = []
    B = []
    r1 = c1 = r2 = c2 = 0

    while True:

        print("\n========== MATRIX MULTIPLICATION MENU ==========")
        print("1. Enter Matrix A")
        print("2. Enter Matrix B")
        print("3. Multiply A × B")
        print("4. Display Matrices")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':

            r1 = int(input("\nEnter number of rows for Matrix A: "))
            c1 = int(input("Enter number of columns for Matrix A: "))

            A = input_matrix(r1, c1, "A")


        elif choice == '2':

            r2 = int(input("\nEnter number of rows for Matrix B: "))
            c2 = int(input("Enter number of columns for Matrix B: "))

            B = input_matrix(r2, c2, "B")


        elif choice == '3':

            if not A or not B:
                print("\nPlease enter both matrices first.")

            else:

                result, time_taken = multiply_matrix(A, B, r1, c1, r2, c2)

                if result is not None:

                    display_matrix(A, "A")
                    display_matrix(B, "B")
                    display_matrix(result, "Result (A × B)")

                    print(f"\nTime taken for multiplication: {time_taken:.8f} seconds")


        elif choice == '4':

            if A:
                display_matrix(A, "A")
            else:
                print("\nMatrix A not entered.")

            if B:
                display_matrix(B, "B")
            else:
                print("Matrix B not entered.")


        elif choice == '5':

            print("\nExiting program.")
            break


        else:
            print("\nInvalid choice. Try again.")


# Run program
main()
