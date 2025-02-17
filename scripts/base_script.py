from selenium import webdriver
from selenium.webdriver.common.by import By
from chromedriver_py import binary_path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
)
import os
import time
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

service = webdriver.ChromeService(executable_path=binary_path)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

driver.get("https://www.hannaford.com/")
time.sleep(2)

location_bubble = None

try:
    location_bubble = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "tipso_bubble.default.bottom"))
    )
except TimeoutException:
    logger.info("Location bubble not found within 10 seconds.")

if location_bubble:
    close_bubble = location_bubble.find_element(By.CLASS_NAME, "tipso_close")
    close_bubble.click()
    time.sleep(4)
else:
    logger.info("Skipping bubble closure (not found).")

signin_button = driver.find_element(By.ID, "signInLaunch")
signin_button.click()
time.sleep(2)

email_field = wait.until(EC.presence_of_element_located((By.ID, "email1")))
email_value = os.environ.get("HANNAFORD_EMAIL")
if email_value:
    email_field.send_keys(email_value)
    logger.info(f"Email filled in: {email_value[:4]}*** (partially masked for log)")
else:
    logger.warning(
        "HANNAFORD_EMAIL environment variable not set. Cannot fill email field."
    )

password_field = wait.until(EC.presence_of_element_located((By.ID, "passwordField")))
password_value = os.environ.get("HANNAFORD_PASSWORD")
if password_value:
    password_field.send_keys(password_value)
    logger.info("Password filled in (masked in logs).")
else:
    logger.warning(
        "HANNAFORD_PASSWORD environment variable not set. Cannot fill password field."
    )

signin_submit_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign in')]"))
)
signin_submit_button.click()
logger.info("Clicked 'Sign in' button.")
time.sleep(10)

print("Email from ENV:", os.environ.get("HANNAFORD_EMAIL", "Not Set"))
print("Password from ENV:", os.environ.get("HANNAFORD_PASSWORD", "Not Set"))
driver.quit()
