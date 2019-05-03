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
Sleep(10000) ;Add a delay of 10 seconds before the next step

; Run setup for Visual C++ 2008 Redistributable
Run($vc2008_exe)
BlockInput(1)
WinWaitActive("Microsoft Visual C++ 2008 Redistributable Setup", "Select one of the options below: ")
Sleep(2000)
;ControlClick("Microsoft Visual C++ 2008 Redistributable Setup","","610")
Sleep(2000)
;ControlClick("Microsoft Visual C++ 2008 Redistributable Setup","","289")

WinWaitActive("Microsoft Visual C++ 2008 Redistributable Setup", "has been successfully repaired.")
ControlClick("Microsoft Visual C++ 2008 Redistributable Setup","","2")
BlockInput(0)
Sleep(5000) ;Add a delay of 5 seconds before the next step

;Run the setup of MATLAB Compiler Runtime 7.9
Run($MCR_exe)
BlockInput(1)
WinWaitActive("Choose Setup Language", "the language for this installation from")
Sleep(1000)
ControlClick("Choose Setup Language", "OK", 1006) ;Click on "OK" button for the Language selection screen
WinWaitActive("MATLAB(R) Compiler Runtime 7.9 - InstallShield Wizard", "allow you to modify, repair, or remove MATLAB(R) Compiler Runtime 7.9") ; Walking throught the MCR 7.9 setup - Step 1
Sleep(1000)
Send("!n") ;Click on "Next" button (ALT+n)
WinWaitActive("MATLAB(R) Compiler Runtime 7.9 - InstallShield Wizard", "Modify, repair, or remove the program.") ; Walking throught the MCR 7.9 setup - Step 2
Sleep(1000)
Send("!n") ;Click on "Next" button (ALT+n)
WinWaitActive("MATLAB(R) Compiler Runtime 7.9 - InstallShield Wizard", "This feature requires 0KB on your hard drive") ; Walking throught the MCR 7.9 setup - Step 3
Sleep(1000)
Send("!n") ;Click on "Next" button (ALT+n)
WinWaitActive("MATLAB(R) Compiler Runtime 7.9 - InstallShield Wizard", "Ready to Modify the Program") ; Walking throught the MCR 7.9 setup - Step 4
Sleep(1000)
Send("!i") ;Click on "Install" button (ALT+i)
WinWaitActive("MATLAB(R) Compiler Runtime 7.9 - InstallShield Wizard", "The InstallShield Wizard has successfully installed MATLAB(R) Compiler Runtime 7.9. ") ; Walking throught the MCR 7.9 setup - Step 5 (Final Step)
Sleep(1000)
Send("!f") ;Click on "Finish" button (ALT+f)
BlockInput(0)
Sleep(10000) ;Add a delay of 10 seconds before the next step

