# Chat API Proxy

## 简介

这个项目是一个基于 Flask 的 API 转发服务，可以用于转发特定域名下的请求，并将结果返回给客户端。

## 使用

### 环境和依赖

目前的 requirements.txt 中列出的依赖适用于 Python 3.9+。

理论上讲，你的计算机上有 Python3 且已安装 Flask 和 requests 库就应该可以使用。

### 转发说明和使用示例

我们假设你的运行地址是 `http://127.0.0.1:9000`。

- 请将 `https://api.openai.com/...` 下的请求转发到 `http://127.0.0.1:9000/api.openai.com/...`
- 请将 `https://generativelanguage.googleapis.com/...` 下的请求转发到 `http://127.0.0.1:9000/generativelanguage.googleapis.com/...`

对于 Python 中调用 OpenAI 的示例：

```python
from openai import OpenAI

client = OpenAI(
    api_key="<API_KEY>",
    base_url='http://127.0.0.1:9000/api.openai.com/v1',
)

response = client.chat.completions.create(...)
...
```

## 部署到腾讯云函数

### 函数部署

腾讯云的 Serverless 服务支持海外地域运行，可以用于部署这个项目。

下面是关于如何将这个项目部署到腾讯云函数的简要教程：

1. 在 [Release](https://github.com/yxzlwz/chat-api-proxy/releases/latest) 中下载文件 `chat-api-proxy.zip`，或将代码下载到本地后压缩为zip文件（需包含`app.py` `scf_bootstrap` `requirements.txt`）

2. 打开 [腾讯云云函数控制台](https://console.cloud.tencent.com/scf/list?rid=25&ns=default)，然后点击新建。

![1](https://github.com/yxzlwz/chat-api-proxy/assets/75941562/b9234f37-11dd-4080-8cef-579bfd9e8359)


3. 配置如下信息：
   - 页面上方选择“从头开始”
   - 函数类型选择“Web函数”
   - 函数名称任取，例如 `chat-proxy-api`
   - 地域建议选择东京或新加坡，**强烈不建议选择香港**，~~不会有人选择内地的对吧~~
   - 运行环境选择 `Python 3.9`

4. 下拉到函数代码处，选择“本地上传zip包”，上传第1步获取的zip包

![2](https://github.com/yxzlwz/chat-api-proxy/assets/75941562/300822fb-f7bc-468e-b4f0-4b289c52f99b)

5. 其余项目按需修改即可，大多数人可直接使用默认，然后进入下一步，耐心等待创建完成

6. 创建完成后会跳转到函数管理界面，点击“编辑”，将选项中的“执行超时时间”设置为30秒（截图中为修改前的状态）

![3](https://github.com/yxzlwz/chat-api-proxy/assets/75941562/be3b3d19-cdbb-4cdf-92d8-170f5279fe5f)

7. 点击页面上方的“函数代码”，等待编辑器加载完成后在编辑器上方选项中点击 `终端>新建终端`（可能被折叠在三个点中），执行如下命令：

```bash
cd src
/var/lang/python39/bin/python3.9 -m pip install -r requirements.txt --target=.
```

![4](https://github.com/yxzlwz/chat-api-proxy/assets/75941562/44aa3ebe-83a3-4a22-87dc-2baedc59af75)

8. 等待命令运行结束后点击“部署”，看到部署成功提示后点击“测试”，看到输出“Hello, World!”即代表成功

![5](https://github.com/yxzlwz/chat-api-proxy/assets/75941562/a87bfc26-886b-4e91-af4c-e52b4c386557)

**此时，我们的云函数已经部署完成。** 你可以通过测试按钮旁提供的函数域名进行访问。例如此时要在 Python 中使用：

```python
from openai import OpenAI

client = OpenAI(
    api_key="<API_KEY>",
    base_url='https://service-xxxxxxxx.jp.tencentapigw.com/release/api.openai.com/v1',
)

response = client.chat.completions.create(...)
...
```

腾讯云为新用户提供了一定的免费额度，为了服务稳定性，建议大家向账户中充值一元。如果你需要绑定自定义域名使用，请继续阅读下面的内容。

### 绑定自定义域名

有空再来更新。
