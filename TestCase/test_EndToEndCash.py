import random
import time
import datetime
from datetime import datetime
import logging
from allure_commons.types import AttachmentType

import allure
import pytest
from selenium.webdriver.common.by import By
from self import self
import pytest_check as check

from Pages.HomePageActivities import HomePageActivities
from Pages.LoginPageActivities import LoginPageActivities
from TestCase import setUp, UserAssigner
from DataProvider import GlobalVariables
from Utilities import configReader
from Utilities.Util_Logs import Logger

log = Logger(__name__, logging.INFO)

portal_username = "8078151226"
# portal_username = "1709201712"
portal_password = "D1234567"
# username = "1234987650"
# password = "A1234567"
orgCode = "AUTO_PYTHON_TRIAL"
success_Val_Execution = True


@pytest.mark.apiVal
@pytest.mark.dbVals
@pytest.mark.portalVal
# @pytest.mark.usefixtures("log_on_failure","log_on_success")
def test_cash_payment_successOne(method_setup, session_setup, ui_driver):
    userCredentials = UserAssigner.getUserCredentialsFromExcel()
    username = userCredentials[0]
    password = userCredentials[1]

    GlobalVariables.apiLogs = True
    GlobalVariables.portalLogs = True
    GlobalVariables.cnpWareLogs = False
    GlobalVariables.middleWareLogs = False
    global success_Val_Execution
    success_Val_Execution = True

    try:
        print("")
        login_payload = {'username': username, 'password': password}
        setUp.post(login_payload, "login")
        amount = random.randint(1, 99)
        cash_payload = {'username': username, 'password': password, 'amount': amount}
        cashPayment_resp = setUp.post(cash_payload, "cashPayment")
        setUp.get_TC_Exe_Time() # Get execution time
    except:
        setUp.get_TC_Exe_Time()
        print("Testcase did not complete due to exception in testcase execution")
        print("")
        GlobalVariables.EXCEL_TC_Execution = "Fail"
        GlobalVariables.Incomplete_ExecutionCount += 1 # For HTML report Table
        pytest.fail()

    else:
        if str(cashPayment_resp['success']) == "True":
            GlobalVariables.EXCEL_TC_Execution = "Pass"
            current = datetime.now()
            GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")

            txn_id = cashPayment_resp['txnId']
            try:
                data = setUp.getValueFromDB("SELECT amount,username from ezetap_demo.txn where id='" + txn_id + "';")
                dbAmount = str(data['amount'].values[0])
                dbusername = str(data['username'].values[0])
                expectedDBValues = str(amount) + ".0:" + dbAmount + "," + str(username) + ":" + dbusername
            except:
                print("DB Validation did not complete due to exception in reading values from DB")
                print("")
                GlobalVariables.db_ValidationFailureCount +=1
                expectedDBValues = "Failed"
                GlobalVariables.EXCEL_DB_Val = "Fail"
                success_Val_Execution = False

            try:
                portalValues = validatePortal(GlobalVariables.portalDriver)
                portalType = portalValues["portalType"]
                portalStatus = portalValues["portalStatus"]
                portalAmount = portalValues["portalAmount"]
                portalUsername = portalValues["portalUsername"]
                portalTxnId = portalValues["portalTxnId"]
                expectedPortalValues = "CASH:" + portalType + ",Settled:" + portalStatus + ",Rs." + str(
                    amount) + ".00:" + portalAmount + "," + username + ":" + portalUsername + "," + txn_id + ":" + portalTxnId
            except:
                allure.attach(GlobalVariables.portalDriver.get_screenshot_as_png(), name="screenshot",
                              attachment_type=AttachmentType.PNG)
                print("Portal Validation did not complete due to exception in reading values from portal")
                print("")
                GlobalVariables.portal_ValidationFailureCount +=1
                expectedPortalValues = "Failed"
                GlobalVariables.EXCEL_Portal_Val = "Fail"
                success_Val_Execution = False

            expectedAPIValues = str(amount) + ".0:" + str(cashPayment_resp['amount']) + ",True:" + str(
                cashPayment_resp['success'])
            success = setUp.validateValues(expectedAPIValues, expectedDBValues, expectedPortalValues, "")


             #success =True / False
            if success_Val_Execution == False:  #If any validation execution failed
                if success == False: # Validation comparison of values failed
                    pass
                else:
                    pytest.fail()
        else:
            check.equal(str(cashPayment_resp['success']), "True", "Cash payment failed")
            GlobalVariables.EXCEL_TC_Execution = "Fail"
            GlobalVariables.Incomplete_ExecutionCount += 1
            pytest.fail()
    finally:
        UserAssigner.releaseUserInExcel(str(userCredentials[0]))



