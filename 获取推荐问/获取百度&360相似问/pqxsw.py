import requests, json

def get_360_tuijian(line):
    
    url = "https://sug.so.360.cn/suggest"

    word = line

    querystring = {"encodein":"utf-8","encodeout":"utf-8","format":"json","fields":"word",
    "mid":"7f1a3543b933808025bcc4ecd48a4e66","huid":"11vniaFEOYOghcLbDUsniob%2FVeybehzhkRbqhEldti7dQ%3Q","word": word}
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36 QIHU 360EE",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "a8445b5a-e973-4e64-afeb-c3f2f1eac7e2,d6f0931b-8cf4-42d7-b65e-e4f1e812ea1b",
        'Host': "sug.so.360.cn",
        'Accept-Encoding': "gzip, deflate, br",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response360 = requests.request("GET", url, headers=headers, params=querystring)
    outLineJsonStr360 = response360.text
    # print(outLineJsonStr360)
    #连接成功，取得返回值
    if(len(outLineJsonStr360) > 4):
        outLineJson360 = json.loads(outLineJsonStr360)
        #判断返该关键词是否有相关问题
        if(len(outLineJsonStr360) > 300):
            sugestJsonList360 = outLineJson360['result']
            for sugest360 in sugestJsonList360:
                # print(sugest360["word"])
                out_write(sugest360["word"])
        else:
            # print(outLineJson360["query"])
            out_write(outLineJson360["query"])

#获取百度的推荐问
def get_bd_tuijian(line):

    word = line

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
    #将字符串转json
    outLineJsonStrBd =  response.text
    if(len(outLineJsonStrBd) > 4):
        outLineJsonBd = json.loads(outLineJsonStrBd)
        #判断返该关键词是否有相关问题--根据返回总长度
        if(len(outLineJsonStrBd) > 30):
            sugestJsonListBd = outLineJsonBd['g']
            for sugestBd in sugestJsonListBd:
                # print(sugestBd["q"])
                out_write(sugestBd["q"])
        else:
            # print(outLineJsonBd["q"])
            out_write(outLineJsonBd["q"])

#写入单行
def out_write(outLine):
    with open('tj.txt', 'a+', encoding='utf-8') as f:
        f.write(outLine + '\n')

def main():
    print("\n关键词列表文件 -- 开始读取\n")
    with open('wt.txt', 'r+', encoding='utf-8') as f:
        for line in f:
            print("写入相关推荐问题： " + line)
            get_bd_tuijian(line)
            get_360_tuijian(line)
    print("\n关键词列表文件 -- 写入完成")

if __name__ == '__main__':
    main()