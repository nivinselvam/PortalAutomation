# from Pages import BaseActions
import pytest

from TestCase import setUp
from DataProvider import GlobalVariables


#
@pytest.mark.usefixtures("log_on_failure","log_on_success")
def test_fail2(method_setup,session_setup):
    print("================= Execution Started =================")
    # time.sleep(20)
    GlobalVariables.EXCEL_TC_Execution = "Failed"
    print("================= Execution failed =================")
    setUp.get_TC_Exe_Time()

    #
    # apiValues = "aa:bb"
    # dbValues = "db:db"
    # portalValues = "kk:kl"
    # appValues = "gg:gg"
    # setUp.validateValues(apiValues,dbValues,portalValues,appValues)


@pytest.mark.usefixtures("log_on_failure","log_on_success")
def test_skip(function_setup, session_setup):
    pytest.skip("aaaaaaaaaaaaaaa")



















#
#
# @pytest.fixture()
# def log_on_failure(request):
#     yield
#     item = request.node
#     if item.rep_call.failed:
#         if GlobalVariables.apiLogs:
#             print("Fetching logs for the Failed test cases")
#             apiLogs = server_logs.fetchAPILogs()
#             print('@@@@@@@@@@@-----API LOGS----@@@@@@@@@@@@')
#             print(apiLogs)
#
#         if GlobalVariables.portalLogs:
#             portalLogs = server_logs.fetchPortalLogs()
#             print('@@@@@@@@@@@-----PORTAL LOGS----@@@@@@@@@@@@')
#             print(portalLogs)
#
#         if GlobalVariables.middleWareLogs:
#             mwareLogs = server_logs.fetchMiddlewareLogs()
#             print('@@@@@@@@@@@-----MIDDLEWARE LOGS----@@@@@@@@@@@@')
#             print(mwareLogs)
#
#         if GlobalVariables.cnpWareLogs:
#             cnpWareLogs = server_logs.fetchCnpwareLogs()
#             print('@@@@@@@@@@@-----CNPWARE LOGS----@@@@@@@@@@@@')
#             print(cnpWareLogs)
#         #
#         # portalLog.logger.info(portalLogs)
#         # allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
#
#
# @pytest.fixture()
# def log_on_success(request):
#     yield
#     item = request.node
#     if item.rep_call.passed and BaseActions.enter_data_logs("fetch_Logs") == "True":
#         if GlobalVariables.apiLogs:
#             print("Fetching logs for the Failed test cases")
#             apiLogs = server_logs.fetchAPILogs()
#             print('@@@@@@@@@@@-----API LOGS----@@@@@@@@@@@@')
#             print(apiLogs)
#
#         if GlobalVariables.portalLogs:
#             portalLogs = server_logs.fetchPortalLogs()
#             print('@@@@@@@@@@@-----PORTAL LOGS----@@@@@@@@@@@@')
#             print(portalLogs)
#
#         if GlobalVariables.middleWareLogs:
#             mwareLogs = server_logs.fetchMiddlewareLogs()
#             print('@@@@@@@@@@@-----MIDDLEWARE LOGS----@@@@@@@@@@@@')
#             print(mwareLogs)
#
#         if GlobalVariables.cnpWareLogs:
#             cnpWareLogs = server_logs.fetchCnpwareLogs()
#             print('@@@@@@@@@@@-----CNPWARE LOGS----@@@@@@@@@@@@')
#             print(cnpWareLogs)
#         # allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
#
# #

