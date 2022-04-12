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
@pytest.mark.usefixtures("log_on_failure", "log_on_success")
def test_Success(method_setup, session_setup, appium_driver):
    GlobalVariables.apiLogs = True
    try:
        wait = WebDriverWait(GlobalVariables.appDriver, 20)
        GlobalVariables.appDriver.find_element(By.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']").click()
        time.sleep(3)
        # Entering amount.
        GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_3").click()
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
            App_Amount = App_Amount1[2:7]
            GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/trans_amount").click()
            App_Tid = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tidValue").text
            # App_rrn = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/rrnValue").text
            expectedAPPValues = "12345678:"+App_Tid
        except:
            allure.attach(GlobalVariables.appDriver.get_screenshot_as_png(), name="screenshot",
                              attachment_type=AttachmentType.PNG)
            print("App Validation did not complete due to exception in reading values from app")
            print("")
            GlobalVariables.app_ValidationFailureCount +=1
            expectedAPPValues = "Failed"
            GlobalVariables.EXCEL_App_Val = "Fail"
            success_Val_Execution = False


        success = setUp.validateValues("", "", "", expectedAPPValues)

        if success_Val_Execution == False:
            if success == False:
                pass
            else:
                pytest.fail()






# @pytest.mark.usefixtures("log_on_failure", "log_on_success")
# def test_exe_failure(method_setup, session_setup, appium_driver):
#     GlobalVariables.apiLogs = True
#     try:
#         wait = WebDriverWait(GlobalVariables.appDriver, 20)
#         GlobalVariables.appDriver.find_element(By.XPATH,
#                                                "//android.widget.ImageButton[@content-desc='Navigate up']").click()
#         time.sleep(3)
#         # Entering amount.
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_3").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_3").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_2").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_dot").click()
#         actual_Amount = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tv_totalAmount").text
#         print(actual_Amount)
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tv_payBtn").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tv_proceed").click()
#         GlobalVariables.appDriver.find_element(By.XPATH, "//android.view.ViewGroup[@index=1]").click()
#
#         time.sleep(30)
#         element = WebDriverWait(GlobalVariables.appDriver, 10).until(
#             expected_conditions.presence_of_element_located((By.ID, "com.ezetap.service.demo:id/ibtnBack")))
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/ibtnBack").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnYesCancelPayment").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnViewDetails").click()
#
#         App_transactionId = GlobalVariables.appDriver.find_element(By.XPATH,
#                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
#                                                                    '/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview'
#                                                                    '.widget.RecyclerView/android.view.ViewGroup['
#                                                                    '4]/android.widget.LinearLayout/android.widget.TextView[3]').text
#
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnDismiss").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnProceed").click()
#         GlobalVariables.appDriver.find_element(By.XPATH,
#                                                "//android.widget.ImageButton[@content-desc='Navigate up']").click()
#         GlobalVariables.appDriver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
#                                                          "/android.widget.FrameLayout/android.view.ViewGroup/android.widget."
#                                                          "FrameLayout[2]/androidx.drawerlayout.widget.DrawerLayout/android"
#                                                          ".widget.ListView/android.widget.LinearLayout[3]").click()
#
#         App_Amount1 = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/trans_amount").text
#         App_Amount = App_Amount1[2:7]
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/trans_amoun").click() # Actual value 'trans_amount'
#         setUp.get_TC_Exe_Time()
#     except:
#         setUp.get_TC_Exe_Time()
#         print("Exception Occured In Execution")
#         GlobalVariables.EXCEL_TC_Execution = "Fail"
#         GlobalVariables.Incomplete_ExecutionCount += 1
#     else:
#         GlobalVariables.EXCEL_TC_Execution = "Pass"
#         current = datetime.now()
#         GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
#
#         try:
#             App_Tid = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tidValue").text
#             App_rrn = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/rrnValue").text
#         except:
#             print("Exception Occured In Execution of validation")
#             GlobalVariables.app_ValidationFailureCount += 1
#             expectedAPPValues = ""
#         else:
#             # CSVReaderUtility.csvdatacollection()
#             # csv_txn, csv_amount, csv_rrn, csv_tid = CSVReaderUtility.csvdatacollection()
#             expectedAPPValues = "True:True"
#
#         setUp.validateValues("", "", "", expectedAPPValues)
#
#
# @pytest.mark.usefixtures("log_on_failure", "log_on_success")
# def test_val_failure(method_setup, session_setup, appium_driver):
#     GlobalVariables.apiLogs = True
#     try:
#         wait = WebDriverWait(GlobalVariables.appDriver, 20)
#         GlobalVariables.appDriver.find_element(By.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']").click()
#         time.sleep(3)
#         # Entering amount.
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_3").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_2").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_5").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_dot").click()
#         actual_Amount = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tv_totalAmount").text
#         print(actual_Amount)
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tv_payBtn").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tv_proceed").click()
#         GlobalVariables.appDriver.find_element(By.XPATH, "//android.view.ViewGroup[@index=1]").click()
#
#         time.sleep(30)
#         element = WebDriverWait(GlobalVariables.appDriver, 10).until(
#             expected_conditions.presence_of_element_located((By.ID, "com.ezetap.service.demo:id/ibtnBack")))
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/ibtnBack").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnYesCancelPayment").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnViewDetails").click()
#
#
#         App_transactionId = GlobalVariables.appDriver.find_element(By.XPATH,
#                                                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
#                                                              '/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview'
#                                                              '.widget.RecyclerView/android.view.ViewGroup['
#                                                              '4]/android.widget.LinearLayout/android.widget.TextView[3]').text
#
#
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnDismiss").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnProceed").click()
#         GlobalVariables.appDriver.find_element(By.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']").click()
#         GlobalVariables.appDriver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
#                                                    "/android.widget.FrameLayout/android.view.ViewGroup/android.widget."
#                                                    "FrameLayout[2]/androidx.drawerlayout.widget.DrawerLayout/android"
#                                                    ".widget.ListView/android.widget.LinearLayout[3]").click()
#
#         App_Amount1 = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/trans_amount").text
#         App_Amount = App_Amount1[2:7]
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/trans_amount").click()
#         setUp.get_TC_Exe_Time()
#     except:
#         setUp.get_TC_Exe_Time()
#         print("Exception Occured In Execution")
#         GlobalVariables.EXCEL_TC_Execution = "Fail"
#         GlobalVariables.Incomplete_ExecutionCount += 1
#     else:
#         GlobalVariables.EXCEL_TC_Execution = "Pass"
#         current = datetime.now()
#         GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
#
#         try:
#             App_Tid = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tidValue").text
#             App_rrn = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/rrnValue").text
#         except:
#             print("Exception Occured In Execution of validation")
#             GlobalVariables.app_ValidationFailureCount +=1
#             expectedAPPValues = ""
#         else:
#             expectedAPPValues = "23423423423423:123" + ",True:True"
#         setUp.validateValues("", "", "", expectedAPPValues)



