from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    filter_input_locator = (By.ID, "filter-input")
    headers_locator = (By.XPATH, "//div[@class='table']/div/div/a")
    table_rows_locator = (By.XPATH, "//div[@class='table']/div[@class='table-content']/div")
    sorting_options_locator = (By.XPATH, "//select")

    def filter_input(self):
        return self.driver.find_element(*HomePage.filter_input_locator)

    def headers(self):
        return self.driver.find_elements(*HomePage.headers_locator)

    def table_rows(self):
        return self.driver.find_elements(*HomePage.table_rows_locator)

    def sorting_options(self):
        return self.driver.find_element(*HomePage.sorting_options_locator)
