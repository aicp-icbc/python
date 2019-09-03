import requests

word = "信用卡啊"

url = "https://www.baidu.com/sugrec"

querystring = {"pre":"1","p":"3","ie":"utf-8","json":"1","prod":"pc","from":"pc_web","wd":word,"csor":"4"}

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36 QIHU 360EE",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "e939e72c-8aad-454a-a6fc-4d9b274f8746,327f6e96-dee5-49e2-83c8-60077f60fcca",
    'Host': "www.baidu.com",
    'Accept-Encoding': "gzip, deflate, br",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)