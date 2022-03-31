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
import styles

version = "0.9.2"

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        apply_stylesheet(app, theme='dark_red.xml')
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowTitle('P455W1ZZ4RD')
        self.setWindowIcon(QIcon('triple-lock.png'))
        self.ui.footer_label.setText('P455W1ZZ4RD Version ' + version+' | by S3R43o3')
        
        self.showMaximized()
        
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
        self.ui.max_btn.clicked.connect(lambda: self.restoreWindow())
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
            w.setStyleSheet(styles.Styles.MENUBUTTON)

        def moveWindow(e):
            if self.isMaximized() == False: 
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        self.ui.header_frame.mouseMoveEvent = moveWindow

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
        """
        self.password_dic[site] = passwor
        if self.password_file is not None:
            with open(self.password_file, 'a+') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + str(encrypted.decode()) + "\n")
                print("Success! New password saved!\n")
                f.close()
            """        
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
                i.setStyleSheet(styles.Styles.MENUBUTTON)
                i.font().setFamily('JABBA-THE-FONT.REGULAR.TTF')



class PasswordManager:
    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dic = {}

        self.fistRun = True
        self.keySelected = False
        self.pathKey = None
        self.pathSelected = False
        self.pathFile = None

    def createKey(self, path):
        self.key = Fernet.generate_key()
        path = 'data/keys/'+path+'.key'
        with open(path, 'wb') as f:
            f.write(self.key)
            f.close()
        print('Success! New Passwordkey created\n')

    def loadKey(self, path):
        self.pathKey = path
        path = 'data/keys/'+path+'.key'
        with open(path, 'rb') as f:
            self.key = f.read()
            self.keySelected = True
            f.close()

    def createPassFile(self, path, initial_values=None):
        # with open(path, 'w') as f:
        path = 'data/files/'+path+'.pass'
        self.password_file = path
        if initial_values is not None:
            for key, values in initial_values.items():
                self.addPassword(key, values)
        print('Success! New Passwordfile created\n')

    def loadPassFile(self, path):
        self.pathFile = path
        path = 'data/files/'+path+'.pass'
        self.password_file = path
        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.split(":")
                self.password_dic[site] = Fernet(
                    self.key).decrypt(encrypted.encode()).decode()
            self.pathSelected = True
            f.close()

    def addPassword(self, site, password):
        self.password_dic[site] = password
        if self.password_file is not None:
            with open(self.password_file, 'a+') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + str(encrypted.decode()) + "\n")
                print("Success! New password saved!\n")
                f.close()

    def getPassword(self,site):
        return str(self.password_dic[site])
    


    def errMsg(self):
        print('Invalid Option! Please enter a valid Option!')

    def infoPrint(self):
        if self.keySelected:
            print("\nSelected Key: "f"{self.pathKey}\n")
        if self.pathSelected:
            print("\nSelected Passfile: "f"{self.pathFile}\n")

    def resetSelection(self):
        self.keySelected = False
        self.pathKey = None
        self.pathSelected = False
        self.pathFile = None

    def initPassmanager(self, fileDir, keyDir):
        print('>>> P455 W1ZZ4RD started.\n>>> System: initialize relevant data ...')
        sleep(1.5)
        if not os.path.exists('data'):
            print('>>> System: No Savedirectorys found! Create dat directory...')
            os.mkdir('data/')
        if not os.path.exists('data/'+fileDir):
            print('>>> System: No '+fileDir+' dir. Create one...')
            os.mkdir('data/'+fileDir)
        if not os.path.exists('data/'+keyDir):
            print('>>> System: No '+keyDir+' dir. Create one...')
            os.mkdir('data/'+keyDir)


PM = PasswordManager()
app = QApplication([])
if __name__ == '__main__':
    PM.initPassmanager('keys', 'files')
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
