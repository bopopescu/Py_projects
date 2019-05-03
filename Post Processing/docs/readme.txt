Author: Vishal Sawant(QA Silicon solutions)


This tool is still in testing mode. 
The user Guide with known issues/limitations will be updated soon.

To use the tool, 
Please ensure you have installed
1. Python 2.7
2. XLWT package that supports writting to excel sheet
3. NumPy package that allows numerical operation on arrays
4. config file

This tool can work on log file created by the IQfact+ package.
please use following synatx to process log file.
python scriptname.py input_log.txt output.xls
example :
python WiFi_11ac.py log_all.txt output.xls

config file is used for following purpose
1.Measurement_Data : This parameter can be enabled to view all measurements performed and their average values over number of runs performed.
	Tip: Disable this when you are only interested in time or error analysis but not in actual values of EVM, Sensitivity or power.
2.Time_Data : This parameter can be enabled to view all time related information. It reads the average time taken by each test item as well as the complete test flow time from the log.
	Tip: Disable this when test time is not important for your analysis.
3.Error_Messages: This parameter can be enabled to view each error message and summary of failed test items based on limit or functional errors.
4.QA_report_Level: This report uses in built limit table and applies limits to each result. This can be done selectively for EVM, power or RX or all of them. 



