from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

import time

# UTILIZANDO ACTIONCHAINS, ACTIONBUILDER y DURATION
# VAMOS A DIBUJAR UNA LÍNEA EN LA SECCIÓN DE DRAWING

#LOGIN PAGE
username = (AppiumBy.ACCESSIBILITY_ID, 'test-Username')
password = (AppiumBy.ACCESSIBILITY_ID, 'test-Password')
login_button = (AppiumBy.ACCESSIBILITY_ID, 'test-LOGIN')

#PRODUCT PAGE
toggle_button_xpath = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Toggle"]/android.widget.ImageView')
burger_menu_button = (AppiumBy.ACCESSIBILITY_ID, 'test-Menu')
menu_drawing_button = (AppiumBy.ACCESSIBILITY_ID, 'test-DRAWING')
menu_all_items_button = (AppiumBy.ACCESSIBILITY_ID, 'test-ALL ITEMS')


def start_driver():
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

    return driver



driver = start_driver()

driver.find_element(*username).send_keys('standard_user')
driver.find_element(*password).send_keys('secret_sauce')
driver.find_element(*login_button).click()

driver.find_element(*burger_menu_button).click()

driver.find_element(*menu_drawing_button).click()

#ESPERAMOS UN TIEMPO PARA QUE EL CANVAS CARGUE
time.sleep(3)

# DECLARAMOS EL OBJECTO ACTIONS COMO INSTANCIA DE ACTIONCHAINS (INTERACCIONES DE BAJO NIVEL)
actions = ActionChains(driver)
# DECLARAMOS EL OBJETO TOUCH_INPUT, EL CUAL REPRESENTA UN "DEDO"
touch_input = PointerInput(interaction.POINTER_TOUCH, "touch")
# DECLARAMOS EL PRIMER ACTIONBUILDER, PASANDO EL OBJETO TOUCH_INPUT PARA INDICAR QUE NUESTRO
# PUNTERO SERÁ UN DEDO Y DURACIÓN DE ACCIÓN DE 500 MS
actions.w3c_actions = ActionBuilder(driver, mouse=touch_input, duration=500)
# MOVEMOS EL DEDO A LAS COORDENADAS X=500, Y=800 (PERO SIN PULSAR LA PANTALLA, ES DECIR, NOS
# UBICAMOS SOBRE ELLA PERO SIN PULSARLA
actions.w3c_actions.pointer_action.move_to_location(x=500, y=800)
# PRESIONAMOS LA PANTALLA EN ESTE MOMENTO
actions.w3c_actions.pointer_action.pointer_down()
# DECLARAMOS UN NUEVO ACTIONBUILDER, INDICANDO QUE SERÁ TAMBIÉN UN DEDO PERO QUE LAS
# ACCIONES A CONTINUACIÓN SERÁN DE 2000 MS
actions.w3c_actions = ActionBuilder(driver, mouse=touch_input, duration=2000)
# DESPLAZAMOS EL DEDO 400 PX HACIA ABAJO EN EL EJE Y (NUEVAS COORDENADAS X=500, Y=1200)
# COMO YA PULSAMOS LA PANTALLA ANTERIORMENTE, AHORA ESTAMOS INTERACTUANDO EN ELLA, DIBUJANDO UNA
# LINEA
actions.w3c_actions.pointer_action.move_to_location(x=500, y=1200)
# CANCELAMOS TODAS LAS INTERACCIONES, ES DECIR, RETIRAMOS EL PUNTERO (DEDO) DE LA PANTALLA
actions.w3c_actions.pointer_action.release()
# EJECUTAMOS TODAS LAS ACCIONES QUE HEMOS CONCATENADO
# RECORDAD QUE LAS ACCIONES NO FUNCIONAN A TIEMPO REAL. SE CONCATENAN Y POSTERIORMENTE EJECUTAN
actions.perform()
