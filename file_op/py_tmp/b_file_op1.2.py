#os.rename(oldname, newname) # rename a file or folder
#os.remove() removes a file.

#os.rmdir() removes an empty directory.

#shutil.rmtree() deletes a directory and all its contents.

#pathlib.Path.unlink() removes the file or symbolic link.

#pathlib.Path.rmdir() removes the empty directory
#
#By design, rmtree fails on folder trees containing read-only files.
#If you want the folder to be deleted regardless of whether
#it contains read-only files, then use
shutil.rmtree('/folder_name', ignore_errors=True)
import os
os.makedirs("dir\dir1")
#os.mkdir("dir\dirs") # error: mkdir can't make nested directory
#os.path.abspath()
#os.path.split
os.path.abspath("b_file_op2.py")# give full path :  'C:\\Users\\jsun\\Documents\\PyProj\\file_op\\b_file_op2.py'
(f_path, file_name) = os.path.split(fpath)
print("f_path-->{}, file_name-->{} ".format(f_path,file_name) )
a = os.listdir(f_path)

"""
To find files in immediate subdirectories: single '*' is for immediate subdiroor
configfiles = glob.glob(r'C:\Users\sam\Desktop\*\*.txt')
C:\Users\jsun\Documents\PyProj\file_op\logoutput\log1.txt
C:\Users\jsun\Documents\PyProj\file_op\logoutput\log2.txt
C:\Users\jsun\Documents\PyProj\file_op\logoutput\log3.txt
C:\Users\jsun\Documents\PyProj\file_op\logoutput\logOutput.txt
C:\Users\jsun\Documents\PyProj\file_op\temp\log3.txt

For a recursive version that traverse all subdirectories, you could use ** and pass recursive=True since Python 3.5:
configfiles = glob.glob(r'C:\Users\sam\Desktop\**\*.txt', recursive=True)
"C:\Program Files\Python36\python.exe" C:/Users/jsun/Documents/PyProj/file_op/file_test.py
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\MUMU\LogRXRX\logOutput.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\MUMU\LogRXRX\Log_all.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\MUMU\LogRXTX\logOutput.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\MUMU\LogRXTX\Log_all.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\MUMU\Log_TXRX\logOutput.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\MUMU\Log_TXRX\Log_all.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\MUMU\Log_TXTX\logOutput.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\MUMU\Log_TXTX\Log_all.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\MUSU\LogMUSU_RX_RXTX\logOutput.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\MUSU\LogMUSU_RX_RXTX\Log_all.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\MUSU\MUSU_TX_TXRX\logCurrent.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\MUSU\MUSU_TX_TXRX\logOutput.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\MUSU\MUSU_TX_TXRX\Log_all.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\SUMU\LogSUMU\logOutput.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\SUMU\LogSUMU\Log_all.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\SUSU\logOutput.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\SUSU\Log_all.txt
C:\Users\jsun\Documents\PyProj\file_op\logoutput\log1.txt
C:\Users\jsun\Documents\PyProj\file_op\logoutput\log2.txt
C:\Users\jsun\Documents\PyProj\file_op\logoutput\log3.txt
C:\Users\jsun\Documents\PyProj\file_op\logoutput\logOutput.txt
C:\Users\jsun\Documents\PyProj\file_op\temp\log3.txt
"""
filesrch = os.path.join(os.getcwd(),"**","*.txt")
glob.glob(filesrch, recursive=True)

from glob import glob
import os
schfile = os.path.join(os.getcwd(),"**","*.txt")
a = glob(schfile,recursive=True)
for i in a:
    print(i)