from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

# Path to your local greet.html file (absolute path)
file_path = '/test.html'

# Update this path to where your msedgedriver.exe is located
edge_driver_path = "C:/msedgedriver.exe"

service = Service(edge_driver_path)
driver = webdriver.Edge(service=service)

try:
    driver.get(file_path)

    # Find input and button elements
    input_element = driver.find_element(By.ID, "nameInput")
    button_element = driver.find_element(By.TAG_NAME, "button")
    message_element = driver.find_element(By.ID, "greetingMessage")

    # Test 1: Empty input → Expect "Kérlek, add meg a neved!"
    input_element.clear()
    button_element.click()
    time.sleep(2)
    assert message_element.text == "Kérlek, add meg a neved!", "Test 1 failed"

    # Test 2: Name with invalid chars → Expect error message
    input_element.clear()
    input_element.send_keys("Anna1")
    button_element.click()
    time.sleep(2)
    assert message_element.text == "A név csak betűket tartalmazhat!", "Test 2 failed"

    # Test 3: Valid name → Expect greeting
    input_element.clear()
    input_element.send_keys("Anna")
    button_element.click()
    time.sleep(2)
    assert message_element.text == "Szia, Anna!", "Test 3 failed"

    # Test 4: Deliberate error → Expect error
    input_element.clear()
    input_element.send_keys("Anna!")
    button_element.click()
    time.sleep(2)
    assert message_element.text == "Error", "Test 4 failed"

    print("All tests passed")

except AssertionError as e:
    print(e)

finally:
    driver.quit()
