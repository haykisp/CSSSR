from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page():
    def __init__(self):
        self.URL = 'http://blog.csssr.ru/qa-engineer/'
        self.driver = webdriver.Chrome(executable_path='chromedriver')
        self.driver.maximize_window()
        self.driver.get(self.URL)

    def click(self,XPath):
        self.driver.find_element_by_xpath(XPath).click()

    def wait(self,XPath,time):
        wait = WebDriverWait(self.driver, time)
        wait.until(EC.element_to_be_clickable((By.XPATH, XPath)))

    def content(self):
        xpath = '//div[@class="wrap"]'
        return self.driver.find_element_by_xpath(xpath)

    def close(self):
        self.driver.quit()

