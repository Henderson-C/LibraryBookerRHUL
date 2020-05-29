import os
import os.path
import time
import math
from datetime import datetime
from datetime import timedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
##########################################################################
def browserChoice():
    if os.path.exists(os.getcwd()+"\config.txt") == True:
        textFileConfig = open("config.txt","r")
        bChoice = textFileConfig.readline()
        if bChoice == "Firefox": return (webdriver.Firefox())
        elif bChoice == "Edge": return (webdriver.Edge(os.getcwd()+"\msedgedriver.exe"))
        else: return (webdriver.Chrome(os.getcwd()+"\chromedriver.exe"))
    else: return (webdriver.Chrome(os.getcwd()+"\chromedriver.exe"))
##########################################################################
def logIn(driver):
    if os.path.exists(os.getcwd()+"\login.txt") == True:
        textFileLogin = open("login.txt","r")
        usernameUserInput = textFileLogin.readline()
        passwordUserInput = textFileLogin.readline()
        textFileLogin.close()
    else:
        print("Enter username:")
        usernameUserInput = input()
        print("Enter password:")
        passwordUserInput = input()
    userLogin = driver.find_element_by_id("userNameInput")
    userLogin.send_keys(usernameUserInput)
    userLogin = driver.find_element_by_id("passwordInput")
    userLogin.send_keys(passwordUserInput)
    userLogin.send_keys(Keys.RETURN)
##########################################################################
def bookPage(driver):
    try:
        myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ember1115')))
        bookButton = driver.find_element_by_id("ember1115")
        bookButton.click()
    except TimeoutException:
        print ("bookPage took too much time!")
##########################################################################
def roomSelect(driver):
    try:
        myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ember1449')))
        availableNow = driver.find_element_by_id("ember1449")
        availableNow.click()
        firstPass = driver.find_element_by_class_name("resourcesList-item-name")
        firstPass.click()
        time.sleep(1)
        libraryRoom = driver.find_element_by_class_name("resourcesList-item-name")
        libraryRoom.click()
    except TimeoutException:
        print ("roomSelect took too much time!")
##########################################################################
def roomBook(driver):
    try:
        myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'chronos-weekView-day--active')))
        daySelect = driver.find_element_by_class_name("chronos-weekView-day--active")
        daySelect.click()
        #asigns name to booking
        bookingName = driver.find_element_by_class_name("bookingRequestForm-title-input")
        bookingName.click()
        #selects start minute field
        bookingName.send_keys("automatic booking")
        timeSelect = driver.find_element_by_xpath("/html/body/div/div/div/div/div[3]/div/div/div/div/div/div/form/div/div[3]/span[1]/div/div[2]/div[3]/select")
        timeSelect.click()
        #finds out current minute and inputs it (rounded up to nearest 15)
        now=datetime.now().time()
        minutes=roundUp(now.minute,-1)
        timeSelect.send_keys(str(minutes))
        timeSelect.send_keys(Keys.RETURN)
        next=0
        if minutes > 45:
            next=1
        else:
            next=0

        #selects start hour field
        timeSelect = driver.find_element_by_xpath("/html/body/div/div/div/div/div[3]/div/div/div/div/div/div/form/div/div[3]/span[1]/div/div[2]/div[1]/select")
        timeSelect.click()
        #finds out current time and inputs it
        startHour=datetime.now()+timedelta(hours=next)
        current_time=startHour.strftime("%H")
        timeSelect.send_keys(current_time)
        timeSelect.send_keys(Keys.RETURN)
        #selects end minute field
        timeSelect = driver.find_element_by_xpath("/html/body/div/div/div/div/div[3]/div/div/div/div/div/div/form/div/div[3]/span[2]/div/div[2]/div[3]/select")
        timeSelect.click()
        #end minutes same as start minutes 
        timeSelect.send_keys(str(minutes))
        timeSelect.send_keys(Keys.RETURN)
        #selects end hour field
        timeSelect = driver.find_element_by_xpath("/html/body/div/div/div/div/div[3]/div/div/div/div/div/div/form/div/div[3]/span[2]/div/div[2]/div[1]/select")
        timeSelect.click()
        #finds out time in 2 hours and attempts to input it
        endHour=startHour+timedelta(hours=2)
        end_time=endHour.strftime("%H")
        timeSelect.send_keys(end_time)
        timeSelect.send_keys(Keys.RETURN)
        #completes booking
        bookRoom = driver.find_element_by_class_name("asyncButton-label")
        bookRoom.click()
        time.sleep(100)
    except TimeoutException:
        print ("roomBook took too much time!")
##########################################################################
def roundUp(n, decimals=0):
    mult = 15 ** decimals
    rounded = math.ceil(n *mult)/mult
    return rounded
##########################################################################
def main():
    driver = browserChoice()
    driver.get("https://adfs.rhul.ac.uk/adfs/ls/?SAMLRequest=fZHRT4MwEMb%2fFdL30QKC2owl0z24ZItkoA%2b%2bHaVzjdBirxj%2ffAtzcb7wdPmu912%2b%2b3WJ0LU9Xw%2fupA%2fyc5Dogu%2bu1cjHh5wMVnMDqJBr6CRyJ3i53u94HDIOiNI6ZTQJtpucqCbJ7lhzFHEWseYGElangiUJsOhW3Gd1fSTBq7ToDTnxfu9CHORWowPtfIvFbMHSRZxVccTTlEfsjQSFNc4I0z4o3Sj9Pp%2boPg8hf6qqYlE8lxUJ1peUj0bj0ElbSvulhHw57HJycq5HTikKBR5B6KvUTkEoTEdHKKMSMNpp6YEUBh0JNp6S0lP3bwU0RwztaWhDEOHwMWnaIiVXPPv5%2bP3vrWS1HKf5xMeuZkPupYMGHEzxLmJJr%2f1n9f%2bTVz8%3d&RelayState=QRAJdgVX-tynfcuAgRijVYlCtCadx-CZ_IF1kYC7Gg2j62vTxjUzjjSTGqo0GTV-3ujPJua3Ab7vKslqnk5xQWh-3RMivi9xiL9o55BGfPAhxy-XvNZYcmZ9ZyikhJajOeBOqi4D_629sHd_vTPf2LJEClQbjIjbhcs488dGUpB5UNF-aE_DqCfLyMBtstpi-evERqCjAZVbFh-DpDSyuUtJddFSNznXev2UoxJaAItH2Y4nV5KsmVvdIRcI-qnQYoKNcjiPT0ch9HKMFR49mWBQdovVv9WhlfViK_X4i8CftskUxoj-xizg_fjpD2CBaEe-O6diakkx2Hfr7FWp0knG2LbtYCqbOvYmr84yLvB-ilecvli3Omu6ofGrhfKHwvPGCljKf5JgTW5t8el_l24geBPeuO2gXAtAvRkVlXIAIKPQQsPyBBR6q3XuJ4AnEjAxF5F2AaaXBQyxO7ecu4YC0ZXepbAsDBxwfdyKocNTF4G71qF_zWtOL1_VTLBRALe3BIBJIyhTCs4WM8mahs2xNdGdc-C-RUp4QcM7b1I")
    logIn(driver)
    bookPage(driver)
    roomSelect(driver)
    roomBook(driver)
##########################################################################
main()