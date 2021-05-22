import unittest
import xlrd
from cal import call
from ddt import ddt
from ddt import data
from ddt import unpack
class excel():
    wb=xlrd.open_workbook(filename="E:\python1\day17\计算器数据.xlsx",encoding_override=True)
    sheet=wb.sheet_by_name("数据")
    rows=sheet.nrows
    cols=sheet.ncols
    da=[]
    for i in range(rows):
        a=sheet.row_values(i)
        da.append(a)
x=excel()
da=x.da
@ddt
class calTest(unittest.TestCase):
    @data(*da)
    @unpack
    def test_add(self,a,b,c):
        calc=call()
        sum=calc.add(a,b)
        self.assertEqual(c,sum)

