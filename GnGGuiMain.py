from tkinter import *
from tkinter import messagebox
from GnGDB import *
#
# Project : G&G Medical Database
# Filename: GnGGuiMain
# Version: 1
# Date : April 18 2018
# Author: Paul Gierzynski
#
# This file contains the components of a multipage GUI
# This allows particular functionality to be provided page by page
# each pages is a separate class that is either brought to the foreground
# or destroyed as the user switches between gui functions.
#
#

#
# This Class is the main GUI Engine
#
class MainView(Tk):
    # Begin with displaying the first frame
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(LoginWindow) # Star with the login Window

    # Call switch to change GUI Frame
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None: # Make sure its a Frame
            self._frame.destroy() # Blow away old frame to avoid widget conflicts
        self._frame = new_frame # Assert new Frame
        self._frame.pack() # Make visible

#
# Project : G&G Medical Database
# LoginWindow
# Version: 1
# Date : April 18 2018
# Author: Paul Gierzynski
#
# This file acts as a self contained GUI Page or Frame
# when run in conjunction with GnGGuiMain
# This allows particular functionality to be provided page by page
# each pages is a separate class that is either brought to the foreground
# or destroyed as the user switches between gui functions.
# This page provides the required for user logins
#
class LoginWindow(Frame):

    # Validate the username and password entered against the User table in the database
    def validateUserCredentials(self):
        match = False
        # Check to make sure there is something to validate
        if ((self.userNameVar.get() != '') and (self.passwordVar.get() != '')):
            print('validating User Name and Password')
            # Get data entered by user
            uid = str(self.userNameVar.get())
            pswd = str(self.passwordVar.get())
            # Grab all users in the database
            sqlResults = readRecordSpecific("User","uid","password" )
            # Seek the users credentials
            if sqlResults != None:
               # Search list of tuples for a match
                for i in range(len(sqlResults)):
                    if uid and pswd in sqlResults[i]:
                        print('User Name and Password Matched')
                        self.btn7.configure(state=NORMAL)
                        self.btn6.configure(state=DISABLED)
                        match = True
                if match == False:
                    print('User Name and Password not Found')
                    messagebox.showerror('ERROR>', 'Unable to find User Name or Password')
            else:
                messagebox.showerror("ERROR>", 'Cannot Access DataBase !')
        else:
            messagebox.showerror("ERROR>", 'UserName and Password cannot be blank!')


#
# Build Build Login Window Frame
#
    def __init__(self, master):
        Frame.__init__(self, master)

        # Build initial frame
        self.lf1 = Frame(self)
        self.lf1.pack()

        self.lf0 = Frame(self.lf1)
        self.lf0.pack()
        # Add Label
        self.label1 = Label(self.lf0,text='Welcome to the G&G Medical Group Portal - Please Log In',font=('Arial',12), fg = 'darkblue')
        self.label1.pack(side = TOP, padx=10,pady=15)
        # Build second frame
        self.lf2 = Frame(self.lf1)
        self.lf2.pack()
        # Build User Name Data Entry
        self.label2 = Label(self.lf2,text="User Name:")
        self.label2.pack(side=LEFT,padx=5,pady=10)
        self.userNameVar = StringVar()
        self.name = Entry(self.lf2,textvariable=self.userNameVar, width=30, bg='cyan', relief=SUNKEN)
        self.name.pack(side=LEFT,pady=10)
        # Build third frame
        self.lf3 = Frame(self.lf1)
        self.lf3.pack()
        # Build Password Data Entry
        self.label3 = Label(self.lf3,text="Password:  ")
        self.label3.pack(side=LEFT,padx=5,pady=10)
        self.passwordVar = StringVar()
        self.password = Entry(self.lf3,textvariable=self.passwordVar, width=30, bg='cyan', show ="*", relief=SUNKEN)
        self.password.pack(side=LEFT,pady=10)
        # Build fourth frame
        self.lf4 = Frame(self.lf1)
        self.lf4.pack()
        # Build Entry Button
        self.btn6 = Button(self.lf4,text=" Enter ", width=7, fg="black", bg="lightgray", relief=RAISED, command=self.validateUserCredentials)
        self.btn6.pack(side = LEFT,padx=5,pady=15)
        self.btn7 = Button(self.lf4, text="Continue", width=7, fg="black", bg="lightgray", relief=RAISED,command=lambda: master.switch_frame(SelectTasks),state=DISABLED)
        self.btn7.pack(side=LEFT, padx=5, pady=15)

        # End of  Login Window Frame
#
# Project : G&G Medical Database
# Select Tasks
# Version: 1
# Date : April 18 2018
# Author: Paul Gierzynski
#
# This file acts as a self contained GUI Page or Frame
# when run in conjunction with GnGGuiMain
# This allows particular functionality to be provided page by page
# each pages is a separate class that is either brought to the foreground
# or destroyed as the user switches between gui functions.
# This page provides the ability of the user to switch between tasks
# and retun to the same focal point. It appears immediately after
# # logging in
#
#
class SelectTasks(Frame):

    #
    # This exits from the application all together
    #
    def exitProgram(self):
        self.lf1.destroy()
        exit(5)

    def __init__(self, master):
        Frame.__init__(self, master)

        # Create a master frame as a container
        self.lf1 = Frame(self)
        self.lf1.pack()
        # Add label to the Frame
        self.label1 = Label(self.lf1, text='Welcome to G&G Medical Group LLC - Please Select from the Actions Below',fg= 'darkblue',font=('Arial', 12))
        self.label1.pack(side=TOP, padx=10, pady=15)
        # Create a sub frame for the action buttons
        self.lf2 = Frame(self.lf1)
        self.lf2.pack()
        # Create the action buttons
        self.btn1 = Button(self.lf2, text=" Manage Users ", width=16,height= 14, fg="black", bg="lightgray", relief=RAISED,
                              command=lambda: master.switch_frame(ManageUsers))
        self.btn1.pack(side=LEFT, padx=10, pady=15)

        self.btn2 = Button(self.lf2, text=" Manage Data", width=16,height= 14, fg="black", bg="lightgray", relief=RAISED,
                              command=lambda: master.switch_frame(DataEntry))
        self.btn2.pack(side=LEFT, padx=10, pady=15)

        self.btn3 = Button(self.lf2, text=" Make Appointment", width=16,height= 14, fg="black", bg="lightgray", relief=RAISED,
                              command=lambda: master.switch_frame(MakeAppointment)) # change
        self.btn3.pack(side=LEFT, padx=10, pady=15)

        self.btn4 = Button(self.lf2, text=" Show Appointments", width=16,height= 14, fg="black", bg="lightgray", relief=RAISED,
                              command=lambda: master.switch_frame(ShowAppointment)) # Chamge
        self.btn4.pack(side=LEFT, padx=10, pady=15)
        # Create sub frame for exit button
        self.lf3 = Frame(self.lf1)
        self.lf3.pack()

        self.btn4 = Button(self.lf3,text="       EXIT     ", width=18,height= 6, fg="black", bg="lightgray", relief=RAISED, command=self.exitProgram)
        self.btn4.pack(side=BOTTOM, padx=10, pady=15)

        # End of Select Tasks Frame