#Dev3 User
# 5999699900
# A123456

############################### DEV3 ###########################################
# @pytest.mark.usefixtures("log_on_failure", "log_on_success")
# def test_Success(method_setup, session_setup, appium_driver):
#     GlobalVariables.apiLogs = True
#     GlobalVariables.portalLogs = False
#     GlobalVariables.cnpWareLogs = False
#     GlobalVariables.middleWareLogs = False
#     global success_Val_Execution
#     success_Val_Execution = True
#     try:
#         wait = WebDriverWait(GlobalVariables.appDriver, 20)
#         GlobalVariables.appDriver.find_element(By.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']").click()
#         time.sleep(3)
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_3").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_2").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_5").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_dot").click()
#         actual_Amount = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tv_totalAmount").text
#
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tv_payBtn").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tv_proceed").click()
#         GlobalVariables.appDriver.find_element(By.XPATH, "//android.view.ViewGroup[@index=2]").click()
#         element = WebDriverWait(GlobalVariables.appDriver, 10).until(expected_conditions.presence_of_element_located((By.ID, "com.ezetap.service.demo:id/ibtnBack")))
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/ibtnBack").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnYesCancelPayment").click()
#
#         setUp.get_TC_Exe_Time()
#     except:
#         allure.attach(GlobalVariables.appDriver.get_screenshot_as_png(), name="screenshot",
#                       attachment_type=AttachmentType.PNG)
#         setUp.get_TC_Exe_Time()
#         print("Testcase did not complete due to exception in testcase execution")
#         print("")
#         GlobalVariables.EXCEL_TC_Execution = "Fail"
#         GlobalVariables.Incomplete_ExecutionCount += 1
#         pytest.fail()
#     else:
#         GlobalVariables.EXCEL_TC_Execution = "Pass"
#         current = datetime.now()
#         GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
#
#         try:
#             GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnViewDetails").click()
#             App_transactionId = GlobalVariables.appDriver.find_element(By.XPATH,
#                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
#                                                                        '/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview'
#                                                                        '.widget.RecyclerView/android.view.ViewGroup['
#                                                                        '4]/android.widget.LinearLayout/android.widget.TextView[3]').text
#
#             GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnDismiss").click()
#             GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnProceed").click()
#             GlobalVariables.appDriver.find_element(By.XPATH,
#                                                    "//android.widget.ImageButton[@content-desc='Navigate up']").click()
#             GlobalVariables.appDriver.find_element(By.XPATH,
#                                                    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
#                                                    "/android.view.ViewGroup/android.widget.FrameLayout["
#                                                    "2]/androidx.drawerlayout.widget.DrawerLayout/android.widget.ListView/android.widget"
#                                                    ".LinearLayout[5]/android.widget.LinearLayout").click()
#             App_Amount1 = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/trans_amount").text
#             App_Amount = App_Amount1[2:7]
#             GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/trans_amount").click()
#             App_TID = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tidValue").text
#             App_MID = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/midValue").text
#             expectedAPPValues = "47923743:"+App_TID+",749832748372841:"+App_MID
#         except:
#             allure.attach(GlobalVariables.appDriver.get_screenshot_as_png(), name="screenshot",
#                           attachment_type=AttachmentType.PNG)
#             print("App Validation did not complete due to exception in reading values from app")
#             print("")
#             GlobalVariables.app_ValidationFailureCount +=1
#             expectedAPPValues = "Failed"
#             GlobalVariables.EXCEL_App_Val = "Fail"
#             success_Val_Execution = False
#         success = setUp.validateValues("", "", "", expectedAPPValues)
#
#         if success_Val_Execution == False:
#             if success == False:
#                 pass
#             else:
#                 pytest.fail()
#
#
# @pytest.mark.usefixtures("log_on_failure", "log_on_success")
# def test_exe_Failure(method_setup, session_setup, appium_driver):
#     GlobalVariables.apiLogs = True
#     GlobalVariables.portalLogs = False
#     GlobalVariables.cnpWareLogs = False
#     GlobalVariables.middleWareLogs = False
#     global success_Val_Execution
#     success_Val_Execution = True
#     try:
#         wait = WebDriverWait(GlobalVariables.appDriver, 20)
#         GlobalVariables.appDriver.find_element(By.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']").click()
#         time.sleep(3)
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_3").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_2").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_5").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_dot").click()
#         actual_Amount = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tv_totalAmount").text
#
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tv_payBtn").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tv_procee").click() #Real Value 'tv_proceed'
#         GlobalVariables.appDriver.find_element(By.XPATH, "//android.view.ViewGroup[@index=2]").click()
#         element = WebDriverWait(GlobalVariables.appDriver, 10).until(expected_conditions.presence_of_element_located((By.ID, "com.ezetap.service.demo:id/ibtnBack")))
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/ibtnBack").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnYesCancelPayment").click()
#
#         setUp.get_TC_Exe_Time()
#     except:
#         allure.attach(GlobalVariables.appDriver.get_screenshot_as_png(), name="screenshot",
#                       attachment_type=AttachmentType.PNG)
#         setUp.get_TC_Exe_Time()
#         print("Testcase did not complete due to exception in testcase execution")
#         print("")
#         GlobalVariables.EXCEL_TC_Execution = "Fail"
#         GlobalVariables.Incomplete_ExecutionCount += 1
#         pytest.fail()
#     else:
#         GlobalVariables.EXCEL_TC_Execution = "Pass"
#         current = datetime.now()
#         GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
#
#         try:
#             GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnViewDetails").click()
#             App_transactionId = GlobalVariables.appDriver.find_element(By.XPATH,
#                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
#                                                                        '/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview'
#                                                                        '.widget.RecyclerView/android.view.ViewGroup['
#                                                                        '4]/android.widget.LinearLayout/android.widget.TextView[3]').text
#
#             GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnDismiss").click()
#             GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnProceed").click()
#             GlobalVariables.appDriver.find_element(By.XPATH,
#                                                    "//android.widget.ImageButton[@content-desc='Navigate up']").click()
#             GlobalVariables.appDriver.find_element(By.XPATH,
#                                                    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
#                                                    "/android.view.ViewGroup/android.widget.FrameLayout["
#                                                    "2]/androidx.drawerlayout.widget.DrawerLayout/android.widget.ListView/android.widget"
#                                                    ".LinearLayout[5]/android.widget.LinearLayout").click()
#             App_Amount1 = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/trans_amount").text
#             App_Amount = App_Amount1[2:7]
#             GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/trans_amount").click()
#             App_TID = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tidValue").text
#             App_MID = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/midValue").text
#             expectedAPPValues = "47923743:"+App_TID+",749832748372841:"+App_MID
#         except:
#             allure.attach(GlobalVariables.appDriver.get_screenshot_as_png(), name="screenshot",
#                           attachment_type=AttachmentType.PNG)
#             print("AppValidation did not complete due to exception in reading values from app")
#             print("")
#             GlobalVariables.app_ValidationFailureCount +=1
#             expectedAPPValues = "Failed"
#             GlobalVariables.EXCEL_App_Val = "Fail"
#             success_Val_Execution = False
#         success = setUp.validateValues("", "", "", expectedAPPValues)
#
#         if success_Val_Execution == False:
#             if success == False:
#                 pass
#             else:
#                 pytest.fail()
#
#
# @pytest.mark.usefixtures("log_on_failure", "log_on_success")
# def test_val_Failure(method_setup, session_setup, appium_driver):
#     GlobalVariables.apiLogs = True
#     GlobalVariables.portalLogs = False
#     GlobalVariables.cnpWareLogs = False
#     GlobalVariables.middleWareLogs = False
#     global success_Val_Execution
#     success_Val_Execution = True
#     try:
#         wait = WebDriverWait(GlobalVariables.appDriver, 20)
#         GlobalVariables.appDriver.find_element(By.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']").click()
#         time.sleep(3)
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_3").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_2").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_5").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_dot").click()
#         actual_Amount = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tv_totalAmount").text
#
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tv_payBtn").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tv_proceed").click()
#         GlobalVariables.appDriver.find_element(By.XPATH, "//android.view.ViewGroup[@index=2]").click()
#         element = WebDriverWait(GlobalVariables.appDriver, 10).until(expected_conditions.presence_of_element_located((By.ID, "com.ezetap.service.demo:id/ibtnBack")))
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/ibtnBack").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnYesCancelPayment").click()
#
#         setUp.get_TC_Exe_Time()
#     except:
#         allure.attach(GlobalVariables.appDriver.get_screenshot_as_png(), name="screenshot",
#                       attachment_type=AttachmentType.PNG)
#         setUp.get_TC_Exe_Time()
#         print("Testcase did not complete due to exception in testcase execution")
#         print("")
#         GlobalVariables.EXCEL_TC_Execution = "Fail"
#         GlobalVariables.Incomplete_ExecutionCount += 1
#         pytest.fail()
#     else:
#         GlobalVariables.EXCEL_TC_Execution = "Pass"
#         current = datetime.now()
#         GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
#
#         try:
#             GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnViewDetails").click()
#             App_transactionId = GlobalVariables.appDriver.find_element(By.XPATH,
#                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
#                                                                        '/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview'
#                                                                        '.widget.RecyclerView/android.view.ViewGroup['
#                                                                        '4]/android.widget.LinearLayout/android.widget.TextView[3]').text
#
#             GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnDismiss").click()
#             GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnProceed").click()
#             GlobalVariables.appDriver.find_element(By.XPATH,
#                                                    "//android.widget.ImageButton[@content-desc='Navigate up']").click()
#             GlobalVariables.appDriver.find_element(By.XPATH,
#                                                    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
#                                                    "/android.view.ViewGroup/android.widget.FrameLayout["
#                                                    "2]/androidx.drawerlayout.widget.DrawerLayout/android.widget.ListView/android.widget"
#                                                    ".LinearLayout[5]/android.widget.LinearLayout").click()
#             App_Amount1 = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/trans_amount").text
#             App_Amount = App_Amount1[2:7]
#             GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/trans_amount").click()
#             App_TID = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tidValue").text
#             App_MID = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/midValue").text
#             expectedAPPValues = "59923743:"+App_TID+",749832748372841:"+App_MID
#         except:
#             allure.attach(GlobalVariables.appDriver.get_screenshot_as_png(), name="screenshot",
#                           attachment_type=AttachmentType.PNG)
#             print("App Validation did not complete due to exception in reading values from app")
#             print("")
#             GlobalVariables.app_ValidationFailureCount +=1
#             expectedAPPValues = "Failed"
#             GlobalVariables.EXCEL_App_Val = "Fail"
#             success_Val_Execution = False
#         success = setUp.validateValues("", "", "", expectedAPPValues)
#
#         if success_Val_Execution == False:
#             if success == False:
#                 pass
#             else:
#                 pytest.fail()
#
# @pytest.mark.usefixtures("log_on_failure", "log_on_success")
# def test_app_val_exe_failure(method_setup, session_setup, appium_driver):
#     GlobalVariables.apiLogs = True
#     GlobalVariables.portalLogs = False
#     GlobalVariables.cnpWareLogs = False
#     GlobalVariables.middleWareLogs = False
#     global success_Val_Execution
#     success_Val_Execution = True
#     try:
#         wait = WebDriverWait(GlobalVariables.appDriver, 20)
#         GlobalVariables.appDriver.find_element(By.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']").click()
#         time.sleep(3)
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_3").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_2").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_5").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/button_dot").click()
#         actual_Amount = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tv_totalAmount").text
#
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tv_payBtn").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tv_proceed").click()
#         GlobalVariables.appDriver.find_element(By.XPATH, "//android.view.ViewGroup[@index=2]").click()
#         element = WebDriverWait(GlobalVariables.appDriver, 10).until(expected_conditions.presence_of_element_located((By.ID, "com.ezetap.service.demo:id/ibtnBack")))
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/ibtnBack").click()
#         GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnYesCancelPayment").click()
#
#         setUp.get_TC_Exe_Time()
#     except:
#         allure.attach(GlobalVariables.appDriver.get_screenshot_as_png(), name="screenshot",
#                       attachment_type=AttachmentType.PNG)
#         setUp.get_TC_Exe_Time()
#         print("Testcase did not complete due to exception in testcase execution")
#         print("")
#         GlobalVariables.EXCEL_TC_Execution = "Fail"
#         GlobalVariables.Incomplete_ExecutionCount += 1
#         pytest.fail()
#     else:
#         GlobalVariables.EXCEL_TC_Execution = "Pass"
#         current = datetime.now()
#         GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
#
#         try:
#             GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnViewDetails").click()
#             App_transactionId = GlobalVariables.appDriver.find_element(By.XPATH,
#                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
#                                                                        '/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview'
#                                                                        '.widget.RecyclerView/android.view.ViewGroup['
#                                                                        '4]/android.widget.LinearLayout/android.widget.TextView[3]').text
#
#             GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnDismiss").click()
#             GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.service.demo:id/btnProceed").click()
#             GlobalVariables.appDriver.find_element(By.XPATH,
#                                                    "//android.widget.ImageButton[@content-desc='Navigate up']").click()
#             GlobalVariables.appDriver.find_element(By.XPATH,
#                                                    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
#                                                    "/android.view.ViewGroup/android.widget.FrameLayout["
#                                                    "2]/androidx.drawerlayout.widget.DrawerLayout/android.widget.ListView/android.widget"
#                                                    ".LinearLayout[5]/android.widget.LinearLayout").click()
#             App_Amount1 = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/trans_amount").text
#             App_Amount = App_Amount1[2:7]
#             GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/trans_amount").click()
#             App_TID = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/tidValuesss").text #tidValue
#             App_MID = GlobalVariables.appDriver.find_element(By.ID, "com.ezetap.basicapp:id/midValue").text
#             expectedAPPValues = "47923743:"+App_TID+",749832748372841:"+App_MID
#         except:
#             allure.attach(GlobalVariables.appDriver.get_screenshot_as_png(), name="screenshot",
#                           attachment_type=AttachmentType.PNG)
#             print("App Validation did not complete due to exception in reading values from app")
#             print("")
#             GlobalVariables.app_ValidationFailureCount +=1
#             expectedAPPValues = "Failed"
#             GlobalVariables.EXCEL_App_Val = "Fail"
#             success_Val_Execution = False
#         success = setUp.validateValues("", "", "", expectedAPPValues)
#
#         if success_Val_Execution == False:
#             if success == False:
#                 pass
#             else:
#                 pytest.fail()



