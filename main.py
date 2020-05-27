import os
import os.path
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as BC

if os.path.exists(os.getcwd()+"\login.txt") == True:
    textFile = open("login.txt","r")
    usernameUserInput = textFile.readline()
    passwordUserInput = textFile.readline()
    textFile.close()
else:
    print("Enter username:")
    usernameUserInput = input()
    print("Enter password:")
    passwordUserInput = input()

PATH = os.getcwd()+"\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://adfs.rhul.ac.uk/adfs/ls/?SAMLRequest=fZHRT4MwEMb%2fFdL30QKC2owl0z24ZItkoA%2b%2bHaVzjdBirxj%2ffAtzcb7wdPmu912%2b%2b3WJ0LU9Xw%2fupA%2fyc5Dogu%2bu1cjHh5wMVnMDqJBr6CRyJ3i53u94HDIOiNI6ZTQJtpucqCbJ7lhzFHEWseYGElangiUJsOhW3Gd1fSTBq7ToDTnxfu9CHORWowPtfIvFbMHSRZxVccTTlEfsjQSFNc4I0z4o3Sj9Pp%2boPg8hf6qqYlE8lxUJ1peUj0bj0ElbSvulhHw57HJycq5HTikKBR5B6KvUTkEoTEdHKKMSMNpp6YEUBh0JNp6S0lP3bwU0RwztaWhDEOHwMWnaIiVXPPv5%2bP3vrWS1HKf5xMeuZkPupYMGHEzxLmJJr%2f1n9f%2bTVz8%3d&RelayState=QRAJdgVX-tynfcuAgRijVYlCtCadx-CZ_IF1kYC7Gg2j62vTxjUzjjSTGqo0GTV-3ujPJua3Ab7vKslqnk5xQWh-3RMivi9xiL9o55BGfPAhxy-XvNZYcmZ9ZyikhJajOeBOqi4D_629sHd_vTPf2LJEClQbjIjbhcs488dGUpB5UNF-aE_DqCfLyMBtstpi-evERqCjAZVbFh-DpDSyuUtJddFSNznXev2UoxJaAItH2Y4nV5KsmVvdIRcI-qnQYoKNcjiPT0ch9HKMFR49mWBQdovVv9WhlfViK_X4i8CftskUxoj-xizg_fjpD2CBaEe-O6diakkx2Hfr7FWp0knG2LbtYCqbOvYmr84yLvB-ilecvli3Omu6ofGrhfKHwvPGCljKf5JgTW5t8el_l24geBPeuO2gXAtAvRkVlXIAIKPQQsPyBBR6q3XuJ4AnEjAxF5F2AaaXBQyxO7ecu4YC0ZXepbAsDBxwfdyKocNTF4G71qF_zWtOL1_VTLBRALe3BIBJIyhTCs4WM8mahs2xNdGdc-C-RUp4QcM7b1I")

userLogin = driver.find_element_by_id("userNameInput")
userLogin.send_keys(usernameUserInput)
userLogin = driver.find_element_by_id("passwordInput")
userLogin.send_keys(passwordUserInput)
userLogin.send_keys(Keys.RETURN)
time.sleep(2)
bookButton = driver.find_element_by_id("ember1115")
bookButton.click()
time.sleep(2)
availableNow = driver.find_element_by_id("ember1449")
availableNow.click()
firstPass = driver.find_element_by_class_name("resourcesList-item-name")
firstPass.click()