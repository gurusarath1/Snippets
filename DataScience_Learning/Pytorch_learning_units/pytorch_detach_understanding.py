import torch
import torch.nn as nn

if __name__ == '__main__':

    x = torch.tensor(2, dtype=torch.float64, requires_grad=True)

    y = (x**2) + (x**3)
    y.backward()
    print('x.grad = ', x.grad) #16

    x.grad.zero_() # Zero out the grad
    y = (x**2) + (x.detach()**3) # detach will treat it like a constant
    y.backward()
    print('x.grad = ', x.grad) # 4

