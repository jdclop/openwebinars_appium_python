from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = UiAutomator2Options().load_capabilities({
    "platformName": "android",
    "appium:platformVersion": "13",
    "appium:deviceName": "Pixel_3a_API_33_x86_64",
    "appium:automationName": "uiautomator2",
    "appium:app": "C:/PROJECTS/APPIUM/Android.SauceLabs.Mobile.Sample.app.2.7.1.apk",
    "appium:appActivity": "com.swaglabsmobileapp.MainActivity",
    "appium:appPackage": "com.swaglabsmobileapp",
    "newCommandTimeout": 900    
})

driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

# DESCOMENTAR LAS 3 LÍNEAS SIGUIENTES PARA APLICAR LA ESPERA EXPLÍCITA
# AL TEXTBOX DE USERNAME
'''
wait = WebDriverWait(driver, timeout=10)
username_el = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'test-Username')))
'''

# COMENTAR EL BLOQUE TRY-EXCEPT Y DESCOMENTAR EL DE ESPERA EXPLÍCITA

#EN ESTE BLOQUE TRY-EXCEPT TRATAMOS DE INTERACTUAR CON EL ELEMENTO SIN ESTAR
#LISTO. LA ESPERA EXPLÍCITA AGUARDA EXACTAMENTE A QUE PUEDA RECIBIR CLICK
try:
    username_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='test-Username')
except NoSuchElementException as e:
    print(e)
    print("No se pudo encontrar el elemento")
    print("ESPERAMOS 3 SEGUNDOS")
    time.sleep(3)
    username_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='test-Username')

username_el.send_keys('standard_user')
password_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='test-Password')
password_el.send_keys('secret_sauce')
login_button_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='test-LOGIN')
login_button_el.click()


