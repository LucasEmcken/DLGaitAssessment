import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch
import data_utils
from torch.nn import nn
from torch.nn import Linear, GRU, Conv2d, Dropout, MaxPool2d, BatchNorm1d

# Hyperparameters:
LEARNING_RATE = 1e-3
NUM_EPOCHS = 0

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.l1 = nn.Sequential()
        self.rnn = nn.RNN()

    def forward(self):
        features = self.l1()
        features = self.l2()
        features = self.l3()

net = Net()

optimizer = torch.optim.AdamW(net.parameters(), lr=LEARNING_RATE)
loss_function = nn.CrossEntropyLoss()


def __train__(self):
    net.train()

    for epoch in range(NUM_EPOCHS):
        print(f"Epoch: {epoch+1}")

        # Foreward pass
        output = net.forward()

        # Compute loss
        loss = loss_function(output, target)

        # Gradient and backprop
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
