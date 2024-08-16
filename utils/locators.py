from selenium.webdriver.common.by import By


class HomePageLocators(object):
    LOGIN_LINK = (By.XPATH, "//a[@id='login2']")
    USERNAME = (By.XPATH, "//input[@id='loginusername']")
    PASSWORD = (By.XPATH, "//input[@id='loginpassword']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Log in')]")
    LOGOUT_LINK = (By.XPATH, "//a[@id='logout2']")
    LOGIN_USERNAME = (By.XPATH, "//a[@id='nameofuser']")
    CLOSE_BUTTON = (By.XPATH, "//div[@id='logInModal']//div[@class='modal-dialog']//div[@class='modal-content']//div[@class='modal-footer']//button[@type='button'][contains(text(),'Close')]")

