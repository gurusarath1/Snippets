import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from tqdm import tqdm

def create_simple_ann_pytorch(in_dim, hid_dim, out_dim, num_layers=1, activation_fn=nn.ReLU() ):

    layers = []

    for i in range(num_layers):

        if i == num_layers-1:
            layers.append( nn.Linear(in_dim, out_dim) )
            layers.append( nn.Sigmoid() )
        else:
            layers.append( nn.Linear(in_dim, hid_dim) )
            layers.append( activation_fn )
            in_dim = hid_dim

    return nn.Sequential(*layers)


if __name__ == '__main__':

    dataset_1 = np.genfromtxt('dataset_1.csv', delimiter=',', skip_header=1) 
    dataset_1_x = dataset_1[:,:-1]
    dataset_1_y = dataset_1[:,-1]

    # Train test split --------------------
    dataset_1_x_train, dataset_1_x_validation, dataset_1_y_train, dataset_1_y_validation = train_test_split(dataset_1_x, dataset_1_y, test_size=0.01, shuffle=True)
    dataset_1_x_train = torch.Tensor(dataset_1_x_train)
    dataset_1_y_train = torch.Tensor(dataset_1_y_train)
    dataset_1_x_validation = torch.Tensor(dataset_1_x_validation)
    dataset_1_y_validation = torch.Tensor(dataset_1_y_validation)
    train_ds = TensorDataset(dataset_1_x_train, dataset_1_y_train)
    batch_size = 100
    train_dl = DataLoader(train_ds, batch_size, shuffle=True)


    my_model = create_simple_ann_pytorch(8, 1, 1, num_layers=1) # Logistic regression
    print(my_model)

    loss_fn = nn.BCELoss()
    optimizer = torch.optim.Adam(my_model.parameters(), lr=0.01)


    num_epochs = 50
    train_loss_history = []
    validation_loss_history = []
    train_accuracy_history = []
    validation_accuracy_history = []
    for epoch in (range(num_epochs)):
        
        is_correct = 0
        for x_batch, y_batch in train_dl:

            optimizer.zero_grad()
            pred = my_model(x_batch)[:,0]
            loss = loss_fn(pred, y_batch)
            loss.backward()
            optimizer.step()

            train_loss_history.append(loss.item())
            is_correct += ( (pred>=0.5).float() == y_batch ).sum()
        
        train_accuracy_history.append(is_correct / dataset_1_x_train.shape[0])

        pred =  my_model(dataset_1_x_validation)[:,0]
        loss = loss_fn(pred, dataset_1_y_validation)
        validation_loss_history.append(loss.item())

        is_correct = ((pred >= 0.5).float() == dataset_1_y_validation).sum()
        validation_accuracy_history.append(is_correct / dataset_1_x_validation.shape[0])

    plt.plot(train_accuracy_history, label='Train accuracy')
    plt.plot(validation_accuracy_history, label='Validation Accuracy')
    plt.legend()
    plt.show()

















