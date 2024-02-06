# 学习材料
[python_100_days](https://github.com/jackfrued/Python-100-Days)

# 包的安装
- pip只会解决包依赖，不会解决环境依赖；
- pip安装应该会快一些；

```shell
#在终端安装 xgboost
pip install xgboost
conda install py-xgboost

#网络终端安装包
conda install -c anaconda pandas
conda install scikit-learn

#安装cv2
conda install opencv         # 网速太慢
pip install opencv-python    # 可以

#其他包
pip install Pillow

#安装basemap
conda install geos
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda install basemap  ####使用清华的镜像安装
conda install -c conda-forge basemap

conda install basemap -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
```

# 包的版本
```shell
#pip版本查看
pip -V

# Python版本查看
python -V

# 包查看
pip list
conda list

print(sns.__version__)   # 包版本
print(os.__file__)       # 包位置
print(dir(os))           # 包结构、模块
```

# 常用代码
```python
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

# 勿扰模式
import warnings
warnings.filterwarnings('ignore')

# 省略plt.show()
%matplotlib inline  
```

# 在终端运行脚本
```python
#在终端运行文件
nohup python /../file.py

#查看文件进程
ps aux|grep python

#结束
kill XXXX
```