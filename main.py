import torch

#cria o tensor com números
tensor_1d = torch.arange(1, 11)
print(tensor_1d)

#cria o tamanho
tensor_2d = torch.zeros(3, 3)
print(tensor_2d)

#soma os elementos, ele somou do tensor1
print(tensor_1d.sum())



