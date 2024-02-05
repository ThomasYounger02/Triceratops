# 有效图表
- 在不歪曲事实的情况下传达正确和必要的信息。
- 设计简单，你不必太费力就能理解它。
- 从审美角度支持信息而不是掩盖信息。
- 信息没有超负荷。

# 常用设定
```python
import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt


import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文显示问题-设置字体为黑体
mpl.rcParams['axes.unicode_minus'] = False    # 解决保存图像是负号'-'显示为方块的问题
mpl.rcParams['font.sans-serif'] = ['KaiTi']
mpl.rcParams['font.serif'] = ['KaiTi']

sns.set(font='SimHei', font_scale=0.8)        # 解决Seaborn中文显示问题

import warnings                               # 勿扰模式
warnings.filterwarnings('ignore')

%matplotlib inline                            # 可以省略plt.show()


# 高分辨率显示
%config InlineBackend.figure_format='retina'

# 样式
sns.set(palette="muted", color_codes=True)    # seaborn样式，根据案例设定
```

# 绘图示例
```python
# 画布准备
fig, ax = plt.subplots(figsize=(16, 9))                # 常用设定1，fig-画布，ax-子图
fig, ax = plt.subplots(1, 3, figsize=(16, 9))          # 常用设定2


# 画布操作
plt.xlim(0, 30, 2)        # x轴范围及步长
plt.legend(loc=2)         # 图例设定


# 多图示例
fig, ax = plt.subplots(1, 3, figsize=(15, 10), sharey=True)      # 1行3个子图，整体大小为15*10.

sns.distplot(data_ads['Ads'], ax=ax[0])                            # 左图，ax作为参数指定放置的画框
sns.distplot(data_ads['Ads'], hist=False, ax=ax[1])                # 中图
sns.distplot(data_ads['Ads'], kde=False, ax=ax[2]);                # 右图


# 图片保存
plt.savefig('./result/pic_name.jpg')                                 # 保存图片，跟在每个作图代码的最后
```

# 常用分类做图
```python
#饼图和柱状图
f,ax = plt.subplots(1, 2, figsize=(18,8))

data['Survived'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
ax[0].set_title('Survived')
ax[0].set_ylabel('')

sns.countplot('Survived', data=data, ax=ax[1])
ax[1].set_title('Survived')

plt.show()
```