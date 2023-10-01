# Advanced_DataStructure_and_Algorithm_Assignment
Assignment 1
You are given an array of integers, and you are required to sort this array using one of the following sorting algorithms: Bubble Sort, Selection Sort, or Insertion Sort. Your task is to implement the chosen sorting algorithm and analyze its time complexity.

Input:
•	An unsorted list of integers (e.g., [5, 2, 9, 1, 5, 6]).

Output:
•	The sorted list of integers.

Instructions:
1.	Choose one of the sorting algorithms (Bubble Sort, Selection Sort, or Insertion Sort) and implement it in Python.
2.	Apply your chosen sorting algorithm to the provided input array.
3.	Provide the sorted array as the output.
4.	Analyze the time complexity of the sorting algorithm and discuss its stability and performance on different input data.
5.	Compare the time complexity of your chosen sorting algorithm with at least one other sorting algorithm, and explain when you would prefer one over the other.


Assignment 2 
You are given a sequence of matrices with dimensions that are suitable for matrix multiplication. Your task is to find the optimal way to parenthesize the matrices to minimize the total number of scalar multiplications required to compute their product.

Input:
•	A list of matrices, each represented by its dimensions. For example, a list of matrices [A, B, C] could be represented as [(2, 3), (3, 4), (4, 2)] where the dimensions of matrix A are 2x3, the dimensions of matrix B are 3x4, and the dimensions of matrix C are 4x2.

Output:
•	The optimal parenthesization of matrices as a sequence of matrix multiplications.
•	The minimum number of scalar multiplications required for the optimal parenthesization.

Instructions:
1.	Implement a dynamic programming algorithm to solve the matrix chain multiplication problem in Python.
2.	Apply your algorithm to the provided list of matrices to find the optimal parenthesization.
3.	Calculate and provide the minimum number of scalar multiplications required for the optimal parenthesization.
4.	Explain the dynamic programming approach, including the initialization, recurrence relation, and reconstruction of the optimal parenthesization.
5.	Analyze the time and space complexity of your algorithm and discuss its efficiency for large instances of the problem.


Assignment 3
You are tasked with solving the N-Queens problem using a backtracking algorithm. The N-Queens problem is to place N chess queens on an N×N chessboard so that no two queens threaten each other. Thus, a solution requires that no two queens share the same row, column, or diagonal. Your goal is to implement the algorithm, find all possible solutions for a given N, and analyze its time complexity.

Input:
•	An integer N (N ≥ 4) representing the size of the N×N chessboard and the number of queens to place.

Output:
•	All possible solutions to the N-Queens problem for the given N, presented as chessboard representations.

Instructions:
1.	Implement a backtracking algorithm to solve the N-Queens problem in Python.
2.	Apply your algorithm to find all possible solutions for the provided value of N (e.g., N = 4 or N = 8).
3.	Present the solutions as chessboard representations, indicating the placement of queens (e.g., using 'Q' for queens and '.' for empty squares).
4.	Explain the backtracking approach, including solution generation, validation, and conflict resolution.
5.	Analyze the time complexity of your algorithm and discuss its performance for larger N values.
