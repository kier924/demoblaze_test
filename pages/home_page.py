from selenium.common import NoSuchElementException

from pages.base_page import BasePage
from utils.locators import *


class HomePage(BasePage):
    def __init__(self, driver):
        # Call to the BasePage init function.
        super().__init__(driver)
        # Import the locators for this page.
        self.locator = HomePageLocators

    def open_login_form(self):
        self.wait_for_element(self.locator.LOGIN_LINK)
        self.driver.find_element(*self.locator.LOGIN_LINK).click()

    def enter_username(self, username):
        self.wait_for_element(self.locator.USERNAME)
        self.driver.find_element(*self.locator.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.wait_for_element(self.locator.PASSWORD)
        self.driver.find_element(*self.locator.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.wait_for_element_to_be_clickable(self.locator.LOGIN_BUTTON)
        self.driver.find_element(*self.locator.LOGIN_BUTTON).click()

    def click_close_button(self):
        self.wait_for_element_to_be_clickable(self.locator.CLOSE_BUTTON)
        self.driver.find_element(*self.locator.CLOSE_BUTTON).click()

    def fill_login_form(self, username, password):
        self.open_login_form()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def click_logout_link(self):
        self.wait_for_element_to_be_clickable(self.locator.LOGOUT_LINK)
        self.driver.find_element(*self.locator.LOGOUT_LINK).click()

    def get_login_user(self):
        self.wait_for_element(self.locator.LOGIN_USERNAME)
        return self.driver.find_element(*self.locator.LOGIN_USERNAME).text

    def get_alert_text(self):
        self.wait_for_alert()
        alert = self.driver.switch_to.alert
        # alert.accept()
        return alert.text

    def get_password_attribute(self):
        self.wait_for_element(self.locator.PASSWORD)
        return self.driver.find_element(*self.locator.PASSWORD).get_attribute("type")

    def get_close_button_visibility(self):
        self.wait_for_element_to_not_be_visible(self.locator.CLOSE_BUTTON)
        return self.driver.find_element(*self.locator.CLOSE_BUTTON).is_displayed()

    def get_login_link_visibility(self):
        self.wait_for_element(self.locator.LOGIN_LINK)
        return self.driver.find_element(*self.locator.LOGIN_LINK).is_displayed()
