"""
Author : Tony Varghese

Objective : 1) Ensure that sorting feature on the page works as expected
            2) Ensure that test solution is robust to handle new rows or columns of data

Test Cases : 1) Ensure that when you Sort By Name, Webtable is sorted by name alphabetically
             2) Ensure that when you Sort by Number Of Cases, Webtable is sorted from low to high and Test Solution handles k=1000, M=1000000 etc
             3) Ensure that when you Sort by Impact Score, Webtable is sorted from low to high
             2) Ensure that when you Sort by Complexity, Webtable is sorted as low, medium, high respectively

"""
import pytest
from selenium.webdriver.support.select import Select
from pyTestFramework_EclecticIQ_Tony.pageObjects.HomePage import HomePage
from pyTestFramework_EclecticIQ_Tony.testData.TestData import TestData
from pyTestFramework_EclecticIQ_Tony.utilities.BaseClass import BaseClass
from pytest_html_reporter import attach


class TestSortingFeatures(BaseClass):

    def test_sortByName(self, getDataName):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        """ Test Case 1: Sorting by Name """
        sortingOptions = Select(homepage.sorting_options())
        sortingOptions.select_by_visible_text(getDataName["SortingOptionsData"])
        extractedData = self.sorting_extracteddata(homepage, getDataName["HeadersData"])
        log.info("SortByName :: Extracted Data from WebPage --> {}".format(extractedData))
        sortedNames = sorted(extractedData, key=str.lower)
        attach(data=self.driver.get_screenshot_as_png())
        assert sortedNames == extractedData
        assert len(sortedNames) == len(extractedData)
        self.driver.refresh()

    def test_sortByCases(self,getDataCases):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        """ Test Case 2: Sorting by Number Of Cases """
        sortingOptions = Select(homepage.sorting_options())
        sortingOptions.select_by_visible_text(getDataCases["SortingOptionsData"])
        extractedData = self.sorting_extracteddata(homepage, getDataCases["HeadersData"])
        log.info("SortByCase :: Extracted Data from WebPage --> {}".format(extractedData))
        assortedCases = self.convert_currencyCategory(extractedData)
        sortedCases = sorted(assortedCases)
        print(sortedCases)
        attach(data=self.driver.get_screenshot_as_png())
        assert sortedCases == assortedCases
        assert len(sortedCases) == len(assortedCases)

    def test_sortByImpact(self,getDataImpact):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        """ Test Case 3: Sorting by Impact Score """
        sortingOptions = Select(homepage.sorting_options())
        sortingOptions.select_by_visible_text(getDataImpact["SortingOptionsData"])
        extractedData = self.sorting_extracteddata(homepage, getDataImpact["HeadersData"])
        log.info("SortByImpact :: Extracted Data from WebPage --> {}".format(extractedData))
        extractedData = [float(i) for i in extractedData]
        sortedImpactScore = sorted(extractedData)
        attach(data=self.driver.get_screenshot_as_png())
        assert sortedImpactScore == extractedData
        assert len(sortedImpactScore) == len(extractedData)

    def test_sortByComplexity(self,getDataComplexity):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        """ Test Case 4: Sorting by Complexity"""
        sortingOptions = Select(homepage.sorting_options())
        sortingOptions.select_by_visible_text(getDataComplexity["SortingOptionsData"])
        extractedData = self.sorting_extracteddata(homepage, getDataComplexity["HeadersData"])
        log.info("SortByComplexity :: Extracted Data from WebPage --> {}".format(extractedData))
        sortedlist = self.complexity_weight(extractedData)
        print(sortedlist)
        attach(data=self.driver.get_screenshot_as_png())
        assert extractedData == sortedlist
        assert len(extractedData) == len(sortedlist)




    @pytest.fixture(params=TestData.test_sortByName_data)
    def getDataName(self, request):
        return request.param

    @pytest.fixture(params=TestData.test_sortByCases_data)
    def getDataCases(self, request):
        return request.param

    @pytest.fixture(params=TestData.test_sortByImpact_data)
    def getDataImpact(self, request):
        return request.param

    @pytest.fixture(params=TestData.test_sortByComplexity_data)
    def getDataComplexity(self, request):
        return request.param
