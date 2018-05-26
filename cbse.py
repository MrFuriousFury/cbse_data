from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://cbseresults.nic.in/class12zpq/class12th18.htm')

filepath = 'marks.txt'
school_number = '72511'
center_number = '8801'
rollnumber = 9100001  #to be iterated

f = open('marks.txt', 'r')
x = f.read().splitlines()

for i in range(800):
  #Enter roll
  roll_box = driver.find_element_by_name("regno").send_keys(roll_number+i)
  #Enter school number
  school_box = driver.find_element_by_name("sch").send_keys(school_number)
  #Enter center number
  center_box = driver.find_element_by_name("cno").send_keys(center_number)
  #Press submit
  sumbmit_button = driver.find_element_by_name("B2")
  
