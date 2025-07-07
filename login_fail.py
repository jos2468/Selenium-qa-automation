from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import qa_logger

# Configure browser
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

start_time = time.time()

try:
    # Open login page
    driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(1)

    # Enter invalid username
    driver.find_element(By.ID, "username").send_keys("Jos123")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()
    time.sleep(2)

    # Capture error message
    message = driver.find_element(By.ID, "flash").text
    print("Message captured:", message)

    # Check if it matches the expected failure text
    assert "Your username is invalid!" in message
    print("Negative test passed.")
    status = "Approved"

except Exception as e:
    print(f"Test failed due to error: {e}")
    message = str(e)
    status = "Failed"

finally:
    driver.quit()
    end_time = time.time()
    duration = end_time - start_time

    qa_logger.log_result(
        test_case_id="TC02",
        actual_result=message,
        expected_result="Your username is invalid!",
        status=status,
        duration=duration,
        notes="Negative login test with invalid username"
    )

    print("Result logged to QA_Report.xlsx")
