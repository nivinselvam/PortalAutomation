import pytest

from TestCase import setUp, rerunTest, UserAssigner
from DataProvider import GlobalVariables
import time
import datetime
from datetime import datetime

from Utilities import configReader
import random

username = "1234987650"
password = "A1234567"

@pytest.mark.apiVal
@pytest.mark.dbVals
@pytest.mark.portalVal
@pytest.mark.usefixtures("log_on_success", "method_setup")
def test_success():
    # userCredentials = UserAssigner.getUserCredentialsFromExcel()
    # username = userCredentials[0]
    # password = userCredentials[1]
    GlobalVariables.apiLogs = True
    GlobalVariables.portalLogs = True
    GlobalVariables.cnpWareLogs = False
    GlobalVariables.middleWareLogs = False
    global success_Val_Execution
    success_Val_Execution = True

    try:
        print("EXECUTING TEST CASE test_success")
        time.sleep(5)
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

        if (configReader.read_config("Validations", "api_validation")) == "True":
            try:
                time.sleep(1)
                expectedAPIValues = "qwerty:qwerty,zxcv:zxcv"
            except:
                print("API Validation did not complete due to exception")
                print("")
                GlobalVariables.api_ValidationFailureCount += 1
                expectedAPIValues = "Failed"
                GlobalVariables.EXCEL_API_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedAPIValues = ""

        if (configReader.read_config("Validations", "db_validation")) == "True":
            try:
                time.sleep(1)
                expectedDBValues = "10.0:10.0,787878:787878"
            except:
                print("DB Validation did not complete due to exception in reading values from DB")
                print("")
                GlobalVariables.db_ValidationFailureCount += 1
                expectedDBValues = "Failed"
                GlobalVariables.EXCEL_DB_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedDBValues = ""

        if (configReader.read_config("Validations", "portal_validation")) == "True":
            try:
                time.sleep(1)
                expectedPortalValues = "CASH:CASH,909090:909090"
            except:
                print("Portal Validation did not complete due to exception in reading values from portal")
                print("")
                GlobalVariables.portal_ValidationFailureCount += 1
                expectedPortalValues = "Failed"
                GlobalVariables.EXCEL_Portal_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedPortalValues = ""

        success = setUp.validateValues(expectedAPIValues, expectedDBValues, expectedPortalValues, "")

        if success_Val_Execution == False:
            if success == False:
                pass
            else:
                pytest.fail()
    # finally:
        # UserAssigner.releaseUserInExcel(str(userCredentials[0]))



@pytest.mark.apiVal
@pytest.mark.dbVals
@pytest.mark.portalVal
@pytest.mark.usefixtures("log_on_success", "method_setup")
def test_successTwo():
    GlobalVariables.apiLogs = False
    GlobalVariables.portalLogs = False
    GlobalVariables.cnpWareLogs = False
    GlobalVariables.middleWareLogs = False
    global success_Val_Execution
    success_Val_Execution = True

    try:
        print("EXECUTING test_successTwo")
        time.sleep(30)
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

        if (configReader.read_config("Validations", "api_validation")) == "True":
            try:
                time.sleep(1)
                expectedAPIValues = "qwerty:qwerty,zxcv:zxcv"
            except:
                print("API Validation did not complete due to exception")
                print("")
                GlobalVariables.api_ValidationFailureCount += 1
                expectedAPIValues = "Failed"
                GlobalVariables.EXCEL_API_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedAPIValues = ""

        if (configReader.read_config("Validations", "db_validation")) == "True":
            try:
                time.sleep(1)
                expectedDBValues = "10.0:10.0,787878:787878"
            except:
                print("DB Validation did not complete due to exception in reading values from DB")
                print("")
                GlobalVariables.db_ValidationFailureCount += 1
                expectedDBValues = "Failed"
                GlobalVariables.EXCEL_DB_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedDBValues = ""

        if (configReader.read_config("Validations", "portal_validation")) == "True":
            try:
                time.sleep(1)
                expectedPortalValues = "CASH:CASH,909090:909090"
            except:
                print("Portal Validation did not complete due to exception in reading values from portal")
                print("")
                GlobalVariables.portal_ValidationFailureCount += 1
                expectedPortalValues = "Failed"
                GlobalVariables.EXCEL_Portal_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedPortalValues =""

        success = setUp.validateValues(expectedAPIValues, expectedDBValues, expectedPortalValues, "")

        if success_Val_Execution == False:
            if success == False:
                pass
            else:
                pytest.fail()



