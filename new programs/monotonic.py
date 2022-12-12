def isMonotonic(A):
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))


A = [6, 5, 4, 4]
B = [4, 6, 2, 1]

# Print required result
print(isMonotonic(A))
print(isMonotonic(B))
