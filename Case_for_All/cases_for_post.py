import requests
from Case_for_All.cases_for_token import *
import json

url = "http://omsceshi.ncamc.com.cn/api/operation-finance-product/finance-account/trade-info-maintain/payment/add"
# headers = {
#     'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOiJjNTY3MjM0MjEwNTM0NDczYWViMGJjODZkOGVmMzc4YiIsInRva2VuIjoiZWYwZjliZThjMzVjZjJkMThkNDY2ZDUxOWNhNmJhNDkiLCJ1c2VyQ29kZSI6InRlc3QifQ.fQ5pVIJDCQHGE8ChnQxHYbt5ybP06FayX9lkvAZzFp8',
#     'Content-Type': 'application/json'
# }
headers = {}
cft = cases_for_token()
token = cft.test_token()
headers["Authorization"] = token
headers["Content-Type"] = "application/json"
print(headers)

body1 = {'tradeDate': '2020-05-11', 'productCode': 'BX0001', 'valuationId': 'XTI013', 'finProTypeValue': '3', 'finProName': 'XTI001复制5', 'investCategoryValue': 'IC_FS', 'money': '5111734.00', 'quantity': '5111734.00', 'interest': '1751.00', 'assetId': '75', 'receiptBankText': '农行分红产品托管专户 11-210101040008882', 'remarks': '20200511 接口测试'}
body = json.dumps(body1)
print(type(body))


ret = requests.post(url = url,data= body,headers = headers)

print(ret.text)