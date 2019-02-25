

# libraries
import xlwt
from xlwt import *
import sys
import numpy as np

ezxf = xlwt.easyxf

#opening data file for read

# Default values for file handling
data_file	=	"data_MPS.txt"
output_file =  "myworkbook.xls"
delete_flag = ''


# check first command line argument for test data file
if len( sys.argv ) > 1 :
	data_file = sys.argv[1]
# specify output file name containing results
if len ( sys.argv ) > 2 :	
	output_file=sys.argv[2]
#check if user wants to delete previous result , other options to be added 
#are rename previous result, cancel the processing	
if len ( sys.argv ) > 3 :	
	delete_flag=sys.argv[3]
#Reading config file	
c = open("config.txt", "r")	

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
w	=	open("QA_report.txt",'w')
w.write ('This is a QA report\n')
wb	=	xlwt.Workbook()
 
# Creating sheets for storing results corresponding to each result parameters
#	such as evm, power etc.
if Measurement_flag:	
	evmsheet	=	wb.add_sheet("EVM_AVG",cell_overwrite_ok=True)
	rxsheet		=	wb.add_sheet("RX_SENSITIVITY",cell_overwrite_ok=True)
	powersheet	=	wb.add_sheet("POWER_AVG",cell_overwrite_ok=True)
if Time_Data_flag	:
	timesheet   =   wb.add_sheet("Time_Summary",cell_overwrite_ok=True)
	testtimesheet=  wb.add_sheet("Item_TestTime",cell_overwrite_ok=True)
if Error_Messages_flag:	
	errorsheet  =   wb.add_sheet("Error Messages",cell_overwrite_ok=True)
	errorsummary_sheet=  wb.add_sheet("Error Summary",cell_overwrite_ok=True)

if NO_QA_report==0:
	
	QAreportsheet=  wb.add_sheet("QA report",cell_overwrite_ok=True)

#Counters for row number for each result parameters such as evm, power etc.
evmcounter		=	0
evmbasecounter  =   1 
evm_num         =   0
rxcounter		=	0
rx_num          =   0
rxbasecounter   =   1
powercounter	=	0
powerbasecounter=   1
power_num       =   0
timecounter     =   0
temp_power     =    0
rxfailcounter  = 0
evmfailcounter = 0
powerfailcounter = 0
evmpowerenable =0
negative=0
#Preparing Headers for Sheets
if  Measurement_flag==1:

	evmsheet.write(0,0,"TestID")
	evmsheet.write(0,1,"TestType")
	evmsheet.write(0,2,"Frequency MHz")
	evmsheet.write(0,3,"Data_Rate")
	evmsheet.write(0,4, "Bandwidth")
	evmsheet.write(0,5, "Packet_Width")
	evmsheet.write(0,6,"Antenna")
	evmsheet.write(0,7,"TX1 EVM_Value dB")
	evmsheet.write(0,8,"TX2 EVM_Value dB")
	evmsheet.write(0,9,"TX3 EVM_Value dB")
	evmsheet.write(0,10,"TX4 EVM_Value dB")
	evmsheet.write(0,11,"Upper Limit")
	evmsheet.write(0,12,"Lower Limit")
	evmsheet.write(0,13,"Target power dBm")
	evmsheet.write(0,14,"TX1 Power Average dBm")
	evmsheet.write(0,15,"TX2 Power Average dBm")
	evmsheet.write(0,16,"TX3 Power Average dBm")
	evmsheet.write(0,17,"TX4 Power Average dBm")
	evmsheet.write(0,18,"Upper Limit")
	evmsheet.write(0,19,"Lower Limit")
	

	rxsheet.write(0,0,"TestID")
	rxsheet.write(0,1,"TestType")
	rxsheet.write(0,2,"Frequency MHz")
	rxsheet.write(0,3,"Data_Rate")
	rxsheet.write(0,4, "Bandwidth")
	rxsheet.write(0,5, "Packet_Width")
	rxsheet.write(0,6,"Antenna")
	rxsheet.write(0,7,"RX sensitivity_value")
	rxsheet.write(0,8,"Upper Limit")
	rxsheet.write(0,9,"Lower Limit")

	powersheet.write(0,0,"TestID")
	powersheet.write(0,1,"TestType")
	powersheet.write(0,2,"Frequency MHz")
	powersheet.write(0,3,"Data_Rate")
	powersheet.write(0,4, "Bandwidth")
	powersheet.write(0,5, "Packet_Width")
	powersheet.write(0,6,"Antenna")
	powersheet.write(0,7,"TX1 Power Value dBm")
	powersheet.write(0,8,"TX2 Power Value dBm")
	powersheet.write(0,9,"TX3 Power Value dBm")
	powersheet.write(0,10,"TX4 Power Value dBm")
	powersheet.write(0,13,"Target Power dBm")
	powersheet.write(0,11,"Upper Limit")
	powersheet.write(0,12,"Lower Limit")

