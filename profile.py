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
root.config(background='grey')

def_font = font.Font(family='Hack', size=30)
label1 = tk.Label(root, text = "Face Detect", font = def_font)
label1.grid(column = 0, row = 0)
entryHandle = tk.Entry(root, width = 50, bd = 2)
entryHandle.grid(column = 1, row = 0)

def train:


button = tk.Button(root, text = "Face Detect", font = def_font, bg = 'white', fg = 'blue', command = train)
button.grid(column = 0, row = 4)

root.geometry("500x500")
root.mainloop()


