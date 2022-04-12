
from Pages import BaseActions


class UsersActivities:

    def click_edit_user(self, driver, mobileNumber):
        BaseActions.click_specific(driver, "editUser_XPATH", mobileNumber)