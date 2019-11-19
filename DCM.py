from tkinter import *
#from PIL import ImageTk, Image
import random
import os

###Data for each of the pacing modes###
#NOTE: These must be stored globally so that they may be accessed between windows
#NOTE: -1 denotes an area that will not be editable, as it is not associated with said mode.
#As a result of this, it will be greyed out and not have the ability to be edited when shown
#on the DCM.
#Data order:
AOOData=[0,0,0,0,-1,-1,-1,0]
VOOData=[0,0,-1,-1,0,0,0,-1]
AAIData=[0,0,0,0,-1,-1,-1,0]
VVIData=[0,0,-1,-1,0,0,0,-1]

global root
root=Tk()

loginInfoFile='pacemakerLogins.txt'#Create a variable to store the pacemakerLogins file, containing the login credentials
#of each pacemaker user.

def welcome():
 root.title('Pacemaker DCM')#Window name
 welcomeLabel=Label(root,text="Welcome to the pacemaker DCM! Please enter your login info!")#Welcome message
 welcomeLabel.grid(sticky=N)#Assigns label to border
#End of welcome func

def userInterface():
 def parameterInputData(windowName):
     parameterInputDataInterface=Tk()
     parameterInputDataInterface.title(windowName)

     localInputData=[]
     if (windowName == 'AOO'):
         localInputData=AOOData
     elif (windowName == 'VOO'):
         localInputData=VOOData
     elif (windowName == 'AAI'):
         localInputData=AAIData
     elif (windowName == 'VVI'):
         localInputData=VVIData

     ###Input adjustments###
     # Lower Rate Limit
     lowerRateLimitInputLabel = Label(parameterInputDataInterface, text='Lower Rate Limit')
     lowerRateLimitInputLabel.grid(row=4, column=1)
     lowerRateLimitInput = Entry(parameterInputDataInterface)
     lowerRateLimitInput.grid(row=5, column=1)
     if (localInputData[0]==(-1)):
         lowerRateLimitInput.configure(state='disabled')
     else:
         lowerRateLimitInput.insert(END, localInputData[0])
     # Upper Rate Limit
     upperRateLimitInputLabel = Label(parameterInputDataInterface, text='Upper Rate Limit')
     upperRateLimitInputLabel.grid(row=4, column=2)
     upperRateLimitInput = Entry(parameterInputDataInterface)
     upperRateLimitInput.grid(row=5, column=2)
     if (localInputData[1] == (-1)):
         upperRateLimitInput.configure(state='disabled')
     else:
         upperRateLimitInput.insert(END, localInputData[1])
     # Atrial Amplitude
     atrialAmplitudeInputLabel = Label(parameterInputDataInterface, text='Atrial Amplitude')
     atrialAmplitudeInputLabel.grid(row=4, column=3)
     atrialAmplitudeInput = Entry(parameterInputDataInterface)
     atrialAmplitudeInput.grid(row=5, column=3)
     if (localInputData[2] == (-1)):
         atrialAmplitudeInput.configure(state='disabled')
     else:
         atrialAmplitudeInput.insert(END, localInputData[2])
     # Atrial Pulse Width
     atrialPulseWidthInputLabel = Label(parameterInputDataInterface, text='Atrial Pulse Width')
     atrialPulseWidthInputLabel.grid(row=4, column=4)
     atrialPulseWidthInput = Entry(parameterInputDataInterface)
     atrialPulseWidthInput.grid(row=5, column=4)
     if (localInputData[3] == (-1)):
         atrialPulseWidthInput.configure(state='disabled')
     else:
         atrialPulseWidthInput.insert(END, localInputData[3])
     # Ventricular Amplitude
     ventricularAmplitudeInputLabel = Label(parameterInputDataInterface, text='Ventricular Amplitude')
     ventricularAmplitudeInputLabel.grid(row=6, column=1)
     ventricularAmplitudeInput = Entry(parameterInputDataInterface)
     ventricularAmplitudeInput.grid(row=7, column=1)
     if (localInputData[4] == (-1)):
         ventricularAmplitudeInput.configure(state='disabled')
     else:
         ventricularAmplitudeInput.insert(END, localInputData[4])
     # Ventricular Pulse Width
     ventricularPulseWidthInputLabel = Label(parameterInputDataInterface, text='Ventricular Pulse Width')
     ventricularPulseWidthInputLabel.grid(row=6, column=2)
     ventricularPulseWidthInput = Entry(parameterInputDataInterface)
     ventricularPulseWidthInput.grid(row=7, column=2)
     if (localInputData[5] == (-1)):
         ventricularPulseWidthInput.configure(state='disabled')
     else:
         ventricularPulseWidthInput.insert(END, localInputData[5])
     # VRP
     VRPInputLabel = Label(parameterInputDataInterface, text='VRP')
     VRPInputLabel.grid(row=6, column=3)
     VRPInput = Entry(parameterInputDataInterface)
     VRPInput.grid(row=7, column=3)
     if (localInputData[6] == (-1)):
         VRPInput.configure(state='disabled')
     else:
         VRPInput.insert(END, localInputData[6])
     # ARP
     ARPInputLabel = Label(parameterInputDataInterface, text='ARP')
     ARPInputLabel.grid(row=6, column=4)
     ARPInput = Entry(parameterInputDataInterface)
     ARPInput.grid(row=7, column=4)
     if (localInputData[7] == (-1)):
         ARPInput.configure(state='disabled')
     else:
         ARPInput.insert(END, localInputData[7])

     def updateInputModeInfo():
         newInputModeInfo=[lowerRateLimitInput.get(),upperRateLimitInput.get(),atrialAmplitudeInput.get(),atrialPulseWidthInput.get(),ventricularAmplitudeInput.get(),ventricularPulseWidthInput.get(),VRPInput.get(),ARPInput.get()]
         #The information applied to the selected input mode once the update button is pressed

         #Get the global arrays of input info
         global AOOData
         global VOOData
         global AAIData
         global VVIData

         if (windowName=='AOO'):
             AOOData=newInputModeInfo
         elif (windowName=='VOO'):
             VOOData=newInputModeInfo
         elif (windowName=='AAI'):
             AAIData=newInputModeInfo
         elif (windowName=='VVI'):
             VVIData=newInputModeInfo

     def importSettings():
         # Get the global arrays of input info
         global AOOData
         global VOOData
         global AAIData
         global VVIData

         inputModeSettingsSheet='inputModeSettings.txt'
         with open(inputModeSettingsSheet) as settingsData:
             settings=settingsData.readlines()
             #previousData=[]
             importData=''
             def parseToInt(data):#Convert parsed data from individual char values to ints
                 for i in range(len(data)):
                     data[i]=int(data[i])
                 return data

             if (windowName == 'AOO'):
                 #previousData=AOOData[:]#Stores a copy of the previous AOOData list incase the user wants to revert when prompted
                 importData = settings[0].split(',')
                 #importData=parseToInt(importData)
                 #AOOData = importData[:]
             elif (windowName == 'VOO'):
                 #previousData=VOOData[:]
                 importData = settings[1].split(',')
                 #importData=parseToInt(importData)
                 #VOOData=importData[:]
             elif (windowName == 'AAI'):
                 #previousData = AAIData[:]
                 importData = settings[2].split(',')
                 #importData=parseToInt(importData)
                 #AAIData=importData[:]
             elif (windowName == 'VVI'):
                 #previousData=VVIData[:]
                 importData=settings[3].split(',')
                 #importData=parseToInt(importData)
                 #VVIData=importData[:]
             #print(AOOData, importData, type(importData[0]), type(1))

             importData = parseToInt(importData)

             lowerRateLimitInput.delete(0,END)
             lowerRateLimitInput.insert(END, importData[0])
             upperRateLimitInput.delete(0, END)
             upperRateLimitInput.insert(END, importData[1])
             atrialAmplitudeInput.delete(0, END)
             atrialAmplitudeInput.insert(END, importData[2])
             atrialPulseWidthInput.delete(0, END)
             atrialPulseWidthInput.insert(END, importData[3])
             ventricularAmplitudeInput.delete(0, END)
             ventricularAmplitudeInput.insert(END, importData[4])
             ventricularPulseWidthInput.delete(0, END)
             ventricularPulseWidthInput.insert(END, importData[5])
             VRPInput.delete(0, END)
             VRPInput.insert(END, importData[6])
             ARPInput.delete(0, END)
             ARPInput.insert(END, importData[7])

     updateButton = Button(parameterInputDataInterface, text='Update Info', fg='Black',command=updateInputModeInfo)#Also need to add command so that it actually updates this info
     updateButton.grid(row=8, column=1)

     importButton = Button(parameterInputDataInterface, text='Import Settings',fg='Black',command=importSettings)
     importButton.grid(row=8, column=2)

 def AOOWindow():
     parameterInputData('AOO')

 def VOOWindow():
     parameterInputData('VOO')

 def AAIWindow():
     parameterInputData('AAI')

 def VVIWindow():
     parameterInputData('VVI')

 interface = Tk()
 interface.title('Pacemaker')

 ###Pacing mode interface selection###
 pacingModesLabel=Label(interface,text='Pacing Mode Selection')
 pacingModesLabel.grid(row=1,column=1,columnspan=2)
 AOOButton=Button(interface,text='AOO',command=AOOWindow)
 AOOButton.grid(row=2,column=1)
 VOOButton = Button(interface, text='VOO',command=VOOWindow)
 VOOButton.grid(row=2, column=2)
 AAIButton = Button(interface, text='AAI',command=AAIWindow)
 AAIButton.grid(row=3, column=1)
 VVIButton = Button(interface, text='VVI',command=VVIWindow)
 VVIButton.grid(row=3, column=2)

 ###Communication Status between DCM and Device (board)###
 DCMCommunicationStatusTitleLabel = Label(interface, text='DCM Comms w/ Device')
 DCMCommunicationStatusTitleLabel.grid(row=1, column=3)
 DCMCommunicationStatusLabel = Label(interface, text='OFF')
 DCMCommunicationStatusLabel.grid(row=2, column=3)
 #def recursiveCommCheck():
     #Check if there is a new status between DCM and board comms
     #If there is a new status, we need to adjust the DCMCommunicationStatusLabel to say 'ON' w/ command
     #DCMCommunicationStatusLabel.config(text='ON', fg='Green')
     #DCMCommunicationStatusLabel.after(500, recursiveCommCheck)#Check the communication status every 0.5 seconds (500 milliseconds)
 #recursiveCommCheck()

 ###Identifier for whether new pacemaker is plugged in###
 def newPacemaker():
     newPacemakerBool=FALSE#Will actually be whatever the status of whether there is a new pacemaker or not is
     if (newPacemakerBool==TRUE):
         return 'YES'
     else:
         return 'NO'
 newPacemakerTitleLabel=Label(interface, text='Different Pacemaker')
 newPacemakerTitleLabel.grid(row=1, column=4)
 newPacemakerLabel=Label(interface,text=newPacemaker())
 newPacemakerLabel.grid(row=2, column=4)

