import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

raw_data = pd.read_csv("train_time_series.csv")
train_data = pd.read_csv("train_labels.csv")

print(raw_data.shape)
print(train_data.shape)


