import unittest
import xlrd
import xlwt
import json
from xlrd import open_workbook
from xlutils.copy import copy
from Case_for_All.Client import *
from Case_for_All.cases_for_token import *
from Case_for_All import HTMLTestRunner
from Case_for_All.email_Smtp import email_Smtp


class run3_excel():
    '''读取excel文件
    num_success
    num_fail
    strLast
    workbook
    sheet
    rbook
    wbbok
    w_sheet
    
    url
    method
    info
    header
    body_type
    exp-code
    
    '''
    def test_excel(self,table_name):
        num_success = 0
        num_fail = 0
        strLast = "接口测试结果报告\n"
        workbook = xlrd.open_workbook(table_name)
        sheet = workbook.sheet_by_index(0)
        rbook = xlrd.open_workbook(table_name,formatting_info = False) # 打开文件
        wbook = copy(rbook)
        w_sheet = wbook.get_sheet(0)  # 索引sheet表
        for i in range(1,sheet.nrows):
            configs = sheet.row_values(i)
            url = configs[2]
            method1= configs[3]
            method = method1.upper().strip()
            info1 = configs[4]
            header = json.loads(info1)
            headers = header["Content-Type"]
            # print('&'*100)
            # print(headers)
            body_type = configs[5]
            exp_code = configs[7]
            if method == 'GET':
                info2 = configs[6]
                client = Client(url = url, method = method,params = info2)
                cft = cases_for_token()
                token = cft.test_token()
                client.set_headers("Authorization",token)
                # print('#'*100)
                # print(headers)
                res = client.send()
                # client.check_status_code_is_200()
                # text_info = json.loads(res.text)  # 把返回体转换成字典类型
                if res.content:
                    client.check_status_code_is_200()
                    # print(res.text)
                    try:
                        text_info=json.loads(res.text)
                    except Exception as err:
                        print("[error]:http响应类型错误")
                    status = text_info["status"]
                    if int(exp_code) == status:
                        num_success += 1
                        str1 = u"测试结果：通过\n"
                        strLast += res.url + str1
                        w_sheet.write(i,10,str1)
                        w_sheet.write(i,8,status)
                        w_sheet.write(i,9,res.text)
                        wbook.save(table_name)
                    else:
                        txt = u"期望返回值：" + str(int(exp_code)) + u"; 实际返回值：" + str(status)
                        num_fail += 1
                        str2 = "测试结果：不通过 \n错误信息： " + str(txt) + "\n"
                        strLast += res.url + str2
                        w_sheet.write(i,10,str2)
                        w_sheet.write(i,8,status)
                        w_sheet.write(i,9,res.text)
                        wbook.save(table_name)
            else:
                info2 = configs[6]
                # print("Excel读取到的body类型是%s" % type(info2))
                body = json.loads(info2)
                # print("body的数据类型是%s" % type(body))
                client = Client(url=url,method=method,body_type=BodyType.JSON)
                cft = cases_for_token()
                token = cft.test_token()
                client.set_headers("Authorization",token)
                client.set_headers("Content-Type",headers)
                # print("POST请求地址: %s" % client.url)
                # print("POST请求头: %s"% client.headers)
                client.set_body(body)
                client.body = json.dumps(body)
                # print("POST请求体：%s" % client.body)
                # print("POST请求体的类型是：%s" %  type(client.body))
                res1 = client.send()
                # client.check_status_code_is_200()
                # text_info = json.loads(res1.text)  # 把返回体转成字典类型
                if res1.content:
                    client.check_status_code_is_200()
                    text_info = json.loads(res1.text)
                    status = text_info["status"]
                    if int(exp_code) == status:
                        num_success += 1
                        str1 = u"测试结果：通过\n"
                        strLast += url + str1
                        w_sheet.write(i,10,str1)
                        w_sheet.write(i,8,status)
                        w_sheet.write(i,9,res1.text)
                        wbook.save(table_name)
                    else:
                        txt = u"期望返回值：" + str(int(exp_code)) + u"; 实际返回值：" + str(status)
                        num_fail += 1
                        str2 = "测试结果：不通过 \n 错误信息：" + str(txt) + "\n"
                        strLast += url+str2
                        w_sheet.write(i,10,str2)
                        w_sheet.write(i,8,status)
                        w_sheet.write(i,9,res1.text)
                        wbook.save(table_name)
                else:
                    print("响应异常")
        print("接口用例通过数：%s" % num_success)
        print("接口用例失败数：%s" % num_fail)
        print(strLast)
        strLast += u"接口用例通过数：" + str(num_success)+"\n" + u"接口用例失败数："+str(num_fail)


        email_Smtp('295326448@qq.com', 'gxjthsmawopwbjee', '295326448@qq.com').send_email_msgExcel(table_name, strLast)

if __name__ == '__main__':
    table_name = '../data/Cases_for_yygl_20200921.xlsx'
    test1 = run3_excel()
    test1.test_excel(table_name)