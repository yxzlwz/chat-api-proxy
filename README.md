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

腾讯云的 Serverless 服务支持海外地域运行，可以用于部署这个项目。


下面是关于如何将这个项目部署到腾讯云函数的简要教程：
