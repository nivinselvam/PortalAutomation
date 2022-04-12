import time

import mysql
from selenium import webdriver
from self import self

from Pages.LoginPageActivities import LoginPageActivities
from Pages.HomePageActivities import HomePageActivities
from Pages.UpiSettingsActivities import UpiSettingsActivities
import pytest
import sshtunnel
import pymysql
import pandas as pd

driver = webdriver.Chrome('/home/ezetap/Downloads/chromedriver_linux64/chromedriver')
username = "1709201712"
password = "D1234567"
orgCode="AUTO_PYTHON_TRIAL"


def setup_module(module):
    LoginPageActivities.login(self, driver, username, password)
    time.sleep(5)

    HomePageActivities.search_for_merchant(self, driver, orgCode)
    HomePageActivities.switch_merchant(self, driver, orgCode)
    HomePageActivities.click_on_setup_menu(self, driver)
    HomePageActivities.click_on_upi_settings_in_setup(self, driver)
    time.sleep(5)

def teardown_module(module):
    print("inside teardown")
    driver.close()

def test_bqr():
    print("Inside Test case")
    # # method 1
    setting_values = ["trial@upiset", "522024098030314", "610003", "9845928759238",
                      "57c3f7c3b0d8dc0be189ec63f68fce42"]
    UpiSettingsActivities.create_upi_configuration(self, driver, setting_values)


    # #dev7
    # tunnel = sshtunnel.SSHTunnelForwarder(ssh_address_or_host='dev7', ssh_username="",
    #                                       remote_bind_address=('localhost', 3306))
    # tunnel.start()
    # conn = pymysql.connect(host='localhost', user='ezedemo', passwd='abc123', db='', port=tunnel.local_bind_port)


    # # demo1
    # tunnel = sshtunnel.SSHTunnelForwarder(ssh_address_or_host='127.0.0.1', ssh_username="",
    #                                       remote_bind_address=('localhost', 3307))
    # tunnel.start()
    # conn = pymysql.connect(host='localhost', user='ezedemo1', passwd='abc123', db='', port=tunnel.local_bind_port)


    # query1 = ("SELECT org_code from ezetap_demo.org_employee where username='1709201712';")
    # df1 = pd.read_sql_query(query1, conn)
    # orgCode = df1['org_code'].values[0]
    # print(orgCode)
    # conn.close()
    # tunnel.close()