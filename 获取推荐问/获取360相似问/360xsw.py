import requests, json

def get_360_tuijian(line):

    url = "https://sug.so.360.cn/suggest"

    word = line

    querystring = {"encodein":"utf-8","encodeout":"utf-8","format":"json","fields":"word","word": word}
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

    response = requests.request("GET", url, headers=headers, params=querystring)
    outLineJsonStr = response.text
    print(outLineJsonStr)
    outLineJson = json.loads(outLineJsonStr)
    #判断返该关键词是否有相关问题
    if(len(outLineJson["result"]) > 10):
        sugestJsonList = outLineJson['result']
        for sugest in sugestJsonList:
            print(sugest["word"])
            # out_write(sugest["word"])
    else:
        print(outLineJson["query"])
        # out_write(outLineJson["query"])


def out_write(outLine):
    with open('tj.txt', 'a+', encoding='utf-8') as f:
        f.write(outLine)

def main():
    print("关键词列表文件 -- 开始读取")
    get_360_tuijian("色情")
    get_360_tuijian("信用卡挂失")
    # with open('wt.txt', 'r+', encoding='utf-8') as f:
    #     for line in f:
    #         print("写入相关推荐问题： " + line)
    #         get_360_tuijian(line)
    print("关键词列表文件 -- 写入完成")

if __name__ == '__main__':
    main()