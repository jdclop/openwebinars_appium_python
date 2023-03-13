from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import math
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


def circulo(centroX, centroY, radio, gradoInicio, grados, pasos):
    angulo = grados/pasos
    gradToRad = math.pi/180
    prevX = centroX + radio * math.cos(gradoInicio * gradToRad)
    prevY = centroY + radio * math.sin(gradoInicio * gradToRad)

    touch_input = PointerInput(interaction.POINTER_TOUCH, "touch")
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=touch_input, duration=200)

    actions.w3c_actions.pointer_action.move_to_location(prevX, prevY)
    actions.w3c_actions.pointer_action.pointer_down()
    print("inicial X= "+str(prevX))
    print("inicial Y= "+str(prevY))

    for i in range(1,pasos+2):
        newX = centroX + radio * math.cos((gradoInicio + angulo * i) * gradToRad)
        newY = centroY + radio * math.sin((gradoInicio + angulo * i) * gradToRad)
        print("newX- "+str(i)+"= "+str(newX))
        print("newY- "+str(i)+"= "+str(newY))

        difX = newX - prevX
        difY = newY - prevY
        print("difX- "+str(i)+"= "+str(difX))
        print("difY- "+str(i)+"= "+str(difY))

        actions.w3c_actions.pointer_action.move_to_location(prevX+difX, prevY+difY)

        print("X- "+str(i)+"= "+str(prevX+difX))
        print("Y- "+str(i)+"= "+str(prevY+difY))

        prevX = newX
        prevY = newY

    actions.w3c_actions.pointer_action.release()
    actions.perform()

def uvedoble(origenX, origenY, radio):
    touch_input = PointerInput(interaction.POINTER_TOUCH, "touch")
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=touch_input, duration=300)
    
    pointX = origenX+radio
    pointY = origenY-radio

    actions.w3c_actions.pointer_action.move_to_location(pointX, pointY)
    actions.w3c_actions.pointer_action.pointer_down()
    pointX = pointX+60
    pointY = pointY+(2*radio)
    actions.w3c_actions.pointer_action.move_to_location(pointX, pointY)
    pointX = pointX+60
    pointY = pointY-radio
    actions.w3c_actions.pointer_action.move_to_location(pointX, pointY)
    pointX = pointX+60
    pointY = pointY+radio
    actions.w3c_actions.pointer_action.move_to_location(pointX, pointY)
    pointX = pointX+60
    pointY = pointY-(2*radio)
    actions.w3c_actions.pointer_action.move_to_location(pointX, pointY)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

def dibujar(centroX, centroY, radio, gradoInicio, grados, pasos):
    circulo(centroX, centroY, radio, gradoInicio, grados, pasos)
    uvedoble(centroX, centroY, radio)


options = UiAutomator2Options().load_capabilities(
    {
  "platformName": "android",
  "appium:platformVersion": "13",
  "appium:deviceName": "Pixel_3a_API_33_x86_64",
  "appium:automationName": "uiautomator2",
  "appium:app": "C:/PROJECTS/APPIUM/Android.SauceLabs.Mobile.Sample.app.2.7.1.apk",
  "appium:appActivity": "com.swaglabsmobileapp.MainActivity",
  "appium:appPackage": "com.swaglabsmobileapp",
  "newCommandTimeout": 500
})

driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
driver.implicitly_wait(10)

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='test-Username').send_keys("standard_user")
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='test-Password').send_keys("secret_sauce")
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='test-LOGIN').click()

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='test-Menu').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='test-DRAWING').click()

time.sleep(2)

dibujar(400,1200,100,0,360,15)