def login():
 usernameLabel=Label(root,text='Username: ')#Username text
 passwordLabel=Label(root,text='Password: ')#Password text
 usernameLabel.grid(row=1, sticky=W)#Username text organization
 passwordLabel.grid(row=2, sticky=W)#Password text organization

 usernameEntry=Entry(root)#Username entry text
 passwordEntry=Entry(root, show='*')#Password entry text
 usernameEntry.grid(row=1, sticky=E)#Username entry text organization
 passwordEntry.grid(row=2, sticky=E)#Password entry text organization
 #usernameEntry.insert(END, 'username')
 #passwordEntry.insert(END, 'password')

 def loginCheck():#Check the validity of a login attempt
     with open(loginInfoFile) as f:#Open the loginInfoFile to read from
         fileData = f.readlines()#Read datasheet
         numLines=len(fileData)#Calculate the number of lines in the sheet
         usernamesFromSheet=[]#Starting list of all usernames in the sheet
         passwordsFromSheet=[]#Starting list of all passwords in the sheet
         for index in range((int)(numLines/2)):#Index ranging up to half of the number of lines (as we will be
             #observing both the usernames and passwords and considering them to be one pairing, even though they
             #take up 2 lines)
             usernamesFromSheet.append(fileData[index*2].rstrip())#Append the usernames from the sheet to usernamesFromSheet list.
             #NOTE: This is helpful because now we have two seperate lists containing the usernames and passwords, respectively.
             #This means that we can now compare usernames and passwords at the same index (meaning that they are pertaining
             #to the same user)
             passwordsFromSheet.append(fileData[(index*2)+1].rstrip())#Append the usernames from the sheet to passwordsFromSheet list

     def userNameInSheetEntriesWithMatchingPassword():#To check if there exists a user who has the combination of username
         #and password that the user has entered.
         for j in range(len(usernamesFromSheet)):#Check all usernames for login equality
             if (usernamesFromSheet[j]==usernameEntry.get()):#If username at the current index matches the username
                 #entered by the user
                 if (passwordsFromSheet[j]==passwordEntry.get()):#Only accepts login if username and password come
                     #from same index. This stops someone else's password from being used with a given username
                     return TRUE
         return FALSE#If the end of this function is reached, it means that there is no user with the login credentials
         #entered by the user (meaning that we can go ahead and return a false value)

     if (userNameInSheetEntriesWithMatchingPassword()):
         #Execute function for actual UI
         userInterface()
     else:
         badLogin = Tk()
         badLabel = Label(badLogin, text='Bad username and password.')
         badLabel.grid(row=2, sticky=W)

     # testWindow=Tk()
     # entries=Label(testWindow, text=usernameEntry.get()+" "+passwordEntry.get())
     # sheetUserNameAndPassword=Label(testWindow, text=usernameFromSheet + " " + passwordFromSheet)
     # numLines=Label(testWindow,text=numLines)
     # entries.grid(row=1, sticky=W)
     # sheetUserNameAndPassword.grid(row=2, sticky=W)
     # numLines.grid(row=3, sticky=W)
     f.close()

 loginButton=Button(text='Login', fg='Black', command=loginCheck)#A button called login. When this button is clicked,
 #it executes the loginCheck function by reference to in turn compare the given login credentials to the ones that
 #exist in the data sheet
 loginButton.grid(row=3, sticky=S)
