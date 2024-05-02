# Test Automation Project

This is my first test automation project based on Selenium-Webdriver with Python. It's still developing package of automated tests of [demoqa.com](https://demoqa.com/) demo website.
The collection of tests contains:


## Project Structure
Here you can find a short description of main directories and it's content
- [locators](locators) - there are locators of web elements in locators.py grouped in classes
- [pages](pages) - there are sets of method for each test step
- [tests](tests) - there are sets of tests for main functionalities of website
- [reports](reports) - if you run tests with Allure, tests reports will be saved in this directory
## Getting Started

You need to install packages using pip according to requirements.txt file.
Run the command below in terminal:

```
$ pip install -r requirements.txt
```

## Run Automated Tests

To run selected test without Allure report you need to set pytest as default test runner in Pycharm first
```
File > Settings > Tools > Python Integrated Tools > Testing
```
After that you just need to choose one of the tests from "tests" directory and click "Run test" green arrow. There are 2 versions of test in each test file. In general test cases you can easily modify test inputs. Data-driven tests base on xlsx files from [utils](utils) directory. 

## Generate Test Report

To generate all tests report using Allure you need to run tests by command first:
```
$ pytest --alluredir=<reports directory path>
```
After that you need to use command:
```
$ allure serve <reports directory path>
```