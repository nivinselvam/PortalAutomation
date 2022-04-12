from DataProvider import GlobalVariables

# successExecution = False

# @pytest.mark.usefixtures("log_on_failure", "log_on_success")
# def test_New(method_setup, session_setup):
#     print("")
#     print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#     GlobalVariables.apiLogs = True
#     GlobalVariables.portalLogs = True
#     GlobalVariables.cnpWareLogs = False
#     GlobalVariables.middleWareLogs = False
#     global successExecution
#
#     try:
#         a = 1/1
#         setUp.get_TC_Exe_Time()
#     except:
#         setUp.get_TC_Exe_Time()
#         print("Exception Occurred Execution")
#         GlobalVariables.EXCEL_TC_Execution = "Fail"
#         GlobalVariables.Incomplete_ExecutionCount += 1
#         pytest.fail()
#
#     else:
#         if "True" == "True":
#             print("INSIDE IF CONDITION")
#             GlobalVariables.EXCEL_TC_Execution = "Pass"
#             current = datetime.now()
#             GlobalVariables.EXCEL_TC_Val_Starting_Time = current.strftime("%H:%M:%S")
#             try:
#                 b = 2/2
#                 expectedDBValues = "true:true"
#             except:
#                 print("Exception in reading values from DB")
#                 GlobalVariables.db_ValidationFailureCount += 1
#                 expectedDBValues = ""
#                 successExecution = False
#
#             try:
#                 print("")
#                 c =3/0
#             except:
#                 print("Exception in reading values from portal")
#                 GlobalVariables.portal_ValidationFailureCount += 1
#                 expectedPortalValues = ""
#                 successExecution = False
#             else:
#                 expectedPortalValues = "CASH:CASH"
#
#             expectedAPIValues = "AMOUNT:AMOUNT"
#
#             success = setUp.validateValues(expectedAPIValues, expectedDBValues, expectedPortalValues, "")
#             print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#             print(success)
#
#
#             if successExecution == False:
#                 if success == False:
#                     pass
#                 else:
#                     print("##########################")
#                     pytest.fail()
#         else:
#             print("IF API FAILS")


sessionPass = True

def test_New():
    GlobalVariables.apiLogs = False
    GlobalVariables.portalLogs = False
    GlobalVariables.cnpWareLogs = False
    GlobalVariables.middleWareLogs = False
    global sessionPass
    print("1111111111111111111111")
    print(str(sessionPass))
    sessionPass = False


def test_MEW():
    GlobalVariables.apiLogs = False
    GlobalVariables.portalLogs = False
    GlobalVariables.cnpWareLogs = False
    GlobalVariables.middleWareLogs = False
    global sessionPass
    print("222222222222222222222")
    print(str(sessionPass))
