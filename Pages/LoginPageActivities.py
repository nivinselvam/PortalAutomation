from Pages import BaseActions
from Utilities import configReader


class LoginPageActivities:

    def login(self, driver, username, password):
        url = configReader.read_config("APIs", "baseUrl") + configReader.read_config("APIs", "portalLogin")
        driver.get(url)
        driver.maximize_window()
        BaseActions.enter_data(driver, "username_NAME", username)
        BaseActions.enter_data(driver, "password_NAME", password)
        BaseActions.click(driver, "signIn_NAME")

