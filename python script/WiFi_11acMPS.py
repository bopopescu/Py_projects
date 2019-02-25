
# libraries
import xlwt,xlrd
from xlwt import *
import sys
import numpy as np

ezxf = xlwt.easyxf
style = xlwt.easyxf('font: bold 1, color red;')
stylelimit=xlwt.easyxf('font: bold 1, color orange;')
stylehead=xlwt.easyxf('font: bold 1; align: wrap 1;border: top thick, right thick, bottom thick, left thick;pattern: pattern fine_dots, fore_color white, back_color orange;')
#opening data file for read

# Default values for file handling
data_file	=	"data_MPS.txt"
output_file =  "myworkbook.xls"
output_textfile= "QA_report.txt"
delete_flag = ''
search_string=''

# check first command line argument for test data file
if len( sys.argv ) > 1 :
	data_file = sys.argv[1]
# specify output file name containing results
if len ( sys.argv ) > 2 :	
	output_file=sys.argv[2]+'.xls'
	output_textfile='QA_report_'+sys.argv[2]+'.txt'
#check if user wants to delete previous result , other options to be added 
#are rename previous result, cancel the processing	
if len ( sys.argv ) > 3 :	
	search_string=sys.argv[3]
#Reading config file	
c = open("config.txt", "r")	
freq=0
bandwidth=0
Measurement_flag=0
Time_Data_flag=0
Error_Messages_flag=0
BT_flag=0
Power_QA_report=0
RX_QA_report=0
EVM_QA_report=0
NO_QA_report=0
for line in c:
	if 'Measurement_Data' in line:
		col=line.split()
		Measurement_flag=int(col[2])
			
	if 'Time_Data' in line:	
		col=line.split()
		Time_Data_flag=int(col[2])
		
	if 'Error_Messages' in line:	
		col=line.split()
		Error_Messages_flag=int(col[2])
		
	if 'Bluetooth' in line:	
		col=line.split()
		BT_flag=int(col[2])
			
	if 'QA_report_Level' in line:
		col=line.split()
		QA_report_Level=col[2]
		for i in QA_report_Level:
			if 'Power' in QA_report_Level:
				Power_QA_report=1
			if 'RX' in QA_report_Level:
				RX_QA_report=1		
			if 'EVM' in QA_report_Level:
				EVM_QA_report= int(1)
			if 'NONE' in line:
				EVM_QA_report=0
				RX_QA_report=0
				Power_QA_report=0
				NO_QA_report=1
				
f	=	open(data_file)

#error check on config file
configdir=(Measurement_flag, Time_Data_flag, Error_Messages_flag, BT_flag, Power_QA_report,RX_QA_report, EVM_QA_report)

if configdir.count(1)==0:
	print 'Please check if the config file exists and configured correctly'
	
"""if delete_flag == 'del' :
		del output_file
   if delete_flag=='rename':
		rename myworkbook.xls old_data.xls"""
# NEW end

# Creating the excel file to write
w	=	open(output_textfile,'w')
w.write ('This is a QA report\n')
wb	=	xlwt.Workbook()
 
# Creating sheets for storing results corresponding to each result parameters
#	such as evm, power etc.
if Measurement_flag:	
	evmsheet	=	wb.add_sheet("EVM_AVG",cell_overwrite_ok=True)
	rxsheet		=	wb.add_sheet("RX_SENSITIVITY",cell_overwrite_ok=True)
	powersheet	=	wb.add_sheet("POWER_AVG",cell_overwrite_ok=True)
if BT_flag   :
	BT_TXsheet  = wb.add_sheet("BT_TX",cell_overwrite_ok=True)
	BT_RXsheet  = wb.add_sheet("BT_RX",cell_overwrite_ok=True)
	
if Time_Data_flag	:
	timesheet   =   wb.add_sheet("Time_Summary",cell_overwrite_ok=True)
	testtimesheet=  wb.add_sheet("Item_TestTime",cell_overwrite_ok=True)
if Error_Messages_flag:	
	errorsheet  =   wb.add_sheet("Error Messages",cell_overwrite_ok=True)
	errorsummary_sheet=  wb.add_sheet("Error Summary",cell_overwrite_ok=True)
if search_string!='':
	stringsheet  =   wb.add_sheet("String Messages",cell_overwrite_ok=True)
	
if NO_QA_report==0:
	QAreportsheet=  wb.add_sheet("QA report",cell_overwrite_ok=True)

#Counters for row number for each result parameters such as evm, power etc.
evmcounter		=	0
BT_Tx_counter   =   0
BT_Rx_counter   =   0
evmbasecounter  =   1 
evm_num         =   0
rxcounter		=	0
rx_num          =   0
rxbasecounter   =   1
powercounter	=	0
powerbasecounter=   1
power_num       =   0
timecounter     =   0
stringcounter    =  0
uplimitflag		=0
lowlimitflag	=0

temp_power     =    0
rxfailcounter  = 0
evmfailcounter = 0
powerfailcounter = 0
bt_power_average={}
bt_BER_average={}

ref_bt_tx_number = 0
ref_bt_rx_number = 0
bt_target_values  = 10
negative=0