#
# Project : G&G Medical Database
# DataEntry
# Version: 1
# Date : April 18 2018
# Author: Paul Gierzynski
#
# This file acts as a self contained GUI Page or Frame
# when run in conjunction with GnGGuiMain
# This allows particular functionality to be provided page by page
# each pages is a separate class that is either brought to the foreground
# or destroyed as the user switches between gui functions.
# This page provides the required functionality for general database maintenance
#
#

class DataEntry(Frame):

    #
    # Validate the cursor selected something, print to console the
    # position of the cursor, and return the value of the cursor position
    #
    def selection(self):
        self.select1.curselection()
        print("At %s of %d" % (self.select1.curselection(), len(sqlResults)))
        return int(self.select1.curselection()[0])

    #
    # Get the data entered in the frame entry fields and
    # create a new record in the database, refresh the GUI Listbox,
    # message user indicating addition of the new record
    #
    def addRecord(self) :
        if self.fnameVar.get() != "" and self.lnameVar.get() != "": # be sure fields are not empty
            fname = self.fnameVar.get()
            lname = self.lnameVar.get()
            index = self.rbVal.get()
            table = tableList[int(index)]
            insertRecord(table,fname,lname)
            self.setList()
            messagebox.showinfo("Insert Data","Adding to %s Table: " %table + "%s" %fname + "%s" %lname)
        else:
            messagebox.showerror('ERROR!','Data Entry fields cannot be blank! Please Try again')
            self.setList()
    #
    # Update record information
    # Retrieve information from list
    # print current information to the console
    # Ask user if the wish the update to proceed
    # If ok, print update information to the console
    # Retrieve updated record info from text boxes
    # Call the database update function
    # Refresh the GUI Listbox with the updated info.
    #
    def updateRecord(self):
        #  As if sure you want to update
        if (messagebox.askokcancel(title="Updating record!", message="Update Record? Press OK or Cancel") == 1):
            if self.fnameVar.get() != "" and self.lnameVar.get() != "":  # be sure fields are not empty
                print('New record values are : "%s' % self.fnameVar.get() + '%s' % self.lnameVar.get())
                # get the variables to change
                pid = self.ridVar.get()
                first = self.fnameVar.get()
                last = self.lnameVar.get()
                index = self.rbVal.get()
                table = tableList[int(index)]
                table_id = table + "_id"
                # perform update
                updateRecord2F(table, "fname", first, "lname", last, table_id,pid)
                print('\nUpdating Record...\n')
            else:
                messagebox.showerror('ERROR!','Data Entry fields cannot be blank! Please Try again')
        else:
            print('Update of record Canceled!')
            self.setList()

    #
    # Retrieve data for the current selection
    # Ask user if the deletion should proceed
    # If OK print message to the console indicating record deletion
    # Call db deletion method and passing in the tablename and associated data filed to key on
    # Refresh the GUI Listbox
    #
    def deleteRecord(self) :
        if (messagebox.askokcancel(title="Deleting Record!",message= 'Proceed? Ok or Cancel') == 1):
            # build query info
            pid =self.ridVar.get()
            index = self.rbVal.get()
            table = tableList[int(index)]
            table_id = table + "_id"
            print (table_id)
            # Delete record
            deleteRecord(table, table_id, pid)
        else:
            print('Deletion of record Canceled!')
        self.setList ()

    #
    # Load the value at the index of the GUI Listbox into the data entry fields
    #
    def loadRecord(self) :
       try: # Get data from selected record
           pid,fname,lname = sqlResults[self.selection()]
           # write it to the data fields
           self.ridVar.set(pid)
           self.fnameVar.set(fname)
           self.lnameVar.set(lname)
       except TypeError:  # catch list box cursor selection errors
           messagebox.showerror('Item Selection failed', 'Please re-select')
           self.setList()
       except IndexError:
           messagebox.showerror('Item Selection failed', 'Please re-select')
           self.setList()


    #
    # Populate the GUI Listbox with the selected records
    #
    def setList (self) :
        try:
            global sqlResults
            # Send sqlRequest for records specified by radio button
            index = self.rbVal.get()
            table = tableList[int(index)]
            sqlResults = readRecordAll(table)
            sqlResults.sort(key = lambda x : x[1]) # Sort on name field
            self.select1.delete(0,END) # Clear the GUI listbox
            for pid,fname,lname in sqlResults :
                print(fname,lname)
                self.select1.insert (END,(fname,lname)) # Populate the Listbox
        except ValueError:
            messagebox.showinfo("Error!","Please Select a Category First")


    #
    # Build Frame to be displayed as GUI Window
    #

    def __init__(self, master):
        Frame.__init__(self, master)

        # Globals for passing pertinent data
        global rbVal, fnameVar, lnameVar, tableList,genericlist
        tableList =  ['Doctor','Nurse','Patient']
        # Create primary Frame container
        self.lf9 = Frame(self)
        self.lf9.pack()

        self.label1 = Label(self.lf9, text='Consolidated Data Entry Panel', font=('Arial', 12), fg='black')
        self.label1.pack(side=TOP, pady=15)
        # Create sub frame lables and buttons
        self.lf0 = Frame(self.lf9)
        self.lf0.pack()
        self.label2 = Label(self.lf0, text='Please Select a Category to Select From', font=('Arial', 10), fg='black')
        self.label2.pack(side=TOP, pady=5)

        self.rbVal = StringVar()
        self.rb1 = Radiobutton(self.lf0, text="Doctor", variable=self.rbVal, value=0)
        self.rb2 = Radiobutton(self.lf0, text="Nurse", variable=self.rbVal, value=1)
        self.rb3 = Radiobutton(self.lf0, text="Patient", variable=self.rbVal, value=2)

        self.rb1.pack(side=LEFT, padx=5, pady=10)
        self.rb2.pack(side=LEFT, padx=5, pady=10)
        self.rb3.pack(side=LEFT, padx=5, pady=10)
        # Create subframe for list box

        self.lf2 = Frame(self.lf9)
        self.lf2.pack()

        self.scroll = Scrollbar(self.lf2, orient=VERTICAL)
        self.select1 = Listbox(self.lf2, yscrollcommand=self.scroll.set, height=20, width=100, bg="lightgray", relief=SUNKEN)
        self.scroll.config(command=self.select1.yview)
        self.scroll.pack(side=RIGHT, pady=30, fill=Y)
        self.select1.pack(side=LEFT, pady=30)
        # Create subframe for data entry
        self.lf3 = Frame(self.lf9)
        self.lf3.pack()

        self.label31 = Label(self.lf3, text="RID")
        self.label31.pack(side=LEFT, padx=5, pady=10)
        self.ridVar = StringVar()
        self.userRid = Entry(self.lf3, textvariable=self.ridVar, width=6, bg='cyan', relief=SUNKEN)
        self.userRid.pack(side=LEFT, pady=10)

        self.label3 = Label(self.lf3, text="First Name:  ")
        self.label3.pack(side=LEFT, padx=5, pady=10)
        self.fnameVar = StringVar()
        self.userName = Entry(self.lf3, textvariable=self.fnameVar, width=30, bg='cyan', relief=SUNKEN)
        self.userName.pack(side=LEFT, pady=10)

        self.label3 = Label(self.lf3, text="Last Name:  ")
        self.label3.pack(side=LEFT, padx=5, pady=10)
        self.lnameVar = StringVar()
        self.password = Entry(self.lf3, textvariable=self.lnameVar, width=30, bg='cyan', relief=SUNKEN)
        self. password.pack(side=LEFT, pady=10)
        # Create subframe for action buttons
        self.lf4 = Frame(self.lf9)
        self.lf4.pack()

        self.btn1 = Button(self.lf4, text="  GET", width=7, fg="black", bg="lightgray", relief=RAISED,command=self.setList)
        self.btn1.pack(side=LEFT, padx=5, pady=10)
        self.btn1 = Button(self.lf4, text=" LOAD", width=7, fg="black", bg="lightgray", relief=RAISED, command=self.loadRecord)
        self.btn1.pack(side=LEFT, padx=5, pady=10)
        self.btn2 = Button(self.lf4, text="CREATE", width=7, fg="black", bg="lightgray", relief=RAISED, command=self.addRecord)
        self.btn2.pack(side=LEFT, padx=5, pady=15)
        self.btn3 = Button(self.lf4, text="UPDATE", width=7, fg="black", bg="lightgray", relief=RAISED, command=self.updateRecord)
        self.btn3.pack(side=LEFT, padx=5, pady=15)
        self.btn4 = Button(self.lf4, text=" DELETE", width=7, fg="black", bg="RED", relief=RAISED, command=self.deleteRecord)
        self.btn4.pack(side=LEFT, padx=5, pady=15)
        self.btn5 = Button(self.lf4, text="RETURN", width=7, fg="black", bg="lightgray", relief=RAISED,command=lambda: master.switch_frame(SelectTasks))
        self.btn5.pack(side=LEFT, padx=5, pady=15)

        # End of Data Entry Frame

