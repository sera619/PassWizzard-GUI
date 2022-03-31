from cryptography.fernet import Fernet
from time import sleep
import os
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *





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
        if not os.path.exists('data'):
            print('>>> System: No Savedirectorys found! Create dat directory...')
            os.mkdir('data/')
        if not os.path.exists('data/'+fileDir):
            print('>>> System: No '+fileDir+' dir. Create one...')
            os.mkdir('data/'+fileDir)
        if not os.path.exists('data/'+keyDir):
            print('>>> System: No '+keyDir+' dir. Create one...')
            os.mkdir('data/'+keyDir)