@pytest.mark.apiVal
@pytest.mark.dbVals
@pytest.mark.portalVal
@pytest.mark.usefixtures("log_on_success", "method_setup")
def test_successThree():
    GlobalVariables.apiLogs = False
    GlobalVariables.portalLogs = False
    GlobalVariables.cnpWareLogs = False
    GlobalVariables.middleWareLogs = False
    global success_Val_Execution
    success_Val_Execution = True

    try:
        print("EXECUTING FIRST TEST CASE : SUCCESS")
        time.sleep(1)
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

        if (configReader.read_config("Validations", "api_validation")) == "True":
            try:
                time.sleep(1)
                expectedAPIValues = "qwerty:qwerty,zxcv:zxcv"
            except:
                print("API Validation did not complete due to exception")
                print("")
                GlobalVariables.api_ValidationFailureCount += 1
                expectedAPIValues = "Failed"
                GlobalVariables.EXCEL_API_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedAPIValues = ""

        if (configReader.read_config("Validations", "db_validation")) == "True":
            try:
                time.sleep(1)
                expectedDBValues = "10.0:10.0,787878:787878"
            except:
                print("DB Validation did not complete due to exception in reading values from DB")
                print("")
                GlobalVariables.db_ValidationFailureCount += 1
                expectedDBValues = "Failed"
                GlobalVariables.EXCEL_DB_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedDBValues =""

        if (configReader.read_config("Validations", "portal_validation")) == "True":
            try:
                time.sleep(1)
                expectedPortalValues = "CASH:CASH,909090:909090"
            except:
                print("Portal Validation did not complete due to exception in reading values from portal")
                print("")
                GlobalVariables.portal_ValidationFailureCount += 1
                expectedPortalValues = "Failed"
                GlobalVariables.EXCEL_Portal_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedPortalValues = ""

        success = setUp.validateValues(expectedAPIValues, expectedDBValues, expectedPortalValues, "")

        if success_Val_Execution == False:
            if success == False:
                pass
            else:
                pytest.fail()


@pytest.mark.apiVal
@pytest.mark.dbVals
@pytest.mark.portalVal
@pytest.mark.usefixtures("log_on_success", "method_setup")
def test_failFour():
    GlobalVariables.apiLogs = False
    GlobalVariables.portalLogs = False
    GlobalVariables.cnpWareLogs = False
    GlobalVariables.middleWareLogs = False
    global success_Val_Execution
    success_Val_Execution = True

    try:
        print("EXECUTING FIRST TEST CASE : SUCCESS")
        time.sleep(1)
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

        if (configReader.read_config("Validations", "api_validation")) == "True":
            try:
                time.sleep(1)
                expectedAPIValues = "qwerty:qwerty,zxcv:zxcv"
            except:
                print("API Validation did not complete due to exception")
                print("")
                GlobalVariables.api_ValidationFailureCount += 1
                expectedAPIValues = "Failed"
                GlobalVariables.EXCEL_API_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedAPIValues = ""

        if (configReader.read_config("Validations", "db_validation")) == "True":
            try:
                time.sleep(1)
                expectedDBValues = "10.0:10.0,787878:688788"
            except:
                print("DB Validation did not complete due to exception in reading values from DB")
                print("")
                GlobalVariables.db_ValidationFailureCount += 1
                expectedDBValues = "Failed"
                GlobalVariables.EXCEL_DB_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedDBValues =""

        if (configReader.read_config("Validations", "portal_validation")) == "True":
            try:
                time.sleep(1)
                expectedPortalValues = "CASH:CASH,909090:909090"
            except:
                print("Portal Validation did not complete due to exception in reading values from portal")
                print("")
                GlobalVariables.portal_ValidationFailureCount += 1
                expectedPortalValues = "Failed"
                GlobalVariables.EXCEL_Portal_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedPortalValues = ""

        success = setUp.validateValues(expectedAPIValues, expectedDBValues, expectedPortalValues, "")

        if success_Val_Execution == False:
            if success == False:
                pass
            else:
                pytest.fail()



@pytest.mark.apiVal
@pytest.mark.dbVals
@pytest.mark.portalVal
@pytest.mark.usefixtures("log_on_success", "method_setup")
def test_successFive():
    GlobalVariables.apiLogs = False
    GlobalVariables.portalLogs = False
    GlobalVariables.cnpWareLogs = False
    GlobalVariables.middleWareLogs = False
    global success_Val_Execution
    success_Val_Execution = True

    try:
        print("EXECUTING test_successFive")
        time.sleep(3)
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

        if (configReader.read_config("Validations", "api_validation")) == "True":
            try:
                time.sleep(1)
                expectedAPIValues = "qwerty:qwerty,zxcv:zxcv"
            except:
                print("API Validation did not complete due to exception")
                print("")
                GlobalVariables.api_ValidationFailureCount += 1
                expectedAPIValues = "Failed"
                GlobalVariables.EXCEL_API_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedAPIValues = ""

        if (configReader.read_config("Validations", "db_validation")) == "True":
            try:
                time.sleep(1)
                expectedDBValues = "10.0:10.0,787878:787878"
            except:
                print("DB Validation did not complete due to exception in reading values from DB")
                print("")
                GlobalVariables.db_ValidationFailureCount += 1
                expectedDBValues = "Failed"
                GlobalVariables.EXCEL_DB_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedDBValues =""

        if (configReader.read_config("Validations", "portal_validation")) == "True":
            try:
                time.sleep(1)
                expectedPortalValues = "CASH:CASH,909090:909090"
            except:
                print("Portal Validation did not complete due to exception in reading values from portal")
                print("")
                GlobalVariables.portal_ValidationFailureCount += 1
                expectedPortalValues = "Failed"
                GlobalVariables.EXCEL_Portal_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedPortalValues =""

        success = setUp.validateValues(expectedAPIValues, expectedDBValues, expectedPortalValues, "")

        if success_Val_Execution == False:
            if success == False:
                pass
            else:
                pytest.fail()



