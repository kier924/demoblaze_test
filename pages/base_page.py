from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self, driver):
        # Initialize the LoginPage object with a WebDriver instance.
        self.driver = driver

    # Define a function to wait for the presence of an element on the page.
    def wait_for_element(self, element):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(element)
        )

    def wait_for_element_to_be_clickable(self, element):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(element)
        )

    def wait_for_alert(self):
        WebDriverWait(self.driver, 10).until(
            EC.alert_is_present()
        )

    def wait_for_element_to_not_be_visible(self, element):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(element)
        )
