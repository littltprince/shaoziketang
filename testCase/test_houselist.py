#encoding:utf-8
import unittest
from base.method import Method,IsAssert

class houselist(unittest.TestCase):
    def setUp(self):
        self.Method=Method()
        self.IsAssert=IsAssert()


    '''二手房列表页接口是否正常'''
    def test_houselist(self):
        r = self.Method.post(1)
        self.assertEqual(r.status_code,200)
        self.assertTrue(self.IsAssert.isContent(1,r.text))

    '''二手房列表页title是否存在'''
    def test_housetitle(self):
        r = self.Method.post(1)

    '''列表页价格是够存在'''
    def test_houseprince(self):

    '''列表页委托中介是否存在'''
    def test_housecompany(self):

    ''''''


if __name__ == '__main__':
    unittest.main()