@pytest.mark.apiVal
@pytest.mark.dbVals
@pytest.mark.portalVal
@pytest.mark.usefixtures("log_on_success", "method_setup")
def test_successSix():
    GlobalVariables.apiLogs = False
    GlobalVariables.portalLogs = False
    GlobalVariables.cnpWareLogs = False
    GlobalVariables.middleWareLogs = False
    global success_Val_Execution
    success_Val_Execution = True

    try:
        print("EXECUTING FIRST TEST CASE : SUCCESS")
        time.sleep(1)
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

        if (configReader.read_config("Validations", "api_validation")) == "True":
            try:
                time.sleep(1)
                expectedAPIValues = "qwerty:qwerty,zxcv:zxcv"
            except:
                print("API Validation did not complete due to exception")
                print("")
                GlobalVariables.api_ValidationFailureCount += 1
                expectedAPIValues = "Failed"
                GlobalVariables.EXCEL_API_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedAPIValues = ""

        if (configReader.read_config("Validations", "db_validation")) == "True":
            try:
                time.sleep(1)
                expectedDBValues = "10.0:10.0,787878:787878"
            except:
                print("DB Validation did not complete due to exception in reading values from DB")
                print("")
                GlobalVariables.db_ValidationFailureCount += 1
                expectedDBValues = "Failed"
                GlobalVariables.EXCEL_DB_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedDBValues =""

        if (configReader.read_config("Validations", "portal_validation")) == "True":
            try:
                time.sleep(1)
                expectedPortalValues = "CASH:CASH,909090:909090"
            except:
                print("Portal Validation did not complete due to exception in reading values from portal")
                print("")
                GlobalVariables.portal_ValidationFailureCount += 1
                expectedPortalValues = "Failed"
                GlobalVariables.EXCEL_Portal_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedPortalValues = ""

        success = setUp.validateValues(expectedAPIValues, expectedDBValues, expectedPortalValues, "")

        if success_Val_Execution == False:
            if success == False:
                pass
            else:
                pytest.fail()


@pytest.mark.apiVal
@pytest.mark.dbVals
@pytest.mark.portalVal
@pytest.mark.usefixtures("log_on_success", "method_setup")
def test_successSeven():
    GlobalVariables.apiLogs = False
    GlobalVariables.portalLogs = False
    GlobalVariables.cnpWareLogs = False
    GlobalVariables.middleWareLogs = False
    global success_Val_Execution
    success_Val_Execution = True

    try:
        print("EXECUTING FIRST TEST CASE : SUCCESS")
        time.sleep(1)
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

        if (configReader.read_config("Validations", "api_validation")) == "True":
            try:
                time.sleep(1)
                expectedAPIValues = "qwerty:qwerty,zxcv:zxcv"
            except:
                print("API Validation did not complete due to exception")
                print("")
                GlobalVariables.api_ValidationFailureCount += 1
                expectedAPIValues = "Failed"
                GlobalVariables.EXCEL_API_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedAPIValues = ""

        if (configReader.read_config("Validations", "db_validation")) == "True":
            try:
                time.sleep(1)
                expectedDBValues = "10.0:10.0,787878:787878"
            except:
                print("DB Validation did not complete due to exception in reading values from DB")
                print("")
                GlobalVariables.db_ValidationFailureCount += 1
                expectedDBValues = "Failed"
                GlobalVariables.EXCEL_DB_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedDBValues =""

        if (configReader.read_config("Validations", "portal_validation")) == "True":
            try:
                time.sleep(1)
                expectedPortalValues = "CASH:CASH,909090:909090"
            except:
                print("Portal Validation did not complete due to exception in reading values from portal")
                print("")
                GlobalVariables.portal_ValidationFailureCount += 1
                expectedPortalValues = "Failed"
                GlobalVariables.EXCEL_Portal_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedPortalValues = ""

        success = setUp.validateValues(expectedAPIValues, expectedDBValues, expectedPortalValues, "")

        if success_Val_Execution == False:
            if success == False:
                pass
            else:
                pytest.fail()

@pytest.mark.apiVal
@pytest.mark.usefixtures("log_on_success", "method_setup")
def test_onlyAPI_Val():
    GlobalVariables.apiLogs = False
    GlobalVariables.portalLogs = False
    GlobalVariables.cnpWareLogs = False
    GlobalVariables.middleWareLogs = False
    global success_Val_Execution
    success_Val_Execution = True

    try:
        print("EXECUTING SECOND TEST CASE : EXECUTION FAILURE")
        time.sleep(2)
        a = 1/0
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

        if (configReader.read_config("Validations", "api_validation")) == "True":
            try:
                time.sleep(1)
                expectedAPIValues = "qwerty:qwerty,zxcv:zxcv"
            except:
                print("API Validation did not complete due to exception")
                print("")
                GlobalVariables.api_ValidationFailureCount += 1
                expectedAPIValues = "Failed"
                GlobalVariables.EXCEL_API_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedAPIValues = ""

        success = setUp.validateValues(expectedAPIValues, "", "", "")

        if success_Val_Execution == False:
            if success == False:
                pass
            else:
                pytest.fail()




