#/usr/bin/evn python3

import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
import statsmodels.api as sm 
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols, glm 

input_file_path = '/Users/sunxuanzhi/winequality-both_beta.csv'

#将数据集读到pandas数据框中,域分隔为逗号，标题为第一行
wine = pd.read_csv(input_file_path,sep=',',header=0)
wine.columns=wine.columns.str.replace(' ','_')
print(wine.head())

#显示所有变量的描述性统计量
print(wine.describe())

#找出quality唯一值,并按升序排列
print(sorted(wine.quality.unique()))

#计算频率值
print(wine.quality.value_counts())