def matrix_chain_multiplication(dims):
    n = len(dims)
    # Create a 2D table to store the minimum number of scalar multiplications
    # for each subproblem.
    dp = [[0] * n for _ in range(n)]

    # Initialize the table for chains of length 2 to n.
    for chain_len in range(2, n):
        for i in range(n - chain_len + 1):
            j = i + chain_len - 1
            dp[i][j] = float('inf')  # Initialize to infinity.

            # Try all possible parenthesizations and find the minimum.
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dims[i][0] * dims[k][1] * dims[j][1]
                if cost < dp[i][j]:
                    dp[i][j] = cost

    # The result is stored in dp[0][n-1], which represents the optimal cost.
    min_scalar_multiplications = dp[0][n - 1]

    # Reconstruct the optimal parenthesization.
    parenthesization = construct_parenthesization(dp, 0, n - 1)
    
    return parenthesization, min_scalar_multiplications

def construct_parenthesization(dp, i, j):
    if i == j:
        return f'M{str(i)}'
    else:
        for k in range(i, j):
            if dp[i][j] == dp[i][k] + dp[k + 1][j] + dims[i][0] * dims[k][1] * dims[j][1]:
                left_parenthesis = construct_parenthesization(dp, i, k)
                right_parenthesis = construct_parenthesization(dp, k + 1, j)
                return f'({left_parenthesis} * {right_parenthesis})'

# Input: Dimensions of matrices
dims = [(2, 3), (3, 4), (4, 2)]

# Find the optimal parenthesization and minimum scalar multiplications
parenthesization, min_scalar_multiplications = matrix_chain_multiplication(dims)

# Output results
print("Optimal Parenthesization:", parenthesization)
print("Minimum Scalar Multiplications:", min_scalar_multiplications)
