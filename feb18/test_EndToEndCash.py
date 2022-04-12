import random
import time
from datetime import datetime
import logging

# import pytest
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from self import self
import timeit
# import datetime


from Pages.HomePageActivities import HomePageActivities
from Pages.LoginPageActivities import LoginPageActivities
from TestCase import conftest, setUp
import pytest_check as check

from Utilities import configReader
from Utilities.Util_Logs import Logger

log = Logger(__name__, logging.INFO)

portal_username = "8078151226"
portal_password = "D1234567"
username = "1235671230"
password = "A1234567"
orgCode = "AUTO_PYTHON_TRIAL"
now = datetime.now()
starting_time = now.strftime("%H:%M:%S")


# def setup_module(module):
#     now = datetime.now()
#     starting_time = now.strftime("%H:%M:%S")


def validatePortal():
    driver = webdriver.Chrome('/home/ezetap/Downloads/chromedriver_linux64/chromedriver')
    LoginPageActivities.login(self, driver, portal_username, portal_password)
    time.sleep(5)

    HomePageActivities.search_for_merchant(self, driver, orgCode)
    HomePageActivities.switch_merchant(self, driver, orgCode)
    HomePageActivities.click_on_transactions_menu(self, driver)

    portalType = driver.find_element(By.XPATH, configReader.read_config("locators", "type_XPATH")).text
    portalStatus = driver.find_element(By.XPATH, configReader.read_config("locators", "status_XPATH")).text
    portalAmount = driver.find_element(By.XPATH, configReader.read_config("locators", "amount_XPATH")).text
    portalUsername = driver.find_element(By.XPATH, configReader.read_config("locators", "username_XPATH")).text
    portalTxnId = driver.find_element(By.XPATH, configReader.read_config("locators", "txnId_XPATH")).text

    D1 = {"portalType": portalType, "portalStatus": portalStatus, "portalAmount": portalAmount,
          "portalUsername": portalUsername, "portalTxnId": portalTxnId}
    driver.close()
    return D1


# @pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("my_setup")
def test_cashPayment():
    login_payload = {'username': username, 'password': password}
    setUp.post(login_payload, "login")
    amount = random.randint(1, 99)
    cash_payload = {'username': username, 'password': password, 'amount': amount}
    cashPayment_resp = setUp.post(cash_payload, "cashPayment")

    txnId = cashPayment_resp['txnId']
    data = setUp.getValueFromDB("SELECT amount,username from ezetap_demo.txn where id='" + txnId + "';")

    dbAmount = str(data['amount'].values[0])
    dbusername = str(data['username'].values[0])

    portalValues = validatePortal()
    portalType = portalValues["portalType"]
    portalStatus = portalValues["portalStatus"]
    portalAmount = portalValues["portalAmount"]
    portalUsername = portalValues["portalUsername"]
    portalTxnId = portalValues["portalTxnId"]

    print("Amount from API response : " + str(cashPayment_resp['amount']))
    print("")
    print("Amount from DB table txn : ", dbAmount)
    print("username from DB table txn : ", dbusername)
    print("")
    print("txnType from portal txn history : ", portalType)
    print("txnStatus from portal txn history : ", portalStatus)
    print("Amount from portal txn history : ", portalAmount)
    print("Username from portal txn history : ", portalUsername)
    print("TxnID from portal txn history : ", portalTxnId)
    print("")
    #
    #     #Actual
    #     # expectedAPIValues = str(amount)+".0:" + str(cashPayment_resp['amount'])+",True:"+str(cashPayment_resp['success'])
    #     # expectedDBValues =  str(amount)+".0:" + dbAmount + "," + str(username) + ":" + dbusername
    #     # expectedPortalValues = "CASH:" + portalType + ",Settled:" + portalStatus
    #
    #     # setUp.validateValues(expectedAPIValues, expectedDBValues, expectedPortalValues, "")    #Actual

    # Sample to fail the assertion
    expectedAPIValues = str(amount) + ".10:" + str(cashPayment_resp['amount']) + ",True:" + str(
        cashPayment_resp['success'])
    expectedDBValues = str(amount) + ".0:" + dbAmount + "," + str(username) + ":" + dbusername
    expectedPortalValues = "CAS:" + portalType + ",Settled:" + portalStatus

    setUp.validateValues(expectedAPIValues, expectedDBValues, expectedPortalValues, "")

@pytest.mark.usefixtures("my_setup")
def test_testCaseOne():
    setUp.createStatusTable("False", "True", "True", "True")
    check.equal("hello", "HELLOW")
    # time.sleep(12)

@pytest.mark.usefixtures("my_setup")
def test_testCaseTwo():
    setUp.createStatusTable("False", "True", "True", "True")
    check.equal("AB", "A")
    # time.sleep(18)
#
@pytest.mark.usefixtures("my_setup")
def test_testCaseThree():
    setUp.createStatusTable("True", "True", "True", "True")
    check.equal("B", "B")
    # time.sleep(8)
#
#
@pytest.mark.usefixtures("my_setup")
def test_testCaseThreety():
    setUp.createStatusTable("True", "True", "True", "True")
    check.equal("B", "B")
    # time.sleep(5)

@pytest.mark.usefixtures("my_setup")
def test_skipTest():
    pytest.skip('Skipping test---------------------')
    # time.sleep(3)


def teardown_module(module):
    pass

##################################################### ADD DIFF TYPES OF LINKS ###############################################
# TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'
# @allure.link('https://www.youtube.com/watch?v=4YYzUTYZRMU')
# def test_with_link():
#     pass
# @allure.link('https://www.youtube.com/watch?v=Su5p2TqZxKU', name='Click me')
# def test_with_named_link():
#     pass
# @allure.issue('140', 'Pytest-flaky test retries shows like test steps')
# def test_with_issue_link():
#     pass
# @allure.testcase(TEST_CASE_LINK, 'Test case title')
# def test_with_testcase_link():
#     pass