#
# Project : G&G Medical Database
# ManageUsers
# Version: 1
# Date : April 18 2018
# Author: Paul Gierzynski
#
# This file acts as a self contained GUI Page or Frame
# when run in conjunction with GnGGuiMain
# This allows particular functionality to be provided page by page
# each pages is a separate class that is either brought to the foreground
# or destroyed as the user switches between gui functions.
# This page provides the required functionality for maintaining
# user Id's and passwords
#

class ManageUsers(Frame):

    #
    # Validate the cursor selected something, print to console the
    # position of the cursor, and return the value of the cursor position
    #
    def selection(self):
        self.select2.curselection()
        print("At %s of %d" % (self.select2.curselection(), len(sqlResults)))
        return int(self.select2.curselection()[0])

    #
    # Get the data entered in the frame entry fields and
    # create a new record in the database, refresh the GUI Listbox,
    # message user indicating addition of the new record
    #
    def addRecord(self):
        # be sure fields are not empty
        if self.fnameVar.get() != "" and self.lnameVar.get() != "" and self.userNameVar.get() != "" and self.passwordVar.get() != "":
            fname = self.fnameVar.get()
            lname = self.lnameVar.get()
            uid = self.userNameVar.get()
            password = self.passwordVar.get()
            table = "User"
            insertRecord4F(table,uid,password,fname,lname)
            self.setList()
            messagebox.showinfo("Alert", "Adding New User")
        else:
            messagebox.showerror('ERROR!', 'Data Entry fields cannot be blank! Please Try again')
            self.setList()

    #
    # Update record information
    # Retrieve information from list
    # print current information to the console
    # Ask user if the wish the update to proceed
    # If ok, print update information to the console
    # Retrieve updated record info from text boxes
    # Call the database update function
    # Refresh the GUI Listbox with the updated info.
    #
    def updateRecord(self):
        try:
            if (messagebox.askokcancel(title="Updating record!", message="Update Record? Press OK or Cancel") == 1):
                if self.fnameVar.get() != "" and self.lnameVar.get() != "":  # be sure fields are not empty
                    # get the variables to change
                    pid = self.ridVar.get()
                    first = self.fnameVar.get()
                    last = self.lnameVar.get()
                    userid = self.userNameVar.get()
                    npass = self.passwordVar.get()
                    table =  "User"
                    table_id = table + "_id"
                    print(table_id)# perform update
                    updateRecord4F(table, "uid", userid, "password", npass, "fname", first, "lname", last,table_id, pid)
                    print('\nUpdating Record...\n')
                else:
                    messagebox.showerror('ERROR!', 'Data Entry fields cannot be blank! Please Try again')
            else:
                print('Update of record Canceled!')
                self.setList()
        except TypeError: # catch list box cursor selection error
            messagebox.showerror('Item Selection failed','Please re-select')
            self.setList()
        except IndexError:
            messagebox.showerror('Item Selection failed', 'Please re-select')
            self.setList()

    #
    # Retrieve data for the current selection
    # Ask user if the deletion should proceed
    # If OK print message to the console indicating record deletion
    # Call db deletion method and passing in the tablename and associated data filed to key on
    # Refresh the GUI Listbox
    #
    def deleteRecord(self):
        try:  # get current data
            # Ask user if it's ok
            if (messagebox.askokcancel(title="Deleting Record!", message='Proceed? Ok or Cancel') == 1):
                # build query info
                pid = self.ridVar.get()
                table = "User"
                table_id = table + "_id"
                print(table_id)
                # Delete record
                deleteRecord(table, table_id, pid)
            else:
                print('Deletion of record Canceled!')
            self.setList()
        except TypeError:  # catch list box cursor selection errors
            messagebox.showerror('Item Selection failed', 'Please re-select contact')
            self.setList()
        except IndexError:
            messagebox.showerror('Item Selection failed', 'Please re-select contact')
            self.setList()

    #
    # Load the value at the index of the GUI Listbox into the data entry fields
    #
    def loadRecord(self):
        try:  # Get data from selected record
            pid, uid,password,fname, lname = sqlResults[self.selection()]
            # write it to the data fields
            self.ridVar.set(pid)
            self.fnameVar.set(fname)
            self.lnameVar.set(lname)
            self.userNameVar.set(uid)
            self.passwordVar.set(password)
        except TypeError:  # catch list box cursor selection errors
            messagebox.showerror('Item Selection failed', 'Please re-select')
            self.setList()
        except IndexError:
            messagebox.showerror('Item Selection failed', 'Please re-select')
            self.setList()

    #
    # Populate the GUI Listbox with the selected records
    #
    def setList(self):
        global sqlResults
        # Send sqlRequest for records specified by radio button
        table = "User"
        sqlResults = readRecordAll(table)
        sqlResults.sort(key=lambda x: x[1])  # Sort on name field
        self.select2.delete(0, END)  # Clear the GUI listbox
        for pid, uid,password,fname, lname in sqlResults:
            print(uid, fname, lname)
            self.select2.insert(END, (uid, password,fname, lname))  # Populate the Listbox

    #
    # Build the Frame for Manage Users
    #
    def __init__(self, master):
        Frame.__init__(self, master)
        # Create globals

        # Create master frame as a container for all others
        self.lf1 = Frame(self)
        self.lf1.pack()
        # Label Frame
        self.label1 = Label(self.lf1, text='User Management Panel _ Administrators Only', font=('Arial', 12),
                            fg='red')
        self.label1.pack(side=TOP, pady=15)
        # Create sub frame for listbox
        self.lf2 = Frame(self.lf1)
        self.lf2.pack()
        # Create Listbox
        self.scroll = Scrollbar(self.lf2, orient=VERTICAL)
        self.select2 = Listbox(self.lf2, yscrollcommand=self.scroll.set, height=20, width=100, bg="lightgray",
                               relief=SUNKEN)
        self.scroll.config(command=self.select2.yview)
        self.scroll.pack(side=RIGHT, pady=50, fill=Y)
        self.select2.pack(side=LEFT, pady=50)

        # Create sub Frame for data entry
        self.lf3 = Frame(self.lf1)
        self.lf3.pack()

        # Create data entry fields
        self.label3 = Label(self.lf3, text="RID:")
        self.label3.pack(side=LEFT, padx=5, pady=10)
        self.ridVar = StringVar()
        self.pid = Entry(self.lf3, textvariable=self.ridVar, width=5, bg='cyan', relief=SUNKEN)
        self.pid.pack(side=LEFT, pady=10)

        # Create data entry fields
        self.label3 = Label(self.lf3, text="First Name:  ")
        self.label3.pack(side=LEFT, padx=5, pady=10)
        self.fnameVar = StringVar()
        self.pid = Entry(self.lf3, textvariable=self.fnameVar, width=20, bg='cyan', relief=SUNKEN)
        self.pid.pack(side=LEFT, pady=10)

        self.label4 = Label(self.lf3, text="Last Name:  ")
        self.label4.pack(side=LEFT, padx=5, pady=10)
        self.lnameVar = StringVar()
        self.pid = Entry(self.lf3, textvariable=self.lnameVar, width=20, bg='cyan', relief=SUNKEN)
        self.pid.pack(side=LEFT, pady=10)

        self.label5 = Label(self.lf3, text="User Name:  ")
        self.label5.pack(side=LEFT, padx=5, pady=10)
        self.userNameVar = StringVar()
        self.userName = Entry(self.lf3, textvariable=self.userNameVar, width=20, bg='cyan', relief=SUNKEN)
        self.userName.pack(side=LEFT, pady=10)

        self.label6 = Label(self.lf3, text="Password:  ")
        self.label6.pack(side=LEFT, padx=5, pady=10)
        self.passwordVar = StringVar()
        self.password = Entry(self.lf3, textvariable=self.passwordVar, width=20, bg='cyan', relief=SUNKEN)
        self.password.pack(side=LEFT, pady=10)
        # Create sub frame for action buttons
        self.lf4 = Frame(self.lf1)
        self.lf4.pack()
        # Create Buttons
        self.btn0 = Button(self.lf4, text=" GET", width=7, fg="black", bg="lightgray", relief=RAISED,
                           command=self.setList)
        self.btn0.pack(side=LEFT, padx=5, pady=15)
        self.btn1 = Button(self.lf4, text=" LOAD", width=7, fg="black", bg="lightgray", relief=RAISED,
                           command=self.loadRecord)
        self.btn1.pack(side=LEFT, padx=5, pady=15)
        self.btn2 = Button(self.lf4, text="CREATE", width=7, fg="black", bg="lightgray", relief=RAISED,
                           command=self.addRecord)
        self.btn2.pack(side=LEFT, padx=5, pady=15)
        self.btn3 = Button(self.lf4, text="UPDATE", width=7, fg="black", bg="lightgray", relief=RAISED,
                           command=self.updateRecord)
        self.btn3.pack(side=LEFT, padx=5, pady=15)
        self.btn4 = Button(self.lf4, text=" DELETE", width=7, fg="black", bg="RED", relief=RAISED,
                           command=self.deleteRecord)
        self.btn4.pack(side=LEFT, padx=5, pady=15)
        self.btn5 = Button(self.lf4, text=" RETURN", width=7, fg="black", bg="lightgray", relief=RAISED,
                           command=lambda: master.switch_frame(SelectTasks))
        self.btn5.pack(side=LEFT, padx=5, pady=15)

        # End of Frame
