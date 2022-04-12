import time
import datetime
from datetime import datetime

import allure
import pytest
from selenium.webdriver.common.by import By
from self import self
from allure_commons.types import AttachmentType

from Pages.LoginPageActivities import LoginPageActivities
from Pages.HomePageActivities import HomePageActivities
from Pages.EditMerchantActivities import EditMerchantActivities
from Pages.UsersActivities import UsersActivities
from Pages.UserDetailsActivities import UserDetailsActivities
from TestCase import setUp
from DataProvider import GlobalVariables

# driver = webdriver.Chrome('/home/ezetap/Downloads/chromedriver_linux64/chromedriver')
from Utilities import configReader

portal_username = "8078151226"
portal_password = "D1234567"
username="1012101210"
password="A1234567"
orgCode="AUTO_PYTHON_TRIAL"
appkey = "appKey"

success_Val_Execution = True

@pytest.mark.order(1)
@pytest.mark.usefixtures("log_on_failure","log_on_success")
def test_deactivateMerchant(method_setup, session_setup, ui_driver):
    GlobalVariables.portalLogs = True
    GlobalVariables.apiLogs = False
    GlobalVariables.middleWareLogs = False
    GlobalVariables.cnpWareLogs = False
    global success_Val_Execution
    success_Val_Execution = True
    try:
        LoginPageActivities.login(self, GlobalVariables.portalDriver, portal_username, portal_password)
        time.sleep(5)
        HomePageActivities.search_for_merchant(self, GlobalVariables.portalDriver, orgCode)
        HomePageActivities.switch_merchant(self, GlobalVariables.portalDriver, orgCode)
        HomePageActivities.edit_merchant(self, GlobalVariables.portalDriver)
        EditMerchantActivities.status_inactive(self, GlobalVariables.portalDriver)
        EditMerchantActivities.save_changes(self, GlobalVariables.portalDriver)
        setUp.get_TC_Exe_Time()
    except:
        allure.attach(GlobalVariables.portalDriver.get_screenshot_as_png(), name="screenshot",
                      attachment_type=AttachmentType.PNG)
        setUp.get_TC_Exe_Time()
        print("Testcase did not complete due to exception in testcase execution")
        print("")
        GlobalVariables.EXCEL_TC_Execution = "Fail"
        GlobalVariables.Incomplete_ExecutionCount += 1
        pytest.fail()

    else:
        # Validations
        GlobalVariables.EXCEL_TC_Execution = "Pass"
        current = datetime.now()
        GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")

        try:
            # DB
            data = setUp.getValueFromDB("SELECT status from ezetap_demo.org where org_code='" + orgCode + "';")
            dbStatus = str(data['status'].values[0])
            expectedDBValues = "INACTIVE:" + dbStatus
        except:
            print("DB Validation did not complete due to exception in reading values from DB")
            print("")
            GlobalVariables.db_ValidationFailureCount +=1
            expectedDBValues = "Failed"
            GlobalVariables.EXCEL_DB_Val = "Fail"
            success_Val_Execution = False

        # Portal
        try:
            HomePageActivities.click_on_merchants_menu(self, GlobalVariables.portalDriver)
            HomePageActivities.click_on_merchantName_button(self, GlobalVariables.portalDriver)
            time.sleep(5)
            st = GlobalVariables.portalDriver.find_element(By.XPATH, "//div[@class='form-msg-info']/h3").text
            expectedPortalValues = "No Merchants found:" + st
        except:
            allure.attach(GlobalVariables.portalDriver.get_screenshot_as_png(), name="screenshot",
                          attachment_type=AttachmentType.PNG)
            print("Portal Validation did not complete due to exception in reading values from portal")
            print("")
            GlobalVariables.portal_ValidationFailureCount += 1
            expectedPortalValues = "Failed"
            GlobalVariables.EXCEL_Portal_Val = "Fail"
            success_Val_Execution = False

        success = setUp.validateValues("", expectedDBValues, expectedPortalValues, "")
        if success_Val_Execution == False:
            if success == False:
                pass
            else:
                pytest.fail()