@pytest.mark.usefixtures("log_on_failure","log_on_success")
def test_cash_payment_successTwo(method_setup, session_setup, ui_driver):
    userCredentials = UserAssigner.getUserCredentialsFromExcel()
    username = userCredentials[0]
    password = userCredentials[1]
    GlobalVariables.apiLogs = True
    GlobalVariables.portalLogs = True
    GlobalVariables.cnpWareLogs = False
    GlobalVariables.middleWareLogs = False
    global success_Val_Execution
    success_Val_Execution = True

    try:
        login_payload = {'username': username, 'password': password}
        setUp.post(login_payload, "login")
        amount = random.randint(1, 99)
        cash_payload = {'username': username, 'password': password, 'amount': amount}
        cashPayment_resp = setUp.post(cash_payload, "cashPayment")
        setUp.get_TC_Exe_Time() # Get execution time
    except:
        setUp.get_TC_Exe_Time()
        print("Testcase did not complete due to exception in testcase execution")
        print("")
        GlobalVariables.EXCEL_TC_Execution = "Fail"
        GlobalVariables.Incomplete_ExecutionCount += 1
        pytest.fail()

    else:
        if str(cashPayment_resp['success']) == "True":
            GlobalVariables.EXCEL_TC_Execution = "Pass"
            current = datetime.now()
            GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")

            txn_id = cashPayment_resp['txnId']
            try:
                data = setUp.getValueFromDB("SELECT amount,username from ezetap_demo.txn where id='" + txn_id + "';")
                dbAmount = str(data['amount'].values[0])
                dbusername = str(data['username'].values[0])
                expectedDBValues = str(amount) + ".0:" + dbAmount + "," + str(username) + ":" + dbusername
            except:
                print("DB Validation did not complete due to exception in reading values from DB")
                print("")
                GlobalVariables.db_ValidationFailureCount +=1
                expectedDBValues = "Failed"
                GlobalVariables.EXCEL_DB_Val = "Fail"
                success_Val_Execution = False

            try:
                portalValues = validatePortal(GlobalVariables.portalDriver)
                portalType = portalValues["portalType"]
                portalStatus = portalValues["portalStatus"]
                portalAmount = portalValues["portalAmount"]
                portalUsername = portalValues["portalUsername"]
                portalTxnId = portalValues["portalTxnId"]
                expectedPortalValues = "CASH:" + portalType + ",Settled:" + portalStatus + ",Rs." + str(
                    amount) + ".00:" + portalAmount + "," + username + ":" + portalUsername + "," + txn_id + ":" + portalTxnId
            except:
                allure.attach(GlobalVariables.portalDriver.get_screenshot_as_png(), name="screenshot",
                              attachment_type=AttachmentType.PNG)
                print("Portal Validation did not complete due to exception in reading values from portal")
                print("")
                GlobalVariables.portal_ValidationFailureCount +=1
                expectedPortalValues = "Failed"
                GlobalVariables.EXCEL_Portal_Val = "Fail"
                success_Val_Execution = False

            expectedAPIValues = str(amount) + ".0:" + str(cashPayment_resp['amount']) + ",True:" + str(
                cashPayment_resp['success'])
            success = setUp.validateValues(expectedAPIValues, expectedDBValues, expectedPortalValues, "")

            if success_Val_Execution == False:
                if success == False:
                    pass
                else:
                    pytest.fail()
        else:
            check.equal(str(cashPayment_resp['success']), "True", "Cash payment execution failed")
            GlobalVariables.EXCEL_TC_Execution = "Fail"
            GlobalVariables.Incomplete_ExecutionCount += 1
            pytest.fail()
    finally:
        UserAssigner.releaseUserInExcel(str(userCredentials[0]))


