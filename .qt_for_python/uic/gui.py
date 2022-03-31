# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(566, 340)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(620, 340))
        MainWindow.setMouseTracking(True)
        MainWindow.setWindowOpacity(0.920000000000000)
        MainWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"border-radius:25px;\n"
"\n"
"\n"
"}")
        MainWindow.setInputMethodHints(Qt.ImhNone)
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        palette = QPalette()
        brush = QBrush(QColor(26, 25, 25, 239))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.centralwidget.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Jabba the Font"])
        font.setStyleStrategy(QFont.PreferDefault)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(u"background-color: rgba(26, 25, 25, 239);\n"
"QPushButton{\n"
"	font: 14pt \"Jabba the Font\";\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_frame.sizePolicy().hasHeightForWidth())
        self.header_frame.setSizePolicy(sizePolicy)
        self.header_frame.setMouseTracking(True)
        self.header_frame.setFocusPolicy(Qt.StrongFocus)
        self.header_frame.setStyleSheet(u"")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 6, 0, 0)
        self.header_l_frame = QFrame(self.header_frame)
        self.header_l_frame.setObjectName(u"header_l_frame")
        self.header_l_frame.setFrameShape(QFrame.StyledPanel)
        self.header_l_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.header_l_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.menu_btn = QPushButton(self.header_l_frame)
        self.menu_btn.setObjectName(u"menu_btn")
        self.menu_btn.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.menu_btn.sizePolicy().hasHeightForWidth())
        self.menu_btn.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Jabba the Font"])
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        self.menu_btn.setFont(font1)
        self.menu_btn.setStyleSheet(u"font: 11pt \"Jabba the Font\";\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/assets/icons/align-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_btn.setIcon(icon)
        self.menu_btn.setIconSize(QSize(22, 22))

        self.verticalLayout_5.addWidget(self.menu_btn, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.header_l_frame, 0, Qt.AlignBottom)

        self.header_m_frame = QFrame(self.header_frame)
        self.header_m_frame.setObjectName(u"header_m_frame")
        sizePolicy.setHeightForWidth(self.header_m_frame.sizePolicy().hasHeightForWidth())
        self.header_m_frame.setSizePolicy(sizePolicy)
        self.header_m_frame.setFrameShape(QFrame.StyledPanel)
        self.header_m_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.header_m_frame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 4, 0, 0)
        self.r_title_label = QLabel(self.header_m_frame)
        self.r_title_label.setObjectName(u"r_title_label")
        sizePolicy.setHeightForWidth(self.r_title_label.sizePolicy().hasHeightForWidth())
        self.r_title_label.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Jabba the Font"])
        font2.setPointSize(30)
        font2.setBold(True)
        font2.setItalic(True)
        font2.setKerning(True)
        self.r_title_label.setFont(font2)
        self.r_title_label.setContextMenuPolicy(Qt.PreventContextMenu)
        self.r_title_label.setStyleSheet(u"QLabel{\n"
"font: 700 italic 30pt \"Jabba the Font\";\n"
"}")
        self.r_title_label.setAlignment(Qt.AlignCenter)
        self.r_title_label.setIndent(-1)

        self.verticalLayout_8.addWidget(self.r_title_label, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.header_m_frame)

        self.window_btn_container = QFrame(self.header_frame)
        self.window_btn_container.setObjectName(u"window_btn_container")
        self.window_btn_container.setMaximumSize(QSize(16777215, 16777215))
        self.window_btn_container.setFrameShape(QFrame.StyledPanel)
        self.window_btn_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.window_btn_container)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.min_btn = QPushButton(self.window_btn_container)
        self.min_btn.setObjectName(u"min_btn")
        sizePolicy1.setHeightForWidth(self.min_btn.sizePolicy().hasHeightForWidth())
        self.min_btn.setSizePolicy(sizePolicy1)
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/icons/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.min_btn.setIcon(icon1)
        self.min_btn.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.min_btn, 0, Qt.AlignRight)

        self.max_btn = QPushButton(self.window_btn_container)
        self.max_btn.setObjectName(u"max_btn")
        sizePolicy1.setHeightForWidth(self.max_btn.sizePolicy().hasHeightForWidth())
        self.max_btn.setSizePolicy(sizePolicy1)
        self.max_btn.setFocusPolicy(Qt.StrongFocus)
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/icons/minimize-2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.max_btn.setIcon(icon2)
        self.max_btn.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.max_btn, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.x_btn = QPushButton(self.window_btn_container)
        self.x_btn.setObjectName(u"x_btn")
        sizePolicy1.setHeightForWidth(self.x_btn.sizePolicy().hasHeightForWidth())
        self.x_btn.setSizePolicy(sizePolicy1)
        self.x_btn.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/assets/icons/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.x_btn.setIcon(icon3)
        self.x_btn.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.x_btn, 0, Qt.AlignRight)


        self.horizontalLayout.addWidget(self.window_btn_container, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.header_frame)

        self.mid = QFrame(self.centralwidget)
        self.mid.setObjectName(u"mid")
        self.mid.setFrameShape(QFrame.StyledPanel)
        self.mid.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.mid)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.mid)
        self.menu_frame.setObjectName(u"menu_frame")
        sizePolicy.setHeightForWidth(self.menu_frame.sizePolicy().hasHeightForWidth())
        self.menu_frame.setSizePolicy(sizePolicy)
        self.menu_frame.setMinimumSize(QSize(125, 0))
        self.menu_frame.setMaximumSize(QSize(0, 16777215))
        self.menu_frame.setStyleSheet(u"")
        self.menu_frame.setFrameShape(QFrame.NoFrame)
        self.menu_frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.menu_frame)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 0, 0, 0)
        self.frame_5 = QFrame(self.menu_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setSpacing(12)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 9, 0, -1)
        self.key_btn = QPushButton(self.frame_5)
        self.key_btn.setObjectName(u"key_btn")
        font3 = QFont()
        font3.setFamilies([u"Cantarell"])
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        self.key_btn.setFont(font3)
        icon4 = QIcon()
        icon4.addFile(u":/icons/assets/icons/key.png", QSize(), QIcon.Normal, QIcon.Off)
        self.key_btn.setIcon(icon4)
        self.key_btn.setIconSize(QSize(22, 22))

        self.verticalLayout_6.addWidget(self.key_btn, 0, Qt.AlignLeft)

        self.files_btn = QPushButton(self.frame_5)
        self.files_btn.setObjectName(u"files_btn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/assets/icons/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.files_btn.setIcon(icon5)
        self.files_btn.setIconSize(QSize(22, 22))

        self.verticalLayout_6.addWidget(self.files_btn, 0, Qt.AlignLeft)

        self.getpass_btn = QPushButton(self.frame_5)
        self.getpass_btn.setObjectName(u"getpass_btn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/assets/icons/unlock.png", QSize(), QIcon.Normal, QIcon.Off)
        self.getpass_btn.setIcon(icon6)
        self.getpass_btn.setIconSize(QSize(22, 22))

        self.verticalLayout_6.addWidget(self.getpass_btn, 0, Qt.AlignLeft)

        self.pass_btn = QPushButton(self.frame_5)
        self.pass_btn.setObjectName(u"pass_btn")
        icon7 = QIcon()
        icon7.addFile(u":/icons/assets/icons/plus-square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pass_btn.setIcon(icon7)
        self.pass_btn.setIconSize(QSize(22, 22))

        self.verticalLayout_6.addWidget(self.pass_btn, 0, Qt.AlignLeft)

        self.info_btn = QPushButton(self.frame_5)
        self.info_btn.setObjectName(u"info_btn")
        self.info_btn.setStyleSheet(u"border-radius:25px;")
        icon8 = QIcon()
        icon8.addFile(u":/icons/assets/icons/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.info_btn.setIcon(icon8)
        self.info_btn.setIconSize(QSize(22, 22))

        self.verticalLayout_6.addWidget(self.info_btn, 0, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.frame_5, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.menu_frame, 0, Qt.AlignLeft|Qt.AlignTop)

        self.stackWidget = QStackedWidget(self.mid)
        self.stackWidget.setObjectName(u"stackWidget")
        sizePolicy1.setHeightForWidth(self.stackWidget.sizePolicy().hasHeightForWidth())
        self.stackWidget.setSizePolicy(sizePolicy1)
        self.stackWidget.setFrameShape(QFrame.NoFrame)
        self.stackWidget.setFrameShadow(QFrame.Plain)
        self.createKeys_site = QWidget()
        self.createKeys_site.setObjectName(u"createKeys_site")
        self.horizontalLayout_5 = QHBoxLayout(self.createKeys_site)
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(30, 30, 30, 30)
        self.frame = QFrame(self.createKeys_site)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(250, 0))
        self.frame_2.setMaximumSize(QSize(250, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(280, 0))
        self.label.setMaximumSize(QSize(16777215, 16777215))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"font: 11pt \"Jabba the Font\";")
        self.label.setTextFormat(Qt.AutoText)

        self.verticalLayout_7.addWidget(self.label, 0, Qt.AlignHCenter)

        self.key_list = QTableWidget(self.frame_2)
        if (self.key_list.columnCount() < 1):
            self.key_list.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.key_list.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.key_list.setObjectName(u"key_list")
        self.key_list.setTextElideMode(Qt.ElideMiddle)
        self.key_list.horizontalHeader().setMinimumSectionSize(180)
        self.key_list.horizontalHeader().setDefaultSectionSize(180)
        self.key_list.verticalHeader().setMinimumSectionSize(20)
        self.key_list.verticalHeader().setDefaultSectionSize(20)

        self.verticalLayout_7.addWidget(self.key_list, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addWidget(self.frame_2, 0, Qt.AlignHCenter)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(60, -1, 60, -1)
        self.create_key_label = QLabel(self.frame_6)
        self.create_key_label.setObjectName(u"create_key_label")

        self.verticalLayout_9.addWidget(self.create_key_label, 0, Qt.AlignHCenter)

        self.keyname_input = QLineEdit(self.frame_6)
        self.keyname_input.setObjectName(u"keyname_input")
        self.keyname_input.setStyleSheet(u"border-color: rgb(192, 28, 40);\n"
"border-width:1px;\n"
"border-style: solid ;")

        self.verticalLayout_9.addWidget(self.keyname_input)

        self.create_key_btn = QPushButton(self.frame_6)
        self.create_key_btn.setObjectName(u"create_key_btn")
        self.create_key_btn.setStyleSheet(u"padding: 3px 36px;")

        self.verticalLayout_9.addWidget(self.create_key_btn, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addWidget(self.frame_6)


        self.horizontalLayout_5.addWidget(self.frame)

        self.stackWidget.addWidget(self.createKeys_site)
        self.files_site = QWidget()
        self.files_site.setObjectName(u"files_site")
        self.verticalLayout_11 = QVBoxLayout(self.files_site)
        self.verticalLayout_11.setSpacing(15)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(30, 30, 30, 30)
        self.frame_7 = QFrame(self.files_site)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_7)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(250, 0))
        self.frame_9.setMaximumSize(QSize(250, 16777215))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_9)
        self.verticalLayout_14.setSpacing(4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"font: 11pt \"Jabba the Font\";")

        self.verticalLayout_14.addWidget(self.label_5, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.filesList = QTableWidget(self.frame_9)
        if (self.filesList.columnCount() < 1):
            self.filesList.setColumnCount(1)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.filesList.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        self.filesList.setObjectName(u"filesList")
        self.filesList.setMinimumSize(QSize(0, 0))
        self.filesList.setMaximumSize(QSize(16777215, 16777215))
        self.filesList.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.filesList.setTextElideMode(Qt.ElideMiddle)
        self.filesList.horizontalHeader().setMinimumSectionSize(180)
        self.filesList.horizontalHeader().setDefaultSectionSize(180)
        self.filesList.verticalHeader().setMinimumSectionSize(20)
        self.filesList.verticalHeader().setDefaultSectionSize(20)

        self.verticalLayout_14.addWidget(self.filesList, 0, Qt.AlignHCenter)


        self.verticalLayout_12.addWidget(self.frame_9, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_8)
        self.verticalLayout_13.setSpacing(6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(60, 9, 60, 9)
        self.frame_17 = QFrame(self.frame_8)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_17)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.files_key_input = QComboBox(self.frame_17)
        self.files_key_input.setObjectName(u"files_key_input")
        self.files_key_input.setStyleSheet(u"border-color: rgb(192, 28, 40);\n"
"border-width:1px;\n"
"border-style: solid ;")

        self.horizontalLayout_4.addWidget(self.files_key_input)


        self.verticalLayout_13.addWidget(self.frame_17)

        self.create_file_label = QLabel(self.frame_8)
        self.create_file_label.setObjectName(u"create_file_label")

        self.verticalLayout_13.addWidget(self.create_file_label, 0, Qt.AlignHCenter)

        self.passname_input = QLineEdit(self.frame_8)
        self.passname_input.setObjectName(u"passname_input")
        self.passname_input.setStyleSheet(u"border-color: rgb(192, 28, 40);\n"
"border-width:1px;\n"
"border-style: solid ;")

        self.verticalLayout_13.addWidget(self.passname_input)

        self.createPass_btn = QPushButton(self.frame_8)
        self.createPass_btn.setObjectName(u"createPass_btn")

        self.verticalLayout_13.addWidget(self.createPass_btn, 0, Qt.AlignHCenter)


        self.verticalLayout_12.addWidget(self.frame_8, 0, Qt.AlignVCenter)


        self.verticalLayout_11.addWidget(self.frame_7)

        self.stackWidget.addWidget(self.files_site)
        self.addpass_site = QWidget()
        self.addpass_site.setObjectName(u"addpass_site")
        self.verticalLayout_21 = QVBoxLayout(self.addpass_site)
        self.verticalLayout_21.setSpacing(15)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(30, 30, 30, 30)
        self.frame_4 = QFrame(self.addpass_site)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_4)
        self.verticalLayout_20.setSpacing(15)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(30, 25, 30, 25)
        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font: 11pt \"Jabba the Font\";")

        self.verticalLayout_20.addWidget(self.label_13, 0, Qt.AlignHCenter)

        self.frame_15 = QFrame(self.frame_4)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_15)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_15)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_3.addWidget(self.label_15, 0, 0, 1, 1, Qt.AlignHCenter)

        self.label_16 = QLabel(self.frame_15)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_3.addWidget(self.label_16, 0, 1, 1, 1, Qt.AlignHCenter)

        self.select_key = QComboBox(self.frame_15)
        self.select_key.setObjectName(u"select_key")

        self.gridLayout_3.addWidget(self.select_key, 1, 0, 1, 1)

        self.select_file = QComboBox(self.frame_15)
        self.select_file.setObjectName(u"select_file")

        self.gridLayout_3.addWidget(self.select_file, 1, 1, 1, 1)


        self.verticalLayout_20.addWidget(self.frame_15)

        self.frame_14 = QFrame(self.frame_4)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_14)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_14)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 0, 0, 1, 1, Qt.AlignHCenter)

        self.label_17 = QLabel(self.frame_14)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 0, 1, 1, 1, Qt.AlignHCenter)

        self.new_pass_name = QLineEdit(self.frame_14)
        self.new_pass_name.setObjectName(u"new_pass_name")
        self.new_pass_name.setStyleSheet(u"border-color: rgb(192, 28, 40);\n"
"border-width:1px;\n"
"border-style: solid ;")

        self.gridLayout_2.addWidget(self.new_pass_name, 1, 0, 1, 1)

        self.new_pass_password = QLineEdit(self.frame_14)
        self.new_pass_password.setObjectName(u"new_pass_password")
        self.new_pass_password.setStyleSheet(u"border-color: rgb(192, 28, 40);\n"
"border-width:1px;\n"
"border-style: solid ;")

        self.gridLayout_2.addWidget(self.new_pass_password, 1, 1, 1, 1)


        self.verticalLayout_20.addWidget(self.frame_14)

        self.addpass_info_label = QLabel(self.frame_4)
        self.addpass_info_label.setObjectName(u"addpass_info_label")

        self.verticalLayout_20.addWidget(self.addpass_info_label, 0, Qt.AlignHCenter)

        self.create_pass_btn = QPushButton(self.frame_4)
        self.create_pass_btn.setObjectName(u"create_pass_btn")

        self.verticalLayout_20.addWidget(self.create_pass_btn, 0, Qt.AlignHCenter)


        self.verticalLayout_21.addWidget(self.frame_4)

        self.stackWidget.addWidget(self.addpass_site)
        self.info_site = QWidget()
        self.info_site.setObjectName(u"info_site")
        self.verticalLayout_18 = QVBoxLayout(self.info_site)
        self.verticalLayout_18.setSpacing(15)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(30, 25, 30, 30)
        self.frame_12 = QFrame(self.info_site)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_12)
        self.verticalLayout_19.setSpacing(4)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_12)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"QLabel{\n"
