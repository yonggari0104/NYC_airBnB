import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')



nyc = pd.read_csv('C:\\Users\\user\\.spyder-py3\\nycbnb\\nycbnb.csv')

#SEE IF NaN VALUES EXISTS
print(nyc.isna().any())

print(nyc.info())
print(nyc.head())
print(nyc.dtypes)
print(nyc.describe())