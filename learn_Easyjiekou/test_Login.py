#encoding:utf-8
import unittest
import requests
class TestLogin(unittest.TestCase):

    url='http://api.test.shaoziketang.com/api/v1.0/login/data'

    def test_login(self):
        data={"mobile":17713162100,"rand":678871}
        r=requests.post(url=self.url,data=data)
        self.assertIn('200',r.text)
        print(r.status_code)

    def test_fail(self):
        data = {"mobile": 17713162100, "rand": 67881}
        r = requests.post(url=self.url, data=data)
        self.assertIn('-1',r.text)
        print(r.text)


if __name__ == '__main__':
    unittest.main(verbosity=2)