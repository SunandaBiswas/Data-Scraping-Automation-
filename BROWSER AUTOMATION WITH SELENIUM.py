#!pip install selenium

from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.support.ui import Select

## for opening a specific website by automated test software, chromedriver

driver = webdriver.Chrome(executable_path= 'chromedriver.exe')
driver.get('https://www.imdb.com/')   #To access any website


# maximize window
driver.maximize_window()

# dropdown
dropdown = driver.find_element_by_class_name('ipc-icon--arrow-drop-down')
dropdown.click()  ##automatically opens a dropdown menu
time.sleep(1) #after navigating a dropdown bar will pause for 1second

# accesses the linked page of advanced search from dropdown menu of IMDB website
element = driver.find_element_by_link_text('Advanced Search')
element.click()


# click on avanced title search
adv_title = driver.find_element_by_link_text('Advanced Title Search')
adv_title.click() 


# selecting feature film
feature_film = driver.find_element_by_id('title_type-1')
feature_film.click() 

# select tv movie
tv_movie = driver.find_element_by_id('title_type-12')
tv_movie.click()


# min date
min_date = driver.find_element_by_name('release_date-min')
min_date.click()
min_date.send_keys('1990') ## starting time range 

# max date
max_date = driver.find_element_by_name('release_date-max')
max_date.click()
max_date.send_keys('2020') ## last time range


# rating min
rating_min = driver.find_element_by_name('user_rating-min')
rating_min.click()
dropdown_2 = Select(rating_min)
dropdown_2.select_by_visible_text('1.0') 
##select_by_visible_text has been used for selecting exactly what is shown in dropdown menu

# rating max
rating_max = driver.find_element_by_name('user_rating-max')
rating_max.click()
dropdown_3 = Select(rating_max)
dropdown_3.select_by_visible_text('10')

# oscar Winning
oscar_nominated = driver.find_element_by_id('groups-4')
oscar_nominated.click()

# color info
color = driver.find_element_by_id('colors-3')
color.click()

# language
language = driver.find_element_by_name('languages')
dropdown_4 = Select(language)
dropdown_4.select_by_visible_text('English') 

# 250 results
results_count = driver.find_element_by_id('search-count')
dropdown_5 = Select(results_count)
dropdown_5.select_by_index(2)


# submit
submit = driver.find_element_by_xpath('(//button[@type="submit"])[2]')  ##Xpath Expresssion for button tag
submit.click()

# current
current_url = driver.current_url 
