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
conda install opencv   #网速太慢
pip install opencv-python    #可以

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
```
