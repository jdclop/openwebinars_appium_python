from appium.webdriver.common.appiumby import AppiumBy

from appium.webdriver.extensions.action_helpers import ActionHelpers

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

def click_on(driver, type, locator):
    driver.find_element(by=type, value=locator).click()
    
def write_text(driver, type_element, locator_element, text):
    driver.find_element(by=type_element, value=locator_element).send_keys(text)
    
def scroll(driver, type_origin, locator_origin, type_destination, locator_destination, duration=1500):
    origin_el = driver.find_element(by=type_origin, value=locator_origin)
    destination_el = driver.find_element(by=type_destination, value=locator_destination)
    ActionHelpers.scroll(driver, origin_el, destination_el, duration)
    
def scroll_by_coordinates(driver, start_y, end_y, duration=2000):
    ActionHelpers.swipe(driver, 600, start_y, 600, end_y, duration)
    
def scroll_until_element(driver, type_element, locator_element, duration=2000, attempts=5):
    driver.implicitly_wait(0)
    wait = WebDriverWait(driver, timeout=1)
    for i in range(0,attempts):        
        try:            
            wait.until(EC.presence_of_element_located((type_element, locator_element)))            
        except:
            print("Intento "+str(i+2)+" de "+str(attempts)+"...")
            scroll_by_coordinates(driver, 1100, 400)
    driver.implicitly_wait(10)
    
    
def swipe_left(driver, type_element, locator_element, duration=1100):
    element = driver.find_element(by=type_element, value=locator_element)
    start_x = element.rect['x'] + (element.rect['width']/2)
    start_y = element.rect['y'] + (element.rect['height']/2)
    end_x = start_x - 300
    end_y = start_y
    ActionHelpers.swipe(driver, start_x, start_y, end_x, end_y, duration)
    
def drag_n_drop(driver, type_element, locator_element, type_drop_zone, locator_drop_zone, duration=1500):
    actions = ActionChains(driver)
    touch_input = PointerInput(interaction.POINTER_TOUCH, "touch")
    actions.w3c_actions = ActionBuilder(driver, mouse=touch_input, duration=duration)
    actions.w3c_actions.pointer_action.click_and_hold(driver.find_element(by=type_element, value=locator_element))
    # EN CASO DE QUE AUMENTANDO EL TIEMPO DE DURACIÓN DE LA ACCIÓN NO FUNCIONE
    # AGREGAR EL MÉTODO "PAUSE" CON 1s DE DELAY DARÁ TIEMPO A LA APP PARA REACCIONAR
    actions.w3c_actions.pointer_action.pause(1)
    actions.w3c_actions.pointer_action.move_to(driver.find_element(by=type_drop_zone, value=locator_drop_zone))
    actions.w3c_actions.pointer_action.release()
    actions.perform()
