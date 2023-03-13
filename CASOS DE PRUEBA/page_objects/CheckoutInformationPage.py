from appium.webdriver.common.appiumby import AppiumBy

# LOCALIZADORES PERTENECIENTES A LA PÁGINA DE INFORMACIÓN DE COMPRA
first_name_tb = (AppiumBy.ACCESSIBILITY_ID, 'test-First Name')
last_name_tb = (AppiumBy.ACCESSIBILITY_ID, 'test-Last Name')
zip_code_tb = (AppiumBy.ACCESSIBILITY_ID, 'test-Zip/Postal Code')

continue_btn = (AppiumBy.ACCESSIBILITY_ID, 'test-CONTINUE')

# MÉTODOS PERTENECIENTES A ACCIONES SÓLO EJECUTABLES DENTRO
# DE LA PÁGINA DE INFORMACIÓN DE COMPRA
def fill_form(driver, first_name, last_name, zip_code):
    driver.find_element(*first_name_tb).send_keys(first_name)
    driver.find_element(*last_name_tb).send_keys(last_name)
    driver.find_element(*zip_code_tb).send_keys(zip_code)
    
