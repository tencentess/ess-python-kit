# 腾讯电子签企业版API接入工具包

## 项目说明
项目通过pip工具(`requirements.txt`)引入了腾讯云sdk，补充了调用电子签企业版API所需要的内容，并提供了调用的样例。使用前请先在项目中导入腾讯云sdk。

可以使用下面的命令直接导入:

```bash
pip install -r requirements.txt
```

## 通过 pip 安装腾讯云sdk

您可以通过 pip 安装方式将腾讯云 API Python SDK 安装到您的项目中，如果您的项目环境尚未安装 pip，请详细参见 pip官网 安装。

通过pip方式安装或更新请在命令行中执行以下命令:

```bash
pip install --upgrade tencentcloud-sdk-python
```

中国大陆地区的用户可以使用国内镜像源提高下载速度，例如：`pip install -i https://mirrors.tencent.com/pypi/simple/ --upgrade tencentcloud-sdk-python`。

请注意，如果同时有 python2 和 python3 环境， python3 环境需要使用 pip3 命令安装。

如果只想使用某个具体产品的包，例如云服务器 CVM，可以单独安装，但是注意不能和总包同时工作。`pip install --upgrade tencentcloud-sdk-python-common tencentcloud-sdk-python-cvm`

## 目录文件说明
### api
api目录是对电子签企业版所有API的简单封装，以及调用的Example。
如果需要API更加高级的功能，需要结合业务修改api的封装。

### byfile
byfile目录是电子签企业版的核心场景之一 - 通过文件发起的快速上手样例。
业务方可以结合自己的业务调整，用于正式对接。

### bytemplate
bytemplate目录是电子签企业版的核心场景之一 - 通过模版发起的快速上手样例。
业务方可以结合自己的业务调整，用于正式对接。

### callback
callback目录是电子签企业版对接的回调解密部分。
业务方需要配置好回调地址和加密key，就可以接收到相关的回调了。

### testdata
testdata是一个空白的pdf用于快速发起合同，测试。

### tools
tools目录提供了调用电子签企业版API时涉及到的各种算法样例。 如果不使用sdk调用电子签服务，可参考其中的签名计算方式。

### config.py
里面定义调用电子签企业版API需要的一些核心参数。

## 电子签企业版官网入口
[腾讯电子签企业版](https://cloud.tencent.com/document/product/1323)
