import os
import time

from selenium import webdriver

'''
    We are using the "Geckodriver" by Mozilla
    https://github.com/mozilla/geckodriver/releases
    
    Currently usable only on Windows.
'''


# TODO - Based on the os, have the right "geckodriver"-executable. Maybe auto-download the right one..


def saveScreenshot(driver, fileName, imagesDir, taskPath):
    cwd = os.getcwd()  # Current Working Directory.
    fullFilePath = os.path.join(cwd, taskPath, fileName)
    print('Getting screenshot from: ' + fullFilePath)

    fileFullPath = "file:///" + os.path.join(cwd, taskPath, fileName)
    driver.get(fileFullPath)
    time.sleep(2)  # Wait for the driver to render the html (otherwise the screenshots will be white :-P)
    fileName = fileName.replace(".html", "")
    driver.save_screenshot(os.path.join(imagesDir, fileName + '.png'))


def getScreenshotsFromMaps():
    cwd = os.getcwd()  # Current Working Directory.

    driverDirectory = os.path.join(cwd, '..', 'Resources', 'maps', 'geckodriver')
    driverExecutable = os.path.join(driverDirectory, 'geckodriver.exe')
    driverLogFile = os.path.join(driverDirectory, 'geckodriver.log')

    driver = webdriver.Firefox(executable_path=driverExecutable, service_log_path=driverLogFile)

    task1Path = os.path.join('..', 'Resources', 'maps', 'task1')
    if os.path.isdir(task1Path):
        imagesDir = os.path.join(task1Path, 'images')
        if not os.path.isdir(imagesDir):
            os.makedirs(imagesDir)
        for fileName in os.listdir(task1Path):
            if ".html" in fileName:
                saveScreenshot(driver, fileName, imagesDir, task1Path)

    task2A1Path = os.path.join("..", "Resources", "maps", "task2A1")
    if os.path.isdir(task2A1Path):
        imagesDir = task2A1Path + "/images"
        if not os.path.isdir(imagesDir):
            os.makedirs(imagesDir)
        for fileName in os.listdir(task2A1Path):
            if ".html" in fileName:
                saveScreenshot(driver, fileName, imagesDir, task2A1Path)

    task2A2Path = os.path.join("..", "Resources", "maps", "task2A2")
    if os.path.isdir(task2A2Path):
        imagesDir = os.path.join(task2A2Path, "images")
        if not os.path.isdir(imagesDir):
            os.makedirs(imagesDir)
        for fileName in os.listdir(task2A2Path):
            if ".html" in fileName:
                saveScreenshot(driver, fileName, imagesDir, task2A2Path)

    driver.quit()


if __name__ == '__main__':
    getScreenshotsFromMaps()
    exit()
