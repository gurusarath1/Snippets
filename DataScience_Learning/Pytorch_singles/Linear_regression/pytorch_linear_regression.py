import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn as nn

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

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

    ## Import the whole csv dataset -----------------------
    dataset_1 = np.loadtxt('dataset_1.csv', delimiter=',', skiprows=1)
    dataset_1_x = dataset_1[:,:-1]
    dataset_1_y = dataset_1[:,-1]

    # Train test split --------------------
    dataset_1_x_train, dataset_1_x_test, dataset_1_y_train, dataset_1_y_test = train_test_split(dataset_1_x, dataset_1_y, test_size=0.3, shuffle=True)
    dataset_1_y_train = torch.Tensor(dataset_1_y_train)
    dataset_1_y_test = torch.Tensor(dataset_1_y_test)


    print('num features = ', dataset_1_x_train.shape[1])
    print('num outputs = ', 1)

    # Center the data ----------------
    sc = StandardScaler()
    sc.fit(dataset_1_x_train)
    dataset_1_x_train = sc.transform(dataset_1_x_train)
    dataset_1_x_train = torch.Tensor(dataset_1_x_train)
    # Apply same transformation on the test data
    dataset_1_x_test = sc.transform(dataset_1_x_test)
    dataset_1_x_test = torch.Tensor(dataset_1_x_test)

    # Create the model
    my_model = linear_regression_model_pytorch( dataset_1_x_train.shape[1], 1)
    print(my_model)

    # Define loss function
    loss_fn = nn.MSELoss()

    # Define optimizer
    #optimizer = torch.optim.SGD(my_model.parameters(), lr=0.05)
    optimizer = torch.optim.Adam(my_model.parameters(), lr=0.05)

    # Training --------------------
    num_epochs = 5000
    for epoch in range(num_epochs):
        
        optimizer.zero_grad()
        preds = my_model(dataset_1_x_train)[:,0]
        loss = loss_fn(preds, dataset_1_y_train)
        if epoch%20 == 0: print(loss)
        loss.backward()
        optimizer.step()


    # Print weights ---------------
    for name, param in my_model.named_parameters():
        if param.requires_grad:
            print(name, param.data)


    # Test Data Predictions ------------
    test_preds = my_model(dataset_1_x_test)
    print(test_preds)
    print(dataset_1_y_test)


    # Model Evaluation ------------

    test_preds = test_preds.detach().numpy().squeeze()
    x_max = np.max( [np.max(test_preds), np.max(dataset_1_y_test.detach().numpy())] )
    x_min = np.min( [np.min(test_preds), np.min(dataset_1_y_test.detach().numpy())] )


    # Mean squared error
    mse_test = mean_squared_error(test_preds, dataset_1_y_test)
    # Mean absolute error
    mae_test = mean_absolute_error(test_preds, dataset_1_y_test)

    print('mse_test = ', mse_test)
    print('mae_test = ', mae_test)

    # Residual plot 
    fig, ax = plt.subplots(1,1,figsize=(7,7))

    ax.scatter( test_preds, test_preds - dataset_1_y_test.detach().numpy(), c='red', marker='x', edgecolor='white', label='Test Data' )

    ax.set_xlabel('predicted values')
    ax.legend(loc='upper left')
    ax.hlines(y=0, xmin=x_min-2, xmax=x_max+2, color='grey', lw=2)
    plt.tight_layout()
    plt.show()












