# -*- coding=utf-8 -*-
''' 计算市值加权平均BH
'''

import pandas as pd
import logging

# logging setting
logging.basicConfig(level=logging.INFO)


# Market Capitalization file
MARKET_CAP_FILE = './docs/Market capitalization.xlsx'
# BH file
BH_FILE = './docs/BH.xlsx'
# BH Mean file
BH_MEAN_FILE = 'BH_Mean.xlsx'


# 读取数据
logging.info('读取数据')
with open(MARKET_CAP_FILE,'rb') as fin:
    # 使用首列作为index
    market_cap = pd.read_excel(fin, index_col=0)
    # 将表中的空白单元格换成0
    market_cap.fillna(0, inplace=True)

with open(BH_FILE,'rb') as fin:
    # 使用首列作为index
    bh = pd.read_excel(fin, index_col=0)
    # 将表中的空白单元格换成0
    bh.fillna(0, inplace=True)

# 每个月份的每个公司的市值占比
logging.info('计算市值占比')
share = pd.DataFrame(index=bh.index, columns=bh.columns)
share['stockname'] = bh['stockname']
for month in bh.columns[1:]:
    month_sum = 0
    # 计算每个月份的所有公司的市值总和，不包括BH为0的公司
    for stock in bh.index:
        # 该公司的BH是否为0
        is_zero = bool(bh[month][stock])
        month_sum = month_sum + market_cap[stock][month] * is_zero
    # 计算市值占比
    for stock in bh.index:
        share[month][stock] = market_cap[stock][month] / month_sum

# BH加权平均
logging.info('计算BH加权平均')
bh_mean = pd.DataFrame(index=bh.index, columns=bh.columns)
bh_mean['stockname'] = bh['stockname']
for stock in bh.index:
    for month in bh.columns[1:]:
        bh_mean[month][stock] = bh[month][stock] * share[month][stock]


# 保存文件
#share.to_excel('share.xlsx')
bh_mean.to_excel(BH_MEAN_FILE)
