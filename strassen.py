import util
import math

def mult(A,B):
    if not util.validDim(A, len(A)) or not util.validDim(B, len(B)):
        raise ValueError("Invalid matrix dimensions")
    
    initialDimension = len(A)
    if initialDimension == 0:
        return []

    if len(A) != len(B):
        raise ValueError("Matrices must be the same size")
    
    Apad, Bpad = A, B
    if nextPowerOfTwo(len(A)) != len(A):
        Apad = padMatrix(A, len(A))
        Bpad = padMatrix(B, len(B))
    
    Cpad = strassenMultiplication(Apad, Bpad)
    return unpadMatrix(Cpad, initialDimension)

def strassenMultiplication(A, B):
        ## base case: 1x1 matrix
        if len(A) == 1:
            return [[A[0][0] * B[0][0]]]
        ## recursive case: strassen's algorithm
        else:
            a, b, c, d = splitMatrix(A)
            e, f, g, h = splitMatrix(B)

            p1 = strassenMultiplication(a, subtractMatrices(f, h))
            p2 = strassenMultiplication(addMatrices(a, b),h)
            p3 = strassenMultiplication(addMatrices(c, d), e)
            p4 = strassenMultiplication(d, subtractMatrices(g, e))
            p5 = strassenMultiplication(addMatrices(a, d),addMatrices(e, h))
            p6 = strassenMultiplication(subtractMatrices(b, d),addMatrices(g, h))
            p7 = strassenMultiplication(subtractMatrices(a, c),addMatrices(e, f))

            r = addMatrices(subtractMatrices(addMatrices(p5, p4), p2), p6)
            s = addMatrices(p1, p2)
            t = addMatrices(p3, p4)
            u = subtractMatrices(subtractMatrices(addMatrices(p1, p5), p3), p7)

            C = combineArrays(r,s,t,u)
            return C

def nextPowerOfTwo(n):
    if n <= 0:
        return 1
    ## take ceiling of log base 2 of n, then 2^ that value to find next power of 2
    return 2**math.ceil(math.log2(n))

def splitMatrix(M):
    n = len(M)
    mid = n // 2
    A11 = [row[:mid] for row in M[:mid]]
    A12 = [row[mid:] for row in M[:mid]]
    A21 = [row[:mid] for row in M[mid:]]
    A22 = [row[mid:] for row in M[mid:]]
    return A11, A12, A21, A22

def addMatrices(A, B):
    n = len(A)
    C = util.newMatrix(n)
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def subtractMatrices(A, B):
    n = len(A)
    C = util.newMatrix(n)
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C

def combineArrays(r,s,t,u):
    ## thinking: make array C of size 2n x 2n
    ## r is Q1, s is Q2, t is Q3, u is Q4
    n = len(r)
    C = util.newMatrix(2*n)
    for i in range(n):
        for j in range(n):
            C[i][j] = r[i][j] ## fill Q1
            C[i][j+n] = s[i][j] ## fill Q2
            C[i+n][j] = t[i][j] ## fill Q3
            C[i+n][j+n] = u[i][j] ## fill Q4
    
    return C

def padMatrix(A, n):
    newSize = nextPowerOfTwo(n)
    padded = util.newMatrix(int(newSize))
    for i in range(n):
        for j in range(n):
            padded[i][j] = A[i][j]
    return padded

def unpadMatrix(C, initialDimension):
    return [row[:initialDimension] for row in C[:initialDimension]]
