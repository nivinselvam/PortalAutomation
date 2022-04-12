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

#Dev11 User Sandeep
# 4455445456
# q121212

# ############################### DEV11 ###########################################
# @pytest.mark.usefixtures("log_on_failure", "log_on_success")
def test_BQR_success(method_setup, session_setup, appium_driver):
    # GlobalVariables.apiLogs = True
    global success_Val_Execution
    success_Val_Execution = True
    try:
        wait = WebDriverWait(GlobalVariables.appDriver, 20)
        GlobalVariables.appDriver.find_element(By.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']").click()
        time.sleep(3)
        # Entering amount.
        GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_4").click()
        GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_2").click()
        GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_5").click()
        GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_dot").click()
        actual_Amount = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tv_totalAmount").text
        print(actual_Amount)
        GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tv_payBtn").click()
        GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tv_proceed").click()
        GlobalVariables.appDriver.find_element(By.XPATH, "//android.view.ViewGroup[@index=1]").click()

        time.sleep(30)
        element = WebDriverWait(GlobalVariables.appDriver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "com.ezetap.service.demo:id/ibtnBack")))
        GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/ibtnBack").click()
        GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnYesCancelPayment").click()

        setUp.get_TC_Exe_Time()

    except:
        allure.attach(GlobalVariables.appDriver.get_screenshot_as_png(), name="screenshot",
                          attachment_type=AttachmentType.PNG)
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
        try:
            GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnViewDetails").click()
            App_transactionId = GlobalVariables.appDriver.find_element(By.XPATH,
                                                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                                     '/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview'
                                                                     '.widget.RecyclerView/android.view.ViewGroup['
                                                                     '4]/android.widget.LinearLayout/android.widget.TextView[3]').text


            GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnDismiss").click()
            GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnProceed").click()
            GlobalVariables.appDriver.find_element(By.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']").click()
            GlobalVariables.appDriver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                           "/android.widget.FrameLayout/android.view.ViewGroup/android.widget."
                                                           "FrameLayout[2]/androidx.drawerlayout.widget.DrawerLayout/android"
                                                           ".widget.ListView/android.widget.LinearLayout[3]").click()

            App_Amount1 = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/trans_amount").text
            print("@@@@@@@@@@@@@")
            print(App_Amount1)
            # App_Amount = App_Amount1[2:7]
            GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/trans_amount").click()

            App_Tid = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tidValue").text
            App_mid = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/midValue").text
            expectedAPPValues = "28529837582:"+App_mid+",67456873:"+App_Tid+",₹ 425.00:"+App_Amount1
        except:
            allure.attach(GlobalVariables.appDriver.get_screenshot_as_png(), name="screenshot",
                              attachment_type=AttachmentType.PNG)
            print("App Validation did not complete due to exception in reading values from app")
            print("")
            GlobalVariables.app_ValidationFailureCount +=1
            expectedAPPValues = "Failed"
            GlobalVariables.EXCEL_App_Val = "Fail"
            success_Val_Execution = False
        print("Expected Values")
        print(expectedAPPValues)

        success = setUp.validateValues("", "", "", expectedAPPValues)

        if success_Val_Execution == False:
            if success == False:
                pass
            else:
                pytest.fail()



# @pytest.mark.usefixtures("log_on_failure", "log_on_success")
def test_BQR_failed(method_setup, session_setup, appium_driver):
    # GlobalVariables.apiLogs = True
    global success_Val_Execution
    success_Val_Execution = True
    try:
        wait = WebDriverWait(GlobalVariables.appDriver, 20)
        GlobalVariables.appDriver.find_element(By.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']").click()
        time.sleep(3)
        # Entering amount.
        GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_1").click()
        GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_5").click()
        GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_0").click()
        GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_dot").click()
        actual_Amount = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tv_totalAmount").text
        print(actual_Amount)
        GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tv_payBtn").click()
        GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tv_proceed").click()
        GlobalVariables.appDriver.find_element(By.XPATH, "//android.view.ViewGroup[@index=1]").click()

        time.sleep(30)
        element = WebDriverWait(GlobalVariables.appDriver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "com.ezetap.service.demo:id/ibtnBack")))
        GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/ibtnBack").click()
        GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnYesCancelPayment").click()

        setUp.get_TC_Exe_Time()

    except:
        allure.attach(GlobalVariables.appDriver.get_screenshot_as_png(), name="screenshot",
                          attachment_type=AttachmentType.PNG)
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
        try:
            GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnProceed").click()
            App_transactionId = GlobalVariables.appDriver.find_element(By.XPATH,
                                                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                                     '/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview'
                                                                     '.widget.RecyclerView/android.view.ViewGroup['
                                                                     '4]/android.widget.LinearLayout/android.widget.TextView[3]').text


            GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnDismiss").click()
            GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnProceed").click()
            GlobalVariables.appDriver.find_element(By.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']").click()
            GlobalVariables.appDriver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                           "/android.widget.FrameLayout/android.view.ViewGroup/android.widget."
                                                           "FrameLayout[2]/androidx.drawerlayout.widget.DrawerLayout/android"
                                                           ".widget.ListView/android.widget.LinearLayout[3]").click()

            App_Amount1 = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/trans_amount").text
            GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/trans_amount").click()

            App_Tid = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tidValue").text
            App_mid = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/midValue").text
            expectedAPPValues = "28529837582:"+App_mid+",67456873:"+App_Tid+",₹ 425.00:"+App_Amount1
        except:
            allure.attach(GlobalVariables.appDriver.get_screenshot_as_png(), name="screenshot",
                              attachment_type=AttachmentType.PNG)
            print("App Validation did not complete due to exception in reading values from app")
            print("")
            GlobalVariables.app_ValidationFailureCount +=1
            expectedAPPValues = "Failed"
            GlobalVariables.EXCEL_App_Val = "Fail"
            success_Val_Execution = False
        print("Expected Values")
        print(expectedAPPValues)

        success = setUp.validateValues("", "", "", expectedAPPValues)

        if success_Val_Execution == False:
            if success == False:
                pass
            else:
                pytest.fail()