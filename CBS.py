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
    dest = src + "/.."
    fileNames = os.listdir(src)
    for fileName in fileNames:
        fileSrc = os.path.join(src, fileName)
        shutil.move(fileSrc, dest)

def requestToRemoveCbsDirectory(path):
    path = path + "/CascadingBackupSystem"
    continueLoop = 1
    while continueLoop == 1:
        keepDirectory = input("Would you like the copied files to reside in a CascadingBackupSystem directory? Please enter yes or no: ")
        keepDirectory = keepDirectory.lower()
        if keepDirectory == "no" or keepDirectory == "yes":
            if keepDirectory == "no":
                removeTempDirectory(path)
            continueLoop = 0

# removes "CascadingBackupSystem" directory from dest if the user requests
def removeTempDirectory(path):
    moveDirectoryContentsUpOne(path)
    shutil.rmtree(path)

def copyTree(src,dest):
    dest = dest + "/CascadingBackupSystem"
    dir_util.copy_tree(src,dest)

if __name__ == "__main__":
    src = generateDirectoryPathFromDialogue()
    dest = generateDirectoryPathFromDialogue()
    copyTree(src,dest)
    requestToRemoveCbsDirectory(dest)
