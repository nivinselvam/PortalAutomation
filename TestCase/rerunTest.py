from DataProvider import GlobalVariables
from Utilities import configReader


def immediateRerunLogic(testCaseID):
    ls_failedValidations = ['API Val']
    rerun = False

    print("")
    print("PRINTING DF FROM immediateRerunLogic")
    print(GlobalVariables.df_testCasesDetail)

    if GlobalVariables.df_testCasesDetail == "":
        for column in GlobalVariables.df_testCasesDetail.columns:
            if str(GlobalVariables.df_testCasesDetail[column][testCaseID]).lower() == "fail" or str(GlobalVariables.df_testCasesDetail[column][testCaseID]).lower() == "failed":
                ls_failedValidations.append(column)

        if not ls_failedValidations:
            return False
        else:
            if ls_failedValidations.__contains__("TC Execution") and str(
                    configReader.read_config("Validations", "exe_rerun")).lower() == 'true':
                rerun = True
            elif ls_failedValidations.__contains__("API Val") and str(
                    configReader.read_config("Validations", "api_rerun")).lower() == 'true':
                rerun = True
            elif ls_failedValidations.__contains__("DB Val") and str(
                    configReader.read_config("Validations", "db_rerun")).lower() == 'true':
                rerun = True
            elif ls_failedValidations.__contains__("Portal Val") and str(
                    configReader.read_config("Validations", "portal_rerun")).lower() == 'true':
                rerun = True
            elif ls_failedValidations.__contains__("App Val") and str(
                    configReader.read_config("Validations", "app_rerun")).lower() == 'true':
                rerun = True
            elif ls_failedValidations.__contains__("UI Val") and str(
                    configReader.read_config("Validations", "ui_rerun")).lower() == 'true':
                rerun = True
    return rerun