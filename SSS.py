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
driver.get("https://employer.sss.gov.ph/employer/pbl/hrRegHome")

# Autofill form fields 
driver.find_element(By.NAME, "empid").send_keys("123456789")  
driver.find_element(By.NAME, "mobile").send_keys("9123456789") 
driver.find_element(By.NAME, "email").send_keys("juandelacrux@gmail.com")  
driver.find_element(By.NAME, "confemail").send_keys("juandelacrux@gmail.com")
driver.find_element(By.NAME, "userid").send_keys("JuanDelaCruz12345")  
driver.find_element(By.NAME, "confUserId").send_keys("JuanDelaCruz12345")  

# Keep the browser open for 30 seconds
time.sleep(30)

# Close the browser
driver.quit()
