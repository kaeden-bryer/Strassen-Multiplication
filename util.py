# Generate an n x n matrix filled with 0s
def newMatrix(n):
    out = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(0)
        out.append(row)
    return out    

# Confirm A is an n x n matrix
def validDim(A,n):
    correct = (len(A) == n)
    for row in A:
        correct = correct and (len(row) == n)
        for e in row:
            correct = correct and isinstance(e,int)
    return correct
