#from openpyxl import load_workbook
import xlwt
from selenium import webdriver
import time
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Python Sheet 1")
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
time.sleep(2)
name = driver.findElements(By.xpath("/html/body/div[1]/table[1]/tbody/tr[2]/td[2]/font/b")).getText()
sub1 = driver.findElements(By.xpath("/html/body/div[1]/div/center/table/tbody/tr[2]/td[2]/font")).getText()
sub2 = driver.findElements(By.xpath("/html/body/div[1]/div/center/table/tbody/tr[3]/td[2]/font")).getText()
sub3 = driver.findElements(By.xpath("/html/body/div[1]/div/center/table/tbody/tr[4]/td[2]/font")).getText()
sub4 = driver.findElements(By.xpath("/html/body/div[1]/div/center/table/tbody/tr[5]/td[2]/font")).getText()
sub5 = driver.findElements(By.xpath("/html/body/div[1]/div/center/table/tbody/tr[6]/td[2]/font")).getText()
