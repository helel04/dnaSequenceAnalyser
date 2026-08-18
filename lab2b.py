import time
import math

# ---------- Input Matrix ----------
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
                print(f"Error: Enter exactly {cols} elements.")
            else:
                matrix.append([int(x) for x in row])
                break
    return matrix

# ---------- Display Matrix ----------
def display_matrix(matrix, name):
    print(f"\nMatrix {name}:")
    print("----------------")
    for row in matrix:
        print(" ".join(map(str, row)))

# ---------- Next Power of 2 ----------
def next_power_of_2(n):
    return 1 if n == 0 else 2**math.ceil(math.log2(n))

# ---------- Padding ----------
def pad_matrix(matrix, new_size):
    old_rows = len(matrix)
    old_cols = len(matrix[0])
    padded = [[0]*new_size for _ in range(new_size)]
    for i in range(old_rows):
        for j in range(old_cols):
            padded[i][j] = matrix[i][j]
    return padded

# ---------- Remove Padding ----------
def unpad_matrix(matrix, rows, cols):
    return [row[:cols] for row in matrix[:rows]]

# ---------- Matrix Addition ----------
def add(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

# ---------- Matrix Subtraction ----------
def subtract(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

# ---------- Split ----------
def split(M):
    n = len(M)
    mid = n // 2
    A11 = [row[:mid] for row in M[:mid]]
    A12 = [row[mid:] for row in M[:mid]]
    A21 = [row[:mid] for row in M[mid:]]
    A22 = [row[mid:] for row in M[mid:]]
    return A11, A12, A21, A22

# ---------- Combine ----------
def combine(C11, C12, C21, C22):
    top = [C11[i] + C12[i] for i in range(len(C11))]
    bottom = [C21[i] + C22[i] for i in range(len(C21))]
    return top + bottom

# ---------- Strassen Recursive ----------
def strassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    A11, A12, A21, A22 = split(A)
    B11, B12, B21, B22 = split(B)
    M1 = strassen(add(A11, A22), add(B11, B22))
    M2 = strassen(add(A21, A22), B11)
    M3 = strassen(A11, subtract(B12, B22))
    M4 = strassen(A22, subtract(B21, B11))
    M5 = strassen(add(A11, A12), B22)
    M6 = strassen(subtract(A21, A11), add(B11, B12))
    M7 = strassen(subtract(A12, A22), add(B21, B22))
    C11 = add(subtract(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(subtract(add(M1, M3), M2), M6)
    return combine(C11, C12, C21, C22)

# ---------- Strassen Multiply with Padding ----------
def strassen_multiply(A, B, r1, c1, r2, c2):
    max_size = max(r1, c1, r2, c2)
    new_size = next_power_of_2(max_size)
    A_pad = pad_matrix(A, new_size)
    B_pad = pad_matrix(B, new_size)
    start = time.perf_counter()
    C_pad = strassen(A_pad, B_pad)
    end = time.perf_counter()
    C = unpad_matrix(C_pad, r1, c2)
    return C, end - start

# ---------- Main Menu ----------
def main():
    A = []
    B = []
    r1 = c1 = r2 = c2 = 0
    while True:
        print("\n========== STRASSEN MATRIX MENU (WITH PADDING) ==========")
        print("1. Enter Matrix A")
        print("2. Enter Matrix B")
        print("3. Multiply using Strassen")
        print("4. Display Matrices")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            r1 = int(input("\nEnter rows of Matrix A: "))
            c1 = int(input("Enter columns of Matrix A: "))
            A = input_matrix(r1, c1, "A")

        elif choice == '2':
            r2 = int(input("\nEnter rows of Matrix B: "))
            c2 = int(input("Enter columns of Matrix B: "))
            if c1 != r2:
                print("\nError: Columns of A must equal Rows of B.")
                continue
            B = input_matrix(r2, c2, "B")

        elif choice == '3':
            if not A or not B:
                print("\nEnter both matrices first.")
                continue
            result, time_taken = strassen_multiply(A, B, r1, c1, r2, c2)
            display_matrix(A, "A")
            display_matrix(B, "B")
            display_matrix(result, "Result (Strassen with Padding)")
            print(f"\nTime taken: {time_taken:.8f} seconds")

        elif choice == '4':
            if A:
                display_matrix(A, "A")
            else:
                print("Matrix A not entered.")
            if B:
                display_matrix(B, "B")
            else:
                print("Matrix B not entered.")

        elif choice == '5':
            print("Exiting.")
            break

        else:
            print("Invalid choice.")
            

main()
