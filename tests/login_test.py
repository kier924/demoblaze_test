from tests.base_test import BaseTest
from pages.home_page import HomePage


# Define a test class named TestLogin that inherits from BaseTest.
# TS-001
class TestLogin(BaseTest):
    # TC-001 Login with valid credentials
    def test_login_valid_credentials(self):
        home_page = HomePage(self.driver)
        home_page.fill_login_form(username="testkg", password="testkg123")
        username = home_page.get_login_user()
        self.assertIn("testkg", username)

    # TC-002 Login with invalid username
    def test_login_invalid_username(self):
        home_page = HomePage(self.driver)
        home_page.fill_login_form(username="testkg2", password="testkg123")
        notification_text = home_page.get_alert_text()
        self.assertIn("User does not exist.", notification_text)

    # TC-003 Login with invalid password
    def test_login_invalid_password(self):
        home_page = HomePage(self.driver)
        home_page.fill_login_form(username="testkg", password="testkg456")
        notification_text = home_page.get_alert_text()
        self.assertIn("Wrong password.", notification_text)

    # TC-004 Login with empty username and password fields
    def test_login_empty_fields(self):
        home_page = HomePage(self.driver)
        home_page.fill_login_form(username="", password="")
        notification_text = home_page.get_alert_text()
        self.assertIn("Please fill out Username and Password.", notification_text)

    # TC-005 Check case sensitivity of username
    def test_login_case_sensitive(self):
        home_page = HomePage(self.driver)
        home_page.fill_login_form(username="Testkg", password="testkg123")
        notification_text = home_page.get_alert_text()
        self.assertIn("User does not exist.", notification_text)

    # TC-006 Verify password masking during entry
    def test_login_password_masking(self):
        home_page = HomePage(self.driver)
        home_page.fill_login_form(username="testkg", password="testkg123")
        attribute = home_page.get_password_attribute()
        self.assertEqual(attribute, "password")

    # TC-007 Verify close button functionality
    def test_login_close_button(self):
        home_page = HomePage(self.driver)
        home_page.open_login_form()
        home_page.click_close_button()
        is_displayed = home_page.get_close_button_visibility()
        self.assertFalse(is_displayed)

    # TC-008 Verify redirection after successful login
    def test_login_redirection(self):
        home_page = HomePage(self.driver)
        home_page.fill_login_form(username="testkg", password="testkg123")
        username = home_page.get_login_user()
        self.assertIn("testkg", username)

    # TC-009 Verify that user can log out successfully
    def test_logout(self):
        home_page = HomePage(self.driver)
        home_page.fill_login_form(username="testkg", password="testkg123")
        home_page.click_logout_link()
        is_displayed = home_page.get_login_link_visibility()
        self.assertTrue(is_displayed)
