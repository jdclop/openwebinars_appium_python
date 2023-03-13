from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

from page_objects import LoginPage
from page_objects import ProductPage
from page_objects import CartPage
from page_objects import CheckoutInformationPage
from page_objects import CheckoutOverviewPage
from page_objects import CheckoutCompletePage
from page_objects import AppiumUtils


import unittest

class PruebasUnittest(unittest.TestCase):

    def setUp(self):
        print("Iniciar driver de Appium")
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
        self.driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        print("Cerrar driver de Appium")
        self.driver.quit()

    @unittest.skip("skip")
    def testLoginOK(self):
        LoginPage.login_user(self.driver, "standard_user", "secret_sauce")
        titulo = self.driver.find_element(*ProductPage.products_title).text
        self.assertEqual(titulo, "PRODUCTS")

    @unittest.skip("skip")    
    def testLoginKO(self):
        LoginPage.login_user(self.driver, "locked_out_user", "secret_sauce")
        login_error = self.driver.find_element(*LoginPage.login_error_msg).text
        self.assertEqual(login_error, "Sorry, this user has been locked out.")

    def testFlujoCompleto(self):
        LoginPage.login_user(self.driver, "standard_user", "secret_sauce")

        AppiumUtils.click_on(self.driver, *ProductPage.toggle_btn)

        AppiumUtils.scroll(self.driver, *ProductPage.V_product_item_INDEX(4), *ProductPage.V_product_item_INDEX(1), 2000)

        # AGREGAMOS MEDIANTE DRAG N DROP DOS ELEMENTOS A LA CESTA
        # RECORDAD QUE INDICAMOS EL INDÍCE "2" EN DOS OCASIONES PORQUE
        # AL AGREGAR EL PRIMERO, EL SIGUIENTE PASA A HEREDAR ESE ÍNDICE
        AppiumUtils.drag_n_drop(self.driver, *ProductPage.V_product_item_hdlr_INDEX(2), *ProductPage.drop_zone)
        AppiumUtils.drag_n_drop(self.driver, *ProductPage.V_product_item_hdlr_INDEX(2), *ProductPage.drop_zone)

        AppiumUtils.click_on(self.driver, *ProductPage.cart_btn)

        AppiumUtils.swipe_left(self.driver, *CartPage.product_INDEX(1))
        AppiumUtils.click_on(self.driver, *CartPage.delete_product)
        AppiumUtils.click_on(self.driver, *CartPage.checkout_btn)

        # ALTERNATIVA 1 - A TRAVÉS DE APPIUMUTILS ENVIAMOS TEXTO A LOS DISTINTOS CAMPOS
        '''
        AppiumUtils.write_text(self.driver, *CheckoutInformationPage.first_name_tb, "Jesús")
        AppiumUtils.write_text(self.driver, *CheckoutInformationPage.last_name_tb, "del Castillo")
        AppiumUtils.write_text(self.driver, *CheckoutInformationPage.zip_code_tb, "123456")
        '''
        # ALTERNATIVA 2 - A TRAVÉS DEL PAGE OBJECT UTILIZAMOS EL MÉTODO FILL_FORM
        CheckoutInformationPage.fill_form(self.driver, "Jesús", "del Castillo", "123456")
        
        AppiumUtils.click_on(self.driver, *CheckoutInformationPage.continue_btn)

        AppiumUtils.scroll_until_element(self.driver, *CheckoutOverviewPage.finish_btn)        
        AppiumUtils.click_on(self.driver, *CheckoutOverviewPage.finish_btn)
        
        message = self.driver.find_element(*CheckoutCompletePage.thank_you_title).text
        self.assertEqual(message , "THANK YOU FOR YOU ORDER")
        

        

if __name__ == "__main__":
    unittest.main()