upper_limit=''
lower_limit=''
#Preparing Headers for Sheets
if  Measurement_flag==1:

	evmsheet.write(0,0,"TestID",stylehead)
	evmsheet.write(0,1,"TestType",stylehead)
	evmsheet.write(0,2,"Frequency MHz",stylehead)
	evmsheet.write(0,3,"Data_Rate",stylehead)
	evmsheet.write(0,4, "Bandwidth",stylehead)
	evmsheet.write(0,5, "Packet_Width",stylehead)
	evmsheet.write(0,6,"Antenna",stylehead)
	evmsheet.write(0,7,"EVM_Value dB",stylehead)
	evmsheet.write(0,8,"Upper Limit",stylehead)
	evmsheet.write(0,9,"Lower Limit",stylehead)
	evmsheet.write(0,10,"Target power dBm",stylehead)
	evmsheet.write(0,11,"Power Average dBm",stylehead)
	evmsheet.write(0,12,"Upper Limit",stylehead)
	evmsheet.write(0,13,"Lower Limit",stylehead)
	evmsheet.write(0,14,"Delta_Power_dB",stylehead)

	rxsheet.write(0,0,"TestID",stylehead)
	rxsheet.write(0,1,"TestType",stylehead)
	rxsheet.write(0,2,"Frequency MHz",stylehead)
	rxsheet.write(0,3,"Data_Rate",stylehead)
	rxsheet.write(0,4, "Bandwidth",stylehead)
	rxsheet.write(0,5, "Packet_Width",stylehead)
	rxsheet.write(0,6,"Antenna",stylehead)
	rxsheet.write(0,7,"RX sensitivity_value",stylehead)
	rxsheet.write(0,8,"Upper Limit",stylehead)
	rxsheet.write(0,9,"Lower Limit",stylehead)

	powersheet.write(0,0,"TestID",stylehead)
	powersheet.write(0,1,"TestType",stylehead)
	powersheet.write(0,2,"Frequency MHz",stylehead)
	powersheet.write(0,3,"Data_Rate",stylehead)
	powersheet.write(0,4, "Bandwidth",stylehead)
	powersheet.write(0,5, "Packet_Width",stylehead)
	powersheet.write(0,6,"Antenna",stylehead)
	powersheet.write(0,7,"Power Value dBm",stylehead)
	powersheet.write(0,10,"Target Power dBm",stylehead)
	powersheet.write(0,11,"Delta Power dBm",stylehead)
	powersheet.write(0,8,"Upper Limit",stylehead)
	powersheet.write(0,9,"Lower Limit",stylehead)
if BT_flag :
	BT_TXsheet.write(0,0,"TestID",stylehead)
	BT_TXsheet.write(0,1,"TestType",stylehead)
	BT_TXsheet.write(0,2,"Frequency MHz",stylehead)
	BT_TXsheet.write(0,3,"Data_Rate",stylehead)
	BT_TXsheet.write(0,4,"Power Value dBm",stylehead)
	BT_TXsheet.write(0,5,"Target Power dBm",stylehead)
	BT_TXsheet.write(0,6,"Delta Power dBm",stylehead)
	
	
	BT_RXsheet.write(0,0,"TestID",stylehead)
	BT_RXsheet.write(0,1,"TestType",stylehead)
	BT_RXsheet.write(0,2,"Frequency MHz",stylehead)
	BT_RXsheet.write(0,3,"Data_Rate",stylehead)
	BT_RXsheet.write(0,4,"BER%",stylehead)
	BT_RXsheet.write(0,5,"Upper limit",stylehead)
	BT_RXsheet.write(0,6,"Lower Limit",stylehead)
if Time_Data_flag	:
	timesheet.write(0,0,"RunID",stylehead)
	timesheet.write(0,1,"Flow run time",stylehead)
	timesheet.write(0,2,"Test function time",stylehead)
	timesheet.write(0,3,"AVG Flow Run time",stylehead)
	timesheet.write(0,4,"AVG Test function time",stylehead)
	testtimesheet.write(0,0,"Test Item",stylehead)

if Error_Messages_flag:
	errorsheet.write(0,0,"Run #",stylehead)
	errorsheet.write(0,1,"Test Item Number",stylehead)
	errorsheet.write(0,2,"Frequency",stylehead)
	errorsheet.write(0,3,"Data_Rate",stylehead)
	errorsheet.write(0,4,"Bandwidth",stylehead)               
	errorsheet.write(0,5,"Packet_Width",stylehead)               
	errorsheet.write(0,6,"Antenna",stylehead)                 
	errorsheet.write(0,7,"Error Message",stylehead)


	errorsummary_sheet.write(0,0,"Run #",stylehead)
	errorsummary_sheet.write(0,1,"Limit Failures each run",stylehead)
	errorsummary_sheet.write(0,2,"Total Limit Failures upto this run",stylehead)
	errorsummary_sheet.write(0,3,"Functional Failures each run",stylehead)
	errorsummary_sheet.write(0,4,"Total Functional Failures upto this run",stylehead)

if search_string!='':
	stringsheet.write(0,0,"Run#",stylehead)
	stringsheet.write(0,1,"Test Item Number",stylehead)
	stringsheet.write(0,2,"Frequency",stylehead)
	stringsheet.write(0,3,"Data_Rate",stylehead)
	stringsheet.write(0,4,"Bandwidth",stylehead)               
	stringsheet.write(0,5,"Packet_Width",stylehead)               
	stringsheet.write(0,6,"Antenna",stylehead)                 
	stringsheet.write(0,7,"Message Line",stylehead)
if NO_QA_report==0:
	QAreportsheet.write(0,0,"RunID",stylehead)
	QAreportsheet.write(0,1,"TestID",stylehead)
	QAreportsheet.write(0,2,"Frequency",stylehead)
	QAreportsheet.write(0,3,"Data_Rate",stylehead)
	QAreportsheet.write(0,4,"Bandwidth",stylehead)               
	QAreportsheet.write(0,5,"Packet_Width",stylehead)               
	QAreportsheet.write(0,6,"Antenna",stylehead) 
	QAreportsheet.write(0,7,"Message",stylehead)
	QAreportsheet.write(0,8,"Values dB",stylehead)
	QAmessagecounter=1

LimitEvm_Dict={'MCS0': -5, 'MCS1': -10,'MCS2': -13,'MCS3': -16,'MCS4': -19,'MCS5': -22,'MCS6': -25,'MCS7': -27,'MCS8': -30,'MCS9': -32,
				'OFDM-6': -5,'OFDM-9': -5,'OFDM-12': -5,'OFDM-18': -5,'OFDM-24': -5,'OFDM-36': -5,'OFDM-48': -5,'OFDM-54': -5,
				'DSSS-1': -10, 'DSSS-2': -10, 'CCK-11': -10, 'CCK-5.5':-10}
