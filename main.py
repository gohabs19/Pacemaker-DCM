from tkinter import *
import windows#Import windows.py

loginInfoFile='pacemakerLogins.txt'#Create a variable to store the pacemakerLogins file, containing the login credentials
#of each pacemaker user.
inputSettingsFile='inputModeSettings.txt'#File storing the past input mode settings

global root
root=Tk()#Create the root window that will be used

def main():
    start = windows.windowsStart()
    start.welcomeWindow(root)
    root.mainloop()

if __name__=="__main__":
   main()
