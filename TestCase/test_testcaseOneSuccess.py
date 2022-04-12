import time
import datetime
from datetime import datetime

import pytest

from TestCase import setUp
from DataProvider import GlobalVariables

success_Val_Execution = True

@pytest.mark.usefixtures("log_on_failure","log_on_success")
def test_One_Success(method_setup, session_setup):
    GlobalVariables.apiLogs = False
    GlobalVariables.portalLogs = False
    GlobalVariables.cnpWareLogs = False
    GlobalVariables.middleWareLogs = False
    global success_Val_Execution
    success_Val_Execution = True

    try:
        a = 1+2
        time.sleep(1)
        setUp.get_TC_Exe_Time()  # Get execution time
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
        expectedAPIValues = "true:true,except:except"
        success = setUp.validateValues(expectedAPIValues, "", "", "")
        if success_Val_Execution == False:
            if success == False:
                pass
            else:
                pytest.fail()

@pytest.mark.usefixtures("log_on_failure","log_on_success")
def test_two_Success(method_setup, session_setup):
    GlobalVariables.apiLogs = False
    GlobalVariables.portalLogs = False
    GlobalVariables.cnpWareLogs = False
    GlobalVariables.middleWareLogs = False
    global success_Val_Execution
    success_Val_Execution = True

    try:
        time.sleep(2)
        a = 1/1
        setUp.get_TC_Exe_Time()  # Get execution time
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
        expectedAPIValues = "true:true,except:except"
        success = setUp.validateValues(expectedAPIValues, "", "", "")

        if success_Val_Execution == False:
            if success == False:
                pass
            else:
                pytest.fail()


@pytest.mark.usefixtures("log_on_failure","log_on_success")
def test_three(method_setup, session_setup):
    GlobalVariables.apiLogs = False
    GlobalVariables.portalLogs = False
    GlobalVariables.cnpWareLogs = False
    GlobalVariables.middleWareLogs = False
    global success_Val_Execution
    success_Val_Execution = True

    try:
        time.sleep(3)
        a = 1/1
        setUp.get_TC_Exe_Time()  # Get execution time
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
        expectedAPIValues = "true:true,except:except"
        success = setUp.validateValues(expectedAPIValues, "", "", "")

        if success_Val_Execution == False:
            if success == False:
                pass
            else:
                pytest.fail()


# @pytest.mark.usefixtures("log_on_failure","log_on_success")
# def test_three_Success(method_setup, session_setup):
#     GlobalVariables.apiLogs = False
#     GlobalVariables.portalLogs = False
#     GlobalVariables.cnpWareLogs = False
#     GlobalVariables.middleWareLogs = False
#     global success_Val_Execution
#     success_Val_Execution = True
#
#     time.sleep(3)
#     pytest.skip("Skipped the testcase")
#     GlobalVariables.EXCEL_TC_Execution = "Skip"
#     setUp.get_TC_Exe_Time()  # Get execution time



@pytest.mark.usefixtures("log_on_failure","log_on_success")
def test_four_Success(method_setup, session_setup):
    GlobalVariables.apiLogs = False
    GlobalVariables.portalLogs = False
    GlobalVariables.cnpWareLogs = False
    GlobalVariables.middleWareLogs = False
    global success_Val_Execution
    success_Val_Execution = True

    try:
        a = 1+2
        time.sleep(4)
        setUp.get_TC_Exe_Time()  # Get execution time
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
        expectedAPIValues = "true:true,except:except"
        success = setUp.validateValues(expectedAPIValues, "", "", "")
        if success_Val_Execution == False:
            if success == False:
                pass
            else:
                pytest.fail()
