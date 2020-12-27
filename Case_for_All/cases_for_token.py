import requests
import json
import unittest


class cases_for_token(unittest.TestCase):
    '''
    获取token信息
    '''

    def test_token(self):
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
            "username": "api",
            "password": "123456"
        }
        s = requests.Session()
        login_url = 'http://omsceshi.ncamc.com.cn/api/ms-base-server/jwt/token'
        login_ret = s.post(login_url,  data = json.dumps(body), headers = headers)
        ret1 = json.loads(login_ret.text)
        token = ret1["data"]["token"]
        # print(token)
        return token
        # response_time = login_ret.elapsed.microseconds/1000
        # print("响应时间为:{}".format(response_time))


if __name__ == '__main__':
    unittest.main()