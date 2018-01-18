# data_cleaning
 将不规则数据集整理为标准的csv的形式
 最初始的是分为红酒和白酒两个csv文件，均需要进行清洗。winequality-red.csv和winequality-white.csv
 简单的将两个csv文件合成为一个csv文件。winequality-both.csv
 经过脚本add_type.py之后将酒的属性加到第一列，并将分号改为逗号，标题中多余的双引号去掉，清洗为干净易于处理的csv文件。
 经过wine_quality.py之后对整个dataframe数据框有一定的认识与了解。
