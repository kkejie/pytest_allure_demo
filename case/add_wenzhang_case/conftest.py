# coding:utf-8
import pytest
import os

def pytest_addoption(parser):
    parser.addoption(
        "--cmdhost",
        action="store",
        default="http://49.235.92.12:8020",
        help="test case project host address"
    )

@pytest.fixture(scope="session", autouse=True)
def host(request):
    '''获取命令行参数给到环境变量'''
    os.environ["host"] = request.config.getoption("--cmdhost")
    print("当前用例运行测试环境：%s" %os.environ["host"])
