




##########################################################################################

# Pkgs

##########################################################################################
import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文显示问题-设置字体为黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决保存图像是负号'-'显示为方块的问题
sns.set(font='SimHei', font_scale=0.8)        # 解决Seaborn中文显示问题

import warnings                               # 勿扰模式
warnings.filterwarnings('ignore')

%matplotlib inline                            # 句末可以省略分号;

# 样式

sns.set(palette="muted", color_codes=True)    # seaborn样式，根据案例设定

##########################################################################################

# 基础内容

##########################################################################################

# 画布准备

fig, axes = plt.subplots(figsize=(16, 9))            # 常用设定1
fig, axes = plt.subplots(1, 3, figsize=(16, 9))      # 常用设定2
# fig  > Figure，图的外框，可包含多个ax
# ax   > Axes, 图的内框
# axis > Axis, 坐标轴

# 画布操作

plt.xlim(0, 30, 2)  # x轴范围及步长
plt.legend(loc=2)   # 图例设定

# 多图示例

fig, axes = plt.subplots(1, 3, figsize=(15, 10), sharey=True)        # 1行3个子图，整体大小为15*10.

# 左图

sns.distplot(data_ads['Ads'], ax=axes[0]);                            # ax作为参数指定放置的画框

# 中图

sns.distplot(data_ads['Ads'], hist=False, ax=axes[1]);

# 右图

sns.distplot(data_ads['Ads'], kde=False, ax=axes[2]);

# 图片保存

plt.savefig('12月出勤率.jpg')    # 保存图片，跟在每个作图代码的最后

##########################################################################################
### 有效图表

# - 在不歪曲事实的情况下传达正确和必要的信息。
# - 设计简单，你不必太费力就能理解它。
# - 从审美角度支持信息而不是掩盖信息。
# - 信息没有超负荷。