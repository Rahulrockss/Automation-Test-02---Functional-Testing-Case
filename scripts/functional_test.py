
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_driver_path = ChromeDriverManager().install()  # Install and get path to ChromeDriver
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
try:
    # Step 1: Navigate to the URL
    driver.get('https://demo.dealsdray.com/')
    
    # Step 2: Log in with provided credentials
    username = driver.find_element(By.CLASS_NAME, 'css-l8vkz1')  # Assuming ID 'email' for username field
    password = driver.find_element(By.CLASS_NAME, 'css-r71t31')  # Assuming ID 'password' for password field

    username.send_keys('prexo.mis@dealsdray.com')
    password.send_keys('prexo.mis@dealsdray.com')
    
    login_button = driver.find_element(By.XPATH, '//button[contains(text(),"Login")]')  # Adjust the XPATH according to the actual login button
    login_button.click()

    # Step 3: Wait until logged in and dashboard is loadedcss-i9zxpg
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Dashboard")]')))

    # Step 4: Navigate to the Orders section
    orders_section = driver.find_element(By.CLASS_NAME, 'css-1s178v5')
    orders_section.click()
    
    orders = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Orders")]')))
    orders.click()
    # Step 5: Navigate to Add Bulk Order
    add_bulk_order = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Add Bulk Orders")]')))
    # add_bulk_order.click()
    driver.execute_script("arguments[0].scrollIntoView();", add_bulk_order)
    driver.execute_script("arguments[0].click();", add_bulk_order)
    # Step 6: Upload the XLS file
    upload_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@type="file"]')))
    upload_button.send_keys('E:\Automation-Test-02---Functional-Testing-Case\scripts\demo-data.xlsx')  # Provide the actual path to the XLS file

    # Step 7: Validate Data
    import_button = driver.find_element(By.XPATH, '//button[contains(text(),"Import")]')
    driver.execute_script("arguments[0].scrollIntoView();", import_button)
    driver.execute_script("arguments[0].click();", import_button)
    
    validate_button = driver.find_element(By.XPATH, '//button[contains(text(),"Validate Data")]')
    driver.execute_script("arguments[0].scrollIntoView();", validate_button)
    driver.execute_script("arguments[0].click();", validate_button)
    
    WebDriverWait(driver, 10).until(EC.alert_is_present())  # Wait until the alert is present
    alert = driver.switch_to.alert
    alert.accept()  # This clicks the OK button on the alert

    # Step 8: Capture Screenshot
    time.sleep(10)  # Add a small delay to ensure the page is fully loaded before taking a screenshot
    # Step 9: Capture Full-Page Screenshot
    scroll_script = "window.scrollBy(0, 5000);"  # Scroll down 500 pixels
    driver.execute_script(scroll_script)
    time.sleep(8) 
    # Step 10: Capture Full-Page Screenshot after scrolling
    total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
    total_width = driver.execute_script("return document.body.parentNode.scrollWidth")

    driver.set_window_size(total_width, total_height)  # Adjust browser window to full page size

    screenshot_path = 'full_page_screenshot_after_scroll.png'
    driver.save_screenshot(screenshot_path)
    
    print(f"Full-page screenshot after scrolling saved at: {screenshot_path}")

finally:
    # Close the browser after completion
    driver.quit()
    