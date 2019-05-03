#cs ----------------------------------------------------------------------------
 AutoIt Version: 3.3.8.1
 Author:         ADITYA KARVA
 Date: 			 11/20/2013
 Version: 		 1.0

 Update Log:
 Last Updated:  11/22/2013
 Updated by:    ADITYA KARVA
 Change Log:    Added variables to be read from command line instead of hard coding for path installation.

 Script Function:
	To Install Microsoft Visual C++ and MATLAB Compiler Runtime 7.9 setup before package installation

#ce ----------------------------------------------------------------------------

; Script Start - Add your code below here
AutoItSetOption ("TrayIconDebug", 1);0-off

;Declare your variables here:
Dim $vc2005 = "\VC2005\vcredist_x86.exe" ;Path of the Visual C++ 2005 Executable file
Dim $vc2008 = "\VC2008\vcredist_x86.exe" ;Path of the Visual C++ 2008 Executable file
Dim $MCR = "\MCR79\MCRInstaller.exe" ;Path of the MATLAB Compiler Runtime 7.9 Executable file

; Get the complete path by joining arguments for path of each setup here:
$vc2005_exe = & $CmdLine[1]$vc2005 ;Join the path of the package with VC2005 exe path
$vc2008_exe = & $CmdLine[1]$vc2008 ;Join the path of the package with VC2007 exe path
$MCR_exe = & $CmdLine[1]$MCR ;Join the path of package with MCR7.9 exe path

; Run setup for Visual C++ 2005
Run($vc2005_exe)
Sleep(35000) ;Add a delay of 10 seconds before the next step

; Run setup for Visual C++ 2008 Redistributable
Run($vc2008_exe)
WinWaitActive("Microsoft Visual C++ 2008 Redistributable Setup", "Select one of the options below: ")

ControlClick("Microsoft Visual C++ 2008 Redistributable Setup","","[CLASS:Button; INSTANCE:9]")
;Send("!r") ;Choose the repair option (ALT+r)
Sleep(2000)
Send("!n") ;Click on "Next" button (ALT+n)
WinWaitActive("Microsoft Visual C++ 2008 Redistributable Setup", "It is highly recommended that you download")
Send("!f") ;Click "Finish" button (ALT+f)
Sleep(10000) ;Add a delay of 5 seconds before the next step
; Run Matlab Runtime 7.9
Run($MCR_exe)
WinWaitActive("Choose Setup Language", "Select the language")
send("{ENTER}")
WinWaitActive("InstallShield Wizard", "Click OK to begin installing these requirements")
Send("!i")
WinWaitActive("MATLAB(R) Compiler Runtime 7.9 - InstallShield Wizard", "will allow you to modify, repair, or remove")
Send("!n") ;Click on "Next" button (ALT+n)
WinWaitActive("MATLAB(R) Compiler Runtime 7.9 - InstallShield Wizard", "Modify, repair, or remove the program")
Send("!n") ;Click on "Next" button (ALT+n)
WinWaitActive("MATLAB(R) Compiler Runtime 7.9 - InstallShield Wizard", "Click on an icon in the list")
Send("!n")
WinWaitActive("MATLAB(R) Compiler Runtime 7.9 - InstallShield Wizard", "Click Install to begin the installation")
send("!i")
WinWaitActive("MATLAB(R) Compiler Runtime 7.9 - InstallShield Wizard", "The InstallShield Wizard has successfully")
Send("!f") ;Click on "Finish" button (ALT+f)
Sleep(2000)

