from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

from appium.webdriver.extensions.action_helpers import ActionHelpers

login_page = {
    "username_tb": (AppiumBy.ACCESSIBILITY_ID,'test-Username'),
    "password_tb": (AppiumBy.ACCESSIBILITY_ID,'test-Password'),
    "login_btn":   (AppiumBy.ACCESSIBILITY_ID,'test-LOGIN')
}

products_page = {
    "toggle_btn": (AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="test-Toggle"]/android.widget.ImageView')
}

products_page_vertical = {
    'fourth_product': (AppiumBy.XPATH, '//android.widget.ScrollView[@content-desc="test-PRODUCTS"]/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup'),
    'first_product': (AppiumBy.XPATH, '//android.widget.ScrollView[@content-desc="test-PRODUCTS"]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup')
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


# SCROLLING
driver = createDriver()
loginSauceDemo(driver)

driver.find_element(*products_page["toggle_btn"]).click()

# HACIENDO SCROLLING
origin_el = driver.find_element( *products_page_vertical["fourth_product"])
destination_el = driver.find_element(*products_page_vertical["first_product"])

# APLICANDO ACTIONHELPERS
ActionHelpers.scroll(driver, origin_el, destination_el, 2000)

