# base deps
from tkinter import *
import cv2
from PIL import Image, ImageTK
import time

# v4l2 logging - base qt5
from PyQt5.QtMultimedia import *
from PyQt5. QtCore import QUrl

class View:
    def __init__(self, vid_source = 0):
        self.vid = cv2.VideoCapture(vid_source)
        if not self.vid.isOpened():
            raise ValueError("Media capture failed!", vid_source)

        # dimensions
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def bufferAnalyzer(self):
        if self.vid.isOpened():
            # flag for tuple basing
            isTrue, buffer = self.vid.read()

            if isTrue:
                return(isTrue, cv2.cvtColor(buffer, cv2.COLOR_BGR2RGB))

