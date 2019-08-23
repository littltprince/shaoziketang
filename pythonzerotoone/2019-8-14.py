#encoding:utf-8
import requests
import json
data={'mobile':13701026463,'rand':678871}
r=requests.post(url='http://api.test.shaoziketang.com/api/v1.0/login/data',
                    data=data)
print(json.dumps(r.json(),indent=True,ensure_ascii=False))
