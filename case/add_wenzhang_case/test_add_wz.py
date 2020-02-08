# coding:utf-8
"""
------------------------------------------------------------------------------------------------------------------------
* @file:    test_add_wz.py
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
import pytest
from case.add_wenzhang_case.add_wz import *


@pytest.fixture(scope='session')
def login_xadmin_fix():
    s = requests.session()
    login(s)
    return s


def test_add_wz(login_xadmin_fix):
    s = login_xadmin_fix
    data = add_wenzhang(s, "test0207007")
    result = get_result(data)
    assert result == "test0207007"
