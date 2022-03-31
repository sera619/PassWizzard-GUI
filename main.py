# This Python file uses the following encoding: utf-8
from cryptography.fernet import Fernet
import webbrowser
from time import sleep
import os
import sys
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from ui_gui import Ui_MainWindow
from qt_material import apply_stylesheet
from PySide6 import *
from styles import *
from PassManager import  PasswordManager


version = "1.0.1"

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        apply_stylesheet(app, theme='dark_red.xml')
        self.setWindowIcon(QIcon('triple-lock.png'))
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowTitle('P455W1ZZ4RD')
        self.ui.footer_label.setText('P455W1ZZ4RD Version ' + version+' | by S3R43o3')
        
        #self.showMaximized()
        
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setXOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        self.ui.stackWidget.setCurrentWidget(self.ui.info_site)
        # Styling
        self.ui.menu_frame.layout().setAlignment(Qt.AlignLeft)
        self.ui.r_title_label.font().setFamily('JABBA-THE-FONT.REGULAR.TTF')
        self.ui.menu_frame.setMinimumWidth(0)

        # button events
        self.ui.min_btn.clicked.connect(lambda: self.showMinimized())
        self.ui.max_btn.clicked.connect(lambda: self.keyErrorBox('nokey'))
        self.ui.x_btn.clicked.connect(lambda: self.close())
        self.ui.menu_btn.clicked.connect(lambda: self.menuAnim())
        # sociel button events
        self.ui.yt_btn.clicked.connect(lambda: webbrowser.open('https://www.youtube.com/channel/UCJLXwZV5Kk4XRF6TSY_iPgQ'))
        self.ui.codepen_btn.clicked.connect(lambda: webbrowser.open('https://codepen.io/sera619'))
        self.ui.hackzor_btn.clicked.connect(lambda: webbrowser.open('https://www.hackzor.de'))
        self.ui.git_btn.clicked.connect(lambda: webbrowser.open('https://github.com/sera619'))
        # menu button events
        self.ui.key_btn.clicked.connect(
            lambda: self.ui.stackWidget.setCurrentWidget(self.ui.createKeys_site))
        self.ui.files_btn.clicked.connect(
            lambda: self.ui.stackWidget.setCurrentWidget(self.ui.files_site))
        self.ui.info_btn.clicked.connect(
            lambda: self.ui.stackWidget.setCurrentWidget(self.ui.info_site))
        self.ui.pass_btn.clicked.connect(
            lambda: self.ui.stackWidget.setCurrentWidget(self.ui.addpass_site))
        self.ui.getpass_btn.clicked.connect(
            lambda: self.ui.stackWidget.setCurrentWidget(self.ui.getPass_site))
        
        # get password
        self.ui.getPass_btn.clicked.connect(lambda: self.getPass())
        self.ui.createPass_btn.clicked.connect(lambda: self.createNewFile(self.ui.passname_input.text()))
        self.ui.create_key_btn.clicked.connect(lambda: self.createNewKey(self.ui.keyname_input.text()))
        self.ui.create_pass_btn.clicked.connect(lambda: self.createNewEntry())
        
        self.loadFiles()
        self.loadKeys()

        for w in self.ui.frame_5.findChildren(QPushButton):
            w.font().setFamily('JABBA-THE-FONT.REGULAR.TTF')
            w.setStyleSheet(Styles.MENUBUTTON)

        def moveWindow(e):
            if self.isMaximized() == False: 
                if e.buttons() == Qt.LeftButton:
                    globalPos = e.globalPos() 
                    self.move(self.pos() + globalPos - self.clickPosition)
                    self.clickPosition = globalPos

        self.ui.header_frame.mouseMoveEvent = moveWindow
        self.initCheck()


    def keyErrorBox(self):        
        box = NoKeyDialog(self)
        if box.exec():
            self.ui.stackWidget.setCurrentWidget(self.ui.createKeys_site)
        else:
            sys.exit(app.exec())    
    
    
        
    def initCheck(self):
        saved_keys = os.listdir('data/keys')
        saved_files = os.listdir('data/files')
        if saved_keys == [] or saved_files == []:
            self.keyErrorBox()
    
    
    
    def create_keyBox_item(self, obj):
        self.ui.get_key_input.clear()
        self.ui.files_key_input.clear()
        self.ui.select_key.clear()
        for o in obj:
            self.ui.get_key_input.addItem(o)
            self.ui.files_key_input.addItem(o)
            self.ui.select_key.addItem(o)
            
            
    def create_passBox_item(self, obj):
        self.ui.get_file_input.clear()
        self.ui.select_file.clear()
        for o in obj:
            self.ui.get_file_input.addItem(o)
            self.ui.select_file.addItem(o)
            
    def createNewEntry(self):
        if self.ui.new_pass_name.text() == '' or self.ui.new_pass_password.text()=="":
            self.ui.addpass_info_label.setText('Please enter a name and password!')
            return
        sizeKey = len(str(self.ui.select_key.currentText()))
        sizePass = len(str(self.ui.select_file.currentText())) 
        print(str(self.ui.select_key.currentText()[:sizeKey-4]))
        print(str(self.ui.select_file.currentText()[:sizePass-5]))
        PM.loadKey(self.ui.select_key.currentText()[:sizeKey-4])
        PM.loadPassFile(self.ui.select_file.currentText()[:sizePass-5])
        PM.addPassword(str(self.ui.new_pass_name.text()),str(self.ui.new_pass_password.text()))
        self.ui.addpass_info_label.setText('Success! Password added!')
        
        
    def getPass(self):
        sizeKey = len(str(self.ui.get_key_input.currentText()))
        sizePass = len(str(self.ui.get_file_input.currentText())) 
        print(str(self.ui.get_key_input.currentText()[:sizeKey-4]))
        print(str(self.ui.get_file_input.currentText()[:sizePass-5]))
        PM.loadKey(self.ui.get_key_input.currentText()[:sizeKey-4])
        PM.loadPassFile(self.ui.get_file_input.currentText()[:sizePass-5])
        
        if self.ui.get_account_input.text() != "":
            self.ui.pass_output_label.setText(str(PM.getPassword(self.ui.get_account_input.text())))
        else:
            self.ui.pass_output_label.setText('Please enter an account name!')
        self.ui.get_account_input.clear()
    
    def createNewKey(self, keyname):
        saved_keys = os.listdir('data/keys')
        if keyname in saved_keys:
            self.ui.create_key_label.setText('Key already exists!')
        else:
            PM.createKey(keyname)
        self.loadKeys()
        self.ui.create_file_label.setText('Success! New key created!')

    def createNewFile(self, filename):
        password = {
		"PLACEHOLDER-PASS-1": "743z4782",
	    }
        saved_files = os.listdir('data/files')
        if filename in saved_files:
            self.ui.create_file_label.setText('File already exists!')
            self.ui.passname_input.setText('')
        else:
            size = len(str(self.ui.files_key_input.currentText()))
            PM.loadKey(self.ui.files_key_input.currentText()[:size-4])
            PM.createPassFile(str(self.ui.passname_input.text()),password)
        self.ui.create_file_label.setText('Success! New file created!')
        self.loadFiles()


    def loadKeys(self):
        self.ui.key_list.clear()
        self.ui.key_list.setRowCount(0)
        saved_keys = os.listdir('data/keys')
        for key in saved_keys:
            rowPosition = self.ui.key_list.rowCount()
            self.ui.key_list.insertRow(rowPosition)
            self.create_table_widget(rowPosition, 0, key, 'key_list')
        self.create_keyBox_item(os.listdir('data/keys'))
            
    def loadFiles(self):
        self.ui.filesList.clear()
        self.ui.filesList.setRowCount(0)        
        saved_files =  os.listdir('data/files')
        #print(saved_files)           
        for file in saved_files:
            rowPosition = self.ui.filesList.rowCount()
            self.ui.filesList.insertRow(rowPosition)
            self.create_table_widget(rowPosition,0,file, 'filesList')
        self.create_passBox_item(os.listdir('data/files'))
    
    def create_table_widget(self, rowPosition, columnPosition, text, tableName):
        qtablewidgetitem = QTableWidgetItem()
        getattr(self.ui, tableName).setItem(
            rowPosition, columnPosition, qtablewidgetitem)
        qtablewidgetitem = getattr(self.ui, tableName).item(
            rowPosition, columnPosition)

        qtablewidgetitem.setText(text)
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def restoreWindow(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def menuAnim(self):
        width = self.ui.menu_frame.minimumWidth()
        if width == 125:
            new_width = 0
        else:
            new_width = 125
        self.animation = QPropertyAnimation(
            self.ui.menu_frame, b'minimumWidth')
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def applyButtonStyle(self):
        for i in self.ui.menu_frame.findChildren(QPushButton):
            if i.objectName() != self.sender().objectName():
                i.setStyleSheet(Styles.MENUBUTTON)
                i.font().setFamily('JABBA-THE-FONT.REGULAR.TTF')




PM = PasswordManager()
app = QApplication([])
if __name__ == '__main__':
    PM.initPassmanager('keys', 'files')
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
