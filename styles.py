from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6 import *
class Styles:
    MENU="""
    QLabel {
        font-family: url(JABBA-THE-FONT.REGULAR.TTF);
    }
    """
    MENUBUTTON = """    
    
    
    QPushButton{border-radius: 25px;}
    QPushButton:hover {
        border: 1px solid 25px;
        border-color:rbg(180,0,0);
        border-radius: 25px;    
        }
    """


class NoKeyDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowIcon(QIcon('favicon.ico'))
        self.setWindowTitle("Information")
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout = QVBoxLayout()
        
        message = QLabel("P455W1ZZ4RD cant find a Key/File\n\nP455W1ZZ4RD needs a key/file to work.\nPlease create a key first.\n\n")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)