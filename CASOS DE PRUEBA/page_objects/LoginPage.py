from appium.webdriver.common.appiumby import AppiumBy

# LOCALIZADORES PERTENECIENTES A LA PÁGINA DE LOGIN
# NOTA: LOS LOCALIZADORES QUE HACEN USO DE LA FUNCIÓN LAMBDA LOS
#   UTILIZAMOS PARA RECUPERAR EL ELEMENTO CON ÍNDICE X AL PASARLO
#   COMO PARÁMETRO
username_tb = (AppiumBy.ACCESSIBILITY_ID, "test-Username")
password_tb = (AppiumBy.ACCESSIBILITY_ID, "test-Password")
login_btn = (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")

login_error_msg = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Error message"]/android.widget.TextView')


# MÉTODOS PERTENECIENTES A ACCIONES SÓLO EJECUTABLES
# DENTRO DE LA PÁGINA DE LOGIN
def login_user(driver, username, password):
    driver.find_element(*username_tb).send_keys(username)
    driver.find_element(*password_tb).send_keys(password)
    driver.find_element(*login_btn).click()
    
