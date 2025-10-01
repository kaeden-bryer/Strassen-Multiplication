import util
import math

def mult(A,B):
    isAValid = util.validDim(A, len(A));
    isBValid = util.validDim(B, len(B));
    if not (isAValid and isBValid):
        raise ValueError("Invalid matrix dimensions")
    
    paddedA = padMatrix(A, len(A))
    paddedB = padMatrix(B, len(B))
    


def padMatrix(A, n):
    ## thinking: add 0's to rows and columns to make A a 2^n x 2^n matrix

    ## take ceiling of log base 2 of n, then 2^ that value
    newSize = 2**math.ceil(math.log2(n))

    ## create new matrix of size newSize x newSize
    padded = util.newMatrix(newSize)

    ## copy values from A to padded. Extra rows and columns should already be 0
    for i in range(n):
        for j in range(n):
            padded[i][j] = A[i][j]

    ## print testing
    print(padded)
    return padded

## just use for testing
if __name__ == "__main__":
    A = [[1,2,3,4,5],[4,5,6,7,8],[7,8,9,10,11], [10,11,12,13,14],[13,14,15,16,17]]
    print(len(A))
    padMatrix(A, len(A))