@pytest.mark.usefixtures("log_on_failure","log_on_success")
def test_cash_payment_Portalval_failure(method_setup, session_setup, ui_driver):
    userCredentials = UserAssigner.getUserCredentialsFromExcel()
    username = userCredentials[0]
    password = userCredentials[1]
    GlobalVariables.apiLogs = True
    GlobalVariables.portalLogs = True
    GlobalVariables.cnpWareLogs = False
    GlobalVariables.middleWareLogs = False
    global success_Val_Execution
    success_Val_Execution = True

    try:
        login_payload = {'username': username, 'password': password}
        setUp.post(login_payload, "login")
        amount = random.randint(1, 99)
        cash_payload = {'username': username, 'password': password, 'amount': amount}
        cashPayment_resp = setUp.post(cash_payload, "cashPayment")
        setUp.get_TC_Exe_Time() # Get execution time

    except:
        setUp.get_TC_Exe_Time()
        print("Testcase did not complete due to exception in testcase execution")
        print("")
        GlobalVariables.EXCEL_TC_Execution = "Fail"
        GlobalVariables.Incomplete_ExecutionCount += 1
        pytest.fail()
    else:
        if str(cashPayment_resp['success']) == "True":
            GlobalVariables.EXCEL_TC_Execution = "Pass"

            current = datetime.now()
            GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")

            txn_id = cashPayment_resp['txnId']
            try:
                data = setUp.getValueFromDB("SELECT amount,username from ezetap_demo.txn where id='" + txn_id + "';")
                dbAmount = str(data['amount'].values[0])
                dbusername = str(data['username'].values[0])
                expectedDBValues = str(amount) + ".0:" + dbAmount + "," + str(username) + ":" + dbusername
            except:
                print("DB Validation did not complete due to exception in reading values from DB")
                print("")
                GlobalVariables.db_ValidationFailureCount += 1
                expectedDBValues = "Failed"
                GlobalVariables.EXCEL_DB_Val = "Fail"
                success_Val_Execution = False

            try:
                portalValues = validatePortal(GlobalVariables.portalDriver)
                portalType = portalValues["portalType"]
                portalStatus = portalValues["portalStatus"]
                portalAmount = portalValues["portalAmount"]
                portalUsername = portalValues["portalUsername"]
                portalTxnId = portalValues["portalTxnId"]
                expectedPortalValues = "CASH:" + portalType + ",Settled:" + portalStatus + ",₹ " + str(
                    amount) + ".00:" + portalAmount + "," + username + ":" + portalUsername + "," + txn_id + ":" + portalTxnId
            except:
                allure.attach(GlobalVariables.portalDriver.get_screenshot_as_png(), name="screenshot",
                              attachment_type=AttachmentType.PNG)
                print("Portal Validation did not complete due to exception in reading values from portal")
                print("")
                GlobalVariables.portal_ValidationFailureCount += 1
                expectedPortalValues = "Failed"
                GlobalVariables.EXCEL_Portal_Val = "Fail"
                success_Val_Execution = False

            expectedAPIValues = str(amount) + ".0:" + str(cashPayment_resp['amount']) + ",True:" + str(cashPayment_resp['success'])
            success = setUp.validateValues(expectedAPIValues, expectedDBValues, expectedPortalValues, "")

            if success_Val_Execution == False:
                if success == False:
                    pass
                else:
                    pytest.fail()

        else:
            check.equal(str(cashPayment_resp['success']), "True", "Cash payment execution failed")
            GlobalVariables.EXCEL_TC_Execution = "Fail"
            GlobalVariables.Incomplete_ExecutionCount += 1
    finally:
        UserAssigner.releaseUserInExcel(str(userCredentials[0]))


