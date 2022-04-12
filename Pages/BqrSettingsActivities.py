import time

from Pages import BaseActions

keys = ["txt_visa_primary_id_NAME", "txt_master_primary_id_NAME", "txt_bqr_rupay_primary_id_NAME", "txt_bqr_ifsc_NAME",
        "txt_bqr_acct_numb_NAME",
        "txt_bqr_name_NAME", "txt_bqr_city_NAME", "txt_bqr_pin_NAME", "txt_bqr_category_code_NAME",
        "txt_bqr_currency_code_NAME", "txt_bqr_country_code_NAME"]


class BqrSettingsActivities:

    # method 1
    def create_bqr_configuration(self, driver, values):
        BaseActions.click(driver, "btn_create_bqr_acq_XPATH")
        print("Create Button is clicked")
        time.sleep(5)
        for val in range(len(values)):
            print("key:", values[val])
            BaseActions.enter_data(driver, keys[val], values[val])
        time.sleep(4)
        BaseActions.click(driver, "btn_bqr_add_ID")
        time.sleep(30)





        # BaseActions.click(driver, "drop_bqr_bankcode_NAME")
        # BaseActions.click(driver, "select_dummy_bankcode_XPATH")
        # BaseActions.click(driver, "drop_bqr_status_NAME")
        # BaseActions.click(driver, "select_active_status_XPATH")



    # method 2
    # def create_bqr_configuration(self, driver, dict_values):
    #     # BaseActions.enter_data(driver,"txt_visa_primary_id_NAME","hello")
    #
    #     {"Visa Primary ID": "4403849803031405", "Mastercard Primary ID": "4403849803031405",
    #      "Rupay Primary ID": "4403849803031405", "IFSC": "HDFC00000223", "Account Number": "834752035723",
    #      "Name": "trialOrg", "City": "bangalore", "Pincode": "345345", "Category Code": "567",
    #      "Currency Code": "64", "Country Code": "45"}
    #
    #     for key in dict_values:
    #         print("key:", key, ", Value:", dict_values[key])
    #         if key=="Visa Primary ID":
    #             BaseActions.enter_data(driver, "txt_visa_primary_id_NAME", dict_values[key])
    #         elif key=="Mastercard Primary ID":
    #             BaseActions.enter_data(driver, "txt_visa_primary_id_NAME", dict_values[key])
