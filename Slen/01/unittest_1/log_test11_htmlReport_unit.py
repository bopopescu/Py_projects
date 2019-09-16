import unittest
import HtmlTestRunner
import os
from log_test7_unit import SearchTest
from log_test8_unit import HomePageTest

# pip install html-testRunner

# get the directory path to output report file
dir = os.getcwd()

# get all tests from SearchProductTest and HomePageTest class
search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTest)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([search_tests, home_page_tests ])

# open the report file

# configure HTMLTestRunner options
# runner = HtmlTestRunner.HTMLTestRunner(
#     output="report_folder" ## report_folder is created as a folder 
# )

# setting report name,  and combine reports to single file
runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, output="test_results_dir", \
    report_name="MyReport", add_timestamp=True)

# run the suite using HTMLTestRunner
runner.run(smoke_tests)
