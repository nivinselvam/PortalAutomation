import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

from Pages import BaseActions
from Utilities import configReader

class EditMerchantActivities:
    def status_inactive(self, driver):
        BaseActions.click(driver,"radio_inactive_status_ID")
        time.sleep(10)

    def status_active(self, driver):
        BaseActions.click(driver,"radio_active_status_ID")
        time.sleep(10)

    def save_changes(self, driver):
        BaseActions.click(driver,"btn_save_XPATH")
