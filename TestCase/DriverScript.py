from ConfigurationData import Configuration
from TestCase import Rerun
from Utilities import configReader


Configuration.prepare_Consolidated_List_Of_TestcasesFile()

if configReader.read_config("Validations", "rerun_immediately").lower() == "true" and configReader.read_config("Validations", "rerun_at_the_end").lower() == "false":
    Rerun.prepareImmediateRerunExcel()

Configuration.executeSelectedTestCases()

# Rerun
rerunCount = int(configReader.read_config("Validations", "rerun_count"))

if configReader.read_config("Validations", "rerun_at_the_end").lower() == "true":
    Rerun.prepareAtTheEndRerunExcel()
    while rerunCount > 0:
        rerunCount = rerunCount - 1
        Rerun.setRerunCountForAtTheEnd(rerunCount)
        Rerun.rerunTestAtTheEnd()
    Rerun.prepareAtTheEndRerunExcel()