"	font: italic 13pt \"Jabba the Font\";\n"
"	color: rgb(224, 27, 36);\n"
"}")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_12, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_13)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_13)
        self.label_10.setObjectName(u"label_10")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.label_10.setFont(font4)

        self.gridLayout.addWidget(self.label_10, 2, 3, 1, 1)

        self.yt_btn = QPushButton(self.frame_13)
        self.yt_btn.setObjectName(u"yt_btn")
        self.yt_btn.setStyleSheet(u"QPushButton:hover{\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 30px;\n"
"	selection-color: rgb(224, 27, 36);\n"
"	border-color: rgb(224, 27, 36);\n"
"padding: 1px 2px;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/assets/icons/youtube.png", QSize(), QIcon.Normal, QIcon.Off)
        self.yt_btn.setIcon(icon9)
        self.yt_btn.setIconSize(QSize(28, 22))

        self.gridLayout.addWidget(self.yt_btn, 2, 2, 1, 1, Qt.AlignRight)

        self.git_btn = QPushButton(self.frame_13)
        self.git_btn.setObjectName(u"git_btn")
        self.git_btn.setStyleSheet(u"QPushButton:hover{\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 30px;\n"
"	selection-color: rgb(224, 27, 36);\n"
"	border-color: rgb(224, 27, 36);\n"
"padding: 1px 2px;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icons/assets/icons/github.png", QSize(), QIcon.Normal, QIcon.Off)
        self.git_btn.setIcon(icon10)
        self.git_btn.setIconSize(QSize(28, 22))

        self.gridLayout.addWidget(self.git_btn, 1, 0, 1, 1)

        self.label_8 = QLabel(self.frame_13)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font4)

        self.gridLayout.addWidget(self.label_8, 1, 1, 1, 1)

        self.codepen_btn = QPushButton(self.frame_13)
        self.codepen_btn.setObjectName(u"codepen_btn")
        self.codepen_btn.setStyleSheet(u"QPushButton:hover{\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 30px;\n"
"	selection-color: rgb(224, 27, 36);\n"
"	border-color: rgb(224, 27, 36);\n"
"padding: 1px 2px;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icons/assets/icons/codepen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.codepen_btn.setIcon(icon11)
        self.codepen_btn.setIconSize(QSize(28, 22))

        self.gridLayout.addWidget(self.codepen_btn, 2, 0, 1, 1)

        self.label_9 = QLabel(self.frame_13)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font4)

        self.gridLayout.addWidget(self.label_9, 2, 1, 1, 1)

        self.label_11 = QLabel(self.frame_13)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font4)

        self.gridLayout.addWidget(self.label_11, 1, 3, 1, 1)

        self.hackzor_btn = QPushButton(self.frame_13)
        self.hackzor_btn.setObjectName(u"hackzor_btn")
        self.hackzor_btn.setStyleSheet(u"QPushButton:hover{\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 30px;\n"
"	selection-color: rgb(224, 27, 36);\n"
"	border-color: rgb(224, 27, 36);\n"
"padding: 1px 2px;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icons/assets/icons/book-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.hackzor_btn.setIcon(icon12)
        self.hackzor_btn.setIconSize(QSize(28, 22))

        self.gridLayout.addWidget(self.hackzor_btn, 1, 2, 1, 1)


        self.verticalLayout_19.addWidget(self.frame_13, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_18.addWidget(self.frame_12)

        self.stackWidget.addWidget(self.info_site)
        self.getPass_site = QWidget()
        self.getPass_site.setObjectName(u"getPass_site")
        self.verticalLayout_15 = QVBoxLayout(self.getPass_site)
        self.verticalLayout_15.setSpacing(15)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(30, 30, 30, 30)
        self.frame_16 = QFrame(self.getPass_site)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_16)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_19 = QLabel(self.frame_16)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"font: 11pt \"Jabba the Font\";")

        self.verticalLayout_16.addWidget(self.label_19)


        self.verticalLayout_15.addWidget(self.frame_16, 0, Qt.AlignHCenter)

        self.frame_10 = QFrame(self.getPass_site)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(60, -1, 60, -1)
        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_3 = QLabel(self.frame_10)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 4, 0, 1, 1)

        self.get_key_input = QComboBox(self.frame_10)
        self.get_key_input.setObjectName(u"get_key_input")
        self.get_key_input.setStyleSheet(u"border-color: rgb(192, 28, 40);\n"
"border-width:1px;\n"
"border-style: solid ;")

        self.gridLayout_4.addWidget(self.get_key_input, 0, 1, 1, 1)

        self.get_file_input = QComboBox(self.frame_10)
        self.get_file_input.setObjectName(u"get_file_input")
        self.get_file_input.setStyleSheet(u"border-color: rgb(192, 28, 40);\n"
"border-width:1px;\n"
"border-style: solid ;")

        self.gridLayout_4.addWidget(self.get_file_input, 2, 1, 1, 1)

        self.get_account_input = QLineEdit(self.frame_10)
        self.get_account_input.setObjectName(u"get_account_input")
        self.get_account_input.setStyleSheet(u"border-color: rgb(192, 28, 40);\n"
"border-width:1px;\n"
"border-style: solid ;")

        self.gridLayout_4.addWidget(self.get_account_input, 4, 1, 1, 1)


        self.verticalLayout_15.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.getPass_site)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_11)
        self.verticalLayout_17.setSpacing(5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(10, 10, 10, 10)
        self.label_18 = QLabel(self.frame_11)
        self.label_18.setObjectName(u"label_18")
        font5 = QFont()
        font5.setPointSize(15)
        font5.setBold(True)
        self.label_18.setFont(font5)

        self.verticalLayout_17.addWidget(self.label_18, 0, Qt.AlignHCenter)

        self.pass_output_label = QLabel(self.frame_11)
        self.pass_output_label.setObjectName(u"pass_output_label")

        self.verticalLayout_17.addWidget(self.pass_output_label, 0, Qt.AlignHCenter)

        self.getPass_btn = QPushButton(self.frame_11)
        self.getPass_btn.setObjectName(u"getPass_btn")

        self.verticalLayout_17.addWidget(self.getPass_btn, 0, Qt.AlignHCenter)


        self.verticalLayout_15.addWidget(self.frame_11, 0, Qt.AlignVCenter)

        self.stackWidget.addWidget(self.getPass_site)

        self.horizontalLayout_2.addWidget(self.stackWidget)


        self.verticalLayout.addWidget(self.mid)

        self.footer = QFrame(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Plain)
        self.verticalLayout_10 = QVBoxLayout(self.footer)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(3, 0, 3, 0)
        self.frame_3 = QFrame(self.footer)
        self.frame_3.setObjectName(u"frame_3")
        font6 = QFont()
        font6.setFamilies([u"Quicksand Light"])
        font6.setPointSize(9)
        self.frame_3.setFont(font6)
        self.frame_3.setStyleSheet(u"border-radius:25px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 2, 0, 2)
        self.footer_label = QLabel(self.frame_3)
        self.footer_label.setObjectName(u"footer_label")
        font7 = QFont()
        font7.setFamilies([u"Quicksand Medium"])
        font7.setBold(True)
        self.footer_label.setFont(font7)
        self.footer_label.setStyleSheet(u"QLabel{\n"
"color: rgb(94, 92, 100);\n"
"font-size:9px;}")

        self.verticalLayout_4.addWidget(self.footer_label)


        self.verticalLayout_10.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.footer, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"P455W1ZZ4RD", None))
        self.menu_btn.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.r_title_label.setText(QCoreApplication.translate("MainWindow", u"PASSWIZZARD", None))
        self.min_btn.setText("")
        self.max_btn.setText("")
        self.x_btn.setText("")
        self.key_btn.setText(QCoreApplication.translate("MainWindow", u"Keys", None))
        self.files_btn.setText(QCoreApplication.translate("MainWindow", u"Passfiles", None))
        self.getpass_btn.setText(QCoreApplication.translate("MainWindow", u"Get Pass", None))
        self.pass_btn.setText(QCoreApplication.translate("MainWindow", u"Add Pass", None))
        self.info_btn.setText(QCoreApplication.translate("MainWindow", u" Info", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Your Keys", None))
        ___qtablewidgetitem = self.key_list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        self.create_key_label.setText(QCoreApplication.translate("MainWindow", u"Enter a name for the new key!", None))
        self.create_key_btn.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"YOUR FILES", None))
        ___qtablewidgetitem1 = self.filesList.horizontalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Choose a Key", None))
        self.create_file_label.setText(QCoreApplication.translate("MainWindow", u"Enter a name for a new passfile", None))
        self.createPass_btn.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Add New Password", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Select a Key", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Select a File", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Enter Accountname", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Enter Password", None))
        self.addpass_info_label.setText("")
        self.create_pass_btn.setText(QCoreApplication.translate("MainWindow", u"Add New Entry", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br>APP DESIGN<br>AND<br>DEVELOPMENT<br> BY<br>2022 \u00a9 S3R43o3</p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Youtube", None))
        self.yt_btn.setText("")
        self.git_btn.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"GitHub", None))
        self.codepen_btn.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"CodePen", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"H4ckz0r", None))
        self.hackzor_btn.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Get Password", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Choose a Key", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Choose a Pass-File", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Enter Accountname", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"PASSWORD:", None))
        self.pass_output_label.setText("")
        self.getPass_btn.setText(QCoreApplication.translate("MainWindow", u"Get Pass", None))
        self.footer_label.setText(QCoreApplication.translate("MainWindow", u"P455W1ZZ4RD Version 0.8.2 | S3R43o3", None))
    # retranslateUi

