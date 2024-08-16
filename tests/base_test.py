import unittest
from selenium import webdriver


# Define a test class named BaseTest that inherits from unittest.TestCase.
class BaseTest(unittest.TestCase):

    # This method is called before each test case.
    def setUp(self):
        # Create a Chrome WebDriver instance.
        self.driver = webdriver.Chrome()
        # Navigate to the specified URL.
        self.driver.get("https://www.demoblaze.com/index.html")

    # This method is called after each test case.
    def tearDown(self):
        # Close the WebDriver, terminating the browser session.
        self.driver.quit()


# Check if this script is the main module to be executed.
if __name__ == "__main__":
    # Run the test cases defined in this module
    unittest.main(verbosity=1)
