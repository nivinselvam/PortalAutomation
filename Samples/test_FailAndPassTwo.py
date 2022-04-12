import pytest
import time
import datetime
from datetime import datetime

from TestCase import setUp
from DataProvider import GlobalVariables


@pytest.mark.usefixtures("log_on_failure","log_on_success")
def test_fail3(function_setup, session_setup):
    print("================= Execution Started =================")
    # time.sleep(15)
    print("================= Execution Failed =================")
    setUp.get_TC_Exe_Time()
    GlobalVariables.TC_Execution = "Failed"

    # Get validation time
    current = datetime.now()
    GlobalVariables.TC_Val_Starting_Time = current.strftime("%H:%M:%S")
    time.sleep(10)

    apiValues = "aa:bb"
    dbValues = "db:db"
    portalValues = "kk:kl"
    appValues = "gg:gg"
    setUp.validateValues(apiValues,dbValues,portalValues,appValues)

@pytest.mark.usefixtures("log_on_failure","log_on_success")
def test_Skippp(function_setup, session_setup):
    pytest.skip("22222222222222222222222222")


@pytest.mark.usefixtures("log_on_failure","log_on_success")
def test_fail4(function_setup, session_setup):
    print("================= Execution Started =================")
    # time.sleep(13)
    print("================= Execution Completed =================")
    setUp.get_TC_Exe_Time()
    GlobalVariables.EXCEL_TC_Execution = "Passed"


    current = datetime.now()
    GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
    # time.sleep(13)
    apiValues = "aa:aa"
    dbValues = "db:fg"
    portalValues = "kk:kl"
    appValues = "gg:gg"
    setUp.validateValues(apiValues,dbValues,portalValues,appValues)