if Time_Data_flag	:
	timesheet.write(0,0,"RunID")
	timesheet.write(0,1,"Flow run time")
	timesheet.write(0,2,"Test function time")
	timesheet.write(0,3,"AVG Flow Run time")
	timesheet.write(0,4,"AVG Test function time")
	testtimesheet.write(0,0,"Test Item")

if Error_Messages_flag:
	errorsheet.write(0,0,"Run #")
	errorsheet.write(0,1,"Test Item Number")
	errorsheet.write(0,2,"Frequency")
	errorsheet.write(0,3,"Data_Rate")
	errorsheet.write(0,4,"Bandwidth")               
	errorsheet.write(0,5,"Packet_Width")               
	errorsheet.write(0,6,"Antenna")                 
	errorsheet.write(0,7,"Error Message")


	errorsummary_sheet.write(0,0,"Run #")
	errorsummary_sheet.write(0,1,"Limit Failures each run")
	errorsummary_sheet.write(0,2,"Total Runs failed on limit")
	errorsummary_sheet.write(0,3,"Functional Failures each run")
	errorsummary_sheet.write(0,4,"Total Runs Failed functionally")


if NO_QA_report==0:
	QAreportsheet.write(0,0,"RunID")
	QAreportsheet.write(0,1,"TestID")
	QAreportsheet.write(0,2,"Frequency")
	QAreportsheet.write(0,3,"Data_Rate")
	QAreportsheet.write(0,4,"Bandwidth")               
	QAreportsheet.write(0,5,"Packet_Width")               
	QAreportsheet.write(0,6,"Antenna") 
	QAreportsheet.write(0,7,"Message")
	QAreportsheet.write(0,8,"Difference dB")
	QAreportsheet.write(0,9,"Actual Values dB")
	QAmessagecounter=1

LimitEvm_Dict={'MCS0': -5, 'MCS1': -10,'MCS2': -13,'MCS3': -16,'MCS4': -19,'MCS5': -22,'MCS6': -25,'MCS7': -27,'MCS8': -30,'MCS9': -32,
				'OFDM-6': -5,'OFDM-9': -5,'OFDM-12': -5,'OFDM-18': -5,'OFDM-24': -5,'OFDM-36': -5,'OFDM-48': -5,'OFDM-54': -5,
				'DSSS-1': -10, 'DSSS-2': -10, 'CCK-11': -10, 'CCK-5.5':-10}
Limitrx_Dict={'MCS0': -82, 'MCS1': -81,'MCS2': -79,'MCS3': -77,'MCS4': -74,'MCS5': -70,'MCS6': -66,'MCS7': -65,'MCS8': -59,'MCS9': -55,
				'OFDM-6': -82,'OFDM-9': -79,'OFDM-12': -79,'OFDM-18': -77,'OFDM-24': -74,'OFDM-36': -70,'OFDM-48': -66,'OFDM-54': -65,
				'DSSS-1': -80, 'DSSS-2': -80, 'CCK-11': -80, 'CCK-5.5':-80}				
	
# freezeTopLine(evmsheet)



collect_data=0
collect_time=0
runID=0 #tells current number of run executed
# Matrix form for data collection
# row represents values collected in 1 run for different test items.
# each row is stored in matrix at index (runId-1)

evm_matrix=np.zeros((1000,1000,4))
power_matrix=np.zeros((1000,1000,4))
evmpower_matrix=np.zeros((1000,1000,4))
rx_matrix=np.zeros((1000,1000))

time_rowarray=[]
time_colarray=[]