@pytest.mark.order(2)
@pytest.mark.usefixtures("log_on_failure","log_on_success")
def test_activateMerchant(method_setup, session_setup, ui_driver):
    GlobalVariables.portalLogs = True
    GlobalVariables.apiLogs = False
    GlobalVariables.middleWareLogs = False
    GlobalVariables.cnpWareLogs = False
    global success_Val_Execution
    success_Val_Execution = True
    try:
        LoginPageActivities.login(self, GlobalVariables.portalDriver, portal_username, portal_password)
        time.sleep(5)
        HomePageActivities.click_on_merchants_menu(self, GlobalVariables.portalDriver)

        url = configReader.read_config("APIs", "baseUrl") + configReader.read_config("APIs", "portalEditMerchant")
        GlobalVariables.portalDriver.get(url)
        EditMerchantActivities.status_active(self, GlobalVariables.portalDriver)
        EditMerchantActivities.save_changes(self, GlobalVariables.portalDriver)
        setUp.get_TC_Exe_Time()
    except:
        allure.attach(GlobalVariables.portalDriver.get_screenshot_as_png(), name="screenshot",
                      attachment_type=AttachmentType.PNG)
        setUp.get_TC_Exe_Time()
        print("Testcase did not complete due to exception in testcase execution")
        print("")
        GlobalVariables.EXCEL_TC_Execution = "Fail"
        GlobalVariables.Incomplete_ExecutionCount += 1
        pytest.fail()
    else:
        # Validations
        GlobalVariables.EXCEL_TC_Execution = "Pass"
        current = datetime.now()
        GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")

        # DB
        try:
            data = setUp.getValueFromDB("SELECT status from ezetap_demo.org where org_code='" + orgCode + "';")
            dbStatus = str(data['status'].values[0])
            expectedDBValues = "ACTIVE:" + dbStatus
        except:
            print("DB Validation did not complete due to exception in reading values from DB")
            print("")
            GlobalVariables.db_ValidationFailureCount +=1
            expectedDBValues = "Failed"
            GlobalVariables.EXCEL_DB_Val = "Fail"
            success_Val_Execution = False

        success = setUp.validateValues("", expectedDBValues, "", "")
        if success_Val_Execution == False:
            if success == False:
                pass
            else:
                pytest.fail()


@pytest.mark.order(3)
@pytest.mark.usefixtures("log_on_failure","log_on_success")
def test_deactivateUser(method_setup, session_setup, ui_driver):
    GlobalVariables.portalLogs = True
    GlobalVariables.apiLogs = False
    GlobalVariables.middleWareLogs = False
    GlobalVariables.cnpWareLogs = False
    global success_Val_Execution
    success_Val_Execution = True
    try:
        LoginPageActivities.login(self, GlobalVariables.portalDriver, portal_username, portal_password)
        time.sleep(5)
        HomePageActivities.search_for_merchant(self, GlobalVariables.portalDriver, orgCode)
        HomePageActivities.switch_merchant(self, GlobalVariables.portalDriver, orgCode)
        HomePageActivities.click_on_users_menu(self, GlobalVariables.portalDriver)
        UsersActivities.click_edit_user(self, GlobalVariables.portalDriver, username)
        UserDetailsActivities.inactivate_user(self, GlobalVariables.portalDriver)
        UserDetailsActivities.save_details(self, GlobalVariables.portalDriver)
        setUp.get_TC_Exe_Time()

    except:
        allure.attach(GlobalVariables.portalDriver.get_screenshot_as_png(), name="screenshot",
                      attachment_type=AttachmentType.PNG)
        setUp.get_TC_Exe_Time()
        print("Testcase did not complete due to exception in testcase execution")
        print("")
        GlobalVariables.EXCEL_TC_Execution = "Fail"
        GlobalVariables.Incomplete_ExecutionCount += 1
        pytest.fail()

    else:
        # Validations
        GlobalVariables.EXCEL_TC_Execution = "Pass"
        current = datetime.now()
        GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")

        # DB
        try:
            data = setUp.getValueFromDB("SELECT status from ezetap_demo.org_employee where username='" + username + "';")
            dbStatus = str(data['status'].values[0])
            expectedDBValues = "INACTIVE:" + dbStatus
        except:
            print("DB Validation did not complete due to exception in reading values from DB")
            print("")
            GlobalVariables.db_ValidationFailureCount +=1
            expectedDBValues ="Failed"
            GlobalVariables.EXCEL_DB_Val = "Fail"
            success_Val_Execution = False
        try:
            # Portal
            HomePageActivities.click_on_users_menu(self, GlobalVariables.portalDriver)
            UsersActivities.click_edit_user(self, GlobalVariables.portalDriver, username)
            isSelected = GlobalVariables.portalDriver.find_element(By.ID, "status2").is_selected()
            expectedPortalValues = "True" + ":" + str(isSelected)
        except:
            allure.attach(GlobalVariables.portalDriver.get_screenshot_as_png(), name="screenshot",
                          attachment_type=AttachmentType.PNG)
            print("Portal Validation did not complete due to exception in reading values from portal")
            print("")
            GlobalVariables.portal_ValidationFailureCount +=1
            expectedPortalValues = "Failed"
            GlobalVariables.EXCEL_Portal_Val = "Fail"
            success_Val_Execution = False


        success = setUp.validateValues("", expectedDBValues, expectedPortalValues, "")
        if success_Val_Execution == False:
            if success == False:
                pass
            else:
                pytest.fail()

