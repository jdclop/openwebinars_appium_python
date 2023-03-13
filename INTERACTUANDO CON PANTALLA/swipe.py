from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

from appium.webdriver.extensions.action_helpers import ActionHelpers

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# RECOGEMOS LOS BOTONES DE PRODUCTOS Y PULSAMOS EN AGREGAR SOBRE 3 DE ELLOS
add_buttons_elements = driver.find_elements(*products_page_vertical['add_btns'])

for add_btn in add_buttons_elements[1:4]:
    add_btn.click()

# CLICK EN CARRITO
driver.find_element(*products_page['cart_btn']).click()

# RECUPERAMOS EL PRIMER PRODUCTO DE LA PÁGINA DE CARRITO
product = driver.find_element(*cart_page['first_product'])

# APLICANDO SWIPE DE ACTIONHELPERS
origin_product_coordX = product.rect['x'] + int(product.rect['width']/2)
origin_product_coordY = product.rect['y'] + int(product.rect['height']/2)
destination_product_coordX = origin_product_coordX - 200
destination_product_coordY = origin_product_coordY

ActionHelpers.swipe(driver, origin_product_coordX, origin_product_coordY, destination_product_coordX, destination_product_coordY, 300)