#
# @pytest.mark.usefixtures("log_on_failure","log_on_success")
# def test_five_Success(method_setup, session_setup):
#     GlobalVariables.apiLogs = False
#     GlobalVariables.portalLogs = False
#     GlobalVariables.cnpWareLogs = False
#     GlobalVariables.middleWareLogs = False
#     global success_Val_Execution
#     success_Val_Execution = True
#
#     try:
#         a = 1+2
#         time.sleep(4)
#         setUp.get_TC_Exe_Time()  # Get execution time
#     except:
#         setUp.get_TC_Exe_Time()
#         print("Testcase did not complete due to exception in testcase execution")
#         print("")
#         GlobalVariables.EXCEL_TC_Execution = "Fail"
#         GlobalVariables.Incomplete_ExecutionCount += 1
#         pytest.fail()
#
#     else:
#         GlobalVariables.EXCEL_TC_Execution = "Pass"
#         current = datetime.now()
#         GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
#         expectedAPIValues = "true:true,except:except"
#         success = setUp.validateValues(expectedAPIValues, "", "", "")
#         if success_Val_Execution == False:
#             if success == False:
#                 pass
#             else:
#                 pytest.fail()
#
# @pytest.mark.usefixtures("log_on_failure","log_on_success")
# def test_Six_Success(method_setup, session_setup):
#     GlobalVariables.apiLogs = False
#     GlobalVariables.portalLogs = False
#     GlobalVariables.cnpWareLogs = False
#     GlobalVariables.middleWareLogs = False
#     global success_Val_Execution
#     success_Val_Execution = True
#
#     try:
#         a = 1+2
#         time.sleep(3)
#         setUp.get_TC_Exe_Time()  # Get execution time
#     except:
#         setUp.get_TC_Exe_Time()
#         print("Testcase did not complete due to exception in testcase execution")
#         print("")
#         GlobalVariables.EXCEL_TC_Execution = "Fail"
#         GlobalVariables.Incomplete_ExecutionCount += 1
#         pytest.fail()
#
#     else:
#         GlobalVariables.EXCEL_TC_Execution = "Pass"
#         current = datetime.now()
#         GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
#         expectedAPIValues = "true:true,except:except"
#         success = setUp.validateValues(expectedAPIValues, "", "", "")
#         if success_Val_Execution == False:
#             if success == False:
#                 pass
#             else:
#                 pytest.fail()
#
#
# @pytest.mark.usefixtures("log_on_failure","log_on_success")
# def test_Seven_Success(method_setup, session_setup):
#     GlobalVariables.apiLogs = False
#     GlobalVariables.portalLogs = False
#     GlobalVariables.cnpWareLogs = False
#     GlobalVariables.middleWareLogs = False
#     global success_Val_Execution
#     success_Val_Execution = True
#
#     try:
#         a = 1+2
#         time.sleep(3)
#         setUp.get_TC_Exe_Time()  # Get execution time
#     except:
#         setUp.get_TC_Exe_Time()
#         print("Testcase did not complete due to exception in testcase execution")
#         print("")
#         GlobalVariables.EXCEL_TC_Execution = "Fail"
#         GlobalVariables.Incomplete_ExecutionCount += 1
#         pytest.fail()
#
#     else:
#         GlobalVariables.EXCEL_TC_Execution = "Pass"
#         current = datetime.now()
#         GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
#         expectedAPIValues = "true:true,except:except"
#         success = setUp.validateValues(expectedAPIValues, "", "", "")
#         if success_Val_Execution == False:
#             if success == False:
#                 pass
#             else:
#                 pytest.fail()
#
#
# @pytest.mark.usefixtures("log_on_failure","log_on_success")
# def test_Eight_Success(method_setup, session_setup):
#     GlobalVariables.apiLogs = False
#     GlobalVariables.portalLogs = False
#     GlobalVariables.cnpWareLogs = False
#     GlobalVariables.middleWareLogs = False
#     global success_Val_Execution
#     success_Val_Execution = True
#
#     try:
#         a = 1+2
#         time.sleep(3)
#         setUp.get_TC_Exe_Time()  # Get execution time
#     except:
#         setUp.get_TC_Exe_Time()
#         print("Testcase did not complete due to exception in testcase execution")
#         print("")
#         GlobalVariables.EXCEL_TC_Execution = "Fail"
#         GlobalVariables.Incomplete_ExecutionCount += 1
#         pytest.fail()
#
#     else:
#         GlobalVariables.EXCEL_TC_Execution = "Pass"
#         current = datetime.now()
#         GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
#         expectedAPIValues = "true:true,except:except"
#         success = setUp.validateValues(expectedAPIValues, "", "", "")
#         if success_Val_Execution == False:
#             if success == False:
#                 pass
#             else:
#                 pytest.fail()
#
#
# @pytest.mark.usefixtures("log_on_failure","log_on_success")
# def test_Nine_Success(method_setup, session_setup):
#     GlobalVariables.apiLogs = False
#     GlobalVariables.portalLogs = False
#     GlobalVariables.cnpWareLogs = False
#     GlobalVariables.middleWareLogs = False
#     global success_Val_Execution
#     success_Val_Execution = True
#
#     try:
#         a = 1+2
#         time.sleep(3)
#         setUp.get_TC_Exe_Time()  # Get execution time
#     except:
#         setUp.get_TC_Exe_Time()
#         print("Testcase did not complete due to exception in testcase execution")
#         print("")
#         GlobalVariables.EXCEL_TC_Execution = "Fail"
#         GlobalVariables.Incomplete_ExecutionCount += 1
#         pytest.fail()
#
#     else:
#         GlobalVariables.EXCEL_TC_Execution = "Pass"
#         current = datetime.now()
#         GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
#         expectedAPIValues = "true:true,except:except"
#         success = setUp.validateValues(expectedAPIValues, "", "", "")
#         if success_Val_Execution == False:
#             if success == False:
#                 pass
#             else:
#                 pytest.fail()
#
#
# @pytest.mark.usefixtures("log_on_failure","log_on_success")
# def test_Ten_Success(method_setup, session_setup):
#     GlobalVariables.apiLogs = False
#     GlobalVariables.portalLogs = False
#     GlobalVariables.cnpWareLogs = False
#     GlobalVariables.middleWareLogs = False
#     global success_Val_Execution
#     success_Val_Execution = True
#
#     try:
#         a = 1+2
#         time.sleep(3)
#         setUp.get_TC_Exe_Time()  # Get execution time
#     except:
#         setUp.get_TC_Exe_Time()
#         print("Testcase did not complete due to exception in testcase execution")
#         print("")
#         GlobalVariables.EXCEL_TC_Execution = "Fail"
#         GlobalVariables.Incomplete_ExecutionCount += 1
#         pytest.fail()
#
#     else:
#         GlobalVariables.EXCEL_TC_Execution = "Pass"
#         current = datetime.now()
#         GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
#         expectedAPIValues = "true:true,except:except"
#         success = setUp.validateValues(expectedAPIValues, "", "", "")
#         if success_Val_Execution == False:
#             if success == False:
#                 pass
#             else:
#                 pytest.fail()


