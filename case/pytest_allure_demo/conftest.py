# coding:utf-8
"""
------------------------------------------------------------------------------------------------------------------------
* @file:    conftest.py
* @content  
------------------------------------------------------------------------------------------------------------------------
* @author:  KeJie
* @contact: 544752682@qq.com
* @time:    2020/2/8
* @desc:    
------------------------------------------------------------------------------------------------------------------------
* Modified: 
* Version:  
------------------------------------------------------------------------------------------------------------------------
"""
import pytest


@pytest.fixture(scope="session")
def login_fix():
    print("测试用例登录")