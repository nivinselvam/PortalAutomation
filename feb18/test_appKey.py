import time

from selenium import webdriver
from self import self

from Pages.LoginPageActivities import LoginPageActivities
from Pages.HomePageActivities import HomePageActivities
from Pages.AppkeyActivities import AppkeyActivities
from TestCase import setUp

driver = webdriver.Chrome('/home/ezetap/Downloads/chromedriver_linux64/chromedriver')
username = "8078151226"
password = "D1234567"
orgCode="AUTO_PYTHON_TRIAL"
appkey = "appKey"


def setup_module(module):
    LoginPageActivities.login(self, driver, username, password)
    time.sleep(5)

    HomePageActivities.search_for_merchant(self, driver, orgCode)
    HomePageActivities.switch_merchant(self, driver, orgCode)
    HomePageActivities.click_on_appkeys_menu(self, driver)

def teardown_module(module):
    print("inside teardown")
    driver.close()

def test_appkey():
    AppkeyActivities.generate_appkey(self,driver,"Trial description")
    data = setUp.getValueFromDB("SELECT description from ezetap_demo.app_key where org_code='" + orgCode + "';")
    dbDescription = str(data['description'].values[0])
    print("Description from DB table txn : ", dbDescription)

    expectedDBValues =  "Trial description"+ ":" + dbDescription

    setUp.validateValues("", expectedDBValues, "", "")

def test_editAppkey():
    appkey =  AppkeyActivities.getAppkey(self, driver, "Trial description")
    AppkeyActivities.editAppkey(self, driver, appkey,"Updated Label")
    data = setUp.getValueFromDB("SELECT label from ezetap_demo.app_key where app_key='" + appkey + "';")
    dbLabel = str(data['label'].values[0])

    print("Label from DB table txn : ", dbLabel)
    expectedDBValues = "Updated Label" + ":" + dbLabel
    setUp.validateValues("", expectedDBValues, "", "")

def test_fdeleteAppkey():
    appkey = AppkeyActivities.getAppkey(self, driver, "Trial description")
    AppkeyActivities.deleteAppkey(self, driver, appkey)
    setUp.validateValues("", "Delete:Delete", "", "")