@pytest.mark.dbVal
@pytest.mark.apiVal
@pytest.mark.portalVal
@pytest.mark.usefixtures("log_on_success", "method_setup")
def test_Exe_Failure():
    GlobalVariables.apiLogs = False
    GlobalVariables.portalLogs = False
    GlobalVariables.cnpWareLogs = False
    GlobalVariables.middleWareLogs = False
    global success_Val_Execution
    success_Val_Execution = True

    try:
        print("EXECUTING SECOND TEST CASE : EXECUTION FAILURE")
        time.sleep(2)
        a = 1/0
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

        if (configReader.read_config("Validations", "api_validation")) == "True":
            try:
                time.sleep(1)
                expectedAPIValues = "qwerty:qwerty,zxcv:zxcv"
            except:
                print("API Validation did not complete due to exception")
                print("")
                GlobalVariables.api_ValidationFailureCount += 1
                expectedAPIValues = "Failed"
                GlobalVariables.EXCEL_API_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedAPIValues = ""

        if (configReader.read_config("Validations", "db_validation")) == "True":
            try:
                time.sleep(1)
                expectedDBValues = "10.0:10.0,787878:787878"
            except:
                print("DB Validation did not complete due to exception in reading values from DB")
                print("")
                GlobalVariables.db_ValidationFailureCount += 1
                expectedDBValues = "Failed"
                GlobalVariables.EXCEL_DB_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedDBValues = ""

        if (configReader.read_config("Validations", "portal_validation")) == "True":
            try:
                time.sleep(1)
                expectedPortalValues = "CASH:CASH,909090:909090"
            except:
                print("Portal Validation did not complete due to exception in reading values from portal")
                print("")
                GlobalVariables.portal_ValidationFailureCount += 1
                expectedPortalValues = "Failed"
                GlobalVariables.EXCEL_Portal_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedPortalValues =""

        success = setUp.validateValues(expectedAPIValues, expectedDBValues, expectedPortalValues, "")

        if success_Val_Execution == False:
            if success == False:
                pass
            else:
                pytest.fail()


@pytest.mark.dbVal
@pytest.mark.apiVal
@pytest.mark.portalVal
@pytest.mark.usefixtures("log_on_success", "method_setup")
def test_api_val_exe_failure():
    GlobalVariables.apiLogs = False
    GlobalVariables.portalLogs = False
    GlobalVariables.cnpWareLogs = False
    GlobalVariables.middleWareLogs = False
    global success_Val_Execution
    success_Val_Execution = True

    try:
        print("EXECUTING THIRD TEST CASE : API VAL EXE FAILURE")
        time.sleep(3)
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

        if (configReader.read_config("Validations", "api_validation")) == "True":
            try:
                time.sleep(1)
                a = 1/0
                expectedAPIValues = "qwerty:qwerty,zxcv:zxcv"
            except:
                print("API Validation did not complete due to exception")
                print("")
                GlobalVariables.api_ValidationFailureCount += 1
                expectedAPIValues = "Failed"
                GlobalVariables.EXCEL_API_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedAPIValues = ""

        if (configReader.read_config("Validations", "db_validation")) == "True":
            try:
                time.sleep(1)
                expectedDBValues = "10.0:10.0,787878:787878"
            except:
                print("DB Validation did not complete due to exception in reading values from DB")
                print("")
                GlobalVariables.db_ValidationFailureCount += 1
                expectedDBValues = "Failed"
                GlobalVariables.EXCEL_DB_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedDBValues =""

        if (configReader.read_config("Validations", "portal_validation")) == "True":
            try:
                time.sleep(1)
                expectedPortalValues = "CASH:CASH,909090:909090"
            except:
                print("Portal Validation did not complete due to exception in reading values from portal")
                print("")
                GlobalVariables.portal_ValidationFailureCount += 1
                expectedPortalValues = "Failed"
                GlobalVariables.EXCEL_Portal_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedPortalValues =""

        success = setUp.validateValues(expectedAPIValues, expectedDBValues, expectedPortalValues, "")

        if success_Val_Execution == False:
            if success == False:
                pass
            else:
                pytest.fail()

