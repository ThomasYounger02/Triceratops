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

# 作图

# 从场景出发

##########################################################################################

# 数据准备1-时间序列

url = "https://raw.githubusercontent.com/Yorko/mlcourse.ai/main/data/ads.csv"
data_ads = pd.read_csv(url)

data_ads['randn'] = np.random.randn(len(data_ads['Ads']))   # 生成一个新列，用于二元绘图
data_ads['date'] = pd.to_datetime(data_ads['Time'])         # 日期格式转换
data_ads['cut_1'] = data_ads['Ads'].map(lambda x: 'H' if x>=16*10000 else('M' if x>=8*10000 else 'L'))
data_ads['cut_2'] = np.where(data_ads['randn']>0,'P', 'NP')

# 数据准备2-设定日期为新的index

new_df = data_ads[['Ads', 'date']].set_index('date')

# 数据准备3-iris

from sklearn.datasets import load_iris
data_iris = pd.DataFrame(load_iris().data, columns=load_iris().feature_names)
data_iris['sample'] = load_iris().target

##########################################################################################

# 分布

##########################################################################################

# 核密度估计

f, ax = plt.subplots(figsize=(15, 10))                                  # create a figure containing a single axes.
    sns.kdeplot(data_ads['Ads'], shade=True, color="r");                     # shade阴影，color曲线和阴影颜色
    sns.kdeplot(data_ads['Ads'], cumulative=True, shade=True, color="r");    # 累计

# 多元平铺密度图

for col in data_iris.columns:
    sns.kdeplot(data_iris[col], shade=True);   #Q:legend如何设定？

# 二元交叉核密度估计 # 有问题

sns.kdeplot(data_ads['Ads'], data_ads['randn'], shade=True, cbar=True);   # cbar颜色棒

# 直方图

sns.distplot(data_ads['Ads'], bins=20, color="r");                              # bins控制直方图划分，cbar颜色棒
sns.distplot(data_ads['Ads'], bins=[x*20000 for x in range(10)], color="r");    # bins控制直方图划分，cbar颜色棒

# 直方图结合密度

sns.displot(data_ads['Ads'], kde=True, color="r"); # 直方图结合密度图

# 箱线图

sns.boxplot(
x, y,
data,
hue,           # 分类用，单个箱线图1拆N
width,         # 箱体的宽度
palette        # 调色板
)

sns.boxplot(data=data_iris,  orient='h');               # 全量数据绘制,v竖放,h横放
sns.boxplot(x=data_iris['sepal length (cm)']);         # 单列数据绘制
sns.boxplot(y=data_iris['sepal length (cm)']);         # 竖放

sns.boxplot(x=data_ads['Ads'], y=data_ads['cut_2'],
# x='Ads', y='cut_2', data=data_ads,                # 列名方法
order=['H', 'M', 'L'],                             # 对标分类数据的范围
width=.6, palette="vlag")                          # width控制箱线宽度

# 箱线图背后的点分布

sns.stripplot(x="Ads", y="cut_1",
data=data_ads,
size=4, linewidth=0, jitter=True, dodge=True)

##########################################################################################

# 时间序列

##########################################################################################
f, ax = plt.subplots(figsize=(16, 9))

x = data_ads['date']
y = data_ads['Ads']
hue_cond = data_ads['cut_2']
sns.lineplot(x, y, hue=hue_cond, data=data_ads);     # 按hue拆分为多条时间序列直线图

# 异动平均+边界+异常值

plotMovingAverage(new_df, 7, plot_intervals=True, scale=1.96, plot_anomalies=True)

##########################################################################################

# 组合作图

##########################################################################################

# 分布+集中点：两侧kde用于分布查看，中间为交叉密度图，可用于判断聚合集中位置

g = sns.JointGrid("Ads", "randn", data_ads,
# xlim=(-6,6),
# ylim=(-5,5)
)
g = g.plot_joint(sns.kdeplot, cmap="Blues", shade=True)
g = g.plot_marginals(sns.kdeplot, shade=True)

##########################################################################################

# pd自带功能

##########################################################################################
pd.plotting.scatter_matrix(data_iris, alpha = 0.3, figsize = (14,8), diagonal = 'kde');   # 两两对比散点图，自身为kde

##########################################################################################

# 相关

##########################################################################################

# 散点图，拆分维度组合后，进行散点图作图

# Q:不能在前面增加 > f, ax = plt.subplots(figsize=(8, 8))

colors = ["black", "lightsteelblue", 'royalblue']
sns.relplot(
data=data_ads,
x="Ads", y="randn",                   # 两列数据
row="year",                           # 按cut2拆分行
col="cut_2",                          # 按cut1拆分列
hue="cut_1",                          # 标识不同的点
palette=colors,                       # 对标hue的颜色数量
kind="scatter",                       # 散点图
height=5,
aspect=.75, facet_kws=dict(sharex=True)
);

# 按row*col组合后拆分子图，每个子图是一个x*y散点图,效果不如sns.relplot(kind=scatter)

