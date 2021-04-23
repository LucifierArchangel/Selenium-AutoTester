from selenium import webdriver

class SeleniumController:
    def __init__ (self):
        self.driver = {}
    
    def initialize(self, driverName):
        if driverName == 'chromium':
            self.driver = webdriver.Chrome(executable_path=driverPath)
        elif driverName == 'firefox':
            self.driver = webdirver.Firefox(executable_path=driverPath)
        else:
            raise 'Unknown browser name'
​
    def execute(self, command, *args):
        if command == 'use':
            self.initialize(args[0])

        elif command == 'open':
            self.driver.open(args[0])

        elif command == 'click':
            if args[0] == 'xpath':
                self.driver.find_element_by_xpath(args[1]).click()
            elif args[0] == 'css-selector'
                self.driver.find_element_by_css_selector(args[1]).click()
        
​
    def open(self, *args):
        pass