from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import qa_logger  # custom module to log results into Excel

# Configure the browser
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

start_time = time.time()

try:
    # Open the login page
    driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(1)

    # Fill in login credentials and click the login button
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()
    time.sleep(2)

    # Capture the success message
    message = driver.find_element(By.ID, "flash").text
    print("Message captured:", message)

    # Check if the success message matches the expected result
    assert "You logged into a secure area!" in message
    print("Login successful. Test passed.")
    status = "Approved"

except Exception as e:
    print(f"Test failed due to error: {e}")
    message = str(e)
    status = "Failed"

finally:
    driver.quit()
    end_time = time.time()
    duration = end_time - start_time

    # Log the result to the Excel report
    qa_logger.log_result(
        test_case_id="TC01",
        actual_result=message,
        expected_result="You logged into a secure area!",
        status=status,
        duration=duration,
        notes="Basic positive login test"
    )

    print("Result logged to QA_Report.xlsx")
