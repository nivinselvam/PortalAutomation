import time

import mysql
from selenium import webdriver
from self import self

from Pages.LoginPageActivities import LoginPageActivities
from Pages.HomePageActivities import HomePageActivities
from Pages.OrgSettingsActivities import OrgSettingsActivities
from Pages.UpiSettingsActivities import UpiSettingsActivities
import pytest
import sshtunnel
import pymysql
import pandas as pd

driver = webdriver.Chrome('/home/ezetap/Downloads/chromedriver_linux64/chromedriver')
username = "1709201712"
password = "D1234567"
orgCode = "AUTO_PYTHON_TRIAL"


def setup_module(module):
    LoginPageActivities.login(self, driver, username, password)
    time.sleep(5)

    HomePageActivities.search_for_merchant(self, driver, orgCode)
    HomePageActivities.switch_merchant(self, driver, orgCode)
    time.sleep(20)
    HomePageActivities.select_org_settings(self, driver)
    time.sleep(5)


def teardown_module(module):
    print("inside teardown")
    OrgSettingsActivities.save_all_org_settings(self, driver)
    time.sleep(30)
    driver.close()


def test_enter_min_txn_amt():
    print("Inside Test case")
    OrgSettingsActivities.enter_min_txn_amt(self, driver, "10")


def test_enable_signature_for_cash_and_cheque():
    OrgSettingsActivities.enable_signature_for_cash_and_cheque(self, driver)


def test_number_of_txns_per_day():
    OrgSettingsActivities.number_of_txns_per_day(self, driver, "20")

def test_max_refund_allowed():
    OrgSettingsActivities.max_refund_allowed(self, driver, "30")
