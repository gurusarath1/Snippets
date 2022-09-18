import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn as nn

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


class linear_regression_model_pytorch(nn.Module):

    def __init__(self, in_dim, out_dim):
        super().__init__()
        l1 = nn.Linear(in_dim, out_dim)
        l = [l1]
        self.module_list = nn.ModuleList(l)

    def forward(self, x):
        for f in self.module_list:
            x = f(x)
        return x


# This function is not used in the main function
# This function is onlu for extra information
def center_features_and_scale(data_x, eps=0.01):
    '''
    columns are features
    each row is a data point
    '''
    means_x = torch.mean(data_x, 0)
    stds_x = torch.std(data_x, 0)
    data_x_centered = (data_x - means_x) / (stds_x + eps)
    return data_x_centered



if __name__ == '__main__':

    ## Import the whole csv dataset
    dataset_1 = np.loadtxt('dataset_1.csv', delimiter=',', skiprows=1)
    dataset_1_x = dataset_1[:,:-1]
    dataset_1_y = dataset_1[:,-1]

    # Train test split
    dataset_1_x_train, dataset_1_x_test, dataset_1_y_train, dataset_1_y_test = train_test_split(dataset_1_x, dataset_1_y, test_size=0.1, shuffle=True)
    dataset_1_y_train = torch.Tensor(dataset_1_y_train)
    dataset_1_y_test = torch.Tensor(dataset_1_y_test)


    print('num features = ', dataset_1_x_train.shape[1])
    print('num outputs = ', 1)

    # Center the data
    sc = StandardScaler()
    sc.fit(dataset_1_x_train)
    dataset_1_x_train = sc.transform(dataset_1_x_train)
    dataset_1_x_train = torch.Tensor(dataset_1_x_train)
    dataset_1_x_test = sc.transform(dataset_1_x_test)
    dataset_1_x_test = torch.Tensor(dataset_1_x_test)

    # Create the model
    my_model = linear_regression_model_pytorch( dataset_1_x_train.shape[1], 1)
    print(my_model)

    # Define loss function
    loss_fn = nn.MSELoss()

    # Define optimizer
    optimizer = torch.optim.SGD(my_model.parameters(), lr=0.05)

    num_epochs = 100
    for epoch in range(num_epochs):
        
        optimizer.zero_grad()
        preds = my_model(dataset_1_x_train)[:,0]
        loss = loss_fn(preds, dataset_1_y_train)
        if epoch%20 == 0: print(loss)
        loss.backward()
        optimizer.step()


    # Print weights
    for name, param in my_model.named_parameters():
        if param.requires_grad:
            print(name, param.data)


    test_preds = my_model(dataset_1_x_test)
    print(test_preds)
    print(dataset_1_y_test)