Limitrx_Dict={'MCS0': -82, 'MCS1': -81,'MCS2': -79,'MCS3': -77,'MCS4': -74,'MCS5': -70,'MCS6': -66,'MCS7': -65,'MCS8': -59,'MCS9': -55,
				'OFDM-6': -82,'OFDM-9': -79,'OFDM-12': -79,'OFDM-18': -77,'OFDM-24': -74,'OFDM-36': -70,'OFDM-48': -66,'OFDM-54': -65,
				'DSSS-1': -80, 'DSSS-2': -80, 'CCK-11': -80, 'CCK-5.5':-80}				
	

#Initialization
#Flag to check if EVM, power or RX sweep is included in the test block or not
evmenable=0 
powerenable=0 
rxsweepenable=0


collect_data=0
collect_time=0
disableiteminfo= 1
runID=0 #tells current number of run executed
# Matrix form for data collection
# row represents values collected in 1 run for different test items.
# each row is stored in matrix at index (runId-1)

evm_matrix=np.zeros((3000,3000))
power_matrix=np.zeros((3000,3000))
evmpower_matrix=np.zeros((3000,3000))
rx_matrix=np.zeros((3000,3000))
bt_power_matrix=np.zeros((4000,4000))
bt_BER_matrix=np.zeros((4000,4000))


time_matrix=np.zeros((3000,3000))



evm_average={}
power_average={}
rx_average={}
time_average={}
evmpower_average={}
flowtime_average=0
testtime_average=0
flowtime_sum=0	
testtime_sum=0
percounter=1
#Lists that stores input parameters of all test items in one block. They are reset at start of new test block
antenna='' 
data_rate=[] 
TX_power=[] 
test_type=[] 
packet_format=[] 
evm_flag=[] 
mask_flag=[]  
power_flag=[] 
spectrum_flag=[] 
low_power_rx_flag=[]
high_power_rx_flag=[]
rx_sweep_flag=[]
tx=0 #future
rx=0 #future
firstID=0
errorcounter=0
stringcounter=0

# Variable used to extract current test item ID
current_test_function	=	""
current_test_num		=	0

# NEW end

#Reference numbers for test items to be checked
ref_testprapare_number=0
ref_subtest_num=0
ref_result_num = 0

