import time

from Pages import BaseActions

class OrgSettingsActivities:

    def number_of_txns_per_day(self, driver, value):
        BaseActions.enter_data(driver, "number_of_txns_per_day_XPATH", value)

    def enter_min_txn_amt(self, driver, value):
        BaseActions.enter_data(driver, "minimum_amount_allowed_for_a_transaction_ID", value)

    def enable_signature_for_cash_and_cheque(self, driver):
        BaseActions.click(driver, "enable_sign_for_cash_and_cheque_XPATH")

    def max_refund_allowed(self, driver, value):
        BaseActions.enter_data(driver, "max_refund_allowed_XPATH",value)

    def save_all_org_settings(self, driver):
        BaseActions.click(driver, "btn_save_button_XPATH")
        alert_obj = driver.switch_to.alert
        alert_obj.accept()