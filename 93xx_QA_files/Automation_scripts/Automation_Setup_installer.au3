; Get the complete path by joining arguments for path of each setup here:
$vc2005_exe = "C:\Users\litepoint\Desktop\Package\IQfact+_QCA_6174_3.2.1.RC4\VC2005\vcredist_x86.exe"
$vc2008_exe = "C:\Users\litepoint\Desktop\Package\IQfact+_QCA_6174_3.2.1.RC4\VC2008\vcredist_x86.exe"
$MCR_exe = "C:\Users\litepoint\Desktop\Package\IQfact+_QCA_6174_3.2.1.RC4\MCR79\MCRInstaller.exe"

; Run setup for Visual C++ 2005
BlockInput(0)
RunWait($vc2005_exe)
;Sleep(100000) ;Add a delay of 10 seconds before the next step

; Run setup for Visual C++ 2008 Redistributable
Run($vc2008_exe)

WinWaitActive("Microsoft Visual C++ 2008 Redistributable Setup", "Select one of the options below: ")
Sleep(500)
ControlClick("Microsoft Visual C++ 2008 Redistributable Setup","",610)
Sleep(500)
Send("!r")
Sleep(500)
WinWaitActive("Microsoft Visual C++ 2008 Redistributable Setup", "Select one of the options below: ")
Sleep(500)
ControlClick("Microsoft Visual C++ 2008 Redistributable Setup","",610)
Sleep(500)
Send("!r")

ControlClick("Microsoft Visual C++ 2008 Redistributable Setup","",289)

WinWaitActive("Microsoft Visual C++ 2008 Redistributable Setup", "has been successfully repaired.")
ControlClick("Microsoft Visual C++ 2008 Redistributable Setup","",2)
;Send("!f")
;BlockInput(0)
Sleep(2000) ;Add a delay of 5 seconds before the next step

;Run the setup of MATLAB Compiler Runtime 7.9
Run($MCR_exe)
;BlockInput(1)
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

Sleep(10000) ;Add a delay of 10 seconds before the next step

BlockInput(1)