# coding:utf-8
"""
------------------------------------------------------------------------------------------------------------------------
* @file:    longin.py
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

class Login():
    url = 'http://49.235.92.12:8020/xadmin/'
    r = requests.post(url)