@pytest.mark.dbVal
@pytest.mark.apiVal
@pytest.mark.portalVal
@pytest.mark.usefixtures("log_on_success", "method_setup")
def test_DB_Val_Exe_Failure():
    GlobalVariables.apiLogs = False
    GlobalVariables.portalLogs = False
    GlobalVariables.cnpWareLogs = False
    GlobalVariables.middleWareLogs = False
    global success_Val_Execution
    success_Val_Execution = True

    try:
        print("EXECUTING FOURTH TEST CASE : DB VAL EXE FAILURE")
        time.sleep(2)
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

        if (configReader.read_config("Validations", "api_validation")) == "True":
            try:
                time.sleep(1)
                expectedAPIValues = "qwerty:qwerty,zxcv:zxcv"
            except:
                print("API Validation did not complete due to exception")
                print("")
                GlobalVariables.api_ValidationFailureCount += 1
                expectedAPIValues = "Failed"
                GlobalVariables.EXCEL_API_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedAPIValues = ""

        if (configReader.read_config("Validations", "db_validation")) == "True":
            try:
                time.sleep(1)
                a= 1/0
                expectedDBValues = "10.0:10.0,787878:787878"
            except:
                print("DB Validation did not complete due to exception in reading values from DB")
                print("")
                GlobalVariables.db_ValidationFailureCount += 1
                expectedDBValues = "Failed"
                GlobalVariables.EXCEL_DB_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedDBValues =""

        if (configReader.read_config("Validations", "portal_validation")) == "True":
            try:
                time.sleep(1)
                expectedPortalValues = "CASH:CASH,909090:909090"
            except:
                print("Portal Validation did not complete due to exception in reading values from portal")
                print("")
                GlobalVariables.portal_ValidationFailureCount += 1
                expectedPortalValues = "Failed"
                GlobalVariables.EXCEL_Portal_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedPortalValues =""

        success = setUp.validateValues(expectedAPIValues, expectedDBValues, expectedPortalValues, "")

        if success_Val_Execution == False:
            if success == False:
                pass
            else:
                pytest.fail()




@pytest.mark.dbVal
@pytest.mark.apiVal
@pytest.mark.portalVal
@pytest.mark.usefixtures("log_on_success", "method_setup")
def test_DB_Val_random_Failure():
    GlobalVariables.apiLogs = False
    GlobalVariables.portalLogs = False
    GlobalVariables.cnpWareLogs = False
    GlobalVariables.middleWareLogs = False
    global success_Val_Execution
    success_Val_Execution = True

    try:
        print("EXECUTING FOURTH TEST CASE : DB VAL EXE FAILURE")
        time.sleep(2)
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

        if (configReader.read_config("Validations", "api_validation")) == "True":
            try:
                time.sleep(1)
                expectedAPIValues = "qwerty:qwerty,zxcv:zxcv"
            except:
                print("API Validation did not complete due to exception")
                print("")
                GlobalVariables.api_ValidationFailureCount += 1
                expectedAPIValues = "Failed"
                GlobalVariables.EXCEL_API_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedAPIValues = ""

        if (configReader.read_config("Validations", "db_validation")) == "True":
            try:
                time.sleep(1)
                # To fail the testcase everytime
                a =1/0
                print(a)

                # To fail the testcase randomly
                # a = random.randint(1, 2)
                # expectedDBValues = str(a) + ":2"


                # To pass the testcase everytime
                # expectedDBValues = "a:a,b:b"
            except:
                print("DB Validation did not complete due to exception in reading values from DB")
                print("")
                GlobalVariables.db_ValidationFailureCount += 1
                expectedDBValues = "Failed"
                GlobalVariables.EXCEL_DB_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedDBValues =""

        success = setUp.validateValues(expectedAPIValues, expectedDBValues, "", "")

        if success_Val_Execution == False:
            if success == False:
                pass
            else:
                pytest.fail()


@pytest.mark.dbVal
@pytest.mark.apiVal
@pytest.mark.portalVal
@pytest.mark.usefixtures("log_on_success", "method_setup")
def test_portal_val_exe_failure():
    GlobalVariables.apiLogs = False
    GlobalVariables.portalLogs = False
    GlobalVariables.cnpWareLogs = False
    GlobalVariables.middleWareLogs = False
    global success_Val_Execution
    success_Val_Execution = True

    try:
        print("EXECUTING FIFTH TEST CASE : PORTAL VAL EXE FAILURE")
        time.sleep(2)
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

        if (configReader.read_config("Validations", "api_validation")) == "True":
            try:
                time.sleep(1)
                expectedAPIValues = "qwerty:qwerty,zxcv:zxcv"
            except:
                print("API Validation did not complete due to exception")
                print("")
                GlobalVariables.api_ValidationFailureCount += 1
                expectedAPIValues = "Failed"
                GlobalVariables.EXCEL_API_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedAPIValues = ""

        if (configReader.read_config("Validations", "db_validation")) == "True":
            try:
                time.sleep(1)
                expectedDBValues = "10.0:10.0,787878:787878"
            except:
                print("DB Validation did not complete due to exception in reading values from DB")
                print("")
                GlobalVariables.db_ValidationFailureCount += 1
                expectedDBValues = "Failed"
                GlobalVariables.EXCEL_DB_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedDBValues =""

        if (configReader.read_config("Validations", "portal_validation")) == "True":
            try:
                time.sleep(1)
                a =1/0
                expectedPortalValues = "CASH:CASH,909090:909090"
            except:
                print("Portal Validation did not complete due to exception in reading values from portal")
                print("")
                GlobalVariables.portal_ValidationFailureCount += 1
                expectedPortalValues = "Failed"
                GlobalVariables.EXCEL_Portal_Val = "Fail"
                success_Val_Execution = False
        else:
            expectedPortalValues = ""

        success = setUp.validateValues(expectedAPIValues, expectedDBValues, expectedPortalValues, "")

        if success_Val_Execution == False:
            if success == False:
                pass
            else:
                pytest.fail()

