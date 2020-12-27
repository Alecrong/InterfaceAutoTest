import requests
import json


headers = {
            "Connection": "keep-alive",
            "Content-Length": "39",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "*/*",
            "Referer": "http://omsceshi.ncamc.com.cn/login",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9"
}

body = {
    "username":"test",
    "password":"123456"
}

s = requests.Session()
login_url = "http://omsceshi.ncamc.com.cn/api/ms-base-server/jwt/token"
login_ret = s.post(login_url,data=json.dumps(body),headers = headers)
print(login_ret.text)
print('*'*100)
# token = login_ret.json()["token"]
ret1 = json.loads(login_ret.text)
token = ret1["data"]["token"]
print(token)


get_url = "http://omsceshi.ncamc.com.cn/api/operation-cm-deal-data/notUpload-excel/query?"
params = {"bizDate":"2020-04-06",
         "businessScene":"4000"
}
get_ret = requests.get(url = get_url, params = params)
print(get_ret.url)
print(get_ret.encoding)
print(get_ret.status_code)
print(get_ret.content)  # 获得byte数据


post_url = "http://omsceshi.ncamc.com.cn/api/operation-finance-product/finance-account/trade-info-maintain/payment/add"
data = {
 "tradeDate": "2020-05-09",
 "productCode": "BX0001",
 "valuationId": "XTI013",
 "finProTypeValue": "3",
 "finProName": "XTI001复制5",
 "investCategoryValue": "IC_FS",
 "money": "5111734.00",
 "quantity": "5111734.00",
 "interest": "1751.00",
 "assetId": "75",
 "receiptBankText": "农行分红产品托管专户 11-210101040008882",
 "remarks": "20200513 接口测试"
}

post_headers = {}
post_headers["Content-Type"] = "application/json"
post_headers["Authorization"] = token
print("data的数据类型是：%s" % type(data))
post_ret = requests.post(url = post_url, json = data, headers = post_headers)
print(post_ret.url)
print(post_ret.headers)
print("该POST请求的cookie是：%s" % post_ret.cookies)
print(post_ret.status_code)
post_ret_dict = json.loads(post_ret.text)
print(post_ret_dict)


# 上传文件
# upload_file = {'file':open('report.xls','rb')}
# r = requests.post(url = post_url, files = upload_file)


