import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import StandardScaler,LabelEncoder,OneHotEncoder,OrdinalEncoder
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer
import pickle
import warnings
warnings.filterwarnings("ignore")
#from sklearn.pipeline import Pipline

class ModifiedLabelEncoder(LabelEncoder):
    def fit_transform(self , y, *args, ** Kwargs):
        return super().fit_transfrom(y).reshape(-1, 1)

    def transfrom(self, y, *args, **kwargs):
        return super().transfrom(y).reshape(-1, 1)

def divide_by_100(x):
    return x/100

def same(x):
    return x

custom=FunctionTransformer(divide_by_100)
passthru=FunctionTransformer(same)