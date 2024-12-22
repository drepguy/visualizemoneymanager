from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyperclip
import time
from logger_setup import logger

def try_use_sankeymatic():
    # Step 1: Initialize WebDriver
    options = Options()
    # Do not set headless mode
    driver = webdriver.Chrome(options=options)
    #driver = webdriver.Firefox()  # Or replace with Firefox/Edge WebDriver
    #driver.maximize_window()

    # Step 2: Open the specific website
    url = "https://sankeymatic.com/build/"  # Replace with your desired website
    driver.get(url)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sankey_svg"))
    )

    # Step 3: Wait for the page to load
    time.sleep(1)  # Adjust sleep time as necessary or use WebDriverWait for dynamic elements

    # Step 4: Do not consent cookies
    try:
        #cookie_button = driver.find_element(By.ID, "cookieConsent")
        #cookie_button = driver.find_element(By.XPATH, '//*[@id="cookieConsent"]/div/div/div/button')
        cookie_button = driver.find_element(By.CLASS_NAME,'fc-cta-do-not-consent')
        cookie_button.click()
        logger.info("Cookie consent button clicked.")
    except Exception as e:
        #logger.error(f"Error finding or clicking the cookie consent button: {e}")
        logger.info("No cookie 'do-not-consent' button found. Maybe cookie banner blocked by adblocker.")


    # Step 4: Access clipboard data
    clipboard_data = pyperclip.paste()

    # Step 5: Find the input field and insert data
    try:
        input_field = driver.find_element(By.ID, "flows_in")  # Replace with the appropriate locator
        input_field.clear()  # Clear existing data (if needed)
        input_field.send_keys(clipboard_data)
        logger.info("Data inserted successfully.")
    except Exception as e:
        logger.error(f"Error finding or interacting with input field: {e}")

    time.sleep(1)

    # Step 6: Find and click the button
    try:
        submit_button = driver.find_element(By.ID, "preview_graph")  # Replace with the appropriate locator
        submit_button.click()
        logger.info("Button clicked successfully.")
    except Exception as e:
        logger.error(f"Error finding or clicking the button: {e}")

    # Step 7: Download png
    try:
        download_button = driver.find_element(By.ID, "save_as_png_2x")
        download_button.click()
        logger.info("Download button clicked successfully.")
    except Exception as e:
        logger.error(f"Error finding or clicking the download button: {e}")

    # Step 7: Optional: Wait and close the browser
    time.sleep(10)
    driver.quit()