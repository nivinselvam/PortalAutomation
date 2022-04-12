import datetime
from datetime import datetime
from random import randint

import pytest

from DataProvider import GlobalVariables
from TestCase import setUp, rerun

success_Val_Execution = True
#
#


@pytest.mark.apiVal
@pytest.mark.dbVal
@pytest.mark.portalVal
@pytest.mark.uiVal
@pytest.mark.appVal
@pytest.mark.flaky(reruns=2, condition=rerun.immediateRerunLogic("test_sample3"))
def test_sample1(method_setup, ui_driver, session_setup):
    global success_Val_Execution
    success_Val_Execution = True
    GlobalVariables.EXCEL_TC_Execution = "Pass"
    validatePortal(GlobalVariables.portalDriver)
    expectedAPIValues = "5:5"
    expectedDBValues = "4:5"
    setUp.get_TC_Exe_Time()
    current = datetime.now()
    GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
    setUp.validateValues(expectedAPIValues, expectedDBValues, "", "")
#
#
# @pytest.mark.flaky(reruns=2, condition=rerun.immediateRerunLogic("test_sample3"))
# def test_sample(method_setup, ui_driver, session_setup):
#     global success_Val_Execution
#     success_Val_Execution = True
#     GlobalVariables.EXCEL_TC_Execution = "Pass"
#     validatePortal(GlobalVariables.portalDriver)
#     i = randint(1, 2)
#     expectedPortalValues = str(i)+":2"
#     expectedDBValues = "4:5"
#     setUp.get_TC_Exe_Time()
#     current = datetime.now()
#     GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
#     setUp.validateValues("", expectedDBValues, expectedPortalValues, "")
#
#
# @pytest.mark.flaky(reruns=2, condition=rerun.immediateRerunLogic("test_sample3"))
# def test_sample2(ui_driver, method_setup, session_setup):
#     global success_Val_Execution
#     success_Val_Execution = True
#     GlobalVariables.EXCEL_TC_Execution = "Pass"
#     validatePortal(GlobalVariables.portalDriver)
#     expectedPortalValues = "5:5"
#     expectedDBValues = "4:5"
#     setUp.get_TC_Exe_Time()
#     current = datetime.now()
#     GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
#     setUp.validateValues("", expectedDBValues, expectedPortalValues, "")
#
#
# # @pytest.mark.flaky(reruns=2, condition=(configReader.read_config("Validations", "api_rerun") == "True" or configReader.read_config("Validations", "db_rerun") == "True"))
# @pytest.mark.flaky(reruns=2, condition=rerun.immediateRerunLogic("test_sample3"))
# def test_sample3(method_setup, ui_driver, session_setup):
#     global success_Val_Execution
#     success_Val_Execution = True
#     GlobalVariables.EXCEL_TC_Execution = "Pass"
#     validatePortal(GlobalVariables.portalDriver)
#     expectedAPIValues = "5:5"
#     expectedDBValues = "4:5"
#     setUp.get_TC_Exe_Time()
#     current = datetime.now()
#     GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
#     setUp.validateValues(expectedAPIValues, expectedDBValues, "", "")
#
#
def validatePortal(driver):
    driver.get('https://dev3.ezetap.com/portal/login/')
    driver.quit()
