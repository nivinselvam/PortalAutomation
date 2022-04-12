import time

from Pages import BaseActions


class UserDetailsActivities:


    def enterPassword(self, driver, password):
        BaseActions.enter_data(driver, "txt_password_NAME", password)

    def enterConfirmPassword(self, driver, password):
        BaseActions.enter_data(driver,"txt_confirmPassword_ID", password)

    def inactivate_user(self, driver):
        BaseActions.click(driver, "radio_user_inactive_status_ID")

    def activate_user(self, driver):
        BaseActions.click(driver, "radio_user_active_status_ID")

    def save_details(self, driver):
        BaseActions.click(driver, "btn_next_ID")
        time.sleep(10)