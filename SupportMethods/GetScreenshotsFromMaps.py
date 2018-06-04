import os
import time
from selenium import webdriver


def getScreenshotsFromMaps():

    cwd = os.getcwd()   # Current Working Directory.
    driverFullPath = cwd + "/../Resources/maps/geckodriver.exe"
    driver = webdriver.Firefox(executable_path=driverFullPath)

    # task 1
    task1Path = "../Resources/maps/task1"
    if os.path.isdir(task1Path):
        imagesDir = task1Path + "/images"
        if not os.path.isdir(imagesDir):
            os.makedirs(imagesDir)
        for fileName in os.listdir(task1Path):
            if ".html" in fileName:
                print 'Getting screenshot from: ..task1/' + fileName
                fileFullPath = "file:///" + cwd + "/" + task1Path + "/" + fileName
                #print fileFullPath
                driver.get(fileFullPath)
                time.sleep(2)   # Wait for the driver to render the html (otherwise the screenshots will be white :-P)
                fileName = fileName.replace(".html", "")
                driver.save_screenshot(imagesDir + "/" + fileName + '.png')

    # task 2A1
    task2A1Path = "../Resources/maps/task2A1"
    if os.path.isdir(task2A1Path):
        imagesDir = task2A1Path + "/images"
        if not os.path.isdir(imagesDir):
            os.makedirs(imagesDir)
        for fileName in os.listdir(task2A1Path):
            if ".html" in fileName:
                print 'Getting screenshot from: ..task2A1/' + fileName
                fileFullPath = "file:///" + cwd + "/" + task2A1Path + "/" + fileName
                driver.get(fileFullPath)
                time.sleep(2)  # Wait for the driver to render the html.
                fileName = fileName.replace(".html", "")
                driver.save_screenshot(imagesDir + "/" + fileName + '.png')

    # task 2A2
    task2A2Path = "../Resources/maps/task2A2"
    if os.path.isdir(task2A2Path):
        imagesDir = task2A2Path + "/images"
        if not os.path.isdir(imagesDir):
            os.makedirs(imagesDir)
        for fileName in os.listdir(task2A2Path):
            if ".html" in fileName:
                print 'Getting screenshot from: ..task2A2/' + fileName
                fileFullPath = "file:///" + cwd + "/" + task2A2Path + "/" + fileName
                driver.get(fileFullPath)
                time.sleep(2)  # Wait for the driver to render the html.
                fileName = fileName.replace(".html", "")
                driver.save_screenshot(imagesDir + "/" + fileName + '.png')

    driver.quit()


if __name__ == '__main__':
    getScreenshotsFromMaps()
