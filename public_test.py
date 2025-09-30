import strassen
import util

import random

def naive_mult(A,B):
    n = len(A)
    if n <= 0 or not (util.validDim(A,n) and util.validDim(B,n)):
        raise ValueError('Did not receive square matrices '
            'of the same dimension')
    
    C = util.newMatrix(n)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C

def compare(A,B):
    C1 = naive_mult(A,B)
    C2 = strassen.mult(A,B)

    n = len(A)
    match = util.validDim(B,n)
    for i in range(n):
        for j in range(n):
            match = match and (C1[i][j] == C2[i][j])
    
    return match

def baseCaseTest():
    A = util.newMatrix(1)
    B = util.newMatrix(1)

    A[0][0] = 36
    B[0][0] = 10

    return compare(A,B)

def powerOfTwoSymmetricTest(n):
    A = util.newMatrix(2**n)
    B = util.newMatrix(2**n)

    for i in range(2**n):
        for j in range(2**n):
            A[i][j] = i+j
            B[i][j] = i+j

    return compare(A,B)

def powerOfTwoRandomTest(n):
    A = util.newMatrix(2**n)
    B = util.newMatrix(2**n)

    for i in range(2**n):
        for j in range(2**n):
            A[i][j] = random.randint(0,n)
            B[i][j] = random.randint(0,n)

    return compare(A,B)

def anySizeSymmetricTest(n):
    A = util.newMatrix(n)
    B = util.newMatrix(n)

    for i in range(n):
        for j in range(n):
            A[i][j] = i+j
            B[i][j] = i+j

    return compare(A,B)

def anySizeRandomTest(n):
    A = util.newMatrix(n)
    B = util.newMatrix(n)

    for i in range(n):
        for j in range(n):
            A[i][j] = random.randint(0,n)
            B[i][j] = random.randint(0,n)

    return compare(A,B)

def largeRandomTest():
    n = random.randint(1+2**7,2**8)
    A = util.newMatrix(n)
    B = util.newMatrix(n)

    for i in range(n):
        for j in range(n):
            A[i][j] = random.randint(0,n)
            B[i][j] = random.randint(0,n)

    return compare(A,B)

def inputValidationTest():
    A = util.newMatrix(4)
    B = util.newMatrix(3)

    passed = False

    try:
        C = strassen.mult(A,B)
    except ValueError:
        passed = True

    return passed

def runTest(name,test,*args):
    passed = True

    print("Testing %s..." % name)
    try:
        passed = test(*args)
    except NotImplementedError:
        print("\tTest failed. 'strassen.mult' not implemented.")
        passed = False
    except Exception as e:
        print("\tTest failed. Unexpected error: %s" % e)
        passed = False
    else:
        if passed:
            print("\tPASS")
        else:
            print("\tFAIL")
    
    return passed
    

if __name__ == "__main__":
    n_tests = 0
    n_pass = 0
    n_fail = 0
    
    n_tests += 1
    passing = runTest("base case",baseCaseTest)
    if passing:
        n_pass += 1
    else:
        n_fail += 1

    TEST1MIN = 1
    TEST1MAX = 5
    n_tests += (TEST1MAX - TEST1MIN + 1)
    n = TEST1MIN
    passing = True
    while n <= TEST1MAX and passing:
        passing = runTest("deterministic matrix of dimension %d" % (2**n),
            powerOfTwoSymmetricTest,n)
        if passing:
            n_pass += 1
        else:
            n_fail += 1
        n += 1

    TEST2MIN = 1
    TEST2MAX = 5
    n_tests += (TEST2MAX - TEST2MIN + 1)
    n = TEST2MIN
    passing = True
    while n <= TEST2MAX and passing:
        passing = runTest("random matrix of dimension %d" % (2**n),
            powerOfTwoRandomTest,n)
        if passing:
            n_pass += 1
        else:
            n_fail += 1
        n += 1


    TEST3MIN = 3
    TEST3MAX = 8
    n_tests += (TEST3MAX - TEST3MIN + 1)
    n = TEST3MIN
    passing = True
    while n <= TEST3MAX and passing:
        passing = runTest("deterministic matrix of dimension %d" % n,
            anySizeSymmetricTest,n)
        if passing:
            n_pass += 1
        else:
            n_fail += 1
        n += 1

    TEST4MIN = 11
    TEST4MAX = 19
    n_tests += (TEST4MAX - TEST4MIN + 1)
    n = TEST4MIN
    passing = True
    while n <= TEST4MAX and passing:
        passing = runTest("random matrix of dimension %d" % n,
            anySizeRandomTest,n)
        if passing:
            n_pass += 1
        else:
            n_fail += 1
        n += 1

    n_tests += 1
    passing = runTest("large random matrix",largeRandomTest)
    if passing:
        n_pass += 1
    else:
        n_fail += 1



    n_tests += 1
    passing = runTest("input validation",inputValidationTest)
    if passing:
        n_pass += 1
    else:
        n_fail += 1

    print("\n")
    print("Testing complete.")
    print("\tPASS: %d" % n_pass)
    print("\tFAIL: %d" % n_fail)
    print("\tSKIP: %d" % (n_tests - n_pass - n_fail))
