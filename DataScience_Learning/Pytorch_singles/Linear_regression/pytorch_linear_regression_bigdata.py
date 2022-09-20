import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn as nn

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

from tqdm import tqdm

import pandas as pd

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

    num_features = 5

    # Create the model
    my_model = linear_regression_model_pytorch(num_features, 1)
    print(my_model)

    # Define loss function
    loss_fn = nn.MSELoss()

    # Define optimizer
    #optimizer = torch.optim.SGD(my_model.parameters(), lr=0.05)
    optimizer = torch.optim.Adam(my_model.parameters(), lr=0.1)

    # Training --------------------
    num_epochs = 200
    for epoch in tqdm(range(num_epochs)):

        ## Import the csv dataset in chunks -----------------------
        dataset_1_reader = pd.read_csv('dataset_2_big.csv', chunksize=1000)


        for dataset_1_df in dataset_1_reader:

            dataset_1 = np.array(dataset_1_df)
            dataset_1_x_train = dataset_1[:,:-1]
            dataset_1_y_train = dataset_1[:,-1]

            # Center the data ----------------
            #sc = StandardScaler()
            #sc.fit(dataset_1_x_train)
            #dataset_1_x_train = sc.transform(dataset_1_x_train)
            dataset_1_x_train = torch.Tensor(dataset_1_x_train)
            dataset_1_y_train = torch.Tensor(dataset_1_y_train)

            optimizer.zero_grad()
            preds = my_model(dataset_1_x_train)[:,0]
            loss = loss_fn(preds, dataset_1_y_train)
            loss.backward()
            optimizer.step()


    # Print weights ---------------
    for name, param in my_model.named_parameters():
        if param.requires_grad:
            print(name, param.data)










