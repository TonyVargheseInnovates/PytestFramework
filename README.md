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
5)	Download Chromedrive(if not already done) and update the path of the chromedriver in pyTestFramework_EclecticIQ_Tony/tests/conftest.py
    ```
        browser_name = request.config.getoption("browser_name")
        if browser_name == "chrome":
            driver = webdriver.Chrome(executable_path="C:\\SeleniumWebdriverPython\\chromedriver.exe")  --> Update Chromedriver Path here
        elif browser_name == "firefox":
            driver = webdriver.Firefox(executable_path="C:\\SeleniumWebdriverPython\\geckodriver.exe")  --> Update Geckodriver Path here
    ```

#### User Story:
```

  AS A User
  I WANT TO use the DSL Calculator
  SO THAT I am able to select the best possible tariff for me 

````

-	[x] **Scenario 1 - DSL Result List - verify result list** -> node index_Scenario1

```
  GIVEN the User is on www.verivox.de
  WHEN he is on the DSL calculator
  AND he enters prefix/code “Ihre Vorwahl” as 030 with 16 Mbit/s bandwidth selection AND clicks on the button labeled as "JETZT VERGLEICHEN"
  THEN he should be able see the Result List page with all the available Tariffs

```
-	[x] **Scenario 2 - Result List - verify Offer detail page** -> node index_Scenario2

```
  GIVEN the User is on the DSL Result List (follow scenario 1) 
  WHEN he selects one of the listed Tariffs 
  AND clicks on "mehr zum Tarif" button 
  THEN he should be able see the details of the selected Tariff (see screenshot 2) 
  AND he should also see a button labeled as "In 5 Minuten online wechseln" (see screenshot 3) 
      
  Note : For additional Test Coverage, Checking 5 tariffs on result list page and Details page
```
  -	[x] **Scenario 3 - Lazy loading/pagination for loading the Result List** -> node index_Scenario3
  
  ```
    GIVEN the User is on the DSL Result List (follow scenario 1)  
    WHEN there are more than 20 tariffs available for the provided Vorwahl and bandwidth  
    THEN the User should a button labeled as "20 weitere laden" 
    AND WHEN he/she clicks on this button  
    THEN the list should be appended with next 20 tariffs and so on until all Tariffs are loaded
   ```
