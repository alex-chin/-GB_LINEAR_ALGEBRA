# Произведением матрицы  𝐴=‖‖𝑎𝑖𝑗‖‖ , имеющей порядки  𝑚  и  𝑛 ,
# и матрицы  𝐵=‖‖𝑏𝑖𝑗‖‖ , имеющей порядки  𝑛  и  𝑘 ,
# называется матрица  𝐶=‖‖𝑐𝑖𝑗‖‖ , имеющая порядки  𝑚  и  𝑘
#

def matrix_multi(A, B):
    A_m = len(A)
    A_n = len(A[0])
    B_n = len(B)
    B_k = len(B[0])
    C = [[None]*A_m]*B_k

    for i in range(A_m):
        for j in range(B_k):
            sum0 = 0
            for p in range(A_n):
                sum0 += A[i][p] * B[p][j]
            # print(i, j, sum0)
            print(C)
            C[i][j] = sum0
    return C


a = [[1, 2, 3], [2, 3, 4]]
b = [[2, 1], [3, 1], [1, 1]]
print(matrix_multi(a, b))
