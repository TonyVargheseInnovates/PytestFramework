# QA-Automation
### About Me:

I am Tony Varghese. A QA Specialist with a passion for building full stack apps. As part of Automation Testing, I have primarily worked on Selenium Webdriver with Python using Pytest framework. I am also a Certified ScrumMaster , HP Certified Automation Tester and ISTQB Certified. 

You could get to know more about me by clicking here -> https://tonyvarghese.me/. 
### Task–Test Automation:

The below test automation solution has been completed using **Selenium-Webdriver(Python) :: Pytest Framework **. 

The Objective of the test suite is : 
1) To validate the correctness of Filter Feature and Sort Feature implmented in the webpage
2) Test Solution should be robust to handle changes to webpage, eg, if new rows or colums are added to the webtable

#### Prerequisites :

1)	Latest Version of Python installed   
2)	pip install selenium
3)	pip install pytest
4)	pip install pytest-html-reporter
5)	Download Chromedriver (if not already done) and update the path of the chromedriver in pyTestFramework_EclecticIQ_Tony/tests/conftest.py

    ```
        browser_name = request.config.getoption("browser_name")
        if browser_name == "chrome":
            driver = webdriver.Chrome(executable_path="C:\\SeleniumWebdriverPython\\chromedriver.exe")  --> Update Chromedriver Path here
        elif browser_name == "firefox":
            driver = webdriver.Firefox(executable_path="C:\\SeleniumWebdriverPython\\geckodriver.exe")  --> Update Geckodriver Path here
    ```
#### How To Run :

1) Goto pyTestFramework_EclecticIQ_Tony/tests/
2) py.test --html-report=./report/report.html

#### Test Suite:
The Test Solution has 2 Test Suites :

-	[x] **Filter Feature Test Suite** -> test_filterFeature.py
          Filter Feature Test Suite has 4 test cases which follow a TDD approach to check the below test scenarios
          
            1) Ensure that when you input "high" in filter input, Webtable is populated with only words containing "high"
            2) Ensure that when you input "Man in the Middle" in filter input, Webtable is populated with only words containing "Man in the Middle"
            3) Ensure that when you input substring "hi" in filter input, Webtable is populated with only words containing "hi"
            4) Ensure that when you input substring "phis" in filter input, Webtable is populated with only words containing "phis"

-	[x] **Sort Feature Test Suite** -> test_sortingFeature.py
          Sorting Feature Test Suite has 4 test cases which follow a TDD approach to check the below test scenarios
          
             1) Ensure that when you Sort By Name, Webtable is sorted by name alphabetically
             2) Ensure that when you Sort by Number Of Cases, Webtable is sorted from low to high and Test Solution handles k=1000, M=1000000 etc
             3) Ensure that when you Sort by Impact Score, Webtable is sorted from low to high
             4) Ensure that when you Sort by Complexity, Webtable is sorted as low, medium, high respectively

