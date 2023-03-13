from appium.webdriver.common.appiumby import AppiumBy

# LOCALIZADORES PERTENECIENTES A LA PÁGINA DEL CARRITO DE COMPRA
# NOTA: LOS LOCALIZADORES QUE HACEN USO DE LA FUNCIÓN LAMBDA LOS
#   UTILIZAMOS PARA RECUPERAR EL ELEMENTO CON ÍNDICE X AL PASARLO
#   COMO PARÁMETRO
product_INDEX = (lambda x: (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="test-Item"])['+str(x)+']'))
delete_product = (AppiumBy.ACCESSIBILITY_ID, 'test-Delete')
checkout_btn = (AppiumBy.ACCESSIBILITY_ID, 'test-CHECKOUT')