@pytest.mark.portalVal
@pytest.mark.usefixtures("log_on_success","method_setup")
def test_Portalval_failure(ui_driver):
    GlobalVariables.apiLogs = False
    GlobalVariables.portalLogs = True
    GlobalVariables.cnpWareLogs = False
    GlobalVariables.middleWareLogs = False
    global success_Val_Execution
    success_Val_Execution = True

    try:
        print("Logged in to the portal")
        time.sleep(4)
        setUp.get_TC_Exe_Time() # Get execution time

    except:
        setUp.get_TC_Exe_Time()
        print("Testcase did not complete due to exception in testcase execution")
        print("")
        GlobalVariables.EXCEL_TC_Execution = "Fail"
        GlobalVariables.Incomplete_ExecutionCount += 1
        pytest.fail()
    else:

        GlobalVariables.EXCEL_TC_Execution = "Pass"

        current = datetime.now()
        GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
        amount = 23
        try:
            portalValues = validatePortal(GlobalVariables.portalDriver)
            portalType = portalValues["portalType"]
            portalStatus = portalValues["portalStatus"]
            portalAmount = portalValues["portalAmount"]
            expectedPortalValues = "CASH:" + portalType + ",Settled:" + portalStatus + ",₹ " + str(amount) + ".00:" + portalAmount
        except:
            allure.attach(GlobalVariables.portalDriver.get_screenshot_as_png(), name="screenshot",
                          attachment_type=AttachmentType.PNG)
            print("Portal Validation did not complete due to exception in reading values from portal")
            print("")
            GlobalVariables.portal_ValidationFailureCount += 1
            expectedPortalValues = "Failed"
            GlobalVariables.EXCEL_Portal_Val = "Fail"
            success_Val_Execution = False


        success = setUp.validateValues("", "", expectedPortalValues, "")

        if success_Val_Execution == False:
            if success == False:
                pass
            else:
                pytest.fail()
    # finally:
    #     UserAssigner.releaseUserInExcel(str(userCredentials[0]))



@pytest.mark.usefixtures("log_on_failure","log_on_success")
def test_cash_payment_DBVal_Failure(method_setup, session_setup, ui_driver):
    userCredentials = UserAssigner.getUserCredentialsFromExcel()
    username = userCredentials[0]
    password = userCredentials[1]
    GlobalVariables.apiLogs = True
    GlobalVariables.portalLogs = True
    GlobalVariables.cnpWareLogs = False
    GlobalVariables.middleWareLogs = False
    global success_Val_Execution
    success_Val_Execution = True

    try:
        login_payload = {'username': username, 'password': password}
        setUp.post(login_payload, "login")
        amount = random.randint(1, 99)
        cash_payload = {'username': username, 'password': password, 'amount': amount}
        cashPayment_resp = setUp.post(cash_payload, "cashPayment")
        setUp.get_TC_Exe_Time() # Get execution time
    except:
        setUp.get_TC_Exe_Time()
        print("Testcase did not complete due to exception in testcase execution")
        print("")
        GlobalVariables.EXCEL_TC_Execution = "Fail"
        GlobalVariables.Incomplete_ExecutionCount += 1

        pytest.fail()

    else:
        if str(cashPayment_resp['success']) == "True":
            GlobalVariables.EXCEL_TC_Execution = "Pass"
            current = datetime.now()
            GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")

            txn_id = cashPayment_resp['txnId']
            try:
                data = setUp.getValueFromDB("SELECT amount,username from ezetap_demo.txn where id='" + txn_id + "';")
                dbAmount = str(data['amount'].values[0])
                dbusername = str(data['username'].values[0])
                expectedDBValues = str(amount) + ".000:" + dbAmount + "," + str(username) + ":" + dbusername
            except:
                print("DB Validation did not complete due to exception in reading values from DB")
                print("")
                GlobalVariables.db_ValidationFailureCount +=1
                expectedDBValues = "Failed"
                GlobalVariables.EXCEL_DB_Val = "Fail"
                success_Val_Execution = False

            try:
                portalValues = validatePortal(GlobalVariables.portalDriver)
                portalType = portalValues["portalType"]
                portalStatus = portalValues["portalStatus"]
                portalAmount = portalValues["portalAmount"]
                portalUsername = portalValues["portalUsername"]
                portalTxnId = portalValues["portalTxnId"]
                expectedPortalValues = "CASH:" + portalType + ",Settled:" + portalStatus + ",Rs." + str(
                    amount) + ".00:" + portalAmount + "," + username + ":" + portalUsername + "," + txn_id + ":" + portalTxnId
            except:
                allure.attach(GlobalVariables.portalDriver.get_screenshot_as_png(), name="screenshot",
                              attachment_type=AttachmentType.PNG)
                print("Portal Validation did not complete due to exception in reading values from portal")
                print("")
                GlobalVariables.portal_ValidationFailureCount +=1
                expectedPortalValues = "Failed"
                GlobalVariables.EXCEL_Portal_Val = "Fail"
                success_Val_Execution = False

            expectedAPIValues = str(amount) + ".0:" + str(cashPayment_resp['amount']) + ",True:" + str(
                cashPayment_resp['success'])
            success = setUp.validateValues(expectedAPIValues, expectedDBValues, expectedPortalValues, "")

            if success_Val_Execution == False:
                if success == False:
                    pass
                else:
                    pytest.fail()
        else:
            check.equal(str(cashPayment_resp['success']), "True", "Cash payment execution failed")
            GlobalVariables.EXCEL_TC_Execution = "Fail"
            GlobalVariables.Incomplete_ExecutionCount += 1
            pytest.fail()
    finally:
        UserAssigner.releaseUserInExcel(str(userCredentials[0]))


