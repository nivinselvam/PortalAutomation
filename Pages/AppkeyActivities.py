import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

from Pages import BaseActions
from Utilities import configReader

class AppkeyActivities:
    def generate_appkey(self, driver,description):
        BaseActions.click(driver, "btn_generate_appkey_XPATH")
        time.sleep(3)
        select = Select(driver.find_element(By.NAME, configReader.read_config("locators", "dropdown_processCode_NAME")))
        select.select_by_visible_text('_DEF_PROC')
        time.sleep(5)
        BaseActions.enter_data(driver, "txt_appkey_description_ID", description)
        BaseActions.enter_data(driver, "txt_appkey_label_id", "Label")
        time.sleep(5)
        BaseActions.click(driver, "btn_add_appkey_XPATH")
        time.sleep(30)
        alert_obj = driver.switch_to.alert
        alert_obj.accept()
        driver.refresh()

    def getAppkey(self, driver, appKeyDescription):
        time.sleep(30)
        path = "//td/span[@data-bind = 'text: description' and text()='"+ appKeyDescription + "']/../preceding-sibling::td/span[@data-bind='text: appKey']"
        appKey = driver.find_element(By.XPATH,path).text
        return appKey

    def editAppkey(self, driver, appkey,newLabel):
        driver.find_element(By.XPATH,"//span[text()='" + appkey + "']/../following-sibling::td/button[text()='Edit']").click()
        BaseActions.enter_data(driver, "txt_editLabel_ID", newLabel)
        BaseActions.click(driver,"btn_saveChanges_XPATH")
        time.sleep(20)
        alert_obj = driver.switch_to.alert
        alert_obj.accept()
        driver.refresh()
    def deleteAppkey(self, driver, appKey):
        driver.find_element(By.XPATH,"//span[text()='" + appKey + "']/../following-sibling::td/button[text()='Delete']").click()
        time.sleep(20)
        alert_obj = driver.switch_to.alert
        alert_obj.accept()
        driver.refresh()

