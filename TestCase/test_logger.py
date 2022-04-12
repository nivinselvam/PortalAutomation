import pytest

from TestCase import GlobalVariables
from TestCase import setUp

# N/A  / Failed / Pass / Fail

def test_Exe_Failure():
    try:
        GlobalVariables.apiLogs = True
        GlobalVariables.portalLogs = True
        GlobalVariables.cnpWareLogs = True
        GlobalVariables.middleWareLogs = False
        print("Trying exe")
        pytest.fail()
    finally:
        print("Final block")
    setUp.createStatusTable('N/A','Fail','Pass','N/A')


def test_Exe_Failure1():
    GlobalVariables.apiLogs = True
    GlobalVariables.portalLogs = True
    GlobalVariables.cnpWareLogs = True
    GlobalVariables.middleWareLogs = False

    setUp.createStatusTable('N/A','Fail','Pass','N/A')


def test_Exe_Failure2():
    GlobalVariables.apiLogs = True
    GlobalVariables.portalLogs = True
    GlobalVariables.cnpWareLogs = True
    GlobalVariables.middleWareLogs = False

    setUp.createStatusTable('N/A','Fail','Pass','N/A')


def test_Exe_Failure3():
    GlobalVariables.apiLogs = True
    GlobalVariables.portalLogs = True
    GlobalVariables.cnpWareLogs = False
    GlobalVariables.middleWareLogs = False

    setUp.createStatusTable('N/A','Fail','Pass','N/A')