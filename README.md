# Bachelor_Graduation
本科毕业设计（基于机器学习的新闻标题系统）

bert_base中文预训练模型训练NLPCC2017 Task2新闻标题分类数据集的句向量放在百度网盘链接里，有需要的看客自取~

链接：https://pan.baidu.com/s/11aCCEZ1XaYa6z4Mne9qx6Q 
提取码：8m01 

__注意所有路径改为本地绝对路径！！__

## 一、系统环境配置

Python：3.8.13

操作系统：Windows

数据库：MySQL

Web框架：Flask

模型训练：sklearn

1.Anaconda创建虚拟环境

`conda create -n Graduation python=3.8`

命令行切换到对应目录

2.安装第三方库

`pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple`

3.将数据导入数据库

`mysql -u root -p --local-infile=1 < D:\Bachelor_Graduation\Bachelor_Graduation.sql`

## 二、模型训练

1.执行preprocess.ipynb

2.目录下自动生成model文件夹，里面存放训练好的模型pkl格式文件

## 三、系统启动

运行命令`python main.py`，在浏览器端输入127.0.0.1:5000即可

查看MySQL数据库中用户和管理员表可以得到用户名和密码，登录后可使用该系统