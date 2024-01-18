import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Start Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Open the web application
    driver.get("http://localhost:5000")

    # Verify that the web page title is as expected
    assert "My Web App" in driver.title

    # Interact with the web page elements
    header_text = driver.find_element_by_tag_name("h1").text
    assert "Hello from My Web App!" in header_text

    current_time_text = driver.find_element_by_tag_name("p").text
    print(f"Current time text: {current_time_text}")

    # You can perform more interactions here if needed

finally:
    # Close the browser window
    driver.quit()