# importing libraries
import pandas as pd
import numpy as np
import matplotlib
import warnings
warnings.filterwarnings('ignore')

matplotlib inline
pd.set_option('display.max_colwidth',None)
pd.set_option('display.max_columns',None)

# Graphics in retina format are more sharp and legible
%config InlineBackend.figure_format = 'retina'

data = pd.read_csv("worldometer_data.csv")
data.head(2)

data.shape
data.info()