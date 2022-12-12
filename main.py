from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import mysql.connector
import os
import datetime

print(datetime.datetime.now())
'''
def data_for_mysql_order(data_dict):
    data_arr = []
    for data in data_dict:
        data_vect = (data['name'], data['time'], data['daily_yield'], data['total_yield'], data['daily_hour'])
        data_arr.append(data_vect)
    return data_arr


mydb = mysql.connector.connect(
  host="ba462570.mysql.tools",
  user="ba462570_data212",
  password="8z88y(UFb+",
   database="ba462570_data212"
)
mycursor = mydb.cursor()
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
driver.get('https://www.isolarcloud.eu/?lang=en_US')

print("Connect to page")

login_field = driver.find_element("id", "userAcct")
login_field.send_keys("voloshchukmm1973@gmail.com")

password_field = driver.find_element("id", "userPswd")
password_field.send_keys("mn1epmpx")

button_log = driver.find_element("id", 'login-btn')
button_log.click()
time.sleep(3)
agree_field = driver.find_elements(By.CLASS_NAME, "privacy-agree")
agree_field[0].click()

print("Go to next page")

time.sleep(6)
rep_field = driver.find_elements(By.CLASS_NAME, "reportAll")
rep_field[0].click()
time.sleep(3)
_field = driver.find_elements(By.CLASS_NAME, "reportPs")
_field[0].click()
time.sleep(3)
date_field = driver.find_elements(By.CLASS_NAME, "el-input--suffix")
input_date = date_field[1].find_elements(By.CLASS_NAME, "el-input__inner")
input_date[0].click()
input_date[0].clear()
input_date[0].send_keys("2022-11-30")
time.sleep(3)
time_field = driver.find_elements(By.CLASS_NAME, "el-input--suffix")
time_field[4].click()
time.sleep(3)
time_field_5 = driver.find_elements(By.CLASS_NAME, "el-select-dropdown__item")
time_field_5[0].click()
time.sleep(3)


data = []
data_one = {}
name_data = driver.find_elements(By.CLASS_NAME, "el-table_2_column_6")
time_data = driver.find_elements(By.CLASS_NAME, "el-table_2_column_7")
daily_data = driver.find_elements(By.CLASS_NAME, "el-table_2_column_8")
total_data = driver.find_elements(By.CLASS_NAME, "el-table_2_column_9")
daily_hour_data = driver.find_elements(By.CLASS_NAME, "el-table_2_column_14")

print("Start loop")

for i in range(0,len(name_data)):
    data_one["name"] = name_data[i].text
    data_one["time"] = time_data[i].text
    data_one["daily_yield"] = daily_data[i].text
    data_one["total_yield"] = total_data[i].text
    data_one["daily_hour"] = daily_hour_data[i].text
    data.append(data_one)
    data_one = {}
data.pop(0)
print("Start write to mysql")
print(len(data))
prepare_data_orders = data_for_mysql_order(data)
sql = "INSERT INTO solar (name, date_time, daily_yield, total_yield,  daily_hour) VALUES (%s, %s, %s, %s, %s)"
mycursor.executemany(sql, prepare_data_orders)
mydb.commit()
'''
