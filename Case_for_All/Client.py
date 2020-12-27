import requests
import unittest
import json


class BodyType:
    URL_ENCODE = 1
    FORM = 2
    XML = 3
    JSON =4
    FILE = 5
    URL_TOKEN = 'http://127.0.0.1'


class Client(unittest.TestCase):
    def __init__(self, url, method='GET', params=None,body_type=0):
        self.url = url
        self.method = method
        self.body_type = body_type
        self.headers = {}
        self.body = {}
        self.params = params
        self.res = None
        self._type_equality_funcs = {}   #???起什么作用，哪儿会用到？

    def set_headers(self,headers):
        if isinstance(headers,dict):
            self.headers = headers
        else:
            raise Exception('头信息请以字典格式传递')

    def set_headers(self,key,value):
        self.headers[key] = value

    def set_body(self,body):
        if isinstance(body,dict):
            if self.body_type == 1:
                self.set_headers('Content-Type','application/x-www-form-urlencoded')
            elif self.body_type == 3:
                self.set_headers('Content-Type','text/xml')
            elif self.body_type == 4:
                self.set_headers('Content-Type','application/json')
            else:
                raise Exception('正文格式类型参数错误！')
        else:
            raise Exception('正文内容请以字典格式传递，xml正文格式如下：{"xml":xml字符串}')

    def send(self):
        self.method = self.method.upper().strip()
        if self.method == 'GET':
            self.res = requests.get(url=self.url,headers = self.headers, params = self.params )
            return self.res
        elif self.method == 'POST':
            if self.body_type == 1 or 2:
                self.res = requests.post(url=self.url,headers = self.headers,data =self.body)
                return self.res
            elif self.body_type == 3:
                xml = self.body.get('xml')
                self.res = requests.post(url = self.url,headers = self.headers,data = xml)
                return self.res
            elif self.body_type == 4:
                # self.res = requests.post(url = self.url,headers = self.headers, json = self.body) # 原
                self.res = requests.post(url=self.url, headers=self.headers, data=self.body) # 20200511修改
                return self.res
            elif self.body_type == 5:
                self.res = requests.post(url = self.url,headers = self.headers, files = self.body)
                return self.res
            elif self.body_type == 0:
                self.res = requests.post(url = self.url,headers = self.headers)
            else:
                raise Exception('正文格式类型参数错误！')
        else:
            raise Exception('请求方法异常，暂仅支持GET方法和POST方法')


    @property
    def get_token(self):
        client = Client(url=BodyType.URL_TOKEN, method='POST',body_type = BodyType.JSON)
        client.set_headers("Content-Type","application/json")
        data = {'username':'yu','password':'123456'}
        client.set_body(data)
        res= client.send()
        text_info = json.loads(res.text)
        get_token = text_info["token"]
        return get_token

    @property
    def status_code(self):
        if self.res:
            return self.res.status_code
        else:
            return None

    @property
    def response_time(self):
        if self.res:
            return int(round(self.res.elapsed.total_seconds()*1000))
        else:
            return None

    @property
    def text(self):
        if self.res:
            return self.res.text
        else:
            return None

    @property
    def response_to_json(self):
        if self.res:
            return self.res.json()
        else:
            return None

    def check_status_code_is_200(self):
        self.assertEqual(self.status_code, 200, '响应状态码不是200')

    def check_status_code_is(self,code):
        self.assertEqual(self.status_code,code,'响应状态码不是%d' % code)

    def check_response_time_less_than(self,times=200):
        self.assertLess(self.response_time,times,'响应时间超过%d ms'% times)

    def check_json_value(self,path,exp):
        if self.response_to_json:
            first = self.response_to_json.get(path)
        else:
            first = None
        self.assertEqual(first,exp, '值检查失败。实际结果：{first}; 预期结果：{exp}' .format(first=first,exp=exp))

    def log(self,text):
        print(text)




    
