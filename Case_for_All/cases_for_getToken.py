from Client import *


class cases_for_getToken(unittest.TestCase):
    '''获取token接口'''
    url = 'http://omsceshi.ncamc.com.cn/api/ms-base-server/jwt/token'  # 声明接口地址
    def test_getToken(self):
        data = {
                "username":"yu",
                "password":"123456"
                }    # 声明接口body体的json内容
        # header = {
        #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ",
        #     "Accept": "*/*",
        #     "Accept-Language": "zh-CN,zh;q=0.9",
        #     "Accept-Encoding": "gzip, deflate",
        #     "Content-Type": "application/json",
        #     "X-Requested-With": "XMLHttpRequest",
        #     "Content-Length": "39",
        #     "Connection": "keep-alive"
        # }
        client = Client(url=self.url, method='POST', body_type=BodyType.JSON)  # 初始化cilent类
        # client.set_headers(header)
        client.set_headers("Content-Type","application/json")  # 设置接口头文件
        client.set_body(data)  # 设置接口的body
        res = client.send()  # 发送请求
        print(res.text)
        text_info = json.loads(res.text)  # 把返回体转换成字典类型
        print('*'*100)
        print(text_info)
        # get_token = text_info["token"]  # 获取返回体中token字段的内容
        get_token = text_info["data"]["token"]
        client.check_status_code_is_200()  # 校验接口响应是否等于200
        client.check_response_time_less_than(1000)  # 校验接口请求时间是否大于1000ms
        return get_token


if __name__ == '__main__':
    unittest.main()
