
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome(executable_path= r'C:\Users\sunan\Downloads\chromedriver.exe')
# maximize window
driver.maximize_window()
driver.get('https://www.youtube.com/watch?v=QaR31V5xBQ8&ab_channel=DJBoBo')  

p = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,
                                           '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[3]/div/ytd-player/div/div/div[33]/div[2]/div[1]/button')))
p.click()

# maximize window
driver.maximize_window()
