import torch
import torch.nn as nn


if __name__ == '__main__':

    x = 3

    x = torch.tensor(x,  dtype=torch.float64, requires_grad=True)

    y = x * x

    y.backward(retain_graph=True) # Retain graph will let us use backward twice
    print('y = ', y) #9
    print('x = ', x) #3
    print('x.grad = ', x.grad) #6

    y.backward()
    print('y = ', y) #9
    print('x = ', x) #3
    print('x.grad = ', x.grad) #12 (6+6)