#
# @pytest.mark.usefixtures("log_on_success")
# def test_api_val_failure(method_setup, session_setup):
#     GlobalVariables.apiLogs = False
#     GlobalVariables.portalLogs = False
#     GlobalVariables.cnpWareLogs = False
#     GlobalVariables.middleWareLogs = False
#     global success_Val_Execution
#     success_Val_Execution = True
#
#     try:
#         print("EXECUTING SIXTH TEST CASE : API VALIDATION FAILURE")
#         time.sleep(2)
#         setUp.get_TC_Exe_Time() # Get execution time
#     except:
#         setUp.get_TC_Exe_Time()
#         print("Testcase did not complete due to exception in testcase execution")
#         print("")
#         GlobalVariables.EXCEL_TC_Execution = "Fail"
#         GlobalVariables.Incomplete_ExecutionCount += 1
#
#         pytest.fail()
#
#     else:
#         GlobalVariables.EXCEL_TC_Execution = "Pass"
#         current = datetime.now()
#         GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
#
#         if (configReader.read_config("Validations", "api_validation")) == "True":
#             try:
#                 time.sleep(1)
#                 expectedAPIValues = "qwerty:qwerty,zxcv:abcd"
#             except:
#                 print("API Validation did not complete due to exception")
#                 print("")
#                 GlobalVariables.api_ValidationFailureCount += 1
#                 expectedAPIValues = "Failed"
#                 GlobalVariables.EXCEL_API_Val = "Fail"
#                 success_Val_Execution = False
#         else:
#             expectedAPIValues = ""
#
#         try:
#             time.sleep(1)
#             expectedDBValues = "10.0:10.0,787878:787878"
#         except:
#             print("DB Validation did not complete due to exception in reading values from DB")
#             print("")
#             GlobalVariables.db_ValidationFailureCount += 1
#             expectedDBValues = "Failed"
#             GlobalVariables.EXCEL_DB_Val = "Fail"
#             success_Val_Execution = False
#
#         try:
#             time.sleep(1)
#             expectedPortalValues = "CASH:CASH,909090:909090"
#         except:
#             print("Portal Validation did not complete due to exception in reading values from portal")
#             print("")
#             GlobalVariables.portal_ValidationFailureCount += 1
#             expectedPortalValues = "Failed"
#             GlobalVariables.EXCEL_Portal_Val = "Fail"
#             success_Val_Execution = False
#
#         success = setUp.validateValues(expectedAPIValues, expectedDBValues, expectedPortalValues, "")
#
#         if success_Val_Execution == False:
#             if success == False:
#                 pass
#             else:
#                 pytest.fail()
#
#
#
# @pytest.mark.usefixtures("log_on_success")
# def test_DB_val_failure(method_setup, session_setup):
#     GlobalVariables.apiLogs = False
#     GlobalVariables.portalLogs = False
#     GlobalVariables.cnpWareLogs = False
#     GlobalVariables.middleWareLogs = False
#     global success_Val_Execution
#     success_Val_Execution = True
#
#     try:
#         print("EXECUTING SEVENTH TEST CASE : DB VAL FAILURE")
#         time.sleep(2)
#         setUp.get_TC_Exe_Time() # Get execution time
#     except:
#         setUp.get_TC_Exe_Time()
#         print("Testcase did not complete due to exception in testcase execution")
#         print("")
#         GlobalVariables.EXCEL_TC_Execution = "Fail"
#         GlobalVariables.Incomplete_ExecutionCount += 1
#
#         pytest.fail()
#
#     else:
#         GlobalVariables.EXCEL_TC_Execution = "Pass"
#         current = datetime.now()
#         GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
#
#         if (configReader.read_config("Validations", "api_validation")) == "True":
#             try:
#                 expectedAPIValues = "qwerty:qwerty,zxcv:zxcv"
#             except:
#                 print("API Validation did not complete due to exception")
#                 print("")
#                 GlobalVariables.api_ValidationFailureCount += 1
#                 expectedAPIValues = "Failed"
#                 GlobalVariables.EXCEL_API_Val = "Fail"
#                 success_Val_Execution = False
#         else:
#             expectedAPIValues = ""
#
#         try:
#             time.sleep(1)
#             expectedDBValues = "10.0:10.0,787878:12345"
#         except:
#             print("DB Validation did not complete due to exception in reading values from DB")
#             print("")
#             GlobalVariables.db_ValidationFailureCount += 1
#             expectedDBValues = "Failed"
#             GlobalVariables.EXCEL_DB_Val = "Fail"
#             success_Val_Execution = False
#
#         try:
#             time.sleep(1)
#             expectedPortalValues = "CASH:CASH,909090:909090"
#         except:
#             print("Portal Validation did not complete due to exception in reading values from portal")
#             print("")
#             GlobalVariables.portal_ValidationFailureCount += 1
#             expectedPortalValues = "Failed"
#             GlobalVariables.EXCEL_Portal_Val = "Fail"
#             success_Val_Execution = False
#
#         success = setUp.validateValues(expectedAPIValues, expectedDBValues, expectedPortalValues, "")
#
#         if success_Val_Execution == False:
#             if success == False:
#                 pass
#             else:
#                 pytest.fail()
#
#
#
#
# @pytest.mark.usefixtures("log_on_success")
# def test_portal_val_failure(method_setup, session_setup):
#     GlobalVariables.apiLogs = False
#     GlobalVariables.portalLogs = False
#     GlobalVariables.cnpWareLogs = False
#     GlobalVariables.middleWareLogs = False
#     global success_Val_Execution
#     success_Val_Execution = True
#
#     try:
#         print("EXECUTING EIGHT TEST CASE : PORTAL VAL FAILURE")
#         time.sleep(2)
#         setUp.get_TC_Exe_Time() # Get execution time
#     except:
#         setUp.get_TC_Exe_Time()
#         print("Testcase did not complete due to exception in testcase execution")
#         print("")
#         GlobalVariables.EXCEL_TC_Execution = "Fail"
#         GlobalVariables.Incomplete_ExecutionCount += 1
#
#         pytest.fail()
#
#     else:
#         GlobalVariables.EXCEL_TC_Execution = "Pass"
#         current = datetime.now()
#         GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
#
#         if (configReader.read_config("Validations", "api_validation")) == "True":
#             try:
#                 time.sleep(1)
#                 expectedAPIValues = "qwerty:qwerty,zxcv:zxcv"
#             except:
#                 print("API Validation did not complete due to exception")
#                 print("")
#                 GlobalVariables.api_ValidationFailureCount += 1
#                 expectedAPIValues = "Failed"
#                 GlobalVariables.EXCEL_API_Val = "Fail"
#                 success_Val_Execution = False
#         else:
#             expectedAPIValues = ""
#
#         try:
#             time.sleep(1)
#             expectedDBValues = "10.0:10.0,787878:787878"
#         except:
#             print("DB Validation did not complete due to exception in reading values from DB")
#             print("")
#             GlobalVariables.db_ValidationFailureCount += 1
#             expectedDBValues = "Failed"
#             GlobalVariables.EXCEL_DB_Val = "Fail"
#             success_Val_Execution = False
#
#         try:
#             time.sleep(1)
#             expectedPortalValues = "CASH:CASH,909090:abcdef"
#         except:
#             print("Portal Validation did not complete due to exception in reading values from portal")
#             print("")
#             GlobalVariables.portal_ValidationFailureCount += 1
#             expectedPortalValues = "Failed"
#             GlobalVariables.EXCEL_Portal_Val = "Fail"
#             success_Val_Execution = False
#
#         success = setUp.validateValues(expectedAPIValues, expectedDBValues, expectedPortalValues, "")
#
#         if success_Val_Execution == False:
#             if success == False:
#                 pass
#             else:
#                 pytest.fail()


