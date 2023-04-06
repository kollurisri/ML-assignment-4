import numpy as np
import pandas as pd
test_df = pd.read_csv("test.csv")
train_df = pd.read_csv("train.csv")
combine = [train_df, test_df]
train_df['Sex'].str.get_dummies().corrwith(train_df['Survived']/train_df['Survived'].max())
