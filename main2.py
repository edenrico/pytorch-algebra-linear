import torch

A = torch.tensor([[1, 2], [3, 4]])
B = torch.tensor([[5, 6], [7, 8]])

# Produto matricial, MATRICIAL = combina as duas listas  para obter a terceira lista C,
#álgebra linear para multiplicação de matrizes, 
#multiplicação e soma
C = torch.matmul(A, B)
print(C)

# Transposta, ele usou apenas os numeros da fileira A, 
# 1 com o 1, 2 com o 2
A_transpose = A.T
print(A_transpose)

