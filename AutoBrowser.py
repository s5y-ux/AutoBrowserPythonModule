from selenium.webdriver.common.by import By
from selenium import webdriver
import time

class Browser:
    def __init__(self):
        # Initialize the browser attribute as webdriver.Chrome()
        self.browser = webdriver.Chrome()

    def visit(self, website_parameter):
        # Access the website using the formatted web address
        self.browser.get("https://www.{}/".format(website_parameter))

    def direct_visit(self, website_parameter):
    	self.browser.get(website_parameter)

    def click(self, xpath_parameter):
        # Delay to allow Selenium to find the element after page load
        self.delay(2)

        # Find, parse, and click the object by XPath
        xpath_element = self.browser.find_element(by=By.XPATH, value=xpath_parameter)
        xpath_element.click()

    def fast_click(self, xpath_parameter):
    	
    	# Delay to allow Selenium to find the element after page load
    	self.delay(2)

    	 # Find, and parse the object by XPath
    	xpath_element = self.browser.find_element(by=By.XPATH, value=xpath_parameter)

    	# BOOOM
    	while(True):
        	xpath_element.click()

    def send_keys(self, xpath_parameter, input_parameter, press_enter=False):
        # Delay to allow Selenium to find the element after page load
        self.delay(2)

        # Parse XPath according to Selenium
        xpath_element = self.browser.find_element(by=By.XPATH, value=xpath_parameter)

        # Send keys method from DOM object
        xpath_element.send_keys(input_parameter)

        # Check the keyword to send the Enter keycode to the input object
        if press_enter:
            xpath_element.send_keys(u'\ue007')

    def scroll_to(self, y_position):
        # Delay to allow Selenium to find the element after page load
        self.delay(2)

        # Actual JavaScript Code
        self.browser.execute_script(f"window.scrollTo(0, {y_position})")

    def delay(self, int_parameter):
        # Convenient way to sleep the program
        time.sleep(int_parameter)