@pytest.mark.usefixtures("log_on_failure","log_on_success")
def test_cash_payment_exe_failure(method_setup, session_setup, ui_driver):
    userCredentials = UserAssigner.getUserCredentialsFromExcel()
    username = userCredentials[0]
    password = userCredentials[1]
    GlobalVariables.apiLogs = True
    GlobalVariables.portalLogs = True
    GlobalVariables.cnpWareLogs = False
    GlobalVariables.middleWareLogs = False
    global success_Val_Execution
    success_Val_Execution = True

    try:
        login_payload = {'username': username, 'password': password}
        s = 2/0  #Exception
        print(s) #Exception
        setUp.post(login_payload, "login")
        amount = random.randint(1, 99)
        cash_payload = {'username': username, 'password': password, 'amount': amount}
        cashPayment_resp = setUp.post(cash_payload, "cashPayment")
        setUp.get_TC_Exe_Time() # Get execution time

    except:
        setUp.get_TC_Exe_Time()
        print("Testcase did not complete due to exception in testcase execution")
        print("")
        GlobalVariables.EXCEL_TC_Execution = "Fail"
        GlobalVariables.Incomplete_ExecutionCount += 1
        pytest.fail()

    else:
        if str(cashPayment_resp['success']) == "True":
            GlobalVariables.EXCEL_TC_Execution = "Pass"
            current = datetime.now()
            GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
            txn_id = cashPayment_resp['txnId']

            try:
                data = setUp.getValueFromDB("SELECT amount,username from ezetap_demo.txn where id='" + txn_id + "';")
                dbAmount = str(data['amount'].values[0])
                dbusername = str(data['username'].values[0])
                expectedDBValues = str(amount) + ".0:" + dbAmount + "," + str(username) + ":" + dbusername
            except:
                print("DB Validation did not complete due to exception in reading values from DB")
                print("")
                GlobalVariables.db_ValidationFailureCount +=1
                expectedDBValues = "Failed"
                GlobalVariables.EXCEL_DB_Val = "Fail"
                success_Val_Execution = False

            try:
                portalValues = validatePortal(GlobalVariables.portalDriver)
                portalType = portalValues["portalType"]
                portalStatus = portalValues["portalStatus"]
                portalAmount = portalValues["portalAmount"]
                portalUsername = portalValues["portalUsername"]
                portalTxnId = portalValues["portalTxnId"]
                expectedPortalValues = "CASH:" + portalType + ",Settled:" + portalStatus + ",₹ " + str(
                    amount) + ".00:" + portalAmount + "," + username + ":" + portalUsername + "," + txn_id + ":" + portalTxnId
            except:
                allure.attach(GlobalVariables.portalDriver.get_screenshot_as_png(), name="screenshot",
                              attachment_type=AttachmentType.PNG)
                print("Portal Validation did not complete due to exception in reading values from portal")
                print("")
                GlobalVariables.portal_ValidationFailureCount += 1
                expectedPortalValues = "Failed"
                GlobalVariables.EXCEL_Portal_Val = "Fail"
                success_Val_Execution = False

            expectedAPIValues = str(amount) + ".0:" + str(cashPayment_resp['amount']) + ",True:" + str(
                cashPayment_resp['success'])
            success = setUp.validateValues(expectedAPIValues, expectedDBValues, expectedPortalValues, "")

            if success_Val_Execution == False:
                if success == False:
                    pass
                else:
                    pytest.fail()
        else:
            check.equal(str(cashPayment_resp['success']), "True", "Cash payment execution failed")
            GlobalVariables.EXCEL_TC_Execution = "Fail"
            GlobalVariables.Incomplete_ExecutionCount += 1
    finally:
        UserAssigner.releaseUserInExcel(str(userCredentials[0]))