#
# Project : G&G Medical Database
# MakeAppointment
# Version: 1
# Date : April 18 2018
# Author: Paul Gierzynski
#
# This file acts as a self contained GUI Page or Frame
# when run in conjunction with GnGGuiMain
# This allows particular functionality to be provided page by page
# each pages is a separate class that is either brought to the foreground
# or destroyed as the user switches between gui functions.
# This panel contains the frame work to allow the user to make an appointment with a specified doctor
#
class MakeAppointment(Frame):

    # This fucntion tracks the current selection made by the user
    # and returns the index posotion of the record selected whenever it is called
    def selection(self):
        self.select3.curselection()
        print("At %s of %d" % (self.select3.curselection(), len(sqlResults)))
        return int(self.select3.curselection()[0])

    #
    # This update record will use the collective PIDs for all information gathered
    # to update the appointment table in the database with an appoint for the patient
    #
    def updateRecord(self):  # Needs updating
        # insure all the needed pids are entered
        if (self.patidVar.get() != "" and self.dridVar.get() != "" and self.reasidVar.get() != "" and self.dateidVar.get() != "" and self.timeidVar.get() !=""):
            patient_id = self.patidVar.get()
            doctor_id = self.dridVar.get()
            medical_condition_id = self.reasidVar.get()
            date_id = self.dateidVar.get()
            start_time_id = self.timeidVar.get()
            # perform update
            createAppointmentRecord(patient_id, doctor_id, medical_condition_id, date_id, start_time_id)
            print('\nCreating Appointment...\n')
        else:
            messagebox.showerror('ERROR!', 'Data Entry fields cannot be blank! Please Try again')

    #
    # Load the value at the index of the GUI Listbox into the data entry fields
    #
    def loadRecord(self):
        value = self.rbVal.get()
        try:
            if value == "0":
                pid, pfname, plname = sqlResults[self.selection()]
                self.patidVar.set(pid)
                self.pfnameVar.set(pfname)
                self.plnameVar.set(plname)
            elif value == "1":
                pid, dfname, dlname = sqlResults[self.selection()]
                self.dridVar.set(pid)
                self.dlnameVar.set(dlname)
            elif value == "2":
                pid, condition,stuff = sqlResults[self.selection()]
                self.reasidVar.set(pid)
                self.reasVar.set(condition)
            elif value == "3":
                doctor, dpid, day, tpid, time, = sqlResults[self.selection()]
                self.dateidVar.set(dpid)
                self.dateVar.set(day)
                self.timeidVar.set(tpid)
                self.timeVar.set(time)
        except TypeError:  # catch list box cursor selection errors
            messagebox.showerror('Item Selection failed', 'Please re-select contact')
            self.setList()
        except IndexError:
            messagebox.showerror('Item Selection failed', 'Please re-select contact')
            self.setList()
        except ValueError:
            messagebox.showinfo("Error!","You Must Select a Category First!")

    #
    # Populate the GUI Listbox with the selected records
    #
    def setList(self):
        try:
            global sqlResults
            # Send sqlRequest for records specified by radio button
            value = self.rbVal.get()
            if (value == "0"):
                table = "Patient"
                sqlResults = readRecordAll(table)
                sqlResults.sort(key=lambda x: x[1])  # Sort on name field
                self.select3.delete(0, END)  # Clear the GUI listbox
                for pid, fname, lname in sqlResults:
                    print(pid,fname, lname)
                    patient = fname, lname
                    self.select3.insert(END, (patient))  # Populate the Listbox
            elif value == "1":
                table ='Doctor'
                sqlResults = readRecordAll(table)
                sqlResults.sort(key=lambda x: x[1])  # Sort on name field
                self.select3.delete(0, END)  # Clear the GUI listbox
                for pid,fname, lname in sqlResults:
                    print(pid, fname, lname)
                    self.select3.insert(END, (lname))  # Populate the Listbox
            elif value == "2":
                table ="MedicalCondition"
                sqlResults = readRecordAll(table)
                sqlResults.sort(key=lambda x: x[1])  # Sort on name field
                self.select3.delete(0, END)  # Clear the GUI listbox
                for pid, condition, stuff in sqlResults:
                    print(pid,condition, stuff)
                    self.select3.insert(END, (condition))  # Populate the Listbox
            elif value == "3":
                pid = self.dridVar.get()
                sqlResults = showDoctorAvailability(pid)
                #sqlResults.sort(key=lambda x: x[1])  # Sort on name field
                self.select3.delete(0, END)  # Clear the GUI listbox
                for doctor,dpid,day, tipid, time, in sqlResults:
                    print(doctor, dpid, day,tipid, time)
                    self.select3.insert(END, (doctor, day,time))  # Populate the Listbox
        except ValueError:
            messagebox.showinfo("Error!","You Must Select a Category First!")

    # Build Appointment Frame
    def __init__(self, master):
        Frame.__init__(self, master)

        self.lf1 = Frame(self)
        self.lf1.pack()

        self.label1 = Label(self.lf1, text='Welcome to the Appointment View', font=('Arial', 12), fg='darkblue')
        self.label1.pack(side=TOP, pady=10)

        # Create sub frame lables and buttons
        self.lf0 = Frame(self.lf1)
        self.lf0.pack()
        self.label2 = Label(self.lf0, text='Please Select a Category to Select From', font=('Arial', 10), fg='black')
        self.label2.pack(side=TOP, pady=5)

        self.rbVal = StringVar()
        self.rb1 = Radiobutton(self.lf0, text="Patient", variable=self.rbVal, value=0)
        self.rb2 = Radiobutton(self.lf0, text="Doctor", variable=self.rbVal, value=1)
        self.rb3 = Radiobutton(self.lf0, text="Appt.Type", variable=self.rbVal, value=2)
        self.rb4 = Radiobutton(self.lf0, text="Appt.Date/Time", variable=self.rbVal, value=3)

        self.rb1.pack(side=LEFT, padx=5, pady=10)
        self.rb2.pack(side=LEFT, padx=5, pady=10)
        self.rb3.pack(side=LEFT, padx=5, pady=10)
        self.rb4.pack(side=LEFT, padx=5, pady=10)

        self.lf2 = Frame(self.lf1)
        self.lf2.pack()

        self.scroll = Scrollbar(self.lf2, orient=VERTICAL)
        self.select3 = Listbox(self.lf2, yscrollcommand=self.scroll.set, height=20, width=100, bg="lightgray", relief=SUNKEN)
        self.scroll.config(command=self.select3.yview)
        self.scroll.pack(side=RIGHT, pady=50,fill=Y)
        self.select3.pack(side=LEFT, pady=50)

        self.lf3 = Frame(self.lf1)
        self.lf3.pack()

        self.label31 = Label(self.lf3, text="PID:")
        self.label31.pack(side=LEFT, padx=5, pady=10)
        self.patidVar = StringVar()
        self.pid = Entry(self.lf3, textvariable=self.patidVar, width=6, bg='cyan', relief=SUNKEN)
        self.pid.pack(side=LEFT, pady=10)

        self.label3 = Label(self.lf3, text="First Name:")
        self.label3.pack(side=LEFT, padx=5, pady=10)
        self.pfnameVar = StringVar()
        self.pid = Entry(self.lf3, textvariable=self.pfnameVar, width=15, bg='cyan', relief=SUNKEN)
        self.pid.pack(side=LEFT, pady=10)

        self.label4 = Label(self.lf3, text="Last Name:")
        self.label4.pack(side=LEFT, padx=5, pady=10)
        self.plnameVar = StringVar()
        self.pid = Entry(self.lf3, textvariable=self.plnameVar, width=15, bg='cyan', relief=SUNKEN)
        self.pid.pack(side=LEFT, pady=10)

        self.label51 = Label(self.lf3, text="DRID:")
        self.label51.pack(side=LEFT, padx=5, pady=10)
        self.dridVar = StringVar()
        self.drid = Entry(self.lf3, textvariable=self.dridVar, width=6, bg='cyan', relief=SUNKEN)
        self.drid.pack(side=LEFT, pady=10)

        self.label5 = Label(self.lf3, text="Doctor Last:")
        self.label5.pack(side=LEFT, padx=5, pady=10)
        self.dlnameVar = StringVar()
        self.drlast = Entry(self.lf3, textvariable=self.dlnameVar, width=15, bg='cyan', relief=SUNKEN)
        self.drlast.pack(side=LEFT, pady=10)

        self.lf35 = Frame(self.lf1)
        self.lf35.pack()

        self.label62 = Label(self.lf35, text="RID:")
        self.label62.pack(side=LEFT,pady=10)
        self.reasidVar = StringVar()
        self.reasid = Entry(self.lf35, textvariable=self.reasidVar, width=6, bg='cyan', relief=SUNKEN)
        self.reasid.pack(side=LEFT, pady=10)

        self.label6 = Label(self.lf35, text="Reason:")
        self.label6.pack(side=LEFT, padx=5, pady=10)
        self.reasVar = StringVar()
        self.reason = Entry(self.lf35,textvariable=self.reasVar, width=15, bg='cyan', relief=SUNKEN)
        self.reason.pack(side=LEFT, pady=10)

        self.label63 = Label(self.lf35, text="DID:")
        self.label63.pack(side=LEFT, padx=5, pady=10)
        self.dateidVar = StringVar()
        self.dateid = Entry(self.lf35, textvariable=self.dateidVar, width=6, bg='cyan', relief=SUNKEN)
        self.dateid.pack(side=LEFT, pady=10)

        self.label64 = Label(self.lf35, text="Date:")
        self.label64.pack(side=LEFT, padx=5, pady=10)
        self.dateVar = StringVar()
        self.date = Entry(self.lf35, textvariable=self.dateVar, width=15, bg='cyan', relief=SUNKEN)
        self.date.pack(side=LEFT, pady=10)

        self.label65 = Label(self.lf35, text="TID:")
        self.label65.pack(side=LEFT, padx=5, pady=10)
        self.timeidVar = StringVar()
        self.timeid = Entry(self.lf35, textvariable=self.timeidVar, width=6, bg='cyan', relief=SUNKEN)
        self.timeid.pack(side=LEFT, pady=10)

        self.label65 = Label(self.lf35, text="Time:")
        self.label65.pack(side=LEFT, padx=5, pady=10)
        self.timeVar = StringVar()
        self.time = Entry(self.lf35, textvariable=self.timeVar, width=15, bg='cyan', relief=SUNKEN)
        self.time.pack(side=LEFT, pady=10)

        self.lf4 = Frame(self.lf1)
        self.lf4.pack()

        self.btn1 = Button(self.lf4, text="Get List", width=15, fg="black", bg="lightgray", relief=RAISED, command= self.setList)
        self.btn1.pack(side=LEFT, padx=5, pady=15)
        self.btn2 = Button(self.lf4, text="Load Selected", width=15, fg="black", bg="lightgray", relief=RAISED, command=self.loadRecord)
        self.btn2.pack(side=LEFT, padx=5, pady=15)
        self.btn3 = Button(self.lf4, text="Make Appt", width=15,fg="black", bg="lightgray", relief=RAISED, command=self.updateRecord)
        self.btn3.pack(side=LEFT, padx=5, pady=15)
        self.btn5 = Button(self.lf4, text="Show Appt", width=15, fg="black", bg="lightgray", relief=RAISED,command=lambda: master.switch_frame(ShowAppointment))
        self.btn5.pack(side=LEFT, padx=5, pady=15)
        self.btn5 = Button(self.lf4, text=" RETURN", width=15, fg="black", bg="lightgray", relief=RAISED, command=lambda: master.switch_frame(SelectTasks))
        self.btn5.pack(side=LEFT, padx=5, pady=15)
