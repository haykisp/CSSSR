from selenium import webdriver

class Page():
    def __init__(self):
        """
        Constructor of web page.
        Opens browser with our web page
        """
        self.URL = 'http://blog.csssr.ru/qa-engineer/'
        self.driver = webdriver.Chrome(executable_path='chromedriver')
        self.driver.maximize_window()
        self.driver.get(self.URL)

    def click(self, element):
        """
        This method clicks on element, which given as argument
        :param element:
        :return:
        """
        element.click()


    def content(self):
        """
        Ceating element
        :return:
        """
        xpath = '//div[@class="wrap"]'
        return self.driver.find_element_by_xpath(xpath)

    def close(self):
        """
        This method closing browser
        :return:
        """
        self.driver.quit()
