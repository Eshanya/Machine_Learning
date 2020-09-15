import tkinter as tk
from tkinter import *
import tkinter.font as font
from tkinter import messagebox
import cv2
import os
from PIL import Image
import numpy as np

root = tk.Tk()
root.title("Face Detection")

self.mainFrame = Frame(root)
self.mainFrame.pack()
def_font = font.Font(family='Hack')
label1 = tk.Label(self.mainFrame, text = "Face Detect", font = def_font)
label1.grid(column = 0, row = 0)
entryHandle = tk.Entry(self.mainFrame, width = 50, bd = 10)

root.geometry("500x500")
root.mainloop()


