import pandas as pd
import os

from DataProvider import GlobalVariables
from Utilities import configReader


def prepareTestCaseDetailsDataFrame(path):

    # Defining the columns of dataframe
    dataForDataFrameHeader = {
        'Test Case ID' : [],
        'File Name': [],
        'Directory Name': [],
        'Category': [],
        'Sub-Category': [],
        'OverAll Results':[],
        'TC Execution': [],
        'API Val': [],
        'DB Val': [],
        'Portal Val': [],
        'App Val': [],
        'UI Val': [],
        'Execution Time (sec)': [],
        'Validation Time (sec)': [],
        'Log Coll Time (sec)': [],
        'Total Time (sec)': [],
        'Rerun Attempts': []
    }
    GlobalVariables.df_testCasesDetail = pd.DataFrame(dataForDataFrameHeader)

    # Dataframe by default gets created with datatype as float. Converting the same to string
    convert_dict = {'File Name': str,
                    'Directory Name': str,
                    'Category': str,
                    'Sub-Category': str,
                    'TC Execution': str,
                    'API Val': str,
                    'DB Val': str,
                    'Portal Val': str,
                    'App Val': str,
                    'UI Val': str,
                    'Rerun Attempts':str
                    }
    GlobalVariables.df_testCasesDetail = GlobalVariables.df_testCasesDetail.astype(convert_dict)

    df_overallTClist = pd.read_excel(path)
    df_overallTClist.set_index(configReader.read_config("TestcaseDetails_ColumnNames", "colName_TestCaseID"), inplace=True)

    i=0
    for index in df_overallTClist.index:
        if df_overallTClist['Execute'][index] == False or str(df_overallTClist['Execute'][index]).lower() == "false":
            pass
        else:
            GlobalVariables.df_testCasesDetail.at[i, configReader.read_config("TestcaseDetails_ColumnNames", "colName_TestCaseID")] = index
            GlobalVariables.df_testCasesDetail.at[i, 'File Name'] = df_overallTClist['File Name'][index]
            GlobalVariables.df_testCasesDetail.at[i, 'Directory Name'] = df_overallTClist['Directory Name'][index]
        i = i+1
    GlobalVariables.df_testCasesDetail.set_index(configReader.read_config("TestcaseDetails_ColumnNames", "colName_TestCaseID"), inplace=True)
    return GlobalVariables.df_testCasesDetail


def prepareTestExecutionCommand(testCasesDetailDataFrame):
    commandString = "pytest -v "
    for ind in testCasesDetailDataFrame.index:

        # With Directory
        # commandString = commandString + testCasesDetailDataFrame['Directory Name'][ind]+ "/" + testCasesDetailDataFrame['File Name'][ind] + ".py" + "::" + ind + " "

        # Without Directory
        commandString = commandString + testCasesDetailDataFrame['File Name'][ind] + ".py" + "::" + ind + " "
    commandString = commandString + getValidationConfig() + ' -n2 --alluredir="/home/ezetap/PycharmProjects/PortalAutomation/TestCase/allure" --capture=tee-sys'

    print(commandString)
    return commandString


def getValidationConfig():
    if configReader.read_config("Validations", "api_validation") == True and configReader.read_config("Validations", "db_validation") == True and configReader.read_config("Validations", "portal_validation") == True and configReader.read_config("Validations", "app_validation") == True and configReader.read_config("Validations", "ui_validation") == True :
        commandString = ""
    elif configReader.read_config("Validations", "api_validation") == False and configReader.read_config("Validations", "db_validation") == False and configReader.read_config("Validations", "portal_validation") == False and configReader.read_config("Validations", "app_validation") == False and configReader.read_config("Validations", "ui_validation") == False :
        commandString = ""
    else:
        commandString = '-m "'
        if (configReader.read_config("Validations", "api_validation")).lower() == "true":
            if commandString == '-m "':
                commandString = commandString + "apiVal"
            else:
                commandString = commandString + " or apiVal"

        if (configReader.read_config("Validations", "db_validation")).lower() == "true":
            if commandString == '-m "':
                commandString = commandString + "dbVal"
            else:
                commandString = commandString + " or dbVal"
        if (configReader.read_config("Validations", "portal_validation")).lower() == "true":
            if commandString == '-m "':
                commandString = commandString + "portalVal"
            else:
                commandString = commandString + " or portalVal"
        if (configReader.read_config("Validations", "app_validation")).lower() == "true":
            if commandString == '-m "':
                commandString = commandString + "appVal"
            else:
                commandString = commandString + " or appVal"
        if (configReader.read_config("Validations", "ui_validation")).lower() == "true":
            if commandString == '-m "':
                commandString = commandString + "uiVal"
            else:
                commandString = commandString + " or uiVal"
        commandString= commandString+'"'

    return commandString

def prepare_Consolidated_List_Of_TestcasesFile():
    df_all_rows = pd.DataFrame()

    if os.path.exists(configReader.read_config("ExcelFiles", "FilePath_TestCasesDetail")):
        workbook = pd.read_excel(configReader.read_config("ExcelFiles", "FilePath_TestCasesDetail"), None)
        ls_sheets_functional = workbook.keys()


        # Creating a DF with all testcases
        for sheet in ls_sheets_functional:
            df_testCasesDetail = pd.DataFrame(workbook.get(sheet))
            df_all_rows = pd.concat([df_all_rows, df_testCasesDetail])

    if os.path.exists(configReader.read_config("ExcelFiles", "FilePath_testcases_surfaceUI")):
        workbook = pd.read_excel(configReader.read_config("ExcelFiles", "FilePath_testcases_surfaceUI"), None)
        ls_sheets_surfaceUI = workbook.keys()

        # Creating a DF with all testcases
        for sheet in ls_sheets_surfaceUI:
            df_testCasesDetail = pd.DataFrame(workbook.get(sheet))
            df_all_rows = pd.concat([df_all_rows, df_testCasesDetail])


    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(df_all_rows)
    # Converting DF with all TCs to an excel
    df_all_rows.to_excel("/home/ezetap/PycharmProjects/PortalAutomation/TestCase/AllTestcaseSuite.xlsx")


# Preparing Report excel
# Initiating pytest execution
def executeSelectedTestCases():
    # Creating DF only with the testcases to be executed
    df_testcases = prepareTestCaseDetailsDataFrame("/home/ezetap/PycharmProjects/PortalAutomation/TestCase/AllTestcaseSuite.xlsx")
    df_testcases.to_excel(GlobalVariables.EXCEL_reportFilePath)
    os.system(prepareTestExecutionCommand(df_testcases))



    # Previous implementation
    # df_testcases = prepareTestCaseDetailsDataFrame(configReader.read_config("ExcelFiles", "FilePath_TestCasesDetail"))
    # df_testcases.to_excel(GlobalVariables.EXCEL_reportFilePath)
    # os.system(prepareTestExecutionCommand(df_testcases))



