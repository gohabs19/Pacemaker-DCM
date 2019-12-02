#A file filled with classes relating to the functionality needed for each of the windows in the windows file. This
#includes any functionality related to pressing a button or needed other functionality like text boxes.

from tkinter import *
import windows#Import the windows.py file
import threading
import time

class loginAndRegistrationWindowsFunctionality:#A parent class to hold the functionality that is necessary to both the
    #login and registration functionalities, along with the login and registration classes themselves.

    #Class variables
    username=''#To store the username and password currently on screen. Updated when the user attempts to login or register.
    password=''
    thread=''
    n=1

    # Attain data from the login info sheet. This data is relevant to all login and registration-related methods.
    loginInfoFile = 'pacemakerLogins.txt'
    with open(loginInfoFile) as f:  # Open the loginInfoFile to read from
        fileData = f.readlines()  # Read datasheet
        numLines = len(fileData)  # Calculate the number of lines in the sheet
        usernamesFromSheet = []  # Starting list of all usernames in the sheet
        passwordsFromSheet = []  # Starting list of all passwords in the sheet
        for index in range((int)(numLines / 2)):  # Index ranging up to half of the number of lines (as we will be
            # observing both the usernames and passwords and considering them to be one pairing, even though they
            # take up 2 lines)
            usernamesFromSheet.append(
                fileData[index * 2].rstrip())  # Append the usernames from the sheet to usernamesFromSheet list.
            # NOTE: This is helpful because now we have two seperate lists containing the usernames and passwords, respectively.
            # This means that we can now compare usernames and passwords at the same index (meaning that they are pertaining
            # to the same user)
            passwordsFromSheet.append(
                fileData[(index * 2) + 1].rstrip())  # Append the usernames from the sheet to passwordsFromSheet list

    #Class methods for all login and registry-related functionalities
    def createThread(self,usernameEntry,passwordEntry):
        thread = threading.Thread(target=loginAndRegistrationWindowsFunctionality.updateUsernameAndPassword,args=(self, usernameEntry, passwordEntry))
        thread.daemon = True  # Make thread a daemon (runs in background)
        return thread
    def setCurrentUsername(self,username):#To set the username for the whole class to the one that is currently on-screen
        #incase it needs to be used again.
        loginAndRegistrationWindowsFunctionality.username=username
    def setCurrentPassword(self,password):
        loginAndRegistrationWindowsFunctionality.password=password
    def updateUsernameAndPassword(self,usernameEntry,passwordEntry):
        loginAndRegistrationWindowsFunctionality.n = 1
        while (loginAndRegistrationWindowsFunctionality.n > 0):
            #print('Updating username & password')
            loginAndRegistrationWindowsFunctionality.username = usernameEntry.get()
            loginAndRegistrationWindowsFunctionality.password = passwordEntry.get()
            time.sleep(0.01)#0.01 second delay between username and password updates
            print('N: '+str(loginAndRegistrationWindowsFunctionality.n))
    def usernameAndPasswordEntries(self,root):
        usernameLabel = Label(root, text='Username: ')  # Username text
        usernameLabel.grid(row=1, column=1, sticky=W)  # Username text organization
        usernameEntry = Entry(root)  # Username entry text
        usernameEntry.grid(row=1, column=2, sticky=E)  # Username entry text organization
        passwordLabel = Label(root, text='Password: ')  # Password text
        passwordLabel.grid(row=2, column=1, sticky=W)  # Password text organization
        passwordEntry = Entry(root, show='*')  # Password entry text
        passwordEntry.grid(row=2, column=2, sticky=E)  # Password entry text organization
        loginAndRegistrationWindowsFunctionality.thread=loginAndRegistrationWindowsFunctionality.createThread(self,usernameEntry,passwordEntry)
        loginAndRegistrationWindowsFunctionality.thread.start()
    class loginWindowsFunctionality:
        def fillLoginWindow(self, lWindow):#Fills the login window with necessary pieces (e.g. text, buttons, etc.)
            print('Filling login window')#For debugging
            loginAndRegistrationWindowsFunctionality.usernameAndPasswordEntries(self,lWindow)
            loginButton=Button(lWindow, text='Login', fg='Black', command=lambda: loginAndRegistrationWindowsFunctionality.loginWindowsFunctionality.login(self,lWindow))
            loginButton.grid(row=3, column=1, columnspan=2, sticky=S)
            registrationLabel=Label(lWindow, text="Don't have a login? Register here-->")
            registrationLabel.grid(row=4, column=1, sticky=W)
            registrationButton=Button(lWindow, text='Register', fg='Black', command=lambda: windows.windowsRegister.registerWindow(self, lWindow))
            registrationButton.grid(row=4, column=2, sticky=E)
        def matchingUsernameAndPassword(self, currentUsername,currentPassword):  # To check if there exists a user who has the combination of username
            # and password that the user has entered.
            for j in range(len(loginAndRegistrationWindowsFunctionality.usernamesFromSheet)):  # Check all usernames for login equality
                if (str(loginAndRegistrationWindowsFunctionality.usernamesFromSheet[j]) == str(currentUsername)):  # If username at the current index matches the username
                    # entered by the user
                    if (str(loginAndRegistrationWindowsFunctionality.passwordsFromSheet[j]) == str(currentPassword)):  # Only accepts login if username and password come
                        # from same index. This stops someone else's password from being used with a given username
                        return TRUE
            return FALSE  # If the end of this function is reached, it means that there is no user with the login credentials
            # entered by the user (meaning that we can go ahead and return a false value)
        def login(self, lWindow):#Method used to check if we will log the user in given the information that they have entered.
            print('Login attempt made')
            print('Username: '+loginAndRegistrationWindowsFunctionality.username+'Password: '+loginAndRegistrationWindowsFunctionality.password)


    class registrationWindowsFunctionality:
        def fillRegistrationWindow(self, rWindow):
            print('Filling registration window')
            loginAndRegistrationWindowsFunctionality.n=0
            #loginAndRegistrationWindowsFunctionality.thread.join()
            loginAndRegistrationWindowsFunctionality.usernameAndPasswordEntries(self,rWindow)
            registrationButton = Button(rWindow, text='Register', fg='Black', command=lambda: loginAndRegistrationWindowsFunctionality.registrationWindowsFunctionality.register(self, rWindow))
            registrationButton.grid(row=3, column=1, columnspan=2, sticky=E)
        def register(self, rWindow):
            print('Registration attempt made')
            print('Username: '+loginAndRegistrationWindowsFunctionality.username+'Password: '+loginAndRegistrationWindowsFunctionality.password)
