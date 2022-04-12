from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Utilities import configReader


def enter_data(driver, locator, value):
    if str(locator).endswith("_NAME"):
        element= driver.find_element(By.NAME, configReader.read_config("locators", locator))
        element.clear()
        element.send_keys(value)
    elif str(locator).endswith("_XPATH"):
        element = driver.find_element(By.XPATH, configReader.read_config("locators", locator))
        element.clear()
        element.send_keys(value)
    elif str(locator).endswith("_ID"):
        element = driver.find_element(By.ID, configReader.read_config("locators", locator))
        element.clear()
        element.send_keys(value)


def click(driver, locator):
    if str(locator).endswith("_NAME"):
        driver.find_element(By.NAME, configReader.read_config("locators", locator)).click()

    elif str(locator).endswith("_XPATH"):
        driver.find_element(By.XPATH, configReader.read_config("locators", locator)).click()

    elif str(locator).endswith("_CLASS"):
        driver.find_element(By.CLASS_NAME, configReader.read_config("locators", locator)).click()

    elif str(locator).endswith("_ID"):
        driver.find_element(By.ID, configReader.read_config("locators", locator)).click()


def click_specific(driver, locator, value):
    if str(locator).endswith("_NAME"):
        element = driver.find_element(By.NAME, configReader.read_conf_with_spec_val("locators", locator, value))
        element.click()

    elif str(locator).endswith("_XPATH"):
        element = driver.find_element(By.XPATH, configReader.read_conf_with_spec_val("locators", locator, value))
        element.click()


def press_enter_key(driver, locator):
    if str(locator).endswith("_NAME"):
        driver.find_element(By.NAME, configReader.read_config("locators", locator)).send_keys(Keys.ENTER)
    elif str(locator).endswith("_XPATH"):
        driver.find_element(By.XPATH, configReader.read_config("locators", locator)).send_keys(Keys.ENTER)

def enter_data_logs(locator):
    if str(locator).endswith("_Logs"):
        value = configReader.read_config("logs", locator)
        return str(value)
    if str(locator).endswith("_ss"):
        value = configReader.read_config("logs", locator)
        return str(value)


def environment(locator):
    value = configReader.read_config("environment", locator)
    return str(value)


def pathToLogFile(locator):
    if str(locator).__contains__("dev"):
        value = configReader.read_config("path", locator)
        return str(value)
    if str(locator).__contains__("demo1"):
        value = configReader.read_config("path", locator)
        return str(value)