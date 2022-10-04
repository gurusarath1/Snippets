import torch
import torch.nn as nn


if __name__ == '__main__':

    x = -2
    descend_rate = 0.01

    for i in range(1000):
        x = torch.tensor(x, dtype=torch.float64, requires_grad=True)
        y = (x - 2) ** 2

        y.backward(retain_graph=True)
        print('x.grad = ', x.grad)
        
        x_grad = x.grad.item()
        x = x - (descend_rate * x_grad)
        print('x = ', x.item())
