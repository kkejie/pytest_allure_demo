# coding:utf-8
"""
------------------------------------------------------------------------------------------------------------------------
* @file:    test_qq.py
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
import allure


@allure.step("步骤1：点xxx")
def step_1():
    print("用例步骤：1")


@allure.step("步骤2：点xxx")
def step_2():
    print("用例步骤：2")


@allure.feature("第一个接口测试用例")
class Test_qq():
    """接口的名称描述"""
    @allure.story("这是第一个测试用例")
    @allure.issue("禅道BUG地址1")
    @allure.testcase("禅道用例地址1")
    def test_1(self, login_fix):
        """
        用例的描述：这是一个要先登录的用例
        :param login_fix: 前置条件：登录
        :return:
        """
        step_1()
        step_2()
        print("测试用例：1")
        assert 1 == 1

    @allure.story("这是第二个测试用例")
    @allure.issue("禅道BUG地址2")
    @allure.testcase("禅道用例地址2")
    # @pytest.skip
    def test_2(self):
        """
        用例描述：这个用例不用登录
        :return:
        """
        print("测试用例：2")
        assert 1 == 1

    @allure.story("这是第三个测试用例")
    @allure.issue("禅道BUG地址3")
    @allure.testcase("禅道用例地址3")
    def test_3(self):
        """
        用例描述：这个用例不用登录
        :return:
        """
        print("测试用例：3")
        assert 1 == 2
