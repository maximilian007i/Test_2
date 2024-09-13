from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_purchase():
    
    driver = webdriver.Chrome()
    driver.get("https://saucedemo.com/")
    
    username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name")))
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()
    
    backpack_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    backpack_button.click()
    
    cart_button = driver.find_element(By.ID, "shopping_cart_container")
    cart_button.click()

    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()

    first_name_field = driver.find_element(By.ID, "first-name")
    last_name_field = driver.find_element(By.ID, "last-name")
    zip_code_field = driver.find_element(By.ID, "postal-code")
    continue_button = driver.find_element(By.ID, "continue")

    first_name_field.send_keys("John")
    last_name_field.send_keys("Doe")
    zip_code_field.send_keys("12345")
    continue_button.click()

    finish_button = driver.find_element(By.ID, "finish")
    finish_button.click()
    
    assert "THANK YOU FOR YOUR ORDER" in driver.page_source
    
    driver.quit()

test_purchase()