#################################################### SANDEEPS's CODE WITHOUT GLOBAL VARIABLES START ##################################################
# @pytest.mark.dbVal
# @pytest.mark.apiVal
# @pytest.mark.portalVal
# def test_success():
#     # GlobalVariables.apiLogs = False
#     # GlobalVariables.portalLogs = False
#     # GlobalVariables.cnpWareLogs = False
#     # GlobalVariables.middleWareLogs = False
#     global success_Val_Execution
#     success_Val_Execution = True
#
#     try:
#         print("EXECUTING FIRST TEST CASE : SUCCESS")
#         time.sleep(1)
#         setUp.get_TC_Exe_Time() # Get execution time
#     except:
#         setUp.get_TC_Exe_Time()
#         print("Testcase did not complete due to exception in testcase execution")
#         print("")
#         # GlobalVariables.EXCEL_TC_Execution = "Fail"
#         # GlobalVariables.Incomplete_ExecutionCount += 1
#         pytest.fail()
#
#     else:
#         # GlobalVariables.EXCEL_TC_Execution = "Pass"
#         current = datetime.now()
#         # GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
#
#
#         try:
#             time.sleep(1)
#             expectedAPIValues = "qwerty:qwerty,zxcv:zxcv"
#         except:
#             print("API Validation did not complete due to exception")
#             print("")
#             # GlobalVariables.api_ValidationFailureCount += 1
#             expectedAPIValues = "Failed"
#             # GlobalVariables.EXCEL_API_Val = "Fail"
#             success_Val_Execution = False
#
#         try:
#             time.sleep(1)
#             expectedDBValues = "10.0:10.0,787878:787878"
#         except:
#             print("DB Validation did not complete due to exception in reading values from DB")
#             print("")
#             # GlobalVariables.db_ValidationFailureCount += 1
#             expectedDBValues = "Failed"
#             # GlobalVariables.EXCEL_DB_Val = "Fail"
#             success_Val_Execution = False
#
#         try:
#             time.sleep(1)
#             expectedPortalValues = "CASH:CASH,909090:909090"
#         except:
#             print("Portal Validation did not complete due to exception in reading values from portal")
#             print("")
#             # GlobalVariables.portal_ValidationFailureCount += 1
#             expectedPortalValues = "Failed"
#             # GlobalVariables.EXCEL_Portal_Val = "Fail"
#             success_Val_Execution = False
#
#         success = setUp.validateValues(expectedAPIValues, expectedDBValues, expectedPortalValues, "")
#
#         if success_Val_Execution == False:
#             if success == False:
#                 pass
#             else:
#                 pytest.fail()
#
# @pytest.mark.dbVal
# @pytest.mark.apiVal
# @pytest.mark.portalVal
# def test_Exe_Failure():
#     # GlobalVariables.apiLogs = False
#     # GlobalVariables.portalLogs = False
#     # GlobalVariables.cnpWareLogs = False
#     # GlobalVariables.middleWareLogs = False
#     global success_Val_Execution
#     success_Val_Execution = True
#
#     try:
#         print("EXECUTING SECOND TEST CASE : EXECUTION FAILURE")
#         time.sleep(1)
#         a = 1/0
#         setUp.get_TC_Exe_Time() # Get execution time
#     except:
#         setUp.get_TC_Exe_Time()
#         print("Testcase did not complete due to exception in testcase execution")
#         print("")
#         # GlobalVariables.EXCEL_TC_Execution = "Fail"
#         # GlobalVariables.Incomplete_ExecutionCount += 1
#
#         pytest.fail()
#
#     else:
#         # GlobalVariables.EXCEL_TC_Execution = "Pass"
#         current = datetime.now()
#         # GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
#
#         try:
#             time.sleep(1)
#             expectedAPIValues = "qwerty:qwerty,zxcv:zxcv"
#         except:
#             print("API Validation did not complete due to exception")
#             print("")
#             # GlobalVariables.api_ValidationFailureCount += 1
#             expectedAPIValues = "Failed"
#             # GlobalVariables.EXCEL_API_Val = "Fail"
#             success_Val_Execution = False
#
#         try:
#             time.sleep(1)
#             expectedDBValues = "10.0:10.0,787878:787878"
#         except:
#             print("DB Validation did not complete due to exception in reading values from DB")
#             print("")
#             # GlobalVariables.db_ValidationFailureCount += 1
#             expectedDBValues = "Failed"
#             # GlobalVariables.EXCEL_DB_Val = "Fail"
#             success_Val_Execution = False
#
#         try:
#             time.sleep(1)
#             expectedPortalValues = "CASH:CASH,909090:909090"
#         except:
#             print("Portal Validation did not complete due to exception in reading values from portal")
#             print("")
#             # GlobalVariables.portal_ValidationFailureCount += 1
#             expectedPortalValues = "Failed"
#             # GlobalVariables.EXCEL_Portal_Val = "Fail"
#             success_Val_Execution = False
#
#         success = setUp.validateValues(expectedAPIValues, expectedDBValues, expectedPortalValues, "")
#
#         if success_Val_Execution == False:
#             if success == False:
#                 pass
#             else:
#                 pytest.fail()
#
#
# @pytest.mark.dbVal
# @pytest.mark.apiVal
# @pytest.mark.portalVal
# def test_api_val_exe_failure():
#     # GlobalVariables.apiLogs = False
#     # GlobalVariables.portalLogs = False
#     # GlobalVariables.cnpWareLogs = False
#     # GlobalVariables.middleWareLogs = False
#     global success_Val_Execution
#     success_Val_Execution = True
#
#     try:
#         print("EXECUTING THIRD TEST CASE : API VAL EXE FAILURE")
#         time.sleep(1)
#         setUp.get_TC_Exe_Time() # Get execution time
#     except:
#         setUp.get_TC_Exe_Time()
#         print("Testcase did not complete due to exception in testcase execution")
#         print("")
#         # GlobalVariables.EXCEL_TC_Execution = "Fail"
#         # GlobalVariables.Incomplete_ExecutionCount += 1
#
#         pytest.fail()
#
#     else:
#         # GlobalVariables.EXCEL_TC_Execution = "Pass"
#         current = datetime.now()
#         # GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
#
#         try:
#             time.sleep(1)
#             a = 1/0
#             expectedAPIValues = "qwerty:qwerty,zxcv:zxcv"
#         except:
#             print("API Validation did not complete due to exception")
#             print("")
#             # GlobalVariables.api_ValidationFailureCount += 1
#             expectedAPIValues = "Failed"
#             # GlobalVariables.EXCEL_API_Val = "Fail"
#             success_Val_Execution = False
#
#         try:
#             time.sleep(1)
#             expectedDBValues = "10.0:10.0,787878:787878"
#         except:
#             print("DB Validation did not complete due to exception in reading values from DB")
#             print("")
#             # GlobalVariables.db_ValidationFailureCount += 1
#             expectedDBValues = "Failed"
#             # GlobalVariables.EXCEL_DB_Val = "Fail"
#             success_Val_Execution = False
#
#         try:
#             time.sleep(1)
#             expectedPortalValues = "CASH:CASH,909090:909090"
#         except:
#             print("Portal Validation did not complete due to exception in reading values from portal")
#             print("")
#             # GlobalVariables.portal_ValidationFailureCount += 1
#             expectedPortalValues = "Failed"
#             # GlobalVariables.EXCEL_Portal_Val = "Fail"
#             success_Val_Execution = False
#
#         success = setUp.validateValues(expectedAPIValues, expectedDBValues, expectedPortalValues, "")
#
#         if success_Val_Execution == False:
#             if success == False:
#                 pass
#             else:
#                 pytest.fail()

####################################### Sandeep Code without Global variables END ###################################################