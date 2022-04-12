import allure

from TestCase import setUp
from DataProvider import GlobalVariables
import time
import datetime
from datetime import datetime
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from allure_commons.types import AttachmentType

success_Val_Execution = True


# Dev11 User
invalid_cred_username = "7867456737"
invalid_cred_password = "A1234567"

# ############################### DEV11 ###########################################
# @pytest.mark.usefixtures("log_on_failure", "log_on_success")
def test_login_with_invalid_cred(method_setup, session_setup, appium_driver):
    # GlobalVariables.apiLogs = True

    wait = WebDriverWait(GlobalVariables.appDriver, 20)
    GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/txt_username").send_keys(invalid_cred_username)
    GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/txt_password").send_keys("D1234567")
    GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/btn_login").click()


    asd = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/grp_ezetap_logo_header").text()
    print("33333333333")
    print(asd)



def test_autoLogin():
    pass