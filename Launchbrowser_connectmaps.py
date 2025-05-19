from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

options = Options()

options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--user-data-dir=C:\\Users\\Nagarjuna.E\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
options.add_argument("--profile-directory=Default"); 
options.add_experimental_option("detach", True)

# Launch browser with your profile
driver = webdriver.Chrome(options=options)
driver.maximize_window()
time.sleep(3)

#Opens a new tab and switches to new tab & Lauches the  confluence page and perfomes the signin
driver.get("https://www.google.com/maps/")
time.sleep(2)

#Opens the new tab in window
driver.switch_to.new_window('tab')
driver.get("https://www.amazon.in/")


