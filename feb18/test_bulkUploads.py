import time

import mysql
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from self import self

import Utilities as util
from TestCase import setUp
from Utilities import Util_FileOperations
from Utilities import Util_CsvOperations
from Pages.LoginPageActivities import LoginPageActivities as LoginPage
from Pages.HomePageActivities import HomePageActivities as HomePage
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
    LoginPage.login(self, driver, username, password)
    HomePage.click_on_setup_menu(self, driver)
    HomePage.click_on_bulkuploads_in_setup(self, driver)
    time.sleep(5)
def setup_function(function):
    util.Util_CsvOperations.create_csv_file_with_data(self, "fileCreated")

def teardown_module(module):
    print("inside teardown")
    driver.close()

@pytest.mark.usefixtures("my_setup")
def test_user_creation_modification():
    driver.find_element(By.XPATH, "//tr/td[text()='User Creation/Modification']/..//input[@name='file']").send_keys("/home/ezetap/PycharmProjects/PortalAutomation/TestCase/fileCreated.csv")
    time.sleep(20)
    driver.find_element(By.XPATH, "//tr/td[text()='User Creation/Modification']/..//input[@value='Save']").click()
    time.sleep(20)

    # DB values
    data = setUp.getValueFromDB("SELECT status from ezetap_demo.org_employee where username=' 7812540980';")

    if (len(data) > 0):
        dbStatus = str(data['status'].values[0])
        setUp.validateValues("", "ACTIVE:" + dbStatus, "", "")
    else:
        print("No entry in db table")
        setUp.createStatusTable("", "False", "", "")


    # OrgSettingsActivities.save_all_org_settings(self, driver)

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