time_sum=0

			
for line in f:
	if runID>3000:
		break;
		
	if "*  F A I L  *" in line or "*  P A S S  *" in line:
		print "Now Processing Run Number" ,runID
		collect_data = 0 # Flag that prevents data collection during Test summary section
		collect_time = Time_Data_flag
		disableiteminfo=   0
		
		 
	
			
		
		
	if '= Run' in line:
		collect_data=1 #resume data collection
		collect_time=0
		
		strings=line.strip()
		col=strings.split()
		runID= int(col[2])
		runID=int(runID)
		if firstID == 0:
			firstID=runID
			
		if runID==firstID:
			evmcounter=evmcounter
		else:
			evmbasecounter  =   1
			evm_num=0
			evmcounter=0
			rxbasecounter =   1
			rx_num = 0
			rxcounter = 0
			powerbasecounter = 1
			powercounter = 0
			power_num = 0
			timecounter=0
			BT_Tx_counter = 0
			BT_Rx_counter   =   0
			
			
		
		
	# NEW start
	strings	=	line.strip()
	tokens	=	strings.split()
	if len( tokens ) > 0:
		# split first token by the '.' delimiter 
		first_token_parts = tokens[0].split('.')
		# if '.' was found
		if len( first_token_parts ) > 1:
			# if first part is a number, and second part is NOT a number
			if first_token_parts[0].isdigit() and not first_token_parts[1].isdigit():
				# next test function begins, store current test function and number
				current_test_name	=	first_token_parts[1]
				current_test_num	=	int( first_token_parts[0] )
				#print "DEBUG>>>> current_test_name = ", current_test_name
				#print "DEBUG>>>> current_test_num = ", current_test_num
	# NEW end

	if collect_data==1:
	
	
	
		if '.TEST_PREPARE' in line:  #collect the input parameters for evm test items
			strings=line.strip()
			col=strings.split()
			
			#collect parameters possible from TEST PREPARE Item. They will remain universal for all test items inside block
			freq = int(col[1] )
			bandwidth = col[2]
			ref_testprapare_number = current_test_num
			
			#Reset all list of input parameters at start of new test block
			packet_format = []
			data_rate = []
			TX_power = []
			test_type = []
			evm_flag = []
			power_flag = []
			mask_flag =[ ]
			spectrum_flag = []
			low_power_rx_flag = []
			high_power_rx_flag = []
			rx_sweep_flag = []
			ref_result_num = 0
			negative=0
		#Determine antenna ID from TEST PREPARE item
		if 'ANT1' in line and ref_testprapare_number==current_test_num:
			strings=line.strip()
			col=strings.split()
			if col[2] == '1':
				antenna='TX1'
					
		if 'ANT2' in line and ref_testprapare_number==current_test_num:
			strings=line.strip()
			col=strings.split()
			if col[2] == '1':
				antenna='TX2'
				
		if 'ANT3' in line and ref_testprapare_number==current_test_num:
			strings=line.strip()
			col=strings.split()
			if col[2] == '1':
				antenna='TX3'
		if 'ANT4' in line and ref_testprapare_number==current_test_num:
			strings=line.strip()
			col=strings.split()
			if col[2] == '1':
				antenna='TX4'
		
		if 'TX_TEST_ADD' in line :
			
			
			if current_test_num==1+ref_testprapare_number:
				tx = 1 #counts test numbers inside test blocks
				
				strings=line.strip()
				col=strings.split()
				data_rate.append(col[1])
				
				#Store current test number for cross check
				ref_subtest_num=current_test_num
				
			else:
				tx+= 1
				
				strings=line.strip()
				col=strings.split()
				data_rate.append(col[1])
				
				#Store current test number for cross check
				ref_subtest_num=current_test_num

		if 'RX_TEST_ADD' in line :
			
			
			if current_test_num==1+ref_testprapare_number:
				rx = 1 #counts test numbers inside test blocks
				
				strings = line.strip()
				col = strings.split()
				data_rate.append(col[1])
				
				#Store current test number for cross check
				ref_subtest_num=current_test_num

			else:
				rx+= 1
				
				strings=line.strip()
				col=strings.split()
				data_rate.append(col[1])
				
				#Store current test number for cross check
				ref_subtest_num = current_test_num	
				
				
		if 'PACKET_FORMAT' in line and current_test_num == ref_subtest_num:
			strings = line.strip()
			col = strings.split()
			packet_format.append(col[2])

		if 'TX_POWER_DBM' in line and current_test_num == ref_subtest_num:
			strings = line.strip()
			col = strings.split()
			TX_power.append(float(col[2]))

			
		if 'MEASUREMENTS' in line and current_test_num==ref_subtest_num :
			strings = line.strip()
			col = strings.split()
			test_type.append(col[2]) 
			newlist=test_type.pop().split(',') 
			if 'E' in newlist :
				
				evm_flag.append('1')
								
			else :
				evm_flag.append('0')
				
			if 'M' in newlist:
				mask_flag.append('1')
			else :
				mask_flag.append('0')
			if 'P' in newlist:
				power_flag.append('1')
				
			else :
				mask_flag.append('0')
			if 'S' in newlist:
				spectrum_flag.append('1')
				
			else :
				spectrum_flag.append('0')
			if 'L' in newlist:
				low_power_rx_flag.append('1')
			else:
				low_power_rx_flag.append('0')
			if 'H' in newlist:
				high_power_rx_flag.append('1')
			else:
				high_power_rx_flag.append('0')
			if 'S' in newlist :
				if rx>0:
					rx_sweep_flag.append('1')
				
			else:
				rx_sweep_flag.append('0')

			
		if 'TEST_RUN' in line and Measurement_flag:
			
			
			tx = 0
			rx = 0
			evmenable = 0
			powerenable = 0
			rxsweepenable = 0
			ref_subtest_num = 0
			ref_testprapare_number=0
			
			#Store current test number for cross check
			ref_result_num = current_test_num
		
			if evm_flag.count('1')>=1: 
				evmenable=1
		
				evmbasecounter=evmcounter+1
				evm_num=evm_flag.count('1')
				
				
			if power_flag.count('1')>=1:
				powerenable=1
				powerbasecounter=powercounter+1
				power_num=power_flag.count('1')
				
			if rx_sweep_flag.count('1')>=1:
				rxsweepenable=1
				rxbasecounter=rxcounter+1
				
				rx_num=rx_sweep_flag.count('1')
		if evmenable==1 and current_test_num==ref_result_num:
			
			if 'EVM_AVG_DB.@' in line:
				
				for i in range (len(data_rate)	):	
					
					if data_rate[i] in line:
						
						evmcounter=evmbasecounter+i
						
						strings=line.strip()
						col=strings.split()
						evm_values= float(col[2])
						if data_rate[i] in LimitEvm_Dict.keys() and EVM_QA_report==1:
							limit=float(LimitEvm_Dict[data_rate[i]])
							
							if (float(evm_values)>limit):
								
								QAreportsheet.write( QAmessagecounter,7,'EVM Limit failed by') 
								QAreportsheet.write( QAmessagecounter,8,float(float(evm_values)-LimitEvm_Dict[data_rate[i]]))
								QAreportsheet.write(QAmessagecounter,0,runID)
								QAreportsheet.write(QAmessagecounter,1,current_test_num)
								QAreportsheet.write(QAmessagecounter,2,freq)
								QAreportsheet.write(QAmessagecounter,3,data_rate[i])
								QAreportsheet.write(QAmessagecounter,4,bandwidth)
								QAreportsheet.write(QAmessagecounter,6,antenna)
								QAreportsheet.write(QAmessagecounter,5,packet_format)
								evmfailcounter+=1
								
								#w.write('Limit failed for EVM at '+repr(freq)+' '+repr(data_rate)+' '+repr(packet_format)+' by '+repr(float(float(evm_values)-LimitEvm_Dict[data_rate]))+' dB in  Run# '+repr(runID)+' on '+repr(current_test_num)+' Test ID\n')
								QAmessagecounter+=1
						upper_limit=col[4].strip( '(), ' )
						lower_limit=col[5].strip( '(), ' )
						type='EVM_Test'
						
						if  Measurement_flag==1:
							evmsheet.write(evmcounter,1,type)
							evmsheet.write(evmcounter,2,freq)
							evmsheet.write(evmcounter,3,data_rate[i])
							evmsheet.write(evmcounter,4,bandwidth)
							evmsheet.write(evmcounter,5,packet_format[i])
							evmsheet.write(evmcounter,6,antenna)
							evmsheet.write(evmcounter,8,upper_limit)
							evmsheet.write(evmcounter,9,lower_limit)
							if upper_limit=='' :
								uplimitflag=0
								
							if lower_limit=='' :
								lowlimitflag=0
							evmsheet.write(evmcounter,10,TX_power[i])
							evmsheet.write(evmcounter,0,current_test_num)
							evmsheet.write(evmcounter,7,evm_values)
							evm_matrix[runID-1,current_test_num-1-i]=evm_values
							
							evm_sum=0
							
							if runID==firstID:
						
								evmsheet.write(evmcounter,7,evm_values)
							else:
						
								for x in range(1,runID):
									if evm_matrix[x-1][current_test_num-1-i]==0:
										negative+=1
										
									evm_sum+=(evm_matrix[x-1][current_test_num-1-i])
								
								evm_sum+=float(evm_values)
								evm_average=evm_sum/(runID-negative)
								negative=0		
								tempredflag=0
								if (uplimitflag):
									if (evm_average>upper_limit):
										tempredflag=1
								if (lowlimitflag):
									if (evm_average<lower_limit):
										tempredflag=1
								if (tempredflag):
									evmsheet.write(evmcounter,7,evm_average,style)
								else:
									evmsheet.write(evmcounter,7,evm_average)
									
		if powerenable==1 and current_test_num==ref_result_num:				
			if 'POWER.000.POWER_AVERAGE_DBM.@' in line:
				for i in range (len(data_rate)	):	
					
					if data_rate[i] in line:
						temp_power=TX_power[i]
						powercounter=powerbasecounter+i
						strings=line.strip()
						col=strings.split()
						power_values= float(col[2])
						if (((power_values-temp_power)> 1.5 or (power_values-temp_power)< -1.5)) and Power_QA_report==1:
									
									
									powerfailcounter+=1
									QAreportsheet.write( QAmessagecounter,7,'Power Difference is') 
									QAreportsheet.write( QAmessagecounter,8,power_values-temp_power)
									QAreportsheet.write(QAmessagecounter,0,runID)
									QAreportsheet.write(QAmessagecounter,1,current_test_num)
									QAreportsheet.write(QAmessagecounter,2,freq)
									QAreportsheet.write(QAmessagecounter,3,data_rate[i])
									QAreportsheet.write(QAmessagecounter,4,bandwidth)
									QAreportsheet.write(QAmessagecounter,6,antenna)
									QAreportsheet.write(QAmessagecounter,5,packet_format[i])
									QAmessagecounter+=1
						upper_limit=col[4].strip( '(), ' )
						lower_limit=col[5].strip( '(), ' )
						type='Power_Measurement'
						if  Measurement_flag==1:
							powersheet.write(powercounter,1,type)
							powersheet.write(powercounter,2,freq)
							powersheet.write(powercounter,3,data_rate[i])
							powersheet.write(powercounter,4,bandwidth)
							powersheet.write(powercounter,5,packet_format[i])
							powersheet.write(powercounter,6,antenna)
							powersheet.write(powercounter,7,power_values)
							powersheet.write(powercounter,8,upper_limit)
							powersheet.write(powercounter,9,lower_limit)
							powersheet.write(powercounter,10,TX_power[i])
							powersheet.write(powercounter,0,current_test_num)
							if upper_limit=='' :
								uplimitflag=0
							if lower_limit=='' :
								lowlimitflag=0
							
							power_matrix[runID-1,current_test_num-1-i]=power_values
							
							power_sum=0
							
							if runID==firstID:
						
								
								if (power_values-temp_power)>1.5 or (power_values-temp_power)<-1.5 :
									powersheet.write(powercounter,11,power_values-temp_power,style)
									powersheet.write(powercounter,7,power_values,style)
								else:
									powersheet.write(powercounter,11,power_values-temp_power)
									powersheet.write(powercounter,7,power_values)
							else:
					
								for x in range(1,runID):
									if power_matrix[x-1][current_test_num-1-i]==0:
										negative+=1
										
									power_sum+=(power_matrix[x-1][current_test_num-1-i])
								
								power_sum+=float(power_values)
								power_average=power_sum/(runID-negative)
								negative=0		
								
								
								
								tempredflag=0
								
								if (power_average-temp_power)>1.5 or (power_average-temp_power)<-1.5 :
									tempredflag=1
								if(uplimitflag):
									if (power_average>upper_limit):
										tempredflag=1
								if(lowlimitflag):
									if (power_average<lower_limit):
										tempredflag=1
								
								if(tempredflag):
									powersheet.write(powercounter,11,power_average-temp_power,style)
									powersheet.write(powercounter,7,power_average,style)
								else:
									powersheet.write(powercounter,11,power_average-temp_power)
									powersheet.write(powercounter,7,power_average)
									
		if evmenable==1 and current_test_num==ref_result_num:				
			if 'POWER_AVG_DBM.@' in line and 'EVM' in line:
				
				
				for i in range (len(data_rate)	):	
					
					if data_rate[i] in line:
					
						temp_power=TX_power[i]				
						strings=line.strip()
						col=strings.split()
						evmpower_values= float(col[2])
																	
						upper_limit=col[4].strip( '(), ' )
						lower_limit=col[5].strip( '(), ' )
						
						
						evmpower_matrix[runID-1,current_test_num-1-i]=evmpower_values
						evmpower_sum=0
						if (((evmpower_values-temp_power)> 1.5 or (evmpower_values-temp_power)< -1.5)) and powerenable==0 and Power_QA_report==1:
								
								font0=Font()
								font0.bold = True	
								style0 = XFStyle()
								style0.font = font0
								powerfailcounter+=1
								QAreportsheet.write( QAmessagecounter,7,'Power Difference from EVM test is') 
								QAreportsheet.write( QAmessagecounter,8,evmpower_values-temp_power)
								QAreportsheet.write(QAmessagecounter,0,runID)
								QAreportsheet.write(QAmessagecounter,1,current_test_num)
								QAreportsheet.write(QAmessagecounter,2,freq)
								QAreportsheet.write(QAmessagecounter,3,data_rate[i])
								QAreportsheet.write(QAmessagecounter,4,bandwidth)
								QAreportsheet.write(QAmessagecounter,6,antenna)
								QAreportsheet.write(QAmessagecounter,5,packet_format[i])
								QAmessagecounter+=1
						if  Measurement_flag==1:
								
							evmsheet.write(evmcounter,12,upper_limit)
							evmsheet.write(evmcounter,13,lower_limit)
							if upper_limit=='' :
								uplimitflag=0
						
							if lower_limit=='' :
								lowlimitflag=0
							if runID==firstID:
						
								evmsheet.write(evmcounter,11,evmpower_values)
							
								if (evmpower_values-temp_power)>1.5 or (evmpower_values-temp_power)<-1.5:
									evmsheet.write(evmcounter,14,evmpower_values-temp_power,style)
								else:	
									evmsheet.write(evmcounter,14,evmpower_values-temp_power)
							else:
					
								for x in range(1,runID):
									if evmpower_matrix[x-1][current_test_num-1-i]==0:
										negative+=1
										
									evmpower_sum+=(evmpower_matrix[x-1][current_test_num-1-i])
								
								evmpower_sum+=float(evmpower_values)
								evmpower_average=evmpower_sum/(runID-negative)
								negative=0		
								
								tempredflag=0
								if (evmpower_average-temp_power)>1.5 or (evmpower_average-temp_power)<-1.5 :
									tempredflag=1
								if(uplimitflag):
									if (evmpower_average>upper_limit):
										tempredflag=1
								if(lowlimitflag):
									if (evmpower_average<lower_limit):
										tempredflag=1
																
								if(tempredflag):
									evmsheet.write(evmcounter,14,evmpower_average-temp_power,style)
									evmsheet.write(evmcounter,11,evmpower_average,style)
								else:
									evmsheet.write(evmcounter,14,evmpower_average-temp_power)
									evmsheet.write(evmcounter,11,evmpower_average)	
									
		if rxsweepenable==1 and current_test_num==ref_result_num:
			if 'PER_SWEEP.SENS_POWER_LEVEL_DBM' in line:
				percounter=1
				
				for i in range (len(data_rate)	):
					if data_rate[i] in line:
						
						rxcounter=rxbasecounter+i
						strings=line.strip()
						col=strings.split()
						rx_values=float(col[2])
						if data_rate[i] in Limitrx_Dict.keys() and RX_QA_report==1:
							limit=float(Limitrx_Dict[data_rate[i]])
							
							if (rx_values>limit):
								
								QAreportsheet.write( QAmessagecounter,7,'RX sesitiyivity Limit failed by') 
								QAreportsheet.write( QAmessagecounter,8,float(rx_values-Limitrx_Dict[data_rate[i]]))
								QAreportsheet.write(QAmessagecounter,0,runID)
								QAreportsheet.write(QAmessagecounter,1,current_test_num)
								QAreportsheet.write(QAmessagecounter,2,freq)
								QAreportsheet.write(QAmessagecounter,3,data_rate[i])
								QAreportsheet.write(QAmessagecounter,4,bandwidth)
								QAreportsheet.write(QAmessagecounter,6,antenna)
								QAreportsheet.write(QAmessagecounter,5,packet_format)
								QAmessagecounter+=1
								rxfailcounter+=1
						upper_limit=col[4].strip( '(), ' )
						lower_limit=col[5].strip( '(), ' )
						type='RX Sensitivity'
						if  Measurement_flag==1:
							rxsheet.write(rxcounter,1,type)
							rxsheet.write(rxcounter,2,freq)
							rxsheet.write(rxcounter,3,data_rate[i])
							rxsheet.write(rxcounter,4,bandwidth)
							rxsheet.write(rxcounter,5,packet_format[i])
							rxsheet.write(rxcounter,6,antenna)
							rxsheet.write(rxcounter,7,rx_values)
							rxsheet.write(rxcounter,8,upper_limit)
							rxsheet.write(rxcounter,9,lower_limit)
							if upper_limit=='' :
								uplimitflag=0
								
							if lower_limit=='' :
								lowlimitflag=0
							rxsheet.write(rxcounter,0,current_test_num)
							
							rx_matrix[runID-1,current_test_num-1-i]=rx_values
							rx_sum=0
							
						
				
							for x in range(1,runID):
								if rx_matrix[x-1][current_test_num-1-i]==0:
										negative+=1
										
								rx_sum+=(rx_matrix[x-1][current_test_num-1-i])
								
							rx_sum+=float(rx_values)
							rx_average=rx_sum/(runID-negative)
							negative=0		
								
							
							tempredflag=0
							if (uplimitflag):
								if (rx_average>upper_limit):
									tempredflag=1
							if(lowlimitflag):
								if(rx_average<lower_limit):
									tempredflag=1
							if(tempredflag):
								rxsheet.write(rxcounter,7,rx_average,style)
							else:
								rxsheet.write(rxcounter,7,rx_average)
			#code from here is Debug		
				
		
		if BT_flag==1:				
			if 'TX_EDR_AVERAGE' in line or 'TX_BDR_AVERAGE' in line or 'TX_LE_AVERAGE ' in line:
				garbage=1
				
			else:
				
				if 'TX_BDR' in line or 'TX_EDR' in line or 'TX_LE' in line:
					BT_Tx_counter+=1
					strings=line.strip()
					col=strings.split()
					col[0]=col[0].split('.')
					type= col[0]
					freq=int(col[1])
					data_rate=col[2]
					BT_TXsheet.write(BT_Tx_counter,1,type[1])
					BT_TXsheet.write(BT_Tx_counter,2,freq)
					BT_TXsheet.write(BT_Tx_counter,3,data_rate)
					BT_TXsheet.write(BT_Tx_counter,0,current_test_num)
					ref_bt_tx_number=current_test_num
				
			if 'RX_BDR' in line or 'RX_EDR' in line or '.RX_LE' in line:
					BT_Rx_counter +=1
					strings=line.strip()
					col=strings.split()
					type=col[0].split('.')
					freq=int(col[1])
					data_rate=col[2]
					BT_RXsheet.write(BT_Rx_counter,1,type[1])
					BT_RXsheet.write(BT_Rx_counter,2,freq)
					BT_RXsheet.write(BT_Rx_counter,3,data_rate)
					BT_RXsheet.write(BT_Rx_counter,0,current_test_num)
					ref_bt_rx_number=current_test_num
					
			if 'TARGET_POWER_DBM' in line and current_test_num==ref_bt_tx_number:
				value=line.strip()
				col=value.split()
				bt_target_values=float(col[2])
				BT_TXsheet.write(BT_Tx_counter,5,bt_target_values)
				
			if 'POWER_AVERAGE_DBM' in line and current_test_num==ref_bt_tx_number:
				value=line.strip()
				col=value.split()
				bt_power_values=float(col[2])
				
				bt_power_matrix[runID-1,current_test_num-1]=bt_power_values
				bt_power_sum=0
				
				if runID==firstID:
					if (bt_target_values-bt_power_values)>1.5 or (bt_target_values-bt_power_values)< -1.5:
						BT_TXsheet.write(BT_Tx_counter,4,bt_power_values,style)
					else:
						BT_TXsheet.write(BT_Tx_counter,4,bt_power_values)
				
				else:
					for x in range(1,runID):
						
						if bt_power_matrix[x-1][current_test_num-1]==0:		
							
							negative+=1
							
						bt_power_sum+=(bt_power_matrix[x-1][current_test_num-1])
						
					bt_power_sum+=float(bt_power_values)
					bt_power_average=bt_power_sum/(runID-negative)
					negative=0		
					
					if (bt_power_average-bt_target_values)>1.5 or (bt_power_average-bt_target_values)<-1.5:
						BT_TXsheet.write(BT_Tx_counter,6,bt_power_average-bt_target_values,style)
						BT_TXsheet.write(BT_Tx_counter,4,bt_power_average,style)	
					else:
						BT_TXsheet.write(BT_Tx_counter,6,bt_power_average-bt_target_values)
						BT_TXsheet.write(BT_Tx_counter,4,bt_power_average)		

						
			if ('BER                      :' in line and current_test_num==ref_bt_rx_number) or ('PER                      :' in line and current_test_num==ref_bt_rx_number):
				value=line.strip()
				col=value.split()
				bt_BER_values=float(col[2])
				
				bt_BER_matrix[runID-1,current_test_num-1]=bt_BER_values
				bt_BER_sum=0
				if runID==firstID:
					BT_RXsheet.write(BT_Rx_counter,4,bt_BER_values)
				else:
					for x in range(1,runID):
						
						if bt_BER_matrix[x-1][current_test_num-1]==0:		
							
							negative+=1
							
						bt_BER_sum+=(bt_BER_matrix[x-1][current_test_num-1])
						
					bt_BER_sum+=float(bt_BER_values)
					bt_BER_average=bt_BER_sum/(runID-negative)
					negative=0		
					BT_RXsheet.write(BT_Rx_counter,4,bt_BER_average)
					
		if 'ERROR_MESSAGE ' in line and Error_Messages_flag:
	
			if 'return error' in line :
				errorcounter+=1
				
				error_message=line.strip()
				
				errorsheet.write(errorcounter,7,error_message)
				errorsheet.write(errorcounter,0,runID)
				errorsheet.write(errorcounter,1,current_test_num)
				errorsheet.write(errorcounter,2,freq)
				errorsheet.write(errorcounter,4,bandwidth)
				errorsheet.write(errorcounter,6,antenna)
				errorsheet.write(errorcounter,5,packet_format[:])
				errorsheet.write(errorcounter,3,data_rate)
				
			if 'failed' in line or 'Fail' in line:
				errorcounter+=1
				error_message=line.strip()
				errorsheet.write(errorcounter,0,runID)
				errorsheet.write(errorcounter,1,current_test_num)
				errorsheet.write(errorcounter,7,error_message)
				
			if 'TX Calibration' in line and  'fail' in line:
				errorcounter+=1
				
				error_message=line.strip()
				
				errorsheet.write(errorcounter,7,error_message)
				errorsheet.write(errorcounter,0,runID)
				errorsheet.write(errorcounter,1,current_test_num)
				
		if search_string in line and search_string!='':
			stringcounter+=1
				
			string_message=line
			
			stringsheet.write(stringcounter,7,string_message)
			stringsheet.write(stringcounter,0,runID)
			stringsheet.write(stringcounter,1,current_test_num)
			stringsheet.write(stringcounter,2,freq)
			stringsheet.write(stringcounter,4,bandwidth)
			stringsheet.write(stringcounter,6,antenna)
			stringsheet.write(stringcounter,5,packet_format[:])
			stringsheet.write(stringcounter,3,data_rate)
			
	if collect_time==1:
		if 'Total Run'in line:
			disableiteminfo=1
		timecounter+=1
		strings=line.strip()
		temp=strings.split()
		if len(temp)>0:
			if '.TEST_PREPARE' in line:
				
				Iteminfo=temp[0:3]
				if len(temp)>1:
					col=temp[4]
			else:
				if 'TEST_ADD' in line:
					Iteminfo=temp[0:3]
					if len(temp)>1:
						col=temp[2]
				else:
					if 'TEST_RUN' in line:
						Iteminfo=temp[0]
						if len(temp)>1:
							col=temp[1]
					else:
						if 'TX_CALIBRATION' in line:
							Iteminfo=temp[0:5]
							if len(temp)>1:
								col=temp[4]
							
						else:
							Iteminfo=temp[0]
							if len(temp)>1:
								col=temp[1]
		
		
			
		if (len(temp)>3) and ('BDR' in line or 'EDR' in line or 'LE' in line):
			col=temp[3]
		colvalue=list(col)
		
		time_values=0
		
		if ':' in colvalue:
			colvalue.remove(':')
			s = map(str, colvalue)   # ['1','2','3']
			s = ''.join(s)          # '123'
			
			if len(s)>0:
				time_values = float(s)  
				
		if disableiteminfo==0:
			testtimesheet.write(timecounter,0,Iteminfo)
			if runID<=254:	
				if time_values>100 :
					
					w.write('Time>16 sec at Test # '+repr(current_test_num)+' at run# '+repr(runID)+' with time of '+ repr(time_values)+' seconds\n')
					testtimesheet.write(timecounter,runID,time_values,style)
				else:	
					testtimesheet.write(timecounter,runID,time_values)
				testtimesheet.write(0,runID,runID,stylehead)
		
			time_matrix[runID-1,timecounter-1]=time_values;
		
		time_sum=0
			
	
		for i in range(1,runID):
			
			if len(time_matrix)>1:
				#print i, current_test_num, time_values,timecounter
							
				time_sum+=(time_matrix[i-1][timecounter-1])	
		
		time_sum+=float(time_values)
		time_average=time_sum/(runID)
		if disableiteminfo==0:
			if runID<=254:	
				testtimesheet.write(timecounter,runID+1,time_average)
				testtimesheet.write(0,runID+1,'Time_average',stylehead)
			else:
				testtimesheet.write(timecounter,255,time_average)
				testtimesheet.write(0,255,'Time_average',stylehead)
		
		
		
		if 'Flow Run Time' in line: 
			
			
			
			strings=line.strip()
			temp=strings.split()
			
			col=temp[3]
			colvalue=list(col)
			colvalue.remove(':')
			
			
			s = map(str, colvalue)   # ['1','2','3']
			s = ''.join(s)          # '123'
			flowtime_values = float(s)              # 123
			
			timesheet.write(runID,0,runID)	
			timesheet.write(runID,1,flowtime_values)
									
			flowtime_sum+=float(flowtime_values)
					
			flowtime_average=flowtime_sum/(runID)
				
			timesheet.write(1,3,flowtime_average)
			
			
			
				
		if 'Test Function Time' in line: 
			collect_time=0
			strings=line.strip()
			temp=strings.split()
			col=temp[3]
			colvalue=list(col)
			colvalue.remove(':')
			
			
			s = map(str, colvalue)   # ['1','2','3']
			s = ''.join(s)          # '123'
			testtime_values = float(s)              # 123
			
			timesheet.write(runID,0,runID)	
			timesheet.write(runID,2,testtime_values)
			
										
			testtime_sum+=float(testtime_values)
			testtime_average=testtime_sum/(runID)
			timesheet.write(1,4,testtime_average)
	if Error_Messages_flag==1:
		if 'Failed Run(s) on Limits' in line:
			strings=line.strip()
			temp=strings.split()
			col=temp[4]
				
			colvalue=list(col)
			if ':' in col:
				colvalue.remove(':')
			s = ''.join(colvalue)
			colvalue=int(s)
			errorsummary_sheet.write(runID,0,runID)
			errorsummary_sheet.write(runID,2,colvalue)
		if 'Failed Run(s) on Errors' in line:
			strings=line.strip()
			temp=strings.split()
			col=temp[4]
			colvalue=list(col)
			if ':' in col:
				colvalue.remove(':')
			s = ''.join(colvalue)
			colvalue=int(s)
			errorsummary_sheet.write(runID,0,runID)
			errorsummary_sheet.write(runID,4,colvalue)
		if 'Fail(s) on Limits' in line:
			strings=line.strip()
			temp=strings.split()
			col=temp[3]
			colvalue=list(col)
			if ':' in col:
				colvalue.remove(':')
			s = ''.join(colvalue)
			colvalue=int(s)
			errorsummary_sheet.write(runID,0,runID)
			errorsummary_sheet.write(runID,1,colvalue)
		if 'Fail(s) on Errors' in line:
			strings=line.strip()
			temp=strings.split()
			col=temp[3]
			colvalue=list(col)
			if ':' in col:
				colvalue.remove(':')
			s = ''.join(colvalue)
			colvalue=int(s)
			errorsummary_sheet.write(runID,0,runID)
			errorsummary_sheet.write(runID,3,colvalue)
