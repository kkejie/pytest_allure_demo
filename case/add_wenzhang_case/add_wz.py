# coding:utf-8
"""
------------------------------------------------------------------------------------------------------------------------
* @file:    add_wz.py
* @content  
------------------------------------------------------------------------------------------------------------------------
* @author:  KeJie
* @contact: 544752682@qq.com
* @time:    2020/2/7
* @desc:    
------------------------------------------------------------------------------------------------------------------------
* Modified: 
* Version:  
------------------------------------------------------------------------------------------------------------------------
"""
import requests
import re
from requests_toolbelt import MultipartEncoder
from lxml import etree
import os


def login(s):
    '''登录'''
    url = os.environ["host"]+'/xadmin/'
    r = s.get(url)
    csrfmiddlewaretoken = re.findall("name='csrfmiddlewaretoken' value='(.+?)'", r.text)
    print(csrfmiddlewaretoken[0])
    body = {
        "csrfmiddlewaretoken": csrfmiddlewaretoken[0],
        "username": "admin",
        "password": "yoyo123456",
        "this_is_the_login_form": 1,
        "next": "/xadmin/"
    }
    r2 = s.post(url, data=body)
    print(s.headers)
    # print(r2.text)
    if "主页面 | 后台页面" in r2.text:
        print("登录成功！")
    else:
        print("登录失败！")
    return s

def add_wenzhang(s, title="test"):
    '''新增文章'''
    # s = requests.session()
    url_add_wenzhang = os.environ["host"]+'/xadmin/hello/articledetail/add/'
    r3 = s.get(url_add_wenzhang)
    # print(r3.text)
    token = re.findall("name='csrfmiddlewaretoken' value='(.+?)'", r3.text)
    print(token)
    m = MultipartEncoder(
        fields=[
            ("csrfmiddlewaretoken", token[0]),
            ("csrfmiddlewaretoken", token[0]),
            ("title", title),
            ("auth", "damin"),
            ("classify", "1"),
            ("body", "测试文章"),
            ("detail", "测试备注"),
            ("_save", "")
        ]
    )
    r4 = s.post(url_add_wenzhang, data=m, headers={'Content-Type': m.content_type})
    return r4.text

def get_result(result):
    '''获取添加的数据'''
    htm = etree.HTML(result)
    data = htm.xpath('//*[@id="changelist-form"]/div[1]/table/tbody/tr[1]/td[2]/a')
    return data[0].text

if __name__ == '__main__':
    os.environ["host"] = "http://49.235.92.12:8020"
    s = requests.session()
    login(s)
    data = add_wenzhang(s, "test0207005")
    result = get_result(data)
    assert result == "test0207005"

