from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# UTILIZANDO ACTIONCHAINS, ACTIONBUILDER, DURATION Y PAUSE

login_page = {
    "username_tb": (AppiumBy.ACCESSIBILITY_ID,'test-Username'),
    "password_tb": (AppiumBy.ACCESSIBILITY_ID,'test-Password'),
    "login_btn":   (AppiumBy.ACCESSIBILITY_ID,'test-LOGIN')
}

products_page = {
    "toggle_btn": (AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="test-Toggle"]/android.widget.ImageView'),
    "cart_btn": (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Cart"]/android.view.ViewGroup/android.widget.ImageView')
}

products_page_vertical = {
    'fourth_product': (AppiumBy.XPATH, '//android.widget.ScrollView[@content-desc="test-PRODUCTS"]/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup'),    
    'first_product': (AppiumBy.XPATH, '//android.widget.ScrollView[@content-desc="test-PRODUCTS"]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup'),
    'fifth_product_title': (AppiumBy.XPATH, '(//android.widget.TextView[@content-desc="test-Item title"])[5]'),
    
    'add_btns': (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="test-ADD TO CART"])/android.widget.TextView')
}

cart_page = {
    'first_product': (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="test-Item"])[1]')
}

def createDriver():
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
    return driver
    

def loginSauceDemo(driver):
    driver.find_element(*login_page["username_tb"]).send_keys('standard_user')
    driver.find_element(*login_page["password_tb"]).send_keys('secret_sauce')
    driver.find_element(*login_page["login_btn"]).click()



# LOGIN
driver = createDriver()
loginSauceDemo(driver)

# CAMBIAMOS A LA VISTA VERTICAL
driver.find_element(*products_page["toggle_btn"]).click()

# AGREGAMOS UNA ESPERA EXPLÍCITA PARA EL QUINTO ELEMENTO
# DE LA LISTA. DE ESTE MODO GARANTIZAMOS QUE NOS ENCOMTRAMOS
# EN LA VISTA VERTICAL DE LOS PRODUCTOS
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located(products_page_vertical["fifth_product_title"]))

    
handler2_xpath = '(//android.view.ViewGroup[@content-desc="test-Drag Handle"])[2]/android.widget.TextView'
drop_zone_aid = 'test-Cart drop zone'

origin_el = driver.find_element(AppiumBy.XPATH, handler2_xpath)
destination_el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, drop_zone_aid)

# CREAMOS EL OBJETO ACTIONCHAINS Y AGREGAMOS EL ACTIONBUILDER CON
# UN TOUCH TIPO 'DEDO' Y DELAY DE 2 SEGUNDOS
actions = ActionChains(driver)
touch_input = PointerInput(interaction.POINTER_TOUCH, "touch")
actions.w3c_actions = ActionBuilder(driver, mouse=touch_input, duration=2000)

# APARTE DE UN TIEMPO DE 2 SEGUNDOS PARA EJECUTAR LA ACCIÓN, REALIZAMOS
# UNA PAUSA DE 1 SEGUNDO TRAS PULSAR Y MANTENER EL HANDLER
# DEL ELEMENTO. DE ESTE MODO LA APP TIENE TIEMPO PARA REACCIONAR A LA ACCIÓN
# DE INICIAR EL DRAG AND DROP
actions.w3c_actions.pointer_action.click_and_hold(origin_el)
actions.w3c_actions.pointer_action.pause(1)
actions.w3c_actions.pointer_action.move_to(destination_el)
actions.w3c_actions.pointer_action.release()
actions.perform()
