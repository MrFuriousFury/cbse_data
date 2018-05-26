#from openpyxl import load_workbook
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://cbseresults.nic.in/class12zpq/class12th18.htm')

school_number = '72511'
center_number = '8801'
roll_number = 9100001  #to be iterated

#for i in range(800)
roll_box = driver.find_element_by_name("regno").send_keys(roll_number)
school_box = driver.find_element_by_name("sch").send_keys(school_number)
center_box = driver.find_element_by_name("cno").send_keys(center_number)
sumbmit_button = driver.find_element_by_name("B2")
sumbmit_button.click()
time.sleep(10)
name = driver.find_element_by_xpath("/html/body/div[1]/table[1]/tbody/tr[2]/td[2]/font/b").text
print(name)
for i in range(2,7):
    sub = driver.find_element_by_xpath("/html/body/div[1]/div/center/table/tbody/tr[" + i + "]/td[2]/font").text
    marks = driver.find_element_by_xpath("/html/body/div[1]/div/center/table/tbody/tr[" + i + "]/td[5]/font").text
    print(i+": "+sub)
    print(i+": "+marks)
driver.quit()
