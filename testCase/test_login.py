#encoding:utf-8
import unittest
import json
from base.method import Method,IsAssert

class login(unittest.TestCase):
    def setUp(self):
        self.Method = Method()
        self.IsAssert = IsAssert()


    '''登录接口是否正常'''
    def test_login(self):
        r = self.Method.post(1)
        print(r.text)
        # print(json.dumps(r.json(), indent=True, ensure_ascii=False))
        # self.assertEqual(r.status_code, 200)



if __name__ == '__main__':
    unittest.main()
