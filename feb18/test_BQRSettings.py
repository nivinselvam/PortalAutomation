import time

import mysql
from selenium import webdriver
from self import self

from Pages.LoginPageActivities import LoginPageActivities
from Pages.HomePageActivities import HomePageActivities
from Pages.BqrSettingsActivities import BqrSettingsActivities
import pytest
import sshtunnel
import pymysql
import pandas as pd

from TestCase import setUp

driver = webdriver.Chrome('/home/ezetap/Downloads/chromedriver_linux64/chromedriver')
username = "1709201712"
password = "D1234567"
orgCode="AUTO_PYTHON_TRIAL"


def setup_module(module):
    # pass
    LoginPageActivities.login(self, driver, username, password)
    time.sleep(5)

    HomePageActivities.search_for_merchant(self, driver, orgCode)
    HomePageActivities.switch_merchant(self, driver, orgCode)
    HomePageActivities.click_on_setup_menu(self, driver)
    HomePageActivities.click_on_bqr_settings_in_setup(self, driver)
    time.sleep(5)

def teardown_module(module):
    # pass
    driver.close()

@pytest.mark.usefixtures("my_setup")
def test_bqr():
    print("Inside Test case")
    # # method 1
    setting_values = ["4403849803031405", "522024098030314", "6100030980303145", "DEUT077BGL",
                      "20495830", "trialOrg", "bangalore", "345345", "2741", "356", "IN"]
    BqrSettingsActivities.create_bqr_configuration(self, driver, setting_values)


    #DB values
    data = setUp.getValueFromDB("SELECT status from ezetap_demo.bharatqr_merchant_config where org_code='" + orgCode + "';")

    print(str(data))

    if(len(data)>0):
        dbStatus = str(data['status'].values[0])
        setUp.validateValues("", "ACTIVE:"+dbStatus, "", "")
    else:
        print("No entry in db table")
        setUp.createStatusTable("", "False", "", "")



    # #method 2
    # setting_values = {"Visa Primary ID":"4403849803031405","Mastercard Primary ID":"4403849803031405",
    #                                                               "Rupay Primary ID":"4403849803031405","IFSC":"HDFC00000223","Account Number":"834752035723",
    #                                                               "Name":"trialOrg","City":"bangalore","Pincode":"345345","Category Code":"567",
    #                                                               "Currency Code":"64","Country Code":"45"}
    # BqrSettingsActivities.create_bqr_configuration(self, driver, setting_values)


