from pathlib import Path
from selenium import webdriver
import os
from sys import platform
import time

base_link = "https://www.patreon.com/journeytomicro/posts?filters[media_types]=image"

def start(driver:webdriver):
    login_link = "https://www.patreon.com/login?ru=%2Fjourneytomicro"
    driver.get(login_link)
    for i in range(40):
        print(40-i)
        time.sleep(1)

def get_driver():
    # profile = webdriver.FirefoxProfile()
    # profile.set_preference('browser.download.folderList', 2) # custom location
    # profile.set_preference('browser.download.manager.showWhenStarting', False)
    # profile.set_preference('browser.download.dir', os.getcwd())
    # profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/html')

    low = 'linux'
    lowfile = "geckodriver"
    if platform == "linux" or platform == "linux2":
        low = 'linux'
        lowfile = "geckodriver"
    # linux
    elif platform == "darwin":
        low = 'osx'
        lowfile = "geckodriver"
    # OS X
    elif platform == "win32":
        low = 'windows'
        lowfile = "geckodriver.exe"
    seleniumlocations = Path(__file__).parent /'drivers'/ low / lowfile
    driver = webdriver.Firefox(executable_path=seleniumlocations)
    return driver

def get_images(driver:webdriver):
    aclasses = driver.find_elements_by_class_name("sc-ikJyIC fHGuxZ")
    links = []
    for ac in aclasses:
        if("16x9.png" in ac.text or "Monitor.jpg" ):
            link = ac.getAttribute("href")
            link.click()
            links.append(link)


if __name__ == '__main__':
    driver = get_driver()
    start(driver)
    driver.get(base_link)
    time.sleep(4)
    get_images(driver)