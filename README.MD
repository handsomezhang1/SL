# 项目文件树
整个项目工程结构如下（Git默认设置不能跟踪空文件夹，需要手动创建）
```
SignLanguageRecognition
 ├── config
 │   ├── Net.cfg
 │   ├── SLR_dataset.cfg
 │   ├── SLR_server.cfg
 │   └── __init__.py
 ├── data
 │   └── SLR_dataset
 │       ├── dictionary.txt
 │       ├── processed/
 │       ├── txt2mat.m
 │       ├── xf500_body_depth_mat/
 │       ├── xf500_body_depth_mat.zip
 │       ├── xf500_body_depth_txt/
 │       ├── xf500_body_depth_txt.zip
 │       ├── xf500_color_video/
 │       └── xf500_depth_video/
 ├── data_preprocess.py
 ├── log
 │   ├── SLR_output.log
 │   └── SLR_server.log
 ├── model
 │   └── SLR
 │       └── blstm_output50_input36x24.pkl
 ├── nnet
 │   ├── AutoEncoder.py
 │   ├── blstm.py
 │   ├── lstm.py
 │   └── __init__.py
 ├── requirements.txt
 ├── SLR_flask_server.py
 ├── test.py
 ├── test_server.http
 ├── train.py
 └── utils
     ├── keyframes.py
     ├── logger.py
     ├── parse_config.py
     ├── plot_data.py
     ├── utils.py
     └── __init__.py
```
# 环境配置
+ Ubuntu 18.04 / Windows 10
+ VSCode + Python 3.7
+ PyTorch 1.2.0
# 操作流程
## 安装软件包
```shell
$ pip install -r requirements.txt
```

## 数据预处理
```shell
$ python data_preprocess.py
```
可以在源代码中修改参数，生成数据在`data\SLR_dataset\processed`

## 训练
```shell
$ python train.py
```
## 测试
```shell
$ python test.py
```
训练和测试结果记录在日志文件（`log/`）中，终端也会显示；模型文件保存在`model/`文件夹下
## 服务端运行
```shell
$ python SLR_flask_server.py
```
服务端接口设计较为简单，仅需要1个GET操作和1个POST操作即可，GET操作用来请求系统参数列表，POST用来连接手语词识别的方法，得到数据预测的识别结果。
|接口名称|调用方法|请求参数|返回值说明|
|:----:|:----:|:----:|:----:|
|getSysParameter|GET|-|success：表示操作是否成功；keyframes_num：关键帧数量；frame_len：帧长度；crop_size：图片裁剪大小；|
|predict|POST|keyframes_num：关键帧数量；frame_len：帧长度；skeleton_data：骨骼关节点位置数据，大小约束为keyframes_num×frame_len；|success：表示操作是否成功；prediction：预测结果；|