#End of login func

def register():
 def openRegistrationWindow():
     root.destroy()
     readFile = open(loginInfoFile, "r")
     file = open(loginInfoFile, "a")
     numLines=len(readFile.readlines())
     if (numLines>=20):
         failWindow=Tk()
         failWindow.title('Failed to register')
         failMessage=Label(failWindow, text='Could not register a new user. Too many users already exist.')
         failMessage.grid(row=1, sticky=W)
         return#Escape the function so that the remaining parts do not happen
     registrationWindow = Tk()
     registrationWindow.title('Registration')

     usernameLabelRegistration = Label(registrationWindow, text='Username: ')  # Username text
     passwordLabelRegistration = Label(registrationWindow, text='Password: ')  # Password text
     usernameLabelRegistration.grid(row=1, column=1)  # Username text organization
     passwordLabelRegistration.grid(row=2, column=1)  # Password text organization

     usernameEntryRegistration = Entry(registrationWindow)  # Username entry text
     passwordEntryRegistration = Entry(registrationWindow)  # Password entry text
     usernameEntryRegistration.grid(row=1, column=2)  # Username entry text organization
     passwordEntryRegistration.grid(row=2, column=2)  # Password entry text organization

     def validLogin(usernameOrPassword):
         for index in range(len(usernameOrPassword)):
             if (ord(usernameOrPassword[index])<48 or (ord(usernameOrPassword[index])>57 and ord(usernameOrPassword[index])<65) or (ord(usernameOrPassword[index])>90 and ord(usernameOrPassword[index])<97) or ord(usernameOrPassword[index])>122):
                 return False
         return True

     def userAlreadyExists(username):
         usernameExists=False

         with open(loginInfoFile) as f:  # Open the loginInfoFile to read from
             fileData = f.readlines()  # Read datasheet
             #usernamesFromSheet = []  # Starting list of all usernames in the sheet
             for index in range((int)(numLines / 2)):  # Index ranging up to half of the number of lines (as we will be
                 # observing both the usernames and passwords and considering them to be one pairing, even though they
                 # take up 2 lines)
                 #usernamesFromSheet.append(fileData[index * 2].rstrip())  # Append the usernames from the sheet to usernamesFromSheet list.
                 if (username==fileData[index * 2].rstrip()):
                     usernameExists=True

         return usernameExists


     def writeToSheet():
         if (usernameEntryRegistration.get()=='' or passwordEntryRegistration.get()==''):
             failWindow = Tk()
             failWindow.title('Failed to register')
             failMessage = Label(failWindow, text='Can not create an empty user.')
             failMessage.grid(row=1, sticky=W)
             return  # Escape the function so that the remaining parts do not happen
         elif (userAlreadyExists(usernameEntryRegistration.get())):
             failWindow = Tk()
             failWindow.title('Failed to register')
             failMessage = Label(failWindow, text='A user with this username already exists.')
             failMessage.grid(row=1, sticky=W)
         elif (validLogin(usernameEntryRegistration.get())!=True or validLogin(passwordEntryRegistration.get())!=True):
             failWindow = Tk()
             failWindow.title('Failed to register')
             failMessage = Label(failWindow, text='An invalid character was found within the username and/or password that you entered.')
             failMessage.grid(row=1, sticky=W)
         else:
             successWindow = Tk()
             successWindow.title('Registered!')
             successMessage = Label(successWindow,text='Congratulations. Registration successful')
             successMessage.grid(row=1, sticky=W)
             file.write('\n' + usernameEntryRegistration.get() + '\n' + passwordEntryRegistration.get())
             file.close()
             registrationWindow.destroy()
             userInterface()

     registerButtonRegisterWindow=Button(registrationWindow, text='Register', fg='Black', command=writeToSheet)
     registerButtonRegisterWindow.grid(row=3, column=2)



 ###Option for user to add their login information to the list of registrations###
 notRegisteredText=Label(root, text="Not registered?->")
 notRegisteredText.grid(row=4, sticky=W)

 registerButtonLoginWindow=Button(root, text='Register Here', fg='Black', command=openRegistrationWindow)
 registerButtonLoginWindow.grid(row=4, sticky=S)
#End of register func

def main():
   welcome()
   login()
   register()
   root.mainloop()

if __name__=="__main__":
   main()

