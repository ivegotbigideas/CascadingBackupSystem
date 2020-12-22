import shutil
import os
from distutils import dir_util
from tkinter import filedialog
from tkinter import Tk

def generateDirectoryPathFromDialogue():
    root = Tk()
    root.withdraw()
    path = filedialog.askdirectory()
    return path

# moves all directories and files in src up a directory
def moveDirectoryContentsUpOne(src):
    dest = src + ".."
    fileNames = os.listdir(src)
    for fileName in fileNames:
        fileSrc = os.path.join(src, fileName)
        shutil.move(fileSrc, dest)

# removes "CascadingBackupSystem" directory from dest if the user requests
def removeCbsTempDirectory(path):
    continueLoop = 1
    while continueLoop == 1:
        removeDirectory = input("Would you like the copied files to reside in a CascadingBackupSystem directory? Please enter yes or no: ")
        removeDirectory = removeDirectory.lower()
        if removeDirectory == "no" or removeDirectory == "yes":
            if removeDirectory == "no":
                moveDirectoryContentsUpOne(path)
                shutil.rmtree(path)
            continueLoop = 0