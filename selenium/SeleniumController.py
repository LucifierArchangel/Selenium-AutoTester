from selenium import webdriver
from DriverPaths import paths

class SeleniumController:
    def __init__(self, paths):
        self.driver = {}
        self.paths = paths

    def initialize(self, driverName):
        if driverName == 'chromium':
            self.driver = webdriver.Chrome(executable_path=self.paths.get(driverName))
        elif driverName == 'firefox':
            self.driver = webdriver.Firefox(executable_path=self.paths.get(driverName))

        else:
            raise 'Unknown browser name'

    def execute(self, command, *args):
        if command == 'use':
            self.initialize(args[0])

        elif command == 'open':
            self.driver.get(args[0])
        
        elif command == 'click':
            if args[0] == 'xpath':
                el = self.findElementByXpath(args[1])
                if el != None:
                    el.click()    
                    return 
                raise('element does not exist')

            elif args[0] == 'css-selector':
                el = self.findElementByCssSelector(args[1])
                if el != None:
                    el.click()
                    return
                raise 'Unknown parametr'
                return

        elif command == 'keys':
            if args[0] == 'xpath':
                values = args[2].replace('\'', '')

                el = self.findElementByXpath(args[1])
                if el != None:
                    el.send_keys(values)

            elif args[0] == 'css-selector':

                self.driver.find_elements_by_css_selector(args[1]).send_keys(values)

            else: 
                raise 'Unknown parametr'
                return
    
    def findElementByCssSelector(self, CssSelector):
        try:
            el = self.driver.find_element_by_css_selector(CssSelector) 
            return el
        except:
            return None

    def findElementByXpath(self, xPath):
        try:
            el = self.driver.find_element_by_xpath(xPath)
            return el
        except:
            return None

    def quit(self):
        self.driver.quit()
    