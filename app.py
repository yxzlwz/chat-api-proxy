from flask import Flask, request, Response
import requests

app = Flask(__name__)


@app.route('/generativelanguage.googleapis.com/<path:path>',
           methods=['GET', 'POST'])
def googleapis_proxy(path):
    target_url = f'https:/{request.full_path}'

    headers = dict(request.headers)
    headers.pop('Host')
    data = request.get_data()

    response = requests.request(method=request.method,
                                url=target_url,
                                headers=headers,
                                data=data)

    resp = Response(response.content,
                    status=response.status_code,
                    content_type='application/json')
    return resp


@app.route('/api.openai.com/<path:path>', methods=['GET', 'POST'])
def openai_proxy(path):
    target_url = f'https:/{request.full_path}'

    headers = dict(request.headers)
    headers.pop('Host')
    headers['Accept-Encoding'] = "gzip, deflate"
    data = request.get_data()

    response = requests.request(method=request.method,
                                url=target_url,
                                headers=headers,
                                data=data)

    resp = Response(response.content,
                    status=response.status_code,
                    content_type='application/json')
    return resp


@app.route('/')
def index():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