@pytest.mark.usefixtures("log_on_failure","log_on_success")
def test_cash_payment_val_exe_failure(method_setup, session_setup, ui_driver):
    userCredentials = UserAssigner.getUserCredentialsFromExcel()
    username = userCredentials[0]
    password = userCredentials[1]
    GlobalVariables.apiLogs = True
    GlobalVariables.portalLogs = True
    GlobalVariables.cnpWareLogs = False
    GlobalVariables.middleWareLogs = False
    global success_Val_Execution
    success_Val_Execution = True

    try:
        login_payload = {'username': username, 'password': password}
        setUp.post(login_payload, "login")
        amount = random.randint(1, 99)
        cash_payload = {'username': username, 'password': password, 'amount': amount}
        cashPayment_resp = setUp.post(cash_payload, "cashPayment")
        setUp.get_TC_Exe_Time() # Get execution time

    except:
        setUp.get_TC_Exe_Time()
        print("Testcase did not complete due to exception in testcase execution")
        print("")
        GlobalVariables.EXCEL_TC_Execution = "Fail"
        GlobalVariables.Incomplete_ExecutionCount += 1
        pytest.fail()

    else:
        if str(cashPayment_resp['success']) == "True":
            GlobalVariables.EXCEL_TC_Execution = "Pass"
            current = datetime.now()
            GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
            txn_id = cashPayment_resp['txnId']

            try:
                data = setUp.getValueFromDB("SELECT amount,username from ezetap_demo.txn where id='" + txn_id + "';")
                dbAmount = str(data['amount'].values[0])
                dbusername = str(data['username'].values[0])
                expectedDBValues = str(amount) + ".0:" + dbAmount + "," + str(username) + ":" + dbusername
            except:
                print("DB Validation did not complete due to exception in reading values from DB")
                print("")
                GlobalVariables.db_ValidationFailureCount +=1
                expectedDBValues = "Failed"
                GlobalVariables.EXCEL_DB_Val = "Fail"
                success_Val_Execution = False

            try:
                portalValues = validatePortal(GlobalVariables.portalDriver)
                portalType = portalValues["portalTypesss"]
                portalStatus = portalValues["portalStatus"]
                portalAmount = portalValues["portalAmount"]
                portalUsername = portalValues["portalUsername"]
                portalTxnId = portalValues["portalTxnId"]
                expectedPortalValues = "CASH:" + portalType + ",Settled:" + portalStatus + ",₹ " + str(
                    amount) + ".00:" + portalAmount + "," + username + ":" + portalUsername + "," + txn_id + ":" + portalTxnId
            except:
                allure.attach(GlobalVariables.portalDriver.get_screenshot_as_png(), name="screenshot",
                              attachment_type=AttachmentType.PNG)
                print("Portal Validation did not complete due to exception in reading values from portal")
                print("")
                GlobalVariables.portal_ValidationFailureCount += 1
                expectedPortalValues = "Failed"
                GlobalVariables.EXCEL_Portal_Val = "Fail"
                success_Val_Execution = False

            expectedAPIValues = str(amount) + ".0:" + str(cashPayment_resp['amount']) + ",True:" + str(
                cashPayment_resp['success'])
            success = setUp.validateValues(expectedAPIValues, expectedDBValues, expectedPortalValues, "")

            if success_Val_Execution == False:
                if success == False:
                    pass
                else:
                    pytest.fail()
        else:
            check.equal(str(cashPayment_resp['success']), "True", "Cash payment execution failed")
            GlobalVariables.EXCEL_TC_Execution = "Fail"
            GlobalVariables.Incomplete_ExecutionCount += 1
    finally:
        UserAssigner.releaseUserInExcel(str(userCredentials[0]))