# @pytest.mark.usefixtures("log_on_failure","log_on_success")
# def test_eleven_Success(method_setup, session_setup):
#     GlobalVariables.apiLogs = False
#     GlobalVariables.portalLogs = False
#     GlobalVariables.cnpWareLogs = False
#     GlobalVariables.middleWareLogs = False
#     global success_Val_Execution
#     success_Val_Execution = True
#
#     try:
#         a = 1+2
#         time.sleep(3)
#         setUp.get_TC_Exe_Time()  # Get execution time
#     except:
#         setUp.get_TC_Exe_Time()
#         print("Testcase did not complete due to exception in testcase execution")
#         print("")
#         GlobalVariables.EXCEL_TC_Execution = "Fail"
#         GlobalVariables.Incomplete_ExecutionCount += 1
#         pytest.fail()
#
#     else:
#         GlobalVariables.EXCEL_TC_Execution = "Pass"
#         current = datetime.now()
#         GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
#         expectedAPIValues = "true:true,except:except"
#         success = setUp.validateValues(expectedAPIValues, "", "", "")
#         if success_Val_Execution == False:
#             if success == False:
#                 pass
#             else:
#                 pytest.fail()
#
#
#
# @pytest.mark.usefixtures("log_on_failure","log_on_success")
# def test_Twelve_Success(method_setup, session_setup):
#     GlobalVariables.apiLogs = False
#     GlobalVariables.portalLogs = False
#     GlobalVariables.cnpWareLogs = False
#     GlobalVariables.middleWareLogs = False
#     global success_Val_Execution
#     success_Val_Execution = True
#
#     try:
#         a = 1+2
#         time.sleep(3)
#         setUp.get_TC_Exe_Time()  # Get execution time
#     except:
#         setUp.get_TC_Exe_Time()
#         print("Testcase did not complete due to exception in testcase execution")
#         print("")
#         GlobalVariables.EXCEL_TC_Execution = "Fail"
#         GlobalVariables.Incomplete_ExecutionCount += 1
#         pytest.fail()
#
#     else:
#         GlobalVariables.EXCEL_TC_Execution = "Pass"
#         current = datetime.now()
#         GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
#         expectedAPIValues = "true:true,except:except"
#         success = setUp.validateValues(expectedAPIValues, "", "", "")
#         if success_Val_Execution == False:
#             if success == False:
#                 pass
#             else:
#                 pytest.fail()
#
# @pytest.mark.usefixtures("log_on_failure","log_on_success")
# def test_trial_Success(method_setup, session_setup):
#     GlobalVariables.apiLogs = False
#     GlobalVariables.portalLogs = False
#     GlobalVariables.cnpWareLogs = False
#     GlobalVariables.middleWareLogs = False
#     global success_Val_Execution
#     success_Val_Execution = True
#
#     try:
#         a = 1+2
#         time.sleep(3)
#         setUp.get_TC_Exe_Time()  # Get execution time
#     except:
#         setUp.get_TC_Exe_Time()
#         print("Testcase did not complete due to exception in testcase execution")
#         print("")
#         GlobalVariables.EXCEL_TC_Execution = "Fail"
#         GlobalVariables.Incomplete_ExecutionCount += 1
#         pytest.fail()
#
#     else:
#         GlobalVariables.EXCEL_TC_Execution = "Pass"
#         current = datetime.now()
#         GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
#         expectedAPIValues = "true:true,except:except"
#         success = setUp.validateValues(expectedAPIValues, "", "", "")
#         if success_Val_Execution == False:
#             if success == False:
#                 pass
#             else:
#                 pytest.fail()
#
#
# @pytest.mark.usefixtures("log_on_failure","log_on_success")
# def test_Success(method_setup, session_setup):
#     GlobalVariables.apiLogs = False
#     GlobalVariables.portalLogs = False
#     GlobalVariables.cnpWareLogs = False
#     GlobalVariables.middleWareLogs = False
#     global success_Val_Execution
#     success_Val_Execution = True
#
#     try:
#         a = 1+2
#         time.sleep(3)
#         setUp.get_TC_Exe_Time()  # Get execution time
#     except:
#         setUp.get_TC_Exe_Time()
#         print("Testcase did not complete due to exception in testcase execution")
#         print("")
#         GlobalVariables.EXCEL_TC_Execution = "Fail"
#         GlobalVariables.Incomplete_ExecutionCount += 1
#         pytest.fail()
#
#     else:
#         GlobalVariables.EXCEL_TC_Execution = "Pass"
#         current = datetime.now()
#         GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
#         expectedAPIValues = "true:true,except:except"
#         success = setUp.validateValues(expectedAPIValues, "", "", "")
#         if success_Val_Execution == False:
#             if success == False:
#                 pass
#             else:
#                 pytest.fail()
#
#
# @pytest.mark.usefixtures("log_on_failure","log_on_success")
# def test_SuccessOne(method_setup, session_setup):
#     GlobalVariables.apiLogs = False
#     GlobalVariables.portalLogs = False
#     GlobalVariables.cnpWareLogs = False
#     GlobalVariables.middleWareLogs = False
#     global success_Val_Execution
#     success_Val_Execution = True
#
#     try:
#         a = 1+2
#         time.sleep(3)
#         setUp.get_TC_Exe_Time()  # Get execution time
#     except:
#         setUp.get_TC_Exe_Time()
#         print("Testcase did not complete due to exception in testcase execution")
#         print("")
#         GlobalVariables.EXCEL_TC_Execution = "Fail"
#         GlobalVariables.Incomplete_ExecutionCount += 1
#         pytest.fail()
#
#     else:
#         GlobalVariables.EXCEL_TC_Execution = "Pass"
#         current = datetime.now()
#         GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
#         expectedAPIValues = "true:true,except:except"
#         success = setUp.validateValues(expectedAPIValues, "", "", "")
#         if success_Val_Execution == False:
#             if success == False:
#                 pass
#             else:
#                 pytest.fail()
#
#
# @pytest.mark.usefixtures("log_on_failure","log_on_success")
# def test_SuccessThree(method_setup, session_setup):
#     GlobalVariables.apiLogs = False
#     GlobalVariables.portalLogs = False
#     GlobalVariables.cnpWareLogs = False
#     GlobalVariables.middleWareLogs = False
#     global success_Val_Execution
#     success_Val_Execution = True
#
#     try:
#         a = 1+2
#         time.sleep(3)
#         setUp.get_TC_Exe_Time()  # Get execution time
#     except:
#         setUp.get_TC_Exe_Time()
#         print("Testcase did not complete due to exception in testcase execution")
#         print("")
#         GlobalVariables.EXCEL_TC_Execution = "Fail"
#         GlobalVariables.Incomplete_ExecutionCount += 1
#         pytest.fail()
#
#     else:
#         GlobalVariables.EXCEL_TC_Execution = "Pass"
#         current = datetime.now()
#         GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
#         expectedAPIValues = "true:true,except:except"
#         success = setUp.validateValues(expectedAPIValues, "", "", "")
#         if success_Val_Execution == False:
#             if success == False:
#                 pass
#             else:
#                 pytest.fail()