from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self,driver):
        self.driver=driver

# 定位元素封装
    def base_find_element(self,timeout=30,poll=0.5,loc):
        return WebDriverWait(self.driver,timeout,poll_frequency=poll).untill(lambda x:x.find_element(*loc))

# 点击元素封装
    def base_click(self,loc):
        self.base_find_element(loc).click()

# 输入内容封装
    def base_input(self,loc,text):
        el=self.base_find_element(loc)
        el.clear()
        el.send_keys(text)

"""
     需求：
            1. 打开 Ak_CRM
            2. 输入用户
            3. 输入密码  
            4. 点击登录

"""