@pytest.mark.order(4)
@pytest.mark.usefixtures("log_on_failure","log_on_success")
def test_activateUser(method_setup, session_setup, ui_driver):
    GlobalVariables.portalLogs = True
    GlobalVariables.apiLogs = False
    GlobalVariables.middleWareLogs = False
    GlobalVariables.cnpWareLogs = False
    global success_Val_Execution
    success_Val_Execution = True

    try:
        LoginPageActivities.login(self, GlobalVariables.portalDriver, portal_username, portal_password)
        time.sleep(5)
        HomePageActivities.search_for_merchant(self, GlobalVariables.portalDriver, orgCode)
        HomePageActivities.switch_merchant(self, GlobalVariables.portalDriver, orgCode)
        HomePageActivities.click_on_users_menu(self, GlobalVariables.portalDriver)
        UsersActivities.click_edit_user(self, GlobalVariables.portalDriver, username)
        UserDetailsActivities.activate_user(self, GlobalVariables.portalDriver)
        UserDetailsActivities.save_details(self, GlobalVariables.portalDriver)
        setUp.get_TC_Exe_Time()
    except:
        allure.attach(GlobalVariables.portalDriver.get_screenshot_as_png(), name="screenshot",
                      attachment_type=AttachmentType.PNG)
        setUp.get_TC_Exe_Time()
        print("Testcase did not complete due to exception in testcase execution")
        print("")
        GlobalVariables.EXCEL_TC_Execution = "Fail"
        GlobalVariables.Incomplete_ExecutionCount += 1
        pytest.fail()
    else:
        # Validations
        GlobalVariables.EXCEL_TC_Execution = "Pass"
        current = datetime.now()
        GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")

        # Portal
        try:
            success = GlobalVariables.portalDriver.find_element(By.XPATH, "//div[text()='User information is successfully updated.']").text
            HomePageActivities.click_on_users_menu(self, GlobalVariables.portalDriver)
            UsersActivities.click_edit_user(self, GlobalVariables.portalDriver, username)
            isSelected = GlobalVariables.portalDriver.find_element(By.ID, "status1").is_selected()
            expectedPortalValues = "User information is successfully updated.:" + success + "," + "True" + ":" + str(isSelected)
        except:
            allure.attach(GlobalVariables.portalDriver.get_screenshot_as_png(), name="screenshot",
                          attachment_type=AttachmentType.PNG)
            print("Portal Validation did not complete due to exception in reading values from portal")
            print("")
            GlobalVariables.portal_ValidationFailureCount +=1
            expectedPortalValues = "Failed"
            GlobalVariables.EXCEL_Portal_Val = "Fail"
            success_Val_Execution = False

        # DB
        try:
            data = setUp.getValueFromDB("SELECT status from ezetap_demo.org_employee where username='" + username + "';")
            dbStatus = str(data['status'].values[0])
            expectedDBValues = "ACTIVE:" + dbStatus
        except:
            print("DB Validation did not complete due to exception in reading values from DB")
            print("")
            GlobalVariables.db_ValidationFailureCount += 1
            expectedDBValues = "Failed"
            GlobalVariables.EXCEL_DB_Val = "Fail"
            success_Val_Execution = False

        success = setUp.validateValues("", expectedDBValues, expectedPortalValues, "")

        if success_Val_Execution == False:
            if success == False:
                pass
            else:
                pytest.fail()