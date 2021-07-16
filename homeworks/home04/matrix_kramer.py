import numpy as np
import numpy.linalg as la


# Для системы с  𝑛   уравнениями и  𝑛  неизвестными,
# если система уравнений невырождена (то есть  𝑑𝑒𝑡𝐴≠0  ), то система определена,
# то есть имеет единственное решение, и это решение может быть найдено по формулам Крамера:
#                           𝑥𝑖=𝑑𝑒𝑡𝐴𝑖/𝑑𝑒𝑡𝐴

def matrix_kramer(A, b):
    if A.shape[0] != A.shape[1]:
        raise Exception('Размерность не совпадает')
    det = la.det(A)
    R = []
    for i in range(A.shape[0]):
        A_s = A.copy()
        A_s.T[i] = b
        R.append(la.det(A_s) / det)
    return R


A = np.array([[2, -1, 5], [1, 1, -3], [2, 4, 1]])
b = [10, -2, 1]
print(matrix_kramer(A, b))
