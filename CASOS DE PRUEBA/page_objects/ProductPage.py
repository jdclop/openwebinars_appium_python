from appium.webdriver.common.appiumby import AppiumBy

# LOCALIZADORES PERTENECIENTES A LA PÁGINA DE PRODUCTOS
# NOTA: LOS LOCALIZADORES QUE HACEN USO DE LA FUNCIÓN LAMBDA LOS
#   UTILIZAMOS PARA RECUPERAR EL ELEMENTO CON ÍNDICE X AL PASARLO
#   COMO PARÁMETRO
products_title = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Cart drop zone"]/android.view.ViewGroup/android.widget.TextView')
toggle_btn = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Toggle"]/android.widget.ImageView')                              
cart_btn = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Cart"]/android.view.ViewGroup/android.widget.ImageView')
drop_zone = (AppiumBy.ACCESSIBILITY_ID, 'test-Cart drop zone')


filter_button = (AppiumBy.ACCESSIBILITY_ID, 'test-Modal Selector Button')
filter_price_high_2_low = (AppiumBy.XPATH, '//android.widget.ScrollView[@content-desc="Selector container"]/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup/android.widget.TextView')

V_product_item_INDEX = (lambda x: (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="test-Item"])['+str(x)+']'))
V_product_item_hdlr_INDEX = (lambda x: (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="test-Drag Handle"])['+str(x)+']/android.widget.TextView'))

