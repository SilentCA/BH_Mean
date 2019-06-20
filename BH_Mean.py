# -*- coding=utf-8 -*-
''' 计算市值加权平均BH
'''

import pandas as pd
import logging

# logging setting
logging.basicConfig(level=logging.INFO)


# Market Capitalization file
MARKET_CAP_FILE = 'Market capitalization.xlsx'
# BH file
BH_FILE = 'BH.xlsx'
# BH Mean file
BH_MEAN_FILE = 'BH_Mean.xlsx'


# 读取数据
logging.info('读取数据')
with open(MARKET_CAP_FILE,'rb') as fin:
    market_cap = pd.read_excel(fin, index_col=0)

with open(BH_FILE,'rb') as fin:
    bh = pd.read_excel(fin, index_col=0)

# 每个月份的每个公司的市值占比
logging.info('计算市值占比')
share = pd.DataFrame(index=market_cap.index, columns=market_cap.columns)
for month in market_cap.index[1:]:
    month_sum = 0
    # 计算每个月份的所有公司的市值总和，不包括bh为0的公司
    for stock in market_cap.columns:
        is_zero = bool(bh[month][stock])
        month_sum = month_sum + market_cap[stock][month] * is_zero
    # 计算市值占比
    for stock in market_cap.columns:
        share[stock][month] = market_cap[stock][month] / month_sum

# BH加权平均
logging.info('计算BH加权平均')
bh_mean = pd.DataFrame(index=bh.index, columns=bh.columns)
for stock in bh.index:
    for month in bh.columns[1:]:
        bh_mean[month][stock] = bh[month][stock] * share[stock][month]


# 保存文件
#share.to_excel('share.xlsx')
bh_mean.to_excel(BH_MEAN_FILE)