def validatePortal(driver):
        LoginPageActivities.login(self, driver, portal_username, portal_password)
        time.sleep(3)

        HomePageActivities.search_for_merchant(self, driver, orgCode)
        HomePageActivities.switch_merchant(self, driver, orgCode)
        HomePageActivities.click_on_transactions_menu(self, driver)

        # def get_transaction_details(driver, txn_id):
        #     transactionRow = ""
        #     rowID = "ENT" + txn_id
        #     transactionDetails = {}
        #     total_transactions_count = len(driver.find_elements(By.XPATH, tbl_txnsRows_xpath))
        #     total_attributes_count = len(driver.find_elements(By.XPATH, tbl_txnsCols_xpath))
        #
        #     for row in range(1, total_transactions_count + 1):
        #         element = driver.find_element(By.XPATH, tbl_txnsRows_xpath + "[" + str(row) + "]")
        #         if element.get_attribute("id") == rowID:
        #             transactionRow = row
        #             break
        #     for col in range(1, total_attributes_count):
        #         attribute = driver.find_element(By.XPATH, tbl_txnsCols_xpath + "[" + str(col) + "]").get_attribute(
        #             "aria-label")
        #         if attribute.__contains__(": activate to sort column ascending"):
        #             attribute = attribute.replace(": activate to sort column ascending", "")
        #         attributeValue = driver.find_element(By.XPATH,
        #                                              tbl_txnsRows_xpath + "[" + str(transactionRow) + "]/td[" + str(
        #                                                  col) + "]").text
        #         transactionDetails[attribute] = attributeValue
        #     return transactionDetails
        #
        # # Locators
        # tbl_txns_xpath = "//table[@id='table_txns']"
        # tbl_txnsHeader_xpath = "//table[@id='table_txns']/thead"
        # tbl_txnsBody_xpath = "//table[@id='table_txns']/tbody"
        # tbl_txnsRows_xpath = "//table[@id='table_txns']/tbody/tr"
        # tbl_txnsCols_xpath = "//table[@id='table_txns']/thead//th"
        # ddl_transaction_xpath = "//a[text()='Transactions ']"
        # mnu_transactionSearch_xpath = "//a[text()='Search']"

        portalType = driver.find_element(By.XPATH, configReader.read_config("locators", "type_XPATH")).text
        portalStatus = driver.find_element(By.XPATH, configReader.read_config("locators", "status_XPATH")).text
        portalAmount = driver.find_element(By.XPATH, configReader.read_config("locators", "amount_XPATH")).text
        portalUsername = driver.find_element(By.XPATH, configReader.read_config("locators", "username_XPATH")).text
        portalTxnId = driver.find_element(By.XPATH, configReader.read_config("locators", "txnId_XPATH")).text

        D1 = {"portalType": portalType, "portalStatus": portalStatus, "portalAmount": portalAmount,
              "portalUsername": portalUsername, "portalTxnId": portalTxnId}
        return D1