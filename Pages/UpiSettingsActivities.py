import time

from Pages import BaseActions

keys = ["txt_upi_vpa_NAME","txt_upi_mid_NAME","txt_upi_tid_NAME","txt_upi_merchant_id_NAME","txt_upi_enc_key_NAME"]


class UpiSettingsActivities:
    def create_upi_configuration(self, driver, values):
        BaseActions.click(driver, "btn_new_upi_setting_XPATH")
        time.sleep(2)
        for val in range(len(values)):
            print("key:", values[val])
            BaseActions.enter_data(driver, keys[val], values[val])
            time.sleep(1)
        BaseActions.click(driver, "btn_upi_add_ID")
        time.sleep(10)