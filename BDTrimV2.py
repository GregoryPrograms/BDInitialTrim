import os
import tkinter
from tkinter import filedialog
from pathlib import Path
def main():
    tkinter.Tk().withdraw()
    dirPath = Path(filedialog.askdirectory(title = 'Select directory to trim file names...'))
    fileList = []
    for path, folders, _ in os.walk(dirPath):
        for name in folders:
            fileList.append([Path(path),name])
    for BDFile in fileList:
        for charIndex in range(6,len(BDFile[1])):
            if BDFile[1][charIndex].isalpha():
                os.rename(BDFile[0] / BDFile[1], BDFile[0] / BDFile[1][:charIndex])
                break
if(__name__ == "__main__"):
    main()
