import time

from Pages import BaseActions


class BulkUploadsActivities:

    def number_of_txns_per_day(self, driver, value):
        BaseActions.enter_data(driver, "number_of_txns_per_day_XPATH", value)


