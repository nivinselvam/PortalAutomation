# These values are for updating number of each type of validations (API, Portal, DB and App) in html report
import openpyxl

#These variables are for adding to the second table (Validation) in HTML report
Incomplete_ExecutionCount = 0
api_ValidationFailureCount = 0
db_ValidationFailureCount = 0
portal_ValidationFailureCount = 0
app_ValidationFailureCount = 0
ui_ValidationFailureCount = 0


# These values are for log collection and SS
startLineNumberPortal = ''
startLineNumberAPI = ''
startLineNumberMiddlewware = ''
startLineNumberCnpware = ''
apiLogs = False
portalLogs = False
cnpWareLogs = False
middleWareLogs = False


#These values are for creating final excel report
EXCEL_fileName = "/home/ezetap/PycharmProjects/PortalAutomation/TestCase/Reports.xlsx"
EXCEL_workbook = None
EXCEL_rowNumber = 2

EXCEL_TC_Exe_Starting_Time = 00
EXCEL_TC_Exe_completed_time = 00

EXCEL_TC_Val_Starting_Time = 00
EXCEL_TC_Val_completed_time = 00

EXCEL_TC_LogColl_Starting_Time = 00
EXCEL_TC_LogColl_completed_time = 00

EXCEL_testCaseName = "Default Testcase"
EXCEL_testCaseFileName = ''
EXCEL_TC_Execution = "Skip"
EXCEL_API_Val = "N/A"
EXCEL_DB_Val = "N/A"
EXCEL_Portal_Val = "N/A"
EXCEL_App_Val = "N/A"
EXCEL_UI_Val = "N/A"
EXCEL_Execution_Time = 00
EXCEL_Val_time = 00
EXCEL_LogCollTime = 00
EXCEL_Tot_Time = 00


# For screenshots of App and Portal
appSS = False
portalSS = False
successApp = "N/A"
successPortal = "N/A"
appDriver = ''
portalDriver = ''

passed1 = 0
count = 1

df_testCasesDetail = ""
EXCEL_reportFilePath = "/home/ezetap/PycharmProjects/PortalAutomation/TestCase/Report.xlsx"


# rerunCount = 3
# int_immediateRerunCount = 3


portal_username = ''
portal_password = ''

app_username = ''
app_password = ''


# TC Count
testSuite_totalcases = 0

# Dataframe for results
df_testCasesDetail = ""




