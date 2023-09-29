from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service_obj = Service() # service is responsible for start & close of driver
print('service : ', service_obj)
driver = webdriver.Chrome(service=service_obj)
print('driver : ',driver)
driver.get('https://www.facebook.com')