evm_average={}
power_average={}
rx_average={}
time_average={}
evmpower_average={}
flowtime_average=0
testtime_average=0
flowtime_sum=0	
testtime_sum=0
antenna=[]
# NEW start
firstID=0
errorcounter=0
current_test_function	=	""
current_test_num		=	0
# NEW end

#Reference numbers for test items to be checked
ref_rx_number=0
ref_evm_number=0
ref_power_number=0
time_sum=0
perenable=0
for line in f:
	#Section to collect Run ID, reset Averaging counters
	if "*  F A I L  *" in line or "*  P A S S  *" in line:
		print "Now Processing Run Number" ,runID 
		collect_data=0 # Flag that prevents data collection during Test summary section
		
		collect_time = Time_Data_flag
		
		 
	
			
		
		
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
			evmcounter=0
			rxcounter=0
			powercounter=0
			timecounter=0
			time_colarray.append(time_rowarray)
			time_rowarray=[]
		
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
		
	
			
		if 'TX_VERIFY_EVM' in line :  #collect the input parameters for evm test items
			evmcounter=evmcounter+1
			ref_evm_number=current_test_num
			antenna=[]
			
			strings=line.strip()
			col=strings.split()
			type='EVM_Test'
			freq=int(col[1])
			data_rate=col[2]
			bandwidth=col[3]
			packet_format=[]
			
			if 'TX1' in line:
				antenna.append('TX1')
			if 'TX2' in line:
				antenna.append('TX2')
			if 'TX3' in line:
				antenna.append('TX3')
			if 'TX4' in line:
				antenna.append('TX4')
			if Measurement_flag==1:
				evmsheet.write(evmcounter,1,type)
				evmsheet.write(evmcounter,2,freq)
				evmsheet.write(evmcounter,3,data_rate)
				evmsheet.write(evmcounter,4,bandwidth)
				evmsheet.write(evmcounter,5,packet_format)
				evmsheet.write(evmcounter,6,antenna)
				evmsheet.write(evmcounter,0,current_test_num)
				
	
			
			
		if 'EVM_DB_AVG_' in line and ref_evm_number==current_test_num: #collect output result for evm values
			
						
			value=line.strip()
			col=value.split()
			evm_values=float(col[2])
			
			up_limit=(col[4].strip( '(), ' ))
			lo_limit=(col[5].strip( '(), ' ))
			if 'EVM_DB_AVG_S1' in line:
				evm_matrix[runID-1,current_test_num-1,0]=evm_values
				ant=0
			if 'EVM_DB_AVG_S2' in line:
				evm_matrix[runID-1,current_test_num-1,1]=evm_values
				ant=1
			if 'EVM_DB_AVG_S3' in line:
				evm_matrix[runID-1,current_test_num-1,2]=evm_values
				ant=2
			if 'EVM_DB_AVG_S4' in line:
				evm_matrix[runID-1,current_test_num-1,3]=evm_values
				ant=3
				
			if data_rate in LimitEvm_Dict.keys() and EVM_QA_report==1:
							limit=float(LimitEvm_Dict[data_rate])
							
							if (float(evm_values)>limit):
								
								QAreportsheet.write( QAmessagecounter,7,'EVM Limit failed by') 
								QAreportsheet.write( QAmessagecounter,8,float(evm_values-LimitEvm_Dict[data_rate]))
								QAreportsheet.write( QAmessagecounter,9,evm_values)
								QAreportsheet.write(QAmessagecounter,0,runID)
								QAreportsheet.write(QAmessagecounter,1,current_test_num)
								QAreportsheet.write(QAmessagecounter,2,freq)
								QAreportsheet.write(QAmessagecounter,3,data_rate)
								QAreportsheet.write(QAmessagecounter,4,bandwidth)
								QAreportsheet.write(QAmessagecounter,6,antenna)
								QAreportsheet.write(QAmessagecounter,5,packet_format)
								evmfailcounter+=1
								
								#w.write('Limit failed for EVM at '+repr(freq)+' '+repr(data_rate)+' '+repr(packet_format)+' by '+repr(float(float(evm_values)-LimitEvm_Dict[data_rate]))+' dB in  Run# '+repr(runID)+' on '+repr(current_test_num)+' Test ID\n')
								QAmessagecounter+=1
			
			
			evm_sum=0
			if Measurement_flag==1:
				if runID==firstID:
								
					evmsheet.write(evmcounter,11,(up_limit))
					evmsheet.write(evmcounter,12,(lo_limit))
					evmsheet.write(evmcounter,7+ant,evm_values)
					
				else:
						
					for x in range(1,runID):
						if evm_matrix[x-1][current_test_num-1][ant]==0:
							negative+=1
							
						evm_sum+=(evm_matrix[x-1][current_test_num-1][ant])
					
					evm_sum+=float(evm_values)
					evm_average=evm_sum/(runID-negative)
					negative=0		
					
					evmsheet.write(evmcounter,7+ant,evm_average)
		if 'POWER_DBM_RMS_AVG_S' in line and ref_evm_number==current_test_num: #collect output result for power values
			#temp_power=TX_power[i]
			value=line.strip()
			col=value.split()
			
			evmpower_values=float(col[2])
			up_limit=col[4].strip( '(), ' )
			lo_limit=col[5].strip( '(), ' )
			if 'POWER_DBM_RMS_AVG_S1' in line:
				evmpower_matrix[runID-1,current_test_num-1,0]=evmpower_values
				ant=0
			if 'POWER_DBM_RMS_AVG_S2' in line:
				ant=1
				evmpower_matrix[runID-1,current_test_num-1,1]=evmpower_values
			if 'POWER_DBM_RMS_AVG_S3' in line:
				ant=2
				power_matrix[runID-1,current_test_num-1,2]=evmpower_values
			if 'POWER_DBM_RMS_AVG_S4' in line:
				ant=3
				evmpower_matrix[runID-1,current_test_num-1,3]=evmpower_values
			#debug
			
				
			if (((evmpower_values-Target_power)> 1.5 or (evmpower_values-Target_power)< -1.5)) and evmpowerenable==1 and Power_QA_report==1:
								
				font0=Font()
				font0.bold = True	
				style0 = XFStyle()
				style0.font = font0
				powerfailcounter+=1
				QAreportsheet.write( QAmessagecounter,7,'Power Difference from EVM test is') 
				QAreportsheet.write( QAmessagecounter,8,evmpower_values-temp_power)
				QAreportsheet.write( QAmessagecounter,9,evmpower_values)
				QAreportsheet.write(QAmessagecounter,0,runID)
				QAreportsheet.write(QAmessagecounter,1,current_test_num)
				QAreportsheet.write(QAmessagecounter,2,freq)
				QAreportsheet.write(QAmessagecounter,3,data_rate)
				QAreportsheet.write(QAmessagecounter,4,bandwidth)
				QAreportsheet.write(QAmessagecounter,6,antenna)
				QAreportsheet.write(QAmessagecounter,5,packet_format)
				QAmessagecounter+=1
			
			evmpower_sum=0
			if Measurement_flag==1:
				if runID==firstID:
								
					evmsheet.write(evmcounter,18,up_limit)
					evmsheet.write(evmcounter,19,lo_limit)
					evmsheet.write(evmcounter,14+ant,evmpower_values)
					
				else:
					for x in range(1,runID):
						
						if evmpower_matrix[x-1][current_test_num-1][ant]==0:
							negative+=1
								
						evmpower_sum+=(evmpower_matrix[x-1][current_test_num-1][ant])
						
					evmpower_sum+=float(evmpower_values)
					evmpower_average=evmpower_sum/(runID-negative)
					negative=0		
					evmsheet.write(evmcounter,14+ant,evmpower_average)	
					

		
		if 'RX_SWEEP_PER' in line :  #collect the input parameters for RX test
			rxcounter=rxcounter+1
			ref_rx_number=current_test_num
			antenna=[]
		
			strings=line.strip()
			col=strings.split()
			type='RX_Sensitivity_test'
			freq=col[1]
			data_rate=col[2]
			bandwidth=col[3]
			packet_format=[]
			if 'RX1' in line:
				antenna.append('RX1')
			if 'RX2' in line:
				antenna.append('RX2')
			if 'RX3' in line:
				antenna.append('RX3')
			if 'RX4' in line:
				antenna.append('RX4')
			if Measurement_flag==1:
				rxsheet.write(rxcounter,1,type)
				rxsheet.write(rxcounter,2,freq)
				rxsheet.write(rxcounter,3,data_rate)
				rxsheet.write(rxcounter,4,bandwidth)
				rxsheet.write(rxcounter,5,packet_format)
				rxsheet.write(rxcounter,6,antenna)
				rxsheet.write(rxcounter,0,current_test_num)
		
			
			
		if 'SENS_POWER_LEVEL_DBM' in line and ref_rx_number==current_test_num: #collect output result for RX values
			
			value=line.strip()
			col=value.split()
			rx_values=float(col[2])
			
			up_limit=col[4].strip( '(), ' )
			lo_limit=col[5].strip( '(), ' )
			
			if data_rate in Limitrx_Dict.keys() and RX_QA_report==1:
							limit=float(Limitrx_Dict[data_rate])
							
							if (float(rx_values)>limit):
								
								QAreportsheet.write( QAmessagecounter,7,'RX Sensitivity limit failed by') 
								QAreportsheet.write( QAmessagecounter,8,float(rx_values-Limitrx_Dict[data_rate]))
								QAreportsheet.write( QAmessagecounter,9,rx_values)
								QAreportsheet.write(QAmessagecounter,0,runID)
								QAreportsheet.write(QAmessagecounter,1,current_test_num)
								QAreportsheet.write(QAmessagecounter,2,freq)
								QAreportsheet.write(QAmessagecounter,3,data_rate)
								QAreportsheet.write(QAmessagecounter,4,bandwidth)
								QAreportsheet.write(QAmessagecounter,6,antenna)
								QAreportsheet.write(QAmessagecounter,5,packet_format)
								evmfailcounter+=1
								
								#w.write('Limit failed for EVM at '+repr(freq)+' '+repr(data_rate)+' '+repr(packet_format)+' by '+repr(float(float(evm_values)-LimitEvm_Dict[data_rate]))+' dB in  Run# '+repr(runID)+' on '+repr(current_test_num)+' Test ID\n')
								QAmessagecounter+=1
			
			
			rx_sum=0
			if Measurement_flag==1:
				if runID==firstID:
								
					rxsheet.write(rxcounter,8,up_limit)
					rxsheet.write(rxcounter,9,lo_limit)
							
					rxsheet.write(rxcounter,7,rx_values)
				else:
				
					for x in range(1,runID):
						if rx_matrix[x-1][current_test_num-1]==0:
								negative+=1
								
						rx_sum+=(rx_matrix[x-1][current_test_num-1])
						
					rx_sum+=float(rx_values)
					rx_average=rx_sum/(runID-negative)
					negative=0		
					rxsheet.write(rxcounter,7,rx_average)
		#code from here is Debug		
		if "POWER_LEVELS" in line:
			perenable=0		
		if perenable==1:
			value=line.strip()
			col=value.split()
			per_values=float(col[0])
			percounter+=1
			if Measurement_flag==1:	
				if runID==firstID:
							
					rxsheet.write(rxcounter,9+percounter,per_values)
				
				
		if "PER_VALUES               : " in line and ref_rx_number==current_test_num:		
			value=line.strip()
			col=value.split()
			per_values=float(col[2])
			percounter=1
			perenable=1
			
			if Measurement_flag==1:
				if runID==firstID:
							
					rxsheet.write(rxcounter,9+percounter,per_values)
			
			
			
		if 'TX_VERIFY_POWER' in line:  #collect the input parameters for Power test
			powercounter=powercounter+1
			ref_power_number=current_test_num
			antenna=[]
			
			strings=line.strip()
			col=strings.split()
			type='Power_measurement'
			freq=int(col[1])
			data_rate=col[2]
			bandwidth=col[3]
			packet_format=[]
			if 'TX1' in line:
				antenna.append('TX1')
			if 'TX2' in line:
				antenna.append('TX2')
			if 'TX3' in line:
				antenna.append('TX3')
			if 'TX4' in line:
				antenna.append('TX4')
			if Measurement_flag==1:
				powersheet.write(powercounter,1,type)
				powersheet.write(powercounter,2,freq)
				powersheet.write(powercounter,3,data_rate)
				powersheet.write(powercounter,4,bandwidth)
				powersheet.write(powercounter,5,packet_format)
				powersheet.write(powercounter,6,antenna)
				powersheet.write(powercounter,0,current_test_num)
			
		

			
		if 'POWER_DBM_RMS_MAX_VSA' in line and ref_power_number==current_test_num: #collect output result for power values
			
			value=line.strip()
			col=value.split()
			power_values=float(col[2])
			up_limit=col[4].strip( '(), ' )
			lo_limit=col[5].strip( '(), ' )
			
			if 'POWER_DBM_RMS_MAX_VSA1' in line:
				power_matrix[runID-1,current_test_num-1,0]=power_values
				ant=0
			if 'POWER_DBM_RMS_MAX_VSA2' in line:
				ant=1
				power_matrix[runID-1,current_test_num-1,1]=power_values
			if 'POWER_DBM_RMS_MAX_VSA3' in line:
				ant=2
				power_matrix[runID-1,current_test_num-1,2]=power_values
			if 'POWER_DBM_RMS_MAX_VSA4' in line:
				ant=3
				power_matrix[runID-1,current_test_num-1,3]=power_values
				
			power_sum=0
			if Measurement_flag==1:
				if runID==firstID:
								
					powersheet.write(powercounter,9,up_limit)
					powersheet.write(powercounter,8,lo_limit)
					powersheet.write(powercounter,7+ant,power_values)
				else:
				
					for x in range(1,runID):
						if power_matrix[x-1][current_test_num-1][ant]==0:
							negative+=1
						
						power_sum+=(power_matrix[x-1][current_test_num-1][ant])
				
					power_sum+=float(power_values)
					power_average=power_sum/(runID-negative)
					negative=0		
				
				
					powersheet.write(powercounter,7+ant,power_average)	
				
		if 'TX_POWER_DBM                   :' in line and ref_power_number==current_test_num: #collect Target Power values for Power 
			
			
			if runID==firstID:
				
				value=line.strip()
				col=value.split()
				Target_power=float(col[2])
				temp_power=Target_power
				if Measurement_flag==1:	
					powersheet.write(powercounter,10,Target_power)
		if 'TX_POWER_DBM ' in line and ref_evm_number==current_test_num: #collect Target Power values for EVM  
							
			if runID==firstID:
				value=line.strip()
				col=value.split()
				Target_power=float(col[2])
				if Measurement_flag==1:	
					evmsheet.write(evmcounter,13,Target_power)
				temp_power=Target_power
				
		if 'ERROR_MESSAGE ' in line and Error_Messages_flag:
	
			if 'return error' in line:
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
				
				errorsheet.write(errorcounter,7,error_message)
				errorsheet.write(errorcounter,0,runID)
				errorsheet.write(errorcounter,1,current_test_num)
				errorsheet.write(errorcounter,2,freq)
				errorsheet.write(errorcounter,4,bandwidth)
				errorsheet.write(errorcounter,6,antenna)
				errorsheet.write(errorcounter,5,packet_format[:])
				errorsheet.write(errorcounter,3,data_rate)
				
	if collect_time==1:
		
		col=[ ]
		timecounter+=1
		strings=line.strip()
		temp=strings.split()
		if 'Total Run(s)' in line:
			collect_time=0
		if len(temp)>0:
			Iteminfo=temp[0]
		
		if len(temp)>6:
			
			col=temp[6]
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
			
		testtimesheet.write(timecounter,0,Iteminfo)
		
		if runID<=254:	
			testtimesheet.write(timecounter,runID,time_values)
			testtimesheet.write(0,runID,runID)
			
		time_rowarray.append(float(time_values))
		time_sum=0
			
	
		for i in range(1,runID):
			
			if len(time_colarray)>1:
				if runID>49:
					print i,timecounter
				time_sum+=(time_colarray[i-1][timecounter-1])	
				
		time_sum+=float(time_values)
		time_average=time_sum/(runID)
		if runID<=254:	
			testtimesheet.write(timecounter,runID+1,time_average)
			testtimesheet.write(0,runID+1,'Time_average')
		else:
			testtimesheet.write(timecounter,255,time_average)
			testtimesheet.write(0,255,'Time_average')
		
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
	rxsheet.col(1).width = 0x0d00			
	powersheet.col(1).width = 0x1f00
if Time_Data_flag	:
	timesheet.col(1).width	= 0x0fff
	timesheet.col(2).width	= 0x0fff
	timesheet.col(3).width	= 0x0fff
	timesheet.col(4).width	= 0x0fff
	testtimesheet.col(0).width= 0x1f00
				
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

