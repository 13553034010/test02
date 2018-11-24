import os,sys
# 位置
sys.path.append(os.getcwd())

import pytest
from Base.get_driver import get_driver
from Page.page_login import PageLogin


class TestLogin():
    # 初始化方法
    def setup_class(self):
        # 实例化 PageLogin
        self.login=PageLogin(get_driver())
    # 结束方法
    def teardown_class(self):
        # 关闭驱动对象
        self.login.driver.quit()
    # 测试方法
    def test_login(self,username="18600001111",pwd="123456"):
        # 输入用户名
        self.login.page_input_username(username)
        # 输入密码
        self.login.page_input_password(pwd)
        # 点击登录
        self.login.page_click_login_btn()
if __name__ == '__main__':
    pytest.main("-s test_login.py")