import os
import pathlib
import shutil


downloadFolder = str(pathlib.Path.home()) + "\Downloads"

pathImg = os.path.join(downloadFolder, "Images")
pathDoc = os.path.join(downloadFolder, "Documents")
pathApp = os.path.join(downloadFolder, "Executables")
pathVid = os.path.join(downloadFolder, "Videos")
pathOtr = os.path.join(downloadFolder, "Others")

if not os.path.exists(pathImg):
    os.mkdir(pathImg)

if not os.path.exists(pathDoc):
    os.mkdir(pathDoc)

if not os.path.exists(pathApp):
    os.mkdir(pathApp)

if not os.path.exists(pathVid):
    os.mkdir(pathVid)

if not os.path.exists(pathOtr):
    os.mkdir(pathOtr)

for files in os.listdir(downloadFolder):
    filePath = os.path.join(downloadFolder, files)
    print(filePath)

    if files.__contains__('.'):
        if files.endswith(('.png', '.jpg', '.jpeg', '.webp')):
            shutil.move(filePath, os.path.join(pathImg, files))
            continue
        if files.endswith(('.txt', '.docx', '.zip', '.7z', '.rar', '.pdf')):
            shutil.move(filePath, os.path.join(pathDoc, files))
            continue
        if files.endswith(('.exe', '.msi')):
            shutil.move(filePath, os.path.join(pathApp, files))
            continue
        if files.endswith(('.mp4', '.mp3')):
            shutil.move(filePath, os.path.join(pathVid, files))
            continue
        else:
            shutil.move(filePath, os.path.join(pathOtr, files))