import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import wetter_speech_test_Ende as wt
import inlove

S3_2UI = uic.loadUiType("H:/das Projekt auf V3.6/GUI/S3_2.ui")[0]
class S3_2Dialog(QDialog,S3_2UI):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def bitteWetter(self):
        wettersagen = wt.speech()
        wettersagen

    def nachHause_click_open(self):
        self.inLoveopen = inlove.InLove()
        self.inLoveopen.show()
        self.close()