if Measurement_flag:
	evmsheet.col(1).width = 0x0d00	
	evmsheet.col(2).width = 0x0d00
	evmsheet.col(3).width = 0x0d00
	evmsheet.col(4).width = 0x0d00
	rxsheet.col(1).width = 0x0d00
	rxsheet.col(2).width = 0x0d00	
	rxsheet.col(3).width = 0x0d00
	rxsheet.col(4).width = 0x0d00
	rxsheet.col(7).width = 0x0d00
	powersheet.col(1).width = 0x0d00
	powersheet.col(2).width = 0x0d00
	powersheet.col(3).width = 0x0d00
	powersheet.col(4).width = 0x0d00
if BT_flag:
	BT_RXsheet.col(1).width=0x0d00
	BT_RXsheet.col(2).width=0x0d00
	BT_RXsheet.col(3).width=0x0d00
	BT_TXsheet.col(1).width=0x0d00
	BT_TXsheet.col(2).width=0x0d00
	BT_TXsheet.col(3).width=0x0d00
if Time_Data_flag	:
	timesheet.col(1).width	= 0x0fff
	timesheet.col(2).width	= 0x0fff
	timesheet.col(3).width	= 0x0fff
	timesheet.col(4).width	= 0x0fff
	testtimesheet.col(0).width= 0x1f00
