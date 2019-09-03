import requests, json

#获取主列表数据，headers信息是从浏览器的控制台
#mutch_type --> 1 -->匹配，  ----> -1 --> 未匹配
def get_all_list_match():
    url = "https://aicp.baidu.com/api/v1/label/cluster_list"

    querystring = {"label_list_type":"0","match_type":"0","ps":"200","version":"20180715","referer":"index","perm_code":"label_all"}

    headers = {
        'Accept': "application/json, text/plain, */*",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Agent': "2dac3764-9741-42b9-ac9b-5cd608b0d5de",
        'Cache-Control': "no-cache",
        'Connection': "keep-alive",
        'Cookie': "BIDUPSID=BE243C8D9090FCC161445F9B0D7E7BE2; PSTM=1562721278; BAIDUID=ED0D9C7944AE8098C28E096DDD7536F5:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; AccountType=PASSPORT; MCITY=-%3A; aicpusername=%E7%96%AF%E7%8B%82%E7%9A%84%E7%88%B7%E7%88%B7%E7%9A%84; Hm_lvt_6cda846867fd596b2ca7a177bac2039f=1566020249,1566104716,1566115190,1566436083; BDUSS=0trdklRbjZNaUZtN21iSk5DfmVDSUdoWnRPaThlTjhFVG9MLTRqTnFyR3Rsb1ZkRUFBQUFBJCQAAAAAAAAAAAEAAABuSjMvt-i~8bXE0q~Sr7XEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK0JXl2tCV5dS; BDSFRCVID=DitOJeCmH6VwoRJwVGYLejiec2KK0gOTHllv31jAHvhdMXkVJeC6EG0Ptf8g0KubFTPRogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0P3J; H_BDCLCKID_SF=tJkD_I_hJKt3qn7I5KToh4Athxob2bbXHDo-LIvg24bcOR5JhfA-3R-e046fLfbkBITBBR5Jtqvvhb3O3M7Shb5yDf6CBn535gjvBMQF5l8-sq0x0bOte-bQypoa0q3TLDOMahkM5h7xOKQoQlPK5JkgMx6MqpQJQeQ-5KQN3KJmhpFu-n5jHjQbjH_D3e; Hm_lpvt_6cda846867fd596b2ca7a177bac2039f=1566546543; H_PS_PSSID=26524_1463_21090_18560_29522_29519_29099_29567_29220; delPer=0; PSINO=2, BIDUPSID=BE243C8D9090FCC161445F9B0D7E7BE2; PSTM=1562721278; BAIDUID=ED0D9C7944AE8098C28E096DDD7536F5:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; AccountType=PASSPORT; MCITY=-%3A; aicpusername=%E7%96%AF%E7%8B%82%E7%9A%84%E7%88%B7%E7%88%B7%E7%9A%84; Hm_lvt_6cda846867fd596b2ca7a177bac2039f=1566020249,1566104716,1566115190,1566436083; BDUSS=0trdklRbjZNaUZtN21iSk5DfmVDSUdoWnRPaThlTjhFVG9MLTRqTnFyR3Rsb1ZkRUFBQUFBJCQAAAAAAAAAAAEAAABuSjMvt-i~8bXE0q~Sr7XEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK0JXl2tCV5dS; BDSFRCVID=DitOJeCmH6VwoRJwVGYLejiec2KK0gOTHllv31jAHvhdMXkVJeC6EG0Ptf8g0KubFTPRogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0P3J; H_BDCLCKID_SF=tJkD_I_hJKt3qn7I5KToh4Athxob2bbXHDo-LIvg24bcOR5JhfA-3R-e046fLfbkBITBBR5Jtqvvhb3O3M7Shb5yDf6CBn535gjvBMQF5l8-sq0x0bOte-bQypoa0q3TLDOMahkM5h7xOKQoQlPK5JkgMx6MqpQJQeQ-5KQN3KJmhpFu-n5jHjQbjH_D3e; Hm_lpvt_6cda846867fd596b2ca7a177bac2039f=1566546543; H_PS_PSSID=26524_1463_21090_18560_29522_29519_29099_29567_29220; delPer=0; PSINO=2; aicpusername=%E7%96%AF%E7%8B%82%E7%9A%84%E7%88%B7%E7%88%B7%E7%9A%84",
        'Host': "aicp.baidu.com",
        'Pragma': "no-cache",
        'Referer': "https://aicp.baidu.com/",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text

def get_all_list_un_match():
    url = "https://aicp.baidu.com/api/v1/label/cluster_list"

    querystring = {"label_list_type":"0","match_type":"-1","ps":"200","version":"20180715","referer":"index","perm_code":"label_all"}

    headers = {
        'Accept': "application/json, text/plain, */*",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Agent': "2dac3764-9741-42b9-ac9b-5cd608b0d5de",
        'Cache-Control': "no-cache",
        'Connection': "keep-alive",
        'Cookie': "BIDUPSID=BE243C8D9090FCC161445F9B0D7E7BE2; PSTM=1562721278; BAIDUID=ED0D9C7944AE8098C28E096DDD7536F5:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; AccountType=PASSPORT; MCITY=-%3A; aicpusername=%E7%96%AF%E7%8B%82%E7%9A%84%E7%88%B7%E7%88%B7%E7%9A%84; Hm_lvt_6cda846867fd596b2ca7a177bac2039f=1566020249,1566104716,1566115190,1566436083; BDUSS=0trdklRbjZNaUZtN21iSk5DfmVDSUdoWnRPaThlTjhFVG9MLTRqTnFyR3Rsb1ZkRUFBQUFBJCQAAAAAAAAAAAEAAABuSjMvt-i~8bXE0q~Sr7XEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK0JXl2tCV5dS; BDSFRCVID=DitOJeCmH6VwoRJwVGYLejiec2KK0gOTHllv31jAHvhdMXkVJeC6EG0Ptf8g0KubFTPRogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0P3J; H_BDCLCKID_SF=tJkD_I_hJKt3qn7I5KToh4Athxob2bbXHDo-LIvg24bcOR5JhfA-3R-e046fLfbkBITBBR5Jtqvvhb3O3M7Shb5yDf6CBn535gjvBMQF5l8-sq0x0bOte-bQypoa0q3TLDOMahkM5h7xOKQoQlPK5JkgMx6MqpQJQeQ-5KQN3KJmhpFu-n5jHjQbjH_D3e; H_PS_PSSID=26524_1463_21090_18560_29522_29519_29099_29567_29220; delPer=0; PSINO=6; Hm_lpvt_6cda846867fd596b2ca7a177bac2039f=1566716742, BIDUPSID=BE243C8D9090FCC161445F9B0D7E7BE2; PSTM=1562721278; BAIDUID=ED0D9C7944AE8098C28E096DDD7536F5:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; AccountType=PASSPORT; MCITY=-%3A; aicpusername=%E7%96%AF%E7%8B%82%E7%9A%84%E7%88%B7%E7%88%B7%E7%9A%84; Hm_lvt_6cda846867fd596b2ca7a177bac2039f=1566020249,1566104716,1566115190,1566436083; BDUSS=0trdklRbjZNaUZtN21iSk5DfmVDSUdoWnRPaThlTjhFVG9MLTRqTnFyR3Rsb1ZkRUFBQUFBJCQAAAAAAAAAAAEAAABuSjMvt-i~8bXE0q~Sr7XEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK0JXl2tCV5dS; BDSFRCVID=DitOJeCmH6VwoRJwVGYLejiec2KK0gOTHllv31jAHvhdMXkVJeC6EG0Ptf8g0KubFTPRogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0P3J; H_BDCLCKID_SF=tJkD_I_hJKt3qn7I5KToh4Athxob2bbXHDo-LIvg24bcOR5JhfA-3R-e046fLfbkBITBBR5Jtqvvhb3O3M7Shb5yDf6CBn535gjvBMQF5l8-sq0x0bOte-bQypoa0q3TLDOMahkM5h7xOKQoQlPK5JkgMx6MqpQJQeQ-5KQN3KJmhpFu-n5jHjQbjH_D3e; H_PS_PSSID=26524_1463_21090_18560_29522_29519_29099_29567_29220; delPer=0; PSINO=6; Hm_lpvt_6cda846867fd596b2ca7a177bac2039f=1566716742; aicpusername=%E7%96%AF%E7%8B%82%E7%9A%84%E7%88%B7%E7%88%B7%E7%9A%84",
        'Host': "aicp.baidu.com",
        'Pragma': "no-cache",
        'Referer': "https://aicp.baidu.com/",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        'Postman-Token': "dddd5c24-51f6-4b3e-ad2c-31b886a83ef4,2793c584-9d6e-4da2-bf9f-3b1e89cf7ebb",
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text

#获取单独的子列表数据，headers信息是从浏览器的控制台
def get_child_list_match(perList):
    url = "https://aicp.baidu.com/api/v1/label/list_in_cluster"
    querystring = {"cluster_id":perList['cluster_id'],"source":perList['source'],"type_id":perList['type_id'],
    "label_list_type":"0","match_type":"0","ps":"200","version":"20180715","referer":"index","perm_code":"label_all"}
    headers = {
        'Accept': "application/json, text/plain, */*",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Agent': "2dac3764-9741-42b9-ac9b-5cd608b0d5de",
        'Cache-Control': "no-cache",
        'Connection': "keep-alive",
        'Cookie': "BIDUPSID=BE243C8D9090FCC161445F9B0D7E7BE2; PSTM=1562721278; BAIDUID=ED0D9C7944AE8098C28E096DDD7536F5:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; AccountType=PASSPORT; MCITY=-%3A; aicpusername=%E7%96%AF%E7%8B%82%E7%9A%84%E7%88%B7%E7%88%B7%E7%9A%84; Hm_lvt_6cda846867fd596b2ca7a177bac2039f=1566020249,1566104716,1566115190,1566436083; BDUSS=0trdklRbjZNaUZtN21iSk5DfmVDSUdoWnRPaThlTjhFVG9MLTRqTnFyR3Rsb1ZkRUFBQUFBJCQAAAAAAAAAAAEAAABuSjMvt-i~8bXE0q~Sr7XEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK0JXl2tCV5dS; BDSFRCVID=DitOJeCmH6VwoRJwVGYLejiec2KK0gOTHllv31jAHvhdMXkVJeC6EG0Ptf8g0KubFTPRogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0P3J; H_BDCLCKID_SF=tJkD_I_hJKt3qn7I5KToh4Athxob2bbXHDo-LIvg24bcOR5JhfA-3R-e046fLfbkBITBBR5Jtqvvhb3O3M7Shb5yDf6CBn535gjvBMQF5l8-sq0x0bOte-bQypoa0q3TLDOMahkM5h7xOKQoQlPK5JkgMx6MqpQJQeQ-5KQN3KJmhpFu-n5jHjQbjH_D3e; Hm_lpvt_6cda846867fd596b2ca7a177bac2039f=1566546543; H_PS_PSSID=26524_1463_21090_18560_29522_29519_29099_29567_29220; delPer=0; PSINO=2",
        'Host': "aicp.baidu.com",
        'Pragma': "no-cache",
        'Referer': "https://aicp.baidu.com/",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        'cache-control': "no-cache"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.url)
    dataJson = json.loads(response.text)
    listJson = dataJson['data']['list']
    print("子列表数据项匹配：" + str(dataJson['data']['total']))
    for perList in listJson:
        out_data_list_child(perList)

def get_child_list_un_match(perList):
    url = "https://aicp.baidu.com/api/v1/label/list_in_cluster"
    querystring = {"cluster_id":perList['cluster_id'],"source":perList['source'],"type_id":perList['type_id'],
    "label_list_type":"0","match_type":"-1","ps":"200","version":"20180715","referer":"index","perm_code":"label_all"}
    headers = {
        'Accept': "application/json, text/plain, */*",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Agent': "2dac3764-9741-42b9-ac9b-5cd608b0d5de",
        'Cache-Control': "no-cache",
        'Connection': "keep-alive",
        'Cookie': "BIDUPSID=BE243C8D9090FCC161445F9B0D7E7BE2; PSTM=1562721278; BAIDUID=ED0D9C7944AE8098C28E096DDD7536F5:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; AccountType=PASSPORT; MCITY=-%3A; aicpusername=%E7%96%AF%E7%8B%82%E7%9A%84%E7%88%B7%E7%88%B7%E7%9A%84; Hm_lvt_6cda846867fd596b2ca7a177bac2039f=1566020249,1566104716,1566115190,1566436083; BDUSS=0trdklRbjZNaUZtN21iSk5DfmVDSUdoWnRPaThlTjhFVG9MLTRqTnFyR3Rsb1ZkRUFBQUFBJCQAAAAAAAAAAAEAAABuSjMvt-i~8bXE0q~Sr7XEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK0JXl2tCV5dS; BDSFRCVID=DitOJeCmH6VwoRJwVGYLejiec2KK0gOTHllv31jAHvhdMXkVJeC6EG0Ptf8g0KubFTPRogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0P3J; H_BDCLCKID_SF=tJkD_I_hJKt3qn7I5KToh4Athxob2bbXHDo-LIvg24bcOR5JhfA-3R-e046fLfbkBITBBR5Jtqvvhb3O3M7Shb5yDf6CBn535gjvBMQF5l8-sq0x0bOte-bQypoa0q3TLDOMahkM5h7xOKQoQlPK5JkgMx6MqpQJQeQ-5KQN3KJmhpFu-n5jHjQbjH_D3e; Hm_lpvt_6cda846867fd596b2ca7a177bac2039f=1566546543; H_PS_PSSID=26524_1463_21090_18560_29522_29519_29099_29567_29220; delPer=0; PSINO=2",
        'Host': "aicp.baidu.com",
        'Pragma': "no-cache",
        'Referer': "https://aicp.baidu.com/",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        'cache-control': "no-cache"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.url)
    dataJson = json.loads(response.text)
    listJson = dataJson['data']['list']
    print("子列表数据项未匹配：" + str(dataJson['data']['total']))
    for perList in listJson:
        out_data_list_child(perList)

#打印每一列到txt中 
def out_data_list_child(outListJson):
    cluster_id = outListJson['cluster_id']
    question = outListJson['question']
    count = outListJson['count']
    match_type_value = outListJson['match_type_value']
    type_id_value = outListJson['type_id_value']
    # with open('机器人训练-从列表.txt', 'a+', encoding='utf-8') as f:
    with open('机器人训练-从列表.txt', 'a', encoding='utf-8') as f:
        f.write(str(cluster_id) + match_type_value +'|' + question + '|'+str(count) + '|'+ match_type_value + '|' + type_id_value +'\n')
    
#打印每一列到txt中
def out_data_list_index(outListJson):
    cluster_id = outListJson['cluster_id']
    question = outListJson['question']
    count = outListJson['count']
    match_type_value = outListJson['match_type_value']
    type_id_value = outListJson['type_id_value']
    with open('机器人训练-主列表.txt', 'a', encoding='utf-8') as fper:
        fper.write(str(cluster_id) + match_type_value + '|' + question + '|'+str(count) + '|'+ match_type_value + '|' + type_id_value +'\n')

def main():
    indexResponseMatch = get_all_list_match()
    dataJsonMatch = json.loads(indexResponseMatch)
    print("匹配主列表" + str(dataJsonMatch['data']['total']))
    listJsonMatch = dataJsonMatch['data']['list']

    indexResponseUnMatched = get_all_list_un_match()
    dataJsonUnMatched = json.loads(indexResponseUnMatched)
    print("未匹配主列表" + str(dataJsonUnMatched['data']['total']))
    listJsonUnMatched = dataJsonUnMatched['data']['list']

    print("开始写文件")
    with open('机器人训练-主列表.txt', 'a', encoding='utf-8') as fm:
        fm.write('聚类ID|用户问法|提问次数|匹配类型|匹配内容' + '\n')

    with open('机器人训练-从列表.txt', 'a', encoding='utf-8') as fc:
        fc.write('聚类ID|用户问法|提问次数|匹配类型|匹配内容' + '\n')
    
    print("写入匹配数据")
    for perListMacth in listJsonMatch:
        #打印主列表
        out_data_list_index(perListMacth)
        #打印从列表
        childResponse = get_child_list_match(perListMacth)

    print("写入未匹配数据")
    for perListUnMatch in listJsonUnMatched:
        #打印主列表
        out_data_list_index(perListUnMatch)
        #打印从列表
        childResponse = get_child_list_un_match(perListUnMatch)   
    print("文件写入完成")
if __name__ == '__main__':
    main()