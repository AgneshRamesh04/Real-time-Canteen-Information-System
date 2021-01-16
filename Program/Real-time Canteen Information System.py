#Group Name: CM1, Team 1 : Agnesh Ramesh, Anil Ankitha, Chandrasekhar Aditya
#Installation of PyQt5 and Panda is Required
#Runs better on 1920x1020 Resolution


from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import *
from PyQt5.QtWidgets import QMessageBox
import pandas as pd
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #--------------------------------------------MAIN WINDOW-------------------------------------------

        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(1200,800) 
        MainWindow.setMaximumSize(1200,800) #Setting the minimum and maximum size of window to avoid resizing by user
        MainWindow.setWindowTitle("NTU Canteen System") #Setting the Main Window Name

        icon = QtGui.QIcon() 
        icon.addPixmap(QtGui.QPixmap("image002.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off) 
        MainWindow.setWindowIcon(icon) #Setting the NTU logo as the icon in the MainWindow bar 

        self.centralwidget = QtWidgets.QWidget(MainWindow) #Creating a central widget which is the focus of the main window

        self.frame = QtWidgets.QFrame(self.centralwidget) #Creating a frame for the main window 
        self.frame.setGeometry(QtCore.QRect(0, 0, 1200, 800)) #Setting the size of the frame 

        self.bgpic = QtWidgets.QLabel(self.frame) #Creating the Background picture object
        self.bgpic.setGeometry(QtCore.QRect(-10, -470, 1250, 1500)) # Setting the size of the background picture object
        self.bgpic.setPixmap(QtGui.QPixmap("image001.jpg")) #Retrieving the image
        self.bgpic.setScaledContents(True) #Scaling contents according to the frame

        self.Ntulogo = QtWidgets.QLabel(self.frame)
        self.Ntulogo.setGeometry(QtCore.QRect(525, 180, 121, 141))
        self.Ntulogo.setPixmap(QtGui.QPixmap("image002.png"))
        self.Ntulogo.setScaledContents(True)

        font = QtGui.QFont() #Setting the font for WELCOME 
        font.setFamily("Futura") #Font type
        font.setPointSize(24) #Font size
        font.setBold(True)  #Bold

        self.Welcome = QtWidgets.QLabel(self.frame)
        self.Welcome.setGeometry(QtCore.QRect(125, 350, 900, 75))
        self.Welcome.setFont(font)
        self.Welcome.setAutoFillBackground(True) #Filling the background of WELCOME
        self.Welcome.setFrameShape(QtWidgets.QFrame.Box) 
        self.Welcome.setFrameShadow(QtWidgets.QFrame.Raised) #Setting border to the WELCOME object    
        self.Welcome.setText("   Welcome to NTU Canteen System") #The Text inside WELCOME Object

        self.Continuebutton = QtWidgets.QPushButton(self.frame)
        self.Continuebutton.setGeometry(QtCore.QRect(515, 440, 141, 31))
        self.Continuebutton.setText("Press to Continue")
        self.Continuebutton.setShortcut("Return") #Setting shortcut so button is activated when ENTER is pressed on the keyboard
    
        #--------------------------------------------MENU and TAB WINDOW-------------------------------------------

        MainWindow.setCentralWidget(self.centralwidget) #Creating central widget in main window

        self.frame1 = QtWidgets.QFrame(self.centralwidget) #Creating the frame of MENU Window
        self.frame1.setGeometry(QtCore.QRect(0, 0, 1200, 800))

        self.tabWidget = QtWidgets.QTabWidget(self.frame1) #Creating the frame for the Tabs
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 750, 620))#Setting size of the frame
        self.tabWidget.setIconSize(QtCore.QSize(20,20)) #Setting size of the Icon 
        
        self.labelfont = QtGui.QFont() #Setting the LABEL FONT for Menu Window
        self.labelfont.setFamily("Lucida Bright") 
        self.labelfont.setPointSize(15)
        self.labelfont.setBold(True)

        self.textfont = QtGui.QFont() #Setting the TEXT FONT for Menu Window
        self.textfont.setFamily("Sylfaen")
        self.textfont.setPointSize(11)

        #----------------------------------------MCDONALDS TAB-------------------------------------
        

        self.McD = QtWidgets.QWidget()
        icon = QtGui.QIcon() #Creating the icon for McD Tab 
        icon.addPixmap(QtGui.QPixmap("McDonalds logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.McD,icon,"McDonalds") #Creating the McDonalds Tab

        self.mcdbgpic = QtWidgets.QLabel(self.McD) #Creating McD Background picture
        self.mcdbgpic.setGeometry(QtCore.QRect(-150, -50, 975,850)) #Setting the size of the background picture
        self.mcdbgpic.setPixmap(QtGui.QPixmap("McDonalds bg.jpg")) #Retrieving the background picture
        self.mcdbgpic.setScaledContents(True) #Scaling the background picture for entire proportion

        self.mcdlogo = QtWidgets.QLabel(self.McD) #Creating McD Logo
        self.mcdlogo.setGeometry(QtCore.QRect(320, 20, 131, 111)) 
        self.mcdlogo.setPixmap(QtGui.QPixmap("McDonalds logo.png")) 
        self.mcdlogo.setScaledContents(True) 

        self.mcdmenu = QtWidgets.QLabel(self.McD) #Creating Mcd Menu Title
        self.mcdmenu.setGeometry(QtCore.QRect(105, 160, 186, 41))
        self.mcdmenu.setFont(self.labelfont) #Setting the font for McD Menu Title object
        self.mcdmenu.setAutoFillBackground(True) #Filling the background of McD Menu Title
        self.mcdmenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mcdmenu.setFrameShadow(QtWidgets.QFrame.Raised)  #Setting border to the McD Menu Title Object
        self.mcdmenu.setText("    Menu    ") #The Text inside McD Menu Title Object

        self.mcdmenutext = QtWidgets.QTextEdit(self.McD) #Creating McD Menu
        self.mcdmenutext.setGeometry(QtCore.QRect(70, 220, 295, 225))
        self.mcdmenutext.setFont(self.textfont)
        self.mcdmenutext.setAutoFillBackground(True)
        self.mcdmenutext.setReadOnly(True)

        self.mcdprice = QtWidgets.QLabel(self.McD) #Creating McD Price Title
        self.mcdprice.setGeometry(QtCore.QRect(440, 160, 186, 41))
        self.mcdprice.setFont(self.labelfont)
        self.mcdprice.setAutoFillBackground(True)
        self.mcdprice.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mcdprice.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mcdprice.setText("    Price   ")

        self.mcdpricetext = QtWidgets.QTextEdit(self.McD) #Creating McD Prices
        self.mcdpricetext.setGeometry(QtCore.QRect(435, 220, 200, 225))
        self.mcdpricetext.setFont(self.textfont)
        self.mcdpricetext.setReadOnly(True)
        
        #-----------------------------------------PIZZA HUT EXPRESS TAB----------------------------------------

        self.PizzaHut = QtWidgets.QWidget()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Pizza Hut Express logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.PizzaHut,icon, "Pizza Hut Express")

        self.pizzabgpic = QtWidgets.QLabel(self.PizzaHut)
        self.pizzabgpic.setGeometry(QtCore.QRect(-150, -50, 975,850))
        self.pizzabgpic.setPixmap(QtGui.QPixmap("Pizza Hut Express bg.jpg"))
        self.pizzabgpic.setScaledContents(True)

        self.pizzalogo = QtWidgets.QLabel(self.PizzaHut)
        self.pizzalogo.setGeometry(QtCore.QRect(320, 30, 140, 120))
        self.pizzalogo.setAutoFillBackground(False)
        self.pizzalogo.setPixmap(QtGui.QPixmap("Pizza Hut Express logo.png"))
        self.pizzalogo.setScaledContents(True)

        self.pizzamenu = QtWidgets.QLabel(self.PizzaHut)
        self.pizzamenu.setGeometry(QtCore.QRect(105, 160, 186, 41))
        self.pizzamenu.setFont(self.labelfont)
        self.pizzamenu.setAutoFillBackground(True)
        self.pizzamenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pizzamenu.setFrameShadow(QtWidgets.QFrame.Raised) 
        self.pizzamenu.setText("    Menu    ") 

        self.pizzamenutext = QtWidgets.QTextEdit(self.PizzaHut)
        self.pizzamenutext.setGeometry(QtCore.QRect(70, 220, 255, 225))
        self.pizzamenutext.setFont(self.textfont)
        self.pizzamenutext.setReadOnly(True)

        self.pizzaprice = QtWidgets.QLabel(self.PizzaHut)
        self.pizzaprice.setGeometry(QtCore.QRect(440, 160, 186, 41))
        self.pizzaprice.setFont(self.labelfont)
        self.pizzaprice.setAutoFillBackground(True)
        self.pizzaprice.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pizzaprice.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pizzaprice.setText("    Price   ")    
        
        self.pizzapricetext = QtWidgets.QTextEdit(self.PizzaHut)
        self.pizzapricetext.setGeometry(QtCore.QRect(435, 220, 200, 225))
        self.pizzapricetext.setFont(self.textfont)
        self.pizzapricetext.setReadOnly(True)
        
        #-----------------------------------------BAKERY CUISINE TAB------------------------------------------

        self.Bakery = QtWidgets.QWidget()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Bakery Cuisine logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Bakery,icon, "Bakery Cuisine")

        self.bakerybgpic = QtWidgets.QLabel(self.Bakery)
        self.bakerybgpic.setGeometry(QtCore.QRect(-150, -50, 975,850))
        self.bakerybgpic.setPixmap(QtGui.QPixmap("Bakery Cuisine bg.jpg"))
        self.bakerybgpic.setScaledContents(True)

        self.bakerylogo = QtWidgets.QLabel(self.Bakery)
        self.bakerylogo.setGeometry(QtCore.QRect(250, -15, 250, 220))
        self.bakerylogo.setPixmap(QtGui.QPixmap("Bakery Cuisine logo.png"))
        self.bakerylogo.setScaledContents(True)

        self.bakerymenu = QtWidgets.QLabel(self.Bakery)
        self.bakerymenu.setGeometry(QtCore.QRect(105, 160, 186, 41))
        self.bakerymenu.setFont(self.labelfont)
        self.bakerymenu.setAutoFillBackground(True)
        self.bakerymenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bakerymenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bakerymenu.setText("    Menu    ")

        self.bakerymenutext = QtWidgets.QTextEdit(self.Bakery)
        self.bakerymenutext.setGeometry(QtCore.QRect(70, 220, 258, 225))
        self.bakerymenutext.setFont(self.textfont)
        self.bakerymenutext.setReadOnly(True)

        self.bakeryprice = QtWidgets.QLabel(self.Bakery)
        self.bakeryprice.setGeometry(QtCore.QRect(440, 160, 186, 41))
        self.bakeryprice.setFont(self.labelfont)
        self.bakeryprice.setAutoFillBackground(True)
        self.bakeryprice.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bakeryprice.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bakeryprice.setText("    Price   ")

        self.bakerypricetext = QtWidgets.QTextEdit(self.Bakery)
        self.bakerypricetext.setGeometry(QtCore.QRect(435, 220, 200, 225))
        self.bakerypricetext.setFont(self.textfont)
        self.bakerypricetext.setReadOnly(True)
        
        #---------------------------------------------MINI WOK TAB-------------------------------------------

        self.Miniwok = QtWidgets.QWidget()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("MiniWok logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Miniwok,icon, "MiniWok")

        self.wokbgpic = QtWidgets.QLabel(self.Miniwok)
        self.wokbgpic.setGeometry(QtCore.QRect(-150, -50, 975,850))
        self.wokbgpic.setPixmap(QtGui.QPixmap("MiniWok bg.jpg"))
        self.wokbgpic.setScaledContents(True)

        self.woklogo = QtWidgets.QLabel(self.Miniwok)
        self.woklogo.setGeometry(QtCore.QRect(280, -10, 210, 190))
        self.woklogo.setAutoFillBackground(False)
        self.woklogo.setPixmap(QtGui.QPixmap("MiniWok logo.png"))
        self.woklogo.setScaledContents(True)

        self.wokmenu = QtWidgets.QLabel(self.Miniwok)
        self.wokmenu.setGeometry(QtCore.QRect(105, 160, 186, 41))
        self.wokmenu.setFont(self.labelfont)
        self.wokmenu.setAutoFillBackground(True)
        self.wokmenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wokmenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wokmenu.setText("    Menu    ")

        self.wokmenutext = QtWidgets.QTextEdit(self.Miniwok)
        self.wokmenutext.setGeometry(QtCore.QRect(70, 220, 280, 225))
        self.wokmenutext.setFont(self.textfont)
        self.wokmenutext.setReadOnly(True)

        self.wokprice = QtWidgets.QLabel(self.Miniwok)
        self.wokprice.setGeometry(QtCore.QRect(440, 160, 186, 41))
        self.wokprice.setFont(self.labelfont)
        self.wokprice.setAutoFillBackground(True)
        self.wokprice.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wokprice.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wokprice.setText("    Price   ")

        self.wokpricetext = QtWidgets.QTextEdit(self.Miniwok)
        self.wokpricetext.setGeometry(QtCore.QRect(435, 220, 200, 225))
        self.wokpricetext.setFont(self.textfont)
        self.wokpricetext.setReadOnly(True)
        
        #------------------------------------------DRINKS STALL TAB-----------------------------------------

        self.beverage = QtWidgets.QWidget()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Beverages logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.beverage,icon, "Beverages")

        self.drinksbgpic = QtWidgets.QLabel(self.beverage)
        self.drinksbgpic.setGeometry(QtCore.QRect(-150, -50, 975,850))
        self.drinksbgpic.setPixmap(QtGui.QPixmap("Beverages bg.jpg"))
        self.drinksbgpic.setScaledContents(True)

        self.drinkslogo = QtWidgets.QLabel(self.beverage)
        self.drinkslogo.setGeometry(QtCore.QRect(280, 0, 200, 180))
        self.drinkslogo.setPixmap(QtGui.QPixmap("Beverages logo.png"))
        self.drinkslogo.setScaledContents(True)

        self.drinkmenu = QtWidgets.QLabel(self.beverage)
        self.drinkmenu.setGeometry(QtCore.QRect(105, 160, 186, 41))
        self.drinkmenu.setFont(self.labelfont)
        self.drinkmenu.setAutoFillBackground(True)
        self.drinkmenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.drinkmenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.drinkmenu.setText("    Menu    ")

        self.drinkmenutext = QtWidgets.QTextEdit(self.beverage)
        self.drinkmenutext.setGeometry(QtCore.QRect(70, 220, 255, 225))
        self.drinkmenutext.setFont(self.textfont)
        self.drinkmenutext.setReadOnly(True)

        self.drinkprice = QtWidgets.QLabel(self.beverage)
        self.drinkprice.setGeometry(QtCore.QRect(440, 160, 186, 41))
        self.drinkprice.setFont(self.labelfont)
        self.drinkprice.setAutoFillBackground(True)
        self.drinkprice.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.drinkprice.setFrameShadow(QtWidgets.QFrame.Raised)
        self.drinkprice.setText("    Price   ")

        self.drinkpricetext = QtWidgets.QTextEdit(self.beverage)
        self.drinkpricetext.setGeometry(QtCore.QRect(435, 220, 200, 225))
        self.drinkpricetext.setFont(self.textfont)
        self.drinkpricetext.setTabChangesFocus(False)
        self.drinkpricetext.setReadOnly(True)

        #--------------------------------------------DATE AND TIME FRAME---------------------------------------------

        self.TimeDate = QtWidgets.QFrame(self.frame1) #Creating the time and date frame in MENU Window

        self.TimeDate.setGeometry(QtCore.QRect(750, 30, 425, 600)) 
        self.TimeDate.setFrameShape(QtWidgets.QFrame.Box)
        self.TimeDate.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TimeDate.setLineWidth(9) 
        self.TimeDate.setToolTip("Edit Time to View Menus On Different Time") #Setting tool tip such that this message is displayed on the frame

        self.Calenderbg = QtWidgets.QLabel(self.TimeDate) # Creating Calender background
        self.Calenderbg.setGeometry(QtCore.QRect(13, 13, 403, 578))
        self.Calenderbg.setPixmap(QtGui.QPixmap("timebg.jpg"))
        self.Calenderbg.setScaledContents(True)


        self.Calender = QtWidgets.QCalendarWidget(self.TimeDate) #Creating the Calender Widget
        self.Calender.setGeometry(QtCore.QRect(13, 275,400, 250))
        self.Calender.setToolTip("Select the Date") #Setting tool tip such that this message is displayed on the frame
        now = date.today() #Function to get the present date
        self.Calender.setMinimumDate(QtCore.QDate(now)) #To set minimum date as present date so user cannot accept a date before

        self.Resettimebutton = QtWidgets.QPushButton(self.TimeDate) #Creating the reset time button
        self.Resettimebutton.setGeometry(QtCore.QRect(150, 210, 112, 32))
        self.Resettimebutton.setText("Reset Time")
                
        self.minutecombobox = QtWidgets.QComboBox(self.TimeDate) #Creating the minute box to select time
        self.minutecombobox.setGeometry(QtCore.QRect(230, 170, 80, 30))
        for i in range(0,60): #To add the items in the minute combo box
            self.minutecombobox.addItem(str(i))
            
        self.hourcombobox = QtWidgets.QComboBox(self.TimeDate) #Creating the hour box to select time
        self.hourcombobox.setGeometry(QtCore.QRect(230, 130, 80, 30))
        for i in range(0,24):  #To add the items in the hour combo box
            self.hourcombobox.addItem(str(i))
            
        self.hours = QtWidgets.QLabel(self.TimeDate) #Creating the hours text
        self.hours.setGeometry(QtCore.QRect(70, 130, 130, 26))
        self.hours.setFont(self.textfont)
        self.hours.setText("   Hours:")

        self.minutes = QtWidgets.QLabel(self.TimeDate) #Creating the minute text
        self.minutes.setGeometry(QtCore.QRect(70, 170, 130, 26))
        self.minutes.setFont(self.textfont)      
        self.minutes.setText("   Minutes:")

        self.Time = QtWidgets.QLabel(self.TimeDate) #Creating the Time Title
        self.Time.setGeometry(QtCore.QRect(70, 80, 275, 35))
        self.Time.setAutoFillBackground(True)
        self.Time.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Time.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Time.setFont(self.labelfont)
        self.Time.setText("          Time")

        self.Backbutton = QtWidgets.QPushButton(self.TimeDate) #Creating the Back button to go back to the Main Window
        self.Backbutton.setGeometry(QtCore.QRect(235, 555, 112, 32))
        self.Backbutton.setText("Back")
        self.Backbutton.setShortcut("Backspace") #Creating the shortcut when backspace is pressed button is activated
        self.Backbutton.setToolTip("Press to go to Main Window") #Setting tool tip such that this message is displayed on the frame
        
        #---------------------------------------------STORE INFORMATION FRAME---------------------------------------
        
        self.storeinfo = QtWidgets.QFrame(self.frame1) #Creating Store Information frame
        self.storeinfo.setGeometry(QtCore.QRect(0, 635, 540, 141))
        self.storeinfo.setFrameShape(QtWidgets.QFrame.Panel)
        self.storeinfo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.storeinfo.setLineWidth(13)
        self.storeinfo.setToolTip("Store Information")

        self.storeinfobg = QtWidgets.QLabel(self.storeinfo) #Creating Store information background picture
        self.storeinfobg.setGeometry(QtCore.QRect(13, 15, 514, 114))
        self.storeinfobg.setPixmap(QtGui.QPixmap("storeinfobg.jpg"))
        self.storeinfobg.setScaledContents(True)

        self.Storeinfo = QtWidgets.QLabel(self.storeinfo) #Creating Store information Title
        self.Storeinfo.setGeometry(QtCore.QRect(60, 40, 400, 35))
        self.Storeinfo.setFont(self.labelfont)
        self.Storeinfo.setAutoFillBackground(True)
        self.Storeinfo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Storeinfo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Storeinfo.setText("       Store Information")

        self.storeinfo = QtWidgets.QPushButton(self.storeinfo) #Creating Store information button
        self.storeinfo.setGeometry(QtCore.QRect(150, 80, 215, 30))
        self.storeinfo.setText("Press for Store Information")
        self.storeinfo.setShortcut("Ctrl+I") #Creating the shortcut when Ctrl+I is pressed button is activated

        #-------------------------------------------------WAITING TIME FRAME----------------------------------------
        
        self.Waitingtime = QtWidgets.QFrame(self.frame1) #Creating Waiting Time frame
        self.Waitingtime.setGeometry(QtCore.QRect(540, 635, 638, 141))
        self.Waitingtime.setFrameShape(QtWidgets.QFrame.Panel)
        self.Waitingtime.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Waitingtime.setLineWidth(13)

        self.Waitingtimebg = QtWidgets.QLabel(self.Waitingtime) #Creating waiting time background picture
        self.Waitingtimebg.setGeometry(QtCore.QRect(13, 15, 612, 114))
        self.Waitingtimebg.setLineWidth(-2)
        self.Waitingtimebg.setPixmap(QtGui.QPixmap("waitingbg.jpg"))
        self.Waitingtimebg.setScaledContents(True)

        self.waitingtime = QtWidgets.QLabel(self.Waitingtime) #Creating Waiting Time Title
        self.waitingtime.setGeometry(QtCore.QRect(180, 30, 305, 40))
        self.waitingtime.setFont(self.labelfont)
        self.waitingtime.setAutoFillBackground(True)
        self.waitingtime.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.waitingtime.setFrameShadow(QtWidgets.QFrame.Raised)
        self.waitingtime.setText("      Waiting Time")

        self.numberofppl = QtWidgets.QLabel(self.Waitingtime) #Creating Number of people text
        self.numberofppl.setGeometry(QtCore.QRect(70, 75, 500, 40))
        self.numberofppl.setFont(self.textfont)
        self.numberofppl.setText("   Enter the number of people:")

        self.numberofppltext = QtWidgets.QLineEdit(self.Waitingtime) #Creating text to input the number of people
        self.numberofppltext.setGeometry(QtCore.QRect(380, 86, 91, 30))

        self.Continuewaitingtimebutton = QtWidgets.QPushButton(self.Waitingtime) #Creating the continue button to display waiting time
        self.Continuewaitingtimebutton.setGeometry(QtCore.QRect(500, 86, 112, 32))
        self.Continuewaitingtimebutton.setText("Continue")
        self.Continuewaitingtimebutton.setShortcut( "Return") #Creating the shortcut when Enter is pressed button is activated

    #--------------------------------------------------------------------------------------------------------------------------------------------------

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.cur_time()
        self.frame1.hide()

        self.Continuebutton.clicked.connect(self.go)
        self.Backbutton.clicked.connect(self.back)
        self.Resettimebutton.clicked.connect(self.cur_time)
        self.Calender.clicked.connect(self.updatemenu)
        self.storeinfo.clicked.connect(lambda : self.dispinfo("display"))
        self.Continuewaitingtimebutton.clicked.connect(self.waiting_time)

        self.timer=QtCore.QTimer() # Creates a QTimer
        self.timer.timeout.connect(self.clock_dis) # Call the function clock_dis at every time out of the timer
        self.timer.start(1000)       # Starts the Timer at an interval of 1000ms 

        self.tabWidget.currentChanged.connect(self.updatemenu)
        self.hourcombobox.currentIndexChanged.connect(self.updatemenu)
        self.minutecombobox.currentIndexChanged.connect(self.updatemenu)
                
    #-------------------------------------------------------USER DEFINED FUNCTIONS--------------------------------------------------------------------

    def go(self): #Function to continue to the Main Menu Frame
        self.frame1.show() #Displays the Main menu Frame
        self.frame.hide() #Hides the Welcome Frame
        self.cur_time()  #Update Current time
        self.updatemenu() #Update menu according to current time


    def back(self): #Function to go Back to Welcome Frame
        self.frame.show() #Hides the Main menu Frame
        self.frame1.hide() #Displays the Welcome Frame
        MainWindow.setWindowTitle("NTU Canteen System") #Set the Window Title
        

    def cur_time(self):
        now = date.today() #Built-in function to find current date
        self.Calender.setSelectedDate(QtCore.QDate(now)) #Current date is automatically set into calender
        
        now = datetime.now() #Built-in function to find current time
        to = now.strftime("%H") #Changing the format of time into hours
        self.hourcombobox.setCurrentIndex((int(to))) #Setting current hour in combo box
        
        to = now.strftime("%M") #Changing the format of time into minutes
        self.minutecombobox.setCurrentIndex((int(to))) #Setting current minute in combo box
    
    def clock_dis(self): #Function to update current time
        now = datetime.now()
        time = now.strftime("%H:%M:%S") #Changing the format to hour:minute:second
        self.Time.setText("  Time -  " + str(time)) #Setting the updated Current time to the label
        

    def stalls(self): #Function to store value of menu

        data = pd.read_csv("stall_menu.csv") #Reading data saved in excel format

        McD_morn = list(data['Before 12PM'].values[0].split(", ")) #Creating a list by splitting values within table
        McD_eve = list(data['After 12PM'].values[0].split(", "))

        Pizza_Hut = list(data['Same menu'].values[1].split(", "))

        Mini_wok_weekday = list(data['Same menu'].values[2].split(", "))
        Mini_wok_weekend = list(data['Same menu'].values[3].split(", "))

        Juice_shop = list(data['Same menu'].values[4].split(", "))

        Bakery_cuisine = list(data['Same menu'].values[5].split(", "))

        menu={"Mcd1":McD_morn,"Mcd2":McD_eve,"Pizza Hut Express":Pizza_Hut,
              "MiniWok1":Mini_wok_weekday,"MiniWok2":Mini_wok_weekend,
              "Beverages":Juice_shop,"Bakery Cuisine":Bakery_cuisine} #Creating dictionary of stall menu with stall name:list of menu
        return menu

    def updatemenu(self): #Changing the menu according to tab, time and date
        
        store = self.tabWidget.tabText(self.tabWidget.currentIndex()) #Assigning the value of current tab to variable store
        MainWindow.setWindowTitle(store +" Menu") #Setting the Menu title depending on tab

        hr = self.hourcombobox.currentIndex() #Retrieving time from combo box
       	mint = self.minutecombobox.currentIndex() #Retrieving time from combo box
       	time = hr * 100 + mint 

        if self.Calender.selectedDate() == self.Calender.minimumDate() and time < int(datetime.now().strftime("%H%M")): 
        #Checking whether the input time and date have lapsed
        	if ( int(datetime.now().strftime("%H%M")) - time ) < 5: #If the difference b/w current and input time is lesser than 5 minutes
        		self.cur_time() #Set to current time
        		return
        	else:
        		errormsg=QMessageBox() #Popup message to show error
		        errormsg.setWindowTitle("Wrong Time")
		        errormsg.setText("The Selected Time has Lapsed. The Time Has Been Reset to Current Time")
		        errormsg.setIcon(QMessageBox.Critical)
		        errormsg.setStandardButtons(QMessageBox.Ok)
		        x=errormsg.exec_()
		        self.cur_time() #Set back to current time
		        return
	        
       
        bol = self.dispinfo("no") #To check if the stall is still open or not

        if bol:
            stall = self.stalls() #Calling stall() function
            stall_names = ["Mcd1","Mcd2","MiniWok1","MiniWok2"]

            if hr < 12: 
                stall_names.pop(1) #Remove Mcd2 - Afternoon and evening menu
            elif hr >= 12:
                stall_names.pop(0) #Remove Mcd1 - Morning Menu

            weekdays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday") #Days in a week
            day = weekdays[self.Calender.selectedDate().dayOfWeek() - 1] #Finding the day selected in the calendar

            if day == "Saturday" or day=="Sunday": 
                stall_names.remove("MiniWok1") #Remove Weekday Menu
            else:
                stall_names.remove("MiniWok2") #Remove Weekend Menu

            cnt = 1
            menutext,pricetext = "","" 

            if store=="McDonalds": #McDonalds
                
                for x in stall[stall_names[0]]: #Loop through each item in  McDonalds menu
                    for i in x.split(":"): #Splitting menu and prices 
                        if cnt%2!=0:
                            menutext = menutext + i + "\n" #Adding each value to Menu Text
                        else:
                        	pricetext = pricetext + i + "\n" #Adding each value to Price Text
                        cnt += 1
                    self.mcdmenutext.setText(menutext) #Print values on Menu 
                    self.mcdpricetext.setText(pricetext) #Print values on Price

            elif store=="MiniWok":
                
                for x in stall[stall_names[1]]: #MiniWok
                    for i in x.split(":"):
                        if cnt%2!=0:
                        	menutext = menutext + i + "\n"
                        else:
                        	pricetext = pricetext + i + "\n"
                        cnt += 1
                    self.wokmenutext.setText(menutext)
                    self.wokpricetext.setText(pricetext)

            else:
                
                for x in stall[store]: #For other stalls
                    for i in x.split(":"):
                        if cnt%2!=0:
                        	menutext = menutext + i + "\n"
                        else:
                        	pricetext = pricetext + i + "\n"
                        cnt+=1
                    
                    
                    if store == "Pizza Hut Express":
                        self.pizzamenutext.setText(menutext)
                        self.pizzapricetext.setText(pricetext)

                    elif store == "Bakery Cuisine":
                        self.bakerymenutext.setText(menutext)
                        self.bakerypricetext.setText(pricetext)

                    elif store == "Beverages":
                        self.drinkmenutext.setText(menutext)
                        self.drinkpricetext.setText(pricetext)

        else: #If store is closed during the given time
        #Setting the contents of Menu and Price of Selected stall to "Closed"
            if store == "Pizza Hut Express":
                self.pizzamenutext.setText("\t Closed \t") 
                self.pizzapricetext.setText("           Closed \t")

            elif store == "Bakery Cuisine":
                self.bakerymenutext.setText("\t Closed \t")
                self.bakerypricetext.setText("           Closed \t")

            elif store == "Beverages":
                self.drinkmenutext.setText("\t Closed \t")
                self.drinkpricetext.setText("           Closed \t")

            elif store == "McDonalds":
                self.mcdmenutext.setText("\t Closed \t")
                self.mcdpricetext.setText("           Closed \t")

            elif store == "MiniWok":
                self.wokmenutext.setText("\t Closed \t")
                self.wokpricetext.setText("           Closed \t")

    def dispinfo(self,text): #To display the store info and return true or false if store is open or close

        hr = self.hourcombobox.currentIndex() #Collecting data from GUI
        mint = self.minutecombobox.currentIndex()
        time = hr * 100 + mint

        store = self.tabWidget.tabText(self.tabWidget.currentIndex()) #Storing the tab text in store (Eg: McDonlads, Pizza Hut)

        f = open("stall_info.txt", "r").readlines() #Opens and reads file containing store info
        info = f[f.index(store+"\n") + 1 : f.index(store[0:2] + "\n")] #Shortens the list to the stall info


        msg = QMessageBox() #For pop up messages
        msg.setWindowTitle(store+" store info") #To set the title to the popup 
        msg.setStandardButtons(QMessageBox.Ok) #Creating the OK button in pop-up window
        msg.setDetailedText(" ".join(info)) #Additional information to store info

        weekdays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday") #Tuple for Week
        weekday = ("Monday","Tuesday","Wednesday","Thursday","Friday") #Tuple for Weekday

        o_c = eval(open("stall_timing.txt").read()) #Reading the file which contain opening and closing timing as dictionary

        day = weekdays[self.Calender.selectedDate().dayOfWeek()-1] 
        day1 = weekdays[self.Calender.selectedDate().dayOfWeek()-1] #Getting the day of date selected in the calender

        weekday_open = o_c[store]["Weekday"][0] #Weekday opening time
        sat_open = o_c[store]["Saturday"][0] #Saturday opening time
        sun_open = o_c[store]["Sunday"][0] #Sunday opening time
            	
        if day in weekday:
            day="Weekday" #If the day is a weekday

        if o_c[store][day][0] <= time < o_c[store][day][1]: #To check if store is open at give time
            msg.setIcon(QMessageBox.Information) #Information icon
            msg.setText("The store is OPEN for your access")
            msg.setInformativeText("Enjoy your meal! :)")

            self.Waitingtime.setEnabled(True) #Enabling the waiting time frame
            self.Waitingtime.setToolTip("Enter number of people to calculate waiting time") #Tool tip to direct to enter value
            bol = True

        else: #If stall is closed
            self.Waitingtime.setEnabled(False) #Waiting time is disabled
            msg.setIcon(QMessageBox.Warning) #Warning  icon

            if day1 == datetime.now().strftime("%A") and (int(datetime.now().strftime("%H%M"))) >= time : #For current date and time
            	msg.setText("The Store is closed at the moment")
            	self.Waitingtime.setToolTip("The Store is closed at the moment") #Tool tip for Waiting time frame
           
            else: #For user defined date and time
                msg.setText("The store is closed on given date and time")
                self.Waitingtime.setToolTip("The Store is closed on given date and time") #Tool tip for Waiting time frame

            if time > o_c[store][day][1]: #If the store is closed after working hours

                if day1 in weekday: #Weekdays
                    if weekday.index(day1) != 4:     #Any weekday other than friday
                        msg.setInformativeText("The store opens on "+str(weekday[weekday.index(day1)+1])+" at "+str(weekday_open)+"Hrs")
                    elif weekday.index(day1) == 4:    # On Friday
                        if sat_open==0: #If the stall is closed on Saturday
                            if sun_open==0:
                                msg.setInformativeText("The store opens on Monday at "+str(weekday_open)+"Hrs")
                            else:
                                msg.setInformativeText("The store opens on Sunday at "+str(sun_open)+"Hrs")
                        else:
                            msg.setInformativeText("The store opens on Saturday at "+str(sat_open)+"Hrs")
                elif day == "Saturday": #Saturday
                    if sun_open==0:
                        msg.setInformativeText("The store opens on Monday at "+str(weekday_open)+"Hrs")
                    else: 
                        msg.setInformativeText("The store opens on Sunday at "+str(sun_open)+"Hrs")
                elif day =="Sunday": #Sunday
                    msg.setInformativeText("The store opens on Monday at "+str(weekday_open)+"Hrs")

            else: 
                if day1 in weekday:
                    msg.setInformativeText("The store opens on "+ day1+" at "+str(weekday_open)+"Hrs")
                else:
                    msg.setInformativeText("The store opens on "+ day1+" at "+str(o_c[store][day1][0])+"Hrs")
            bol = False
        
    
        font = QtGui.QFont() #Font of Message box
        font.setFamily("Sylfaen") #Font type
        font.setPointSize(12) #Font size
        msg.setFont(font)

        if text == "display" or not bol: #If this function is called with display or store is closed
            y = msg.exec_() #Run the pop-up window
        return bol

    def waiting_time(self): #For waiting time
        store = self.tabWidget.tabText(self.tabWidget.currentIndex()) #Storing the tab text in store (Eg: McDonlads, Pizza Hut)

        try:
        	people = int(self.numberofppltext.text()) #Retrieving no of people

        except ValueError: #If input value not integer
        	
            errormsg = QMessageBox() #Popup box
            errormsg.setWindowTitle("Error")
            errormsg.setText("Please Enter Number Of People In Numbers")
            errormsg.setIcon(QMessageBox.Critical) #Critical icon
            errormsg.setStandardButtons(QMessageBox.Ok)
            x = errormsg.exec_()
            self.numberofppltext.clear() #Clearing the no of people text box
            return

        if people < 0: #If input is Negative
            errormsg = QMessageBox() #Popup box
            errormsg.setWindowTitle("Error")
            errormsg.setText("Please Enter Number Of People In Numbers (Positive Integer)")
            errormsg.setIcon(QMessageBox.Critical) #Critical icon
            errormsg.setStandardButtons(QMessageBox.Ok)
            x = errormsg.exec_()
            self.numberofppltext.clear() #Clearing the no of people text box
            return

        if people > 99: #If input is too big
            errormsg = QMessageBox() #Popup box
            errormsg.setWindowTitle("Error")
            errormsg.setText("Please Enter a Reasonable Number Of People")
            errormsg.setIcon(QMessageBox.Critical) #Critical icon
            errormsg.setStandardButtons(QMessageBox.Ok)
            x = errormsg.exec_()
            self.numberofppltext.clear() #Clearing the no of people text box
            return

        if store == "McDonalds" or store == "Pizza Hut Express" or store == "Bakery Cuisine":
            i = 2
        elif store == "MiniWok":
            i = 4
        else:
            i = 1
        waitingTime = (people * i) + i #Calculating waiting time

        msg = QMessageBox()
        font = QtGui.QFont() #Font of Message box 
        font.setFamily("Sylfaen") 
        font.setPointSize(12) 
        msg.setFont(font)

        msg.setWindowTitle(store + " Waiting time info")
        msg.setText("It will take " + str(waitingTime) + " minutes for you to receive your order ") #Displaying the waiting time
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        y = msg.exec_()
        self.numberofppltext.clear()

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv) #Creates a QApplication (sys.agrv is the path for the file/program)
    MainWindow = QtWidgets.QMainWindow() 
    ui = Ui_MainWindow() #Creates object of the class Ui_MainWindow()
    ui.setupUi(MainWindow) #Calls the function setupUi- for setting the GUI
    MainWindow.show() #Displaying the Mainwindow 
    sys.exit(app.exec_()) #Executing the application and exiting the program then the application is closed