if Error_Messages_flag==1:
	errorsummary_sheet.col(1).width	= 0x0fff
	errorsummary_sheet.col(2).width	= 0x0fff
	errorsummary_sheet.col(3).width	= 0x0fff
	errorsummary_sheet.col(4).width	= 0x0fff
	errorsheet.col(1).width	= 0x0fff
	errorsheet.col(2).width	= 0x0fff
	errorsheet.col(3).width	= 0x0fff
	errorsheet.col(4).width	= 0x0fff
if NO_QA_report==0:
	QAreportsheet.col(7).width= 0x1f00
wb.save(output_file)
if EVM_QA_report:
	w.write('EVM limit failed '+repr(evmfailcounter)+' times\n')
if RX_QA_report:
	w.write('RX sensitivity limit failed '+repr(rxfailcounter)+' times\n')	
if Power_QA_report:
	w.write('Power is off from target power for '+repr(powerfailcounter)+' times\n')
if Error_Messages_flag:
	w.write('There are '+repr(errorcounter)+' functional errors\n')	
w.close()
print "Post processing finished successfully. Please check file ", output_file
f.close()

#f	=	open(output_file)
#evmsheet	=	wb.open_sheet("EVM_AVG")
#piece of code that can help making bold writing
"""font0 = Font()
					font0.name = 'Times New Roman'
					font0.bold = True	
					style0 = XFStyle()
					style0.font = font0	"""