#
# Project : G&G Medical Database
# ShowAppointment
# Version: 1
# Date : April 18 2018
# Author: Paul Gierzynski
#
# This file acts as a self contained GUI Page or Frame
# when run in conjunction with GnGGuiMain
# This allows particular functionality to be provided page by page
# each pages is a separate class that is either brought to the foreground
# or destroyed as the user switches between gui functions.
# This panel contains the frame work to allow the user to view appointments by  patient, doctor, or week
# it also allows the user to cancel or close completed appointments
#
class ShowAppointment(Frame):
    global sqlResults

    def showByWeek(self):
        print('Building list of appointments for the week')

    # This fucntion tracks the current selection made by the user
    # and returns the index posotion of the record selected whenever it is called
    def selection(self):
        self.select4.curselection()
        print("At %s of %d" % (self.select4.curselection(), len(sqlResults)))
        return int(self.select4.curselection()[0])

    #
    # CLose the appointment once it is completed
    #
    def closeIt(self):
        dataIn= sqlResults[self.selection()]
        patient_id = self.patidVar.get()
        date_id = dataIn[6]
        start_time_id = dataIn[7]
        completeAppointmentRecord(patient_id, date_id,start_time_id)

    def cancelIt(self):
        dataIn= sqlResults[self.selection()]
        patient_id = self.patidVar.get()
        doctor_id = self.dridVar.get()
        date_id = dataIn[6]
        start_time_id = dataIn[7]
        cancelAppointmentRecord(patient_id,doctor_id, date_id, start_time_id)

    #
    # Load the values at the index of the GUI Listbox into the data entry fields
    #
    def myAppointments(self):
        global sqlResults
        try:
            value = self.rbVal.get()
            if value == "0":
                pid = self.patidVar.get()
                # Populate the listbox with all appointnments for patient
                sqlResults = showAppointmentRecordsPatient(pid)
                self.select4.delete(0, END)  # Clear the GUI listbox
                for d1,d2,d3,d4,d5,d6,d7,d8 in sqlResults:
                    print(d1,d2,d3,d4,d5,d6,d7,d8)
                    patient = d1,d2,d3,d4,d5,d6,d7,d8
                    self.select4.insert(END, patient)  # Populate the Listbox
            elif value == "1":
                pid = self.dridVar.get()
                # Populate the listbox with all appoitnments for patient
                sqlResults = showAppointmentRecordsDoc(pid)
                #qlResults.sort(key=lambda x: x[1])  # Sort on name field
                self.select4.delete(0, END)  # Clear the GUI listbox
                for d1,d2,d3,d4,d5,d6,d7,d8 in sqlResults:
                    print(d1,d2,d3,d4,d5,d6,d7)
                    doctor = d1,d2,d3,d4,d5,d6,d8
                    self.select4.insert(END, (doctor))  # Populate the Listbox
            elif value == "2":
                sqlResults = showAppointmentRecordsAll()
                self.select4.delete(0, END)  # Clear the GUI listbox
                for d1,d2,d3,d4,d5,d6,d7,d8 in sqlResults:
                    print(d1,d2,d3,d4,d5,d6,d7,d8)
                    allapt = d1,d2,d3,d4,d5,d6,d7,d8
                    self.select4.insert(END, (allapt))  # Populate the Listbox
        except TypeError:  # catch list box cursor selection errors
                messagebox.showerror('Item Selection failed', 'Please re-select contact')
                self.setList()
        except IndexError:
                messagebox.showerror('Item Selection failed', 'Please re-select contact')
                self.setList()

    #
    # Load the value at the index of the GUI Listbox into the data entry fields
    #
    def loadRecord(self):
        value = self.rbVal.get()
        try:
            if value == "0":
                pid, pfname, plname = sqlResults[self.selection()]
                self.patidVar.set(pid)
                self.pfnameVar.set(pfname)
                self.plnameVar.set(plname)
            elif value == "1":
                pid, dfname, dlname = sqlResults[self.selection()]
                self.dridVar.set(pid)
                self.dlnameVar.set(dlname)
            elif value == "2":
                pid, condition, stuff = sqlResults[self.selection()]
                self.reasidVar.set(pid)
                self.reasVar.set(condition)
            elif value == "3":
                doctor, dpid, day, tpid, time, = sqlResults[self.selection()]
                self.dateidVar.set(dpid)
                self.dateVar.set(day)
                self.timeidVar.set(tpid)
                self.timeVar.set(time)
        except TypeError:  # catch list box cursor selection errors
            messagebox.showerror('Item Selection failed', 'Please re-select contact')
            self.setList()
        except IndexError:
            messagebox.showerror('Item Selection failed', 'Please re-select contact')
            self.setList()
        except ValueError:
            messagebox.showinfo("Error!", "You Must Select a Category First!")
    #
    # Populate the GUI Listbox with the selected records
    #
    def setList(self):
        global sqlResults
        try:
            # Send sqlRequest for records specified by radio button
            value = self.rbVal.get()
            if value == "0":
                table = "Patient"
                sqlResults = readRecordAll(table)
                sqlResults.sort(key=lambda x: x[1])  # Sort on name field
                self.select4.delete(0, END)  # Clear the GUI listbox
                for pid, fname, lname in sqlResults:
                    print(pid, fname, lname)
                    patient = fname, lname
                    self.select4.insert(END, (patient))  # Populate the Listbox
            elif value == "1":
                    table = 'Doctor'
                    sqlResults = readRecordAll(table)
                    sqlResults.sort(key=lambda x: x[1])  # Sort on name field
                    self.select4.delete(0, END)  # Clear the GUI listbox
                    for pid, fname, lname in sqlResults:
                        print(pid, fname, lname)
                        self.select4.insert(END, (lname))  # Populate the Listbox
            elif value == "2":
                sqlResults = showAppointmentRecordsAll()
                sqlResults.sort(key=lambda x: x[1])  # Sort on name field
                self.select4.delete(0, END)  # Clear the GUI listbox
                for pid, fname, lname in sqlResults:
                    print(pid, fname, lname)
                    bydoctor = fname, lname
                    self.select4.insert(END, (bydoctor))
        except ValueError:
            messagebox.showinfo("Error!", "You Must Select a Category First!")

    def __init__(self, master):
        Frame.__init__(self, master)

        self.lf1 = Frame(self)
        self.lf1.pack()

        self.label1 = Label(self.lf1, text='Welcome to the Appointment View - Confirmed Appointments', font=('Arial', 12), fg='darkblue')
        self.label1.pack(side=TOP, pady=15)

        # Create sub frame labels and buttons
        self.lf0 = Frame(self.lf1)
        self.lf0.pack()
        self.label2 = Label(self.lf0, text='Please Select a Category to View', font=('Arial', 10), fg='black')
        self.label2.pack(side=TOP, pady=5)

        self.rbVal = StringVar()
        self.rb1 = Radiobutton(self.lf0, text="Patient", variable=self.rbVal, value=0)
        self.rb2 = Radiobutton(self.lf0, text="Doctor", variable=self.rbVal, value=1)
        self.rb3 = Radiobutton(self.lf0, text="Weekly", variable=self.rbVal, value=2)

        self.rb1.pack(side=LEFT, padx=5, pady=10)
        self.rb2.pack(side=LEFT, padx=5, pady=10)
        self.rb3.pack(side=LEFT, padx=5, pady=10)

        self.lf2 = Frame(self.lf1)
        self.lf2.pack()

        self.scroll = Scrollbar(self.lf2, orient=VERTICAL)
        self.select4 = Listbox(self.lf2, yscrollcommand=self.scroll.set, height=20, width=100, bg="lightgray", relief=SUNKEN)
        self.scroll.config(command=self.select4.yview)
        self.scroll.pack(side=RIGHT, pady=50,fill=Y)
        self.select4.pack(side=LEFT, pady=50)

        # Create subframe for data entry
        self.lf3 = Frame(self.lf1)
        self.lf3.pack()

        self.label31 = Label(self.lf3, text="PID:")
        self.label31.pack(side=LEFT, padx=5, pady=10)
        self.patidVar = StringVar()
        self.pid = Entry(self.lf3, textvariable=self.patidVar, width=6, bg='cyan', relief=SUNKEN)
        self.pid.pack(side=LEFT, pady=10)

        self.label3 = Label(self.lf3, text="First Name:")
        self.label3.pack(side=LEFT, padx=5, pady=10)
        self.pfnameVar = StringVar()
        self.pid = Entry(self.lf3, textvariable=self.pfnameVar, width=15, bg='cyan', relief=SUNKEN)
        self.pid.pack(side=LEFT, pady=10)

        self.label4 = Label(self.lf3, text="Last Name:")
        self.label4.pack(side=LEFT, padx=5, pady=10)
        self.plnameVar = StringVar()
        self.pid = Entry(self.lf3, textvariable=self.plnameVar, width=15, bg='cyan', relief=SUNKEN)
        self.pid.pack(side=LEFT, pady=10)

        self.label51 = Label(self.lf3, text="DRID:")
        self.label51.pack(side=LEFT, padx=5, pady=10)
        self.dridVar = StringVar()
        self.drid = Entry(self.lf3, textvariable=self.dridVar, width=6, bg='cyan', relief=SUNKEN)
        self.drid.pack(side=LEFT, pady=10)

        self.label5 = Label(self.lf3, text="Doctor Last:")
        self.label5.pack(side=LEFT, padx=5, pady=10)
        self.dlnameVar = StringVar()
        self.drlast = Entry(self.lf3, textvariable=self.dlnameVar, width=15, bg='cyan', relief=SUNKEN)
        self.drlast.pack(side=LEFT, pady=10)

        # Create subframe for buttons
        self.lf4 = Frame(self.lf1)
        self.lf4.pack()

        self.btn1 = Button(self.lf4, text="GetList", width=15, fg="black", bg="lightgray", relief=RAISED,
                           command=self.setList)
        self.btn1.pack(side=LEFT, padx=5, pady=15)

        self.btn2 = Button(self.lf4, text="Load Selected", width=15, fg="black", bg="lightgray", relief=RAISED,
                           command=self.loadRecord)
        self.btn2.pack(side=LEFT, padx=5, pady=15)

        self.btn3 = Button(self.lf4, text="Show Appt", width=15, fg="black", bg="lightgray", relief=RAISED,
                           command=self.myAppointments)
        self.btn3.pack(side=LEFT, padx=5, pady=15)

        self.btn4 = Button(self.lf4, text="Cancel Appt", width=15, fg="black", bg="lightgray", relief=RAISED,
                           command=self.cancelIt)
        self.btn4.pack(side=LEFT, padx=5, pady=15)

        self.btn5 = Button(self.lf4, text="Close Appt", width=15, fg="black", bg="lightgray", relief=RAISED,
                           command=self.closeIt)
        self.btn5.pack(side=LEFT, padx=5, pady=15)

        self.btn6 = Button(self.lf4, text=" RETURN", width=15, fg="black", bg="lightgray", relief=RAISED,
                           command=lambda: master.switch_frame(SelectTasks))
        self.btn6.pack(side=LEFT, padx=5, pady=15)

        # End of Show Appointments Panel

#
# Run the Gui Main
#
if __name__ == "__main__":

    app = MainView() # Launch the app
    app.title("G & G Medical Group LLC") # Title the Main Frame
    app.update_idletasks()
    # Determine center of screen for any monitor
    sh = app.winfo_screenheight()
    sw = app.winfo_screenwidth()
    w = 1000
    h = 700
    x = (sw / 2) - (w / 2)
    y = (sh / 2) - (h / 2)
    # Set the screen position and run the mainloop
    app.geometry('%dx%d+%d+%d' % (w, h, x, y))
    app.mainloop()
