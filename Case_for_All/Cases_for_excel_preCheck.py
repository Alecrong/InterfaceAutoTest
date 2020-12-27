from run3_excel import run3_excel


class Cases_for_excel():
    '''读取excel文件'''
    def test_excel(self):
        table_name = '../data/cases_for_preCheck.xlsx'
        run3_excel.test_excel(table_name)  # 调用excel读取的封装类，方法传入文件路径即可


if __name__ == '__main__':
    Cases_for_excel().test_excel()