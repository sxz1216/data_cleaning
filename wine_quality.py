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

#计算左右变量的相关矩阵
print(wine.corr())

#从红葡萄酒和白葡萄酒中取出较小的样本进行绘图
def take_sample(data_frame,replace=False,n=200):
	return data_frame.loc[np.random.choice(data_frame.index,replace=replace,size=n)]

reds_sample = take_sample(wine.loc[wine['type']=='red',:])
whites_sample = take_sample(wine.loc[wine['type']=='white',:])
wine_sample = pd.concat([reds_sample,whites_sample])
#创建新列，并根据是否在原数据框中设为1和0
wine['in_sample'] = np.where(wine.index.isin(wine_sample.index),1.,0.)
print(pd.crosstab(wine.in_sample,wine.type,margins=True))

#查看成对变量之间的关系
g = sns.pairplot(wine_sample,kind='reg',plot_kws={'ci':False,'x_jitter':0.25,'y_jitter':0.25},hue='type',diag_kind='hist',\
diag_kws={'bins':10,'alpha':1.0},palette=dict(red='red',white='white'),markers=['o','s'],vars=['quality','alcohol','residual_sugar'])
print(g)
plt.suptitle('Histograms and Scatter Plots of Quality,Alcohol,and Residual Sugar',fontsize=14,horizontalalignment='center',\
verticalalignment='top',x=0.5,y=0.999)
plt.show()







