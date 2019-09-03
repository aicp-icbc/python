import requests, json

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

    #截取json字符串
    # outLineJsonStr = response.text[6:-1]
    #将字符串转json
    outLineJsonStr =  response.text
    outLineJson = json.loads(outLineJsonStr)
    #判断返该关键词是否有相关问题
    if(len(outLineJsonStr) > 30):
        sugestJsonList = outLineJson['g']
        for sugest in sugestJsonList:
            out_write(sugest["q"])
    else:
         out_write(outLineJson["q"])

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
    print("\n关键词列表文件 -- 写入完成")

if __name__ == '__main__':
    main()