import inspect
import logging
import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:

    def filter_extracteddata(self, homepage):
        headers = homepage.headers()
        tableRows = homepage.table_rows()
        extractedData = []
        for i in range(len(headers)):
            if headers[i].text == "NAME":
                for j in range(len(tableRows)):
                    columns = tableRows[j].find_elements_by_xpath("div")
                    unverifiedNames = columns[i]
                    extractedData.append(unverifiedNames.text)
            if headers[i].text == "COMPLEXITY":
                for j in range(len(tableRows)):
                    columns = tableRows[j].find_elements_by_xpath("div")
                    unverifiedNames = columns[i]
                    extractedData.append(unverifiedNames.text)
        extractedDataSort = [x.lower() for x in extractedData]
        return extractedDataSort

    def sorting_extracteddata(self, homepage, getData):
        headers = homepage.headers()
        tableRows = homepage.table_rows()
        extractedData = []
        for i in range(len(headers)):
            if headers[i].text == getData:
                for j in range(len(tableRows)):
                    columns = tableRows[j].find_elements_by_xpath("div")
                    unverifiedData = columns[i]
                    extractedData.append(unverifiedData.text)
        return extractedData

    def convert_currencyCategory(self,extractedData):
        assortedCases = []
        for case in extractedData:
            if 'B' in case:
                newCase = case[:-1]
                value = int(float(newCase) * 1000000000)
                assortedCases.append(str(value))
            elif 'M' in case:
                newCase = case[:-1]
                value = int(float(newCase) * 1000000)
                assortedCases.append(str(value))
            elif 'k' in case:
                newCase = case[:-1]
                value = int(float(newCase) * 1000)
                assortedCases.append(str(value))
            else:
                assortedCases.append(case)
        assortedCases = [int(i) for i in assortedCases]
        return assortedCases

    def complexity_weight(self, extractedData):
        mydict = {'low': 1, 'medium': 2, 'high': 3}
        newlist2 = tuple([mydict[val] for val in extractedData])
        newlist = list(zip(extractedData, newlist2))
        newlist = sorted(newlist, key=lambda x: x[1])
        sortedlist = list(list(zip(*newlist))[0])
        return sortedlist

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s ")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        return logger

