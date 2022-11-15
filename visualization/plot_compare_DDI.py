# import plt , numpy and pandas
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# read in the data
df = pd.read_csv("data/DDI_data_P_compare_1-2_withY_v4.csv")

# calculate error percentage for each model into numpy array
error_1 = np.abs(df["DDI_model_1_predict"] - df["answer"]) / df["answer"] *100
error_2 = np.abs(df["DDI_model_2_predict"] - df["answer"]) / df["answer"] *100

# graph title is "DDI compare of model 1 and 2"
plt.title("DDI compare of model 1 and 2")

# plot y as log 2 scale 
plt.yscale("log")

# plot the error percentage histogram
plt.hist(error_1, bins=100, alpha=0.5, label='DDI_model_1')
plt.hist(error_2, bins=100, alpha=0.5, label='DDI_model_2')

# set the x and y axis label
plt.xlabel("Error Percentage")
plt.ylabel("Frequency")

plt.legend(["DDI_model_1", "DDI_model_2"])
plt.show()

