"""
Author : Tony Varghese

Objective : 1) Ensure that filter feature on the page works as expected
            2) Ensure that test solution is robust to handle new rows or columns of data

Test Cases : 1) Ensure that when you input "high" in filter input, Webtable is populated with only words containing "high"
             2) Ensure that when you input "Man in the Middle" in filter input, Webtable is populated with only words containing "Man in the Middle"
             3) Ensure that when you input substring "hi" in filter input, Webtable is populated with only words containing "hi"
             2) Ensure that when you input substring "phis" in filter input, Webtable is populated with only words containing "phis"

"""

import pytest
from pytest_html_reporter import attach
from pyTestFramework_EclecticIQ_Tony.pageObjects.HomePage import HomePage
from pyTestFramework_EclecticIQ_Tony.testData.TestData import TestData
from pyTestFramework_EclecticIQ_Tony.utilities.BaseClass import BaseClass


class TestFilterFeature(BaseClass):

    def test_filtercases(self, getData):
        filter_string = getData["FilterString"]
        log = self.getLogger()
        homepage = HomePage(self.driver)
        homepage.filter_input().send_keys(filter_string)
        extractedDataSort = self.filter_extracteddata(homepage)
        log.info("Filter Test Case :: Extracted Data from WebPage --> {}".format(extractedDataSort))
        attach(data=self.driver.get_screenshot_as_png())
        assert any(filter_string.lower() in string for string in extractedDataSort)
        self.driver.refresh()

    @pytest.fixture(params=TestData.test_filtercases_data)
    def getData(self, request):
        return request.param