g = sns.FacetGrid(data_ads,
row='cut_1',
col="cut_2",
hue="year",
margin_titles=False
)
g.map(sns.regplot,
"Ads", "randn",
data = data_ads,
fit_reg=False,
x_jitter=0.2);

# 相关系数矩阵图

plt.figure(figsize=(10,10))                         # 长宽相等的图更容易查看
plt.title('Correlation of Features')
sns.heatmap(
data.corr(),
linewidths=0.1, vmax=1.0,
square=True,linecolor='white', annot=True
);

# 散点结合线性拟合关系图

# Q:命名和不命名为g的差异？g是seaborn.axisgrid.FacetGrid对象，有什么“方法”可以继续使用g？

g = sns.lmplot(
data=data_iris,
x="sepal length (cm)", y="sepal width (cm)",
hue="sample",                                 # 图一张图内，区分不同的sample点，并分别进行拟合
order=3,
height=5
);

##########################################################################################

# 对比

##########################################################################################

# 按不同col*row组合拆分子图，对比数据分布

# Q：举例不完善，需要更恰当的例子

sns.factorplot(
data=data_ads,
x="Ads", y="cut_2",
# row='行_分类',                 # 可以省略掉多行划分
col='cut_1',
kind='bar'
)

##########################################################################################

# 函数类

##########################################################################################

## 桑基图

from pyecharts import options as opts
from pyecharts.charts import Sankey

def plot_sankey(data, to_sum=False, fig_name='sankey',series_name='legend', title='sankey'):
'''
设定固定列['source','target','value']，画出桑基图。

```
Args:
    data(pd.DF)  -- DataFrame
    to_sum(bool) -- 指定是否对['source','target']进行汇总value的操作
    fig_name(str) -- 图表文件保存名称
    series_name(str) --
    title(str) -- 图表标题

Return:
    None
'''
#是否对数据进行汇总
if to_sum:
    df = pd.DataFrame(data.groupby(['source','target'])['value'].sum()).reset_index()
else:
    df = data[['source','target','value']]

# 生成节点， 先合并源节点和目标节点，然后去除重复的节点，最后输出成 dict 形式
nn = pd.concat([df['source'], df['target']])
nn = nn.drop_duplicates()
nodes = pd.DataFrame(nn, columns=['name']).to_dict(orient='records')

# 生成连接， dict 形式
links = df.to_dict(orient='records')

# 绘制桑基图
sk =(
    Sankey(init_opts=opts.InitOpts(width="800px", height="600px")) # 页面大小
    .add(
        series_name=series_name, # legend
        nodes=nodes,
        links=links,
        # opacity 透明度； curve 弯曲程度； color 色系
        linestyle_opt=opts.LineStyleOpts(opacity=0.2, curve=0.5, color="source"),
        label_opts=opts.LabelOpts(position="right"), # 节点名称
    )
    .set_global_opts(title_opts=opts.TitleOpts(title=title)) # 标题
    .render(f"{fig_name}.html")                                      # 保存成 html 文件
)

```

##########################################################################################

# 时间序列作图

##########################################################################################
def plot_ts(series, title='fig_title', figsize=(16, 9), save=False):
"""
    plot timeseries fig.
    
    Params:
        series - df or df.series, and index need to be a timeseries
        title - figure title

        Return:
            None
    """
    plt.figure(figsize=figsize)
    plt.plot(series)
    plt.title(title)
    plt.grid(True)
    
    if save:
        plt.savefig(f'{title}.jpg')    # 保存图片，跟在每个作图代码的最后，要在show之前.
    plt.show()                         # Q：为什么要加这个？作用是什么？

# 移动平均作图

def moving_average(series, n):
"""
Calculate average of last n observations
"""
return np.average(series[-n:])
def mean_absolute_percentage_error(y_true, y_pred):
return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

def plotMovingAverage(series, window, plot_intervals=False, scale=1.96, plot_anomalies=False):

```
"""
    series - dataframe with timeseries
    window - rolling window size
    plot_intervals - show confidence intervals
    plot_anomalies - show anomalies
"""
rolling_mean = series.rolling(window=window).mean()

plt.figure(figsize=(15,5))
plt.title("Moving average\\n window size = {}".format(window))
plt.plot(rolling_mean, "g", label="Rolling mean trend")

# Plot confidence intervals for smoothed values
if plot_intervals:
    mae = mean_absolute_error(series[window:], rolling_mean[window:])
    deviation = np.std(series[window:] - rolling_mean[window:])
    lower_bond = rolling_mean - (mae + scale * deviation)
    upper_bond = rolling_mean + (mae + scale * deviation)
    plt.plot(upper_bond, "r--", label="Upper Bond / Lower Bond")
    plt.plot(lower_bond, "r--")

    # Having the intervals, find abnormal values
    if plot_anomalies:
        anomalies = pd.DataFrame(index=series.index, columns=series.columns)
        anomalies[series<lower_bond] = series[series<lower_bond]
        anomalies[series>upper_bond] = series[series>upper_bond]
        plt.plot(anomalies, "ro", markersize=10)

plt.plot(series[window:], label="Actual values")
plt.legend(loc="upper left")
plt.grid(True)

```