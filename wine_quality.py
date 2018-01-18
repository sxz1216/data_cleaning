#/usr/bin/evn python3

import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
import statsmodels.api as sm 
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols, glm 

input_file_path = '/Users/sunxuanzhi/home/file_archive/wine/winequality-both_beta.csv'

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

#按照葡萄酒的类型显示质量的描述性统计量
'''unstack将red与white描述性结果并排显示'''
print(wine.groupby('type')[['quality']].describe().unstack('type'))

#按照葡萄酒的类型查看质量特定分位数值
'''quantile函数计算quality列第25%和75%位数'''
print(wine.groupby('type')[['quality']].quantile([0.25,0.75]).unstack('type'))

#按照葡萄酒类型查看质量分布
red_wine = wine.loc[wine['type']=='red','quality']
white_wine = wine.loc[wine['type']=='white','quality']

#画图
sns.set_style('dark')
print(sns.distplot(red_wine,norm_hist=True,kde=False,color='red',label='Red wine'))
print(sns.distplot(white_wine,norm_hist=True,kde=False,color='white',label='White wine'))
plt.xlabel('Quality Score')
plt.ylabel('Density')
plt.title('Distribution of Quality by Wine Type')
plt.legend()
plt.show()

#检验两种酒的平均质量是否相同
print(wine.groupby('type')[['quality']].agg(['std']))
tstat,pvalue,df = sm.stats.ttest_ind(red_wine,white_wine)
print('tstat: %.3f pvalue: %.4f' % (tstat,pvalue))









