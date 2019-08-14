#encoding:utf-8
import requests
import json
data={'mobile':17713162100,'rand':678871}
r=requests.post(url='http://api.test.shaoziketang.com/api/v1.0/login/data',
                    data=data)
print(r.status_code)
print(r.json())
print(json.dumps(r.json(),indent=True,ensure_ascii=False))
