# Rotate 2D Matrix

This task involves rotating a 2d matrix by 90 degrees clockwise in-place i.e.,
without creating a new matrix.
The strategy employed in my solution is: 1. First reflecting the matrix along the leading diagonal or negative slope
diagonal. 2. Rotating the resulting matrix along the middle.

Tasks 0. Rotate 2D Matrix
mandatory
Given an n x n 2D matrix, rotate it 90 degrees clockwise.

Prototype: def rotate_2d_matrix(matrix):
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.
jessevhedden$ cat main_0.py
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = **import**('0-rotate_2d_matrix').rotate_2d_matrix

if **name** == "**main**":
matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

jessevhedden$
jessevhedden$ ./main_0.py
[[7, 4, 1],
[8, 5, 2],
[9, 6, 3]]
jessevhedden$
Repo:

GitHub repository: alx-interview
Directory: 0x07-rotate_2d_matrix
File: 0-rotate_2d_matrix.py
