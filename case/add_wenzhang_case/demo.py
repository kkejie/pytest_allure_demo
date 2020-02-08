# coding:utf-8
"""
------------------------------------------------------------------------------------------------------------------------
* @file:    作业21.py
* @content
------------------------------------------------------------------------------------------------------------------------
* @author:  KeJie
* @contact: 544752682@qq.com
* @time:    2020/2/2
* @desc:
------------------------------------------------------------------------------------------------------------------------
* Modified:
* Version:
------------------------------------------------------------------------------------------------------------------------
"""
import requests

url = "http://49.235.92.12:9000/api/v1/login"

s = requests.session()

# print(s.headers)
body = {
    "username": "test",
    "password": "123456"
}
r = s.post(url, json=body)
# print(r.text)
token = r.json()["token"]
h1 = {
    "Authorization": "token %s" % token
}
# print(token)
s.headers.update(h1)
# print(s.headers)

url2 = "http://49.235.92.12:9000/api/v1/userinfo"
r2 = s.get(url2)
print(r2.text)


