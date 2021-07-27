import pandas
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


user = 'chaossean@gmail.com'
#user = 'yomotzuve@gmail.com'
psw = 'chaos7823'

url = 'https://mastercoin.top'
url_login = 'https://mastercoin.top/login'
url_bonus = 'https://mastercoin.top/cabinet/bonuses'
url_mining = 'https://mastercoin.top/cabinet'

text_login ='/html/body/div[3]/header/div[2]/div/nav/div/ul/li[6]/a'
usuario = '/html/body/div[3]/section/div/div/div[2]/div/form/div[1]/input'
password = '/html/body/div[3]/section/div/div/div[2]/div/form/div[2]/input'
btn_login = '/html/body/div[3]/section/div/div/div[2]/div/form/div[3]/div[2]/button'
text_bonus = '/html/body/div[3]/header/div[2]/div/nav/div/ul/li[5]/a'
btn_getbonus = '/html/body/div[3]/section/div/div/div[5]/div[1]/div/div/div/div[2]/button'
text_btn_getbonus = '/html/body/div[3]/section/div/div/div[5]/div[1]/div/div/div/div[2]/button/span/i'
text_exit = '/html/body/div[3]/header/div[2]/div/nav/div/ul/li[8]/a'


# Abrir el Navegador:
print('1.-------Abriendo explorador Chrome')
driver = webdriver.Chrome()
driver.maximize_window()

print('2.-------Abriendo URL')
driver.get(url)
time.sleep(7)

# Acciones en la pagina
print('3.-------Click en LOGIN')
driver.find_element_by_xpath(text_login).click()
time.sleep(5)

print('4.-------Correo')
driver.find_element_by_xpath(usuario).send_keys(user)
time.sleep(2)

print('5.-------Password')
driver.find_element_by_xpath(password).send_keys(psw)
time.sleep(2)

print('6.-------Click login')
driver.find_element_by_xpath(btn_login).click()
time.sleep(5)

print('7.-------Click en Bonus')
driver.find_element_by_xpath(text_bonus).click()
time.sleep(2)

print('8.-------Click a Bonus')
try:
    if driver.find_element_by_xpath('/html/body/div[3]/section/div/div/div[5]/div[1]/div/div/div/div[2]/button'):
        driver.find_element_by_xpath(btn_getbonus).click()
except ec:
    pass

time.sleep(2)

print('9.-------Cerrando el navegador')
driver.find_element_by_xpath(text_exit).click()
time.sleep(5)
driver.quit()