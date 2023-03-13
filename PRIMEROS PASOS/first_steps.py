from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

import time

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
driver.implicitly_wait(10)

# RECUPERAMOS EL ELEMENTO TEXTBOX DE USUARIO
username_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='test-Username')
# ESCRIBIMOS "mi usuario" EN LA CAJA
username_el.send_keys("mi usuario")


# OBTENEMOS ALGUNOS ATRIBUTOS DEL ELEMENTO USERNAME
print("USERNAME ESTÁ HABILITADO: "+str(username_el.is_enabled()))
print("TAMAÑO DE USERNAME: "+str(username_el.size))
print("TAMAÑO Y LOCALIZACIÓN DE USERNAME: "+str(username_el.rect))
print("TAMAÑO Y LOCALIZACIÓN DE USERNAME con ATRIBUTO BOUNDS: "+str(username_el.get_attribute("bounds")))

print("TEXTO EN USERNAME ACTUALMENTE: "+str(username_el.text))
print("Borramos el usuario")
username_el.clear()
print("**Escribimos el nombre de usuario 'standard_user'...**")
username_el.send_keys('standard_user')
print("TEXTO NUEVO EN USERNAME: "+str(username_el.text))

# RECUPERAMOS EL ELEMENTO TEXTBOX DE PASSWORD Y ESCRIBIMOS LA CONTRASEÑA
password_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='test-Password')
password_el.send_keys('secret_sauce')

# RECUPERAMOS EL ELEMENTO DEL BOTÓN LOGIN Y LO CLICKAMOS PARA ACCEDER
login_btn = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='test-LOGIN')
login_btn.click()





