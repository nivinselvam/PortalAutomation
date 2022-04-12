import time

from Pages import BaseActions


class HomePageActivities:


    def click_on_transactions_menu(self, driver):
        BaseActions.click(driver, "transactions_XPATH")
        BaseActions.click(driver, "transactions_search_XPATH")
        time.sleep(30)

    def click_on_users_menu(self, driver):
        BaseActions.click(driver, "users_XPATH")

    def search_for_merchant(self, driver, orgcode):
        BaseActions.enter_data(driver, "merchantSearch_XPATH", orgcode)
        BaseActions.press_enter_key(driver, "merchantSearch_XPATH")

    def switch_merchant(self, driver, orgcode):
        BaseActions.click_specific(driver, "switchButton_XPATH", orgcode)

    def edit_merchant(self, driver):
        BaseActions.click(driver,"editMerchant_XPATH")

    def select_org_settings(self, driver):
        BaseActions.click(driver, "orgSettings_XPATH")

    def click_on_appkeys_menu(self, driver):
        BaseActions.click(driver, "appkeysMenu_XPATH")

    def click_on_merchants_menu(self, driver):
        BaseActions.click(driver, "merchantsMenu_XPATH")

    def click_on_merchantName_button(self, driver):
        BaseActions.click(driver,"btn_merchantName_XPATH")

    def click_on_setup_menu(self, driver):
        BaseActions.click(driver, "setupMenu_XPATH")

    def click_on_bulkuploads_in_setup(self, driver):
        BaseActions.click(driver, "bulkUploads_XPATH")

    def click_on_bqr_settings_in_setup(self, driver):
        BaseActions.click(driver, "bqrSettings_XPATH")

    def click_on_upi_settings_in_setup(self, driver):
        BaseActions.click(driver, "upiSettings_XPATH")