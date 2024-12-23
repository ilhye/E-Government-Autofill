from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options 
options = Options()
options.add_argument("--start-maximized") 

# Initialize WebDriver
driver = webdriver.Chrome(options=options)

# Navigate to the URL
driver.get("https://www.pagibigfundservices.com/PubReg/NewReg_Page.aspx")

# Autofill
driver.find_element(By.ID, "txtMemLname").send_keys("Mentos") 
driver.find_element(By.ID, "txtMemFname").send_keys("Fifto") 
driver.find_element(By.ID, "txtMName").send_keys("Canton") 

# Keep the browser open for 30 seconds
time.sleep(30)

# Close the browser
driver.quit()