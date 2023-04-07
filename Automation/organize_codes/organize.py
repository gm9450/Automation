from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configure Edge driver
options = EdgeOptions()
options.use_chromium = True
options.add_argument('--headless')  # Run Edge in headless mode
driver = Edge(options=options)

# Navigate to Carbon website
driver.get('https://carbon.now.sh/')
wait = WebDriverWait(driver, 10)

# Set code and options
code = 'print("Hello, world!")'
theme = '3024-night'
font_size = '14px'
line_numbers = True

# Set code
code_input = wait.until(EC.presence_of_element_located((By.XPATH, '//textarea[@class="input-field"]')))
code_input.clear()
code_input.send_keys(code)

# Set theme
theme_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Change theme"]')))
theme_dropdown.click()
theme_option = wait.until(EC.presence_of_element_located((By.XPATH, f'//div[@role="option"][@aria-label="{theme}"]')))
theme_option.click()

# Set font size
font_size_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@aria-label="Change font size"]')))
font_size_input.clear()
font_size_input.send_keys(font_size)

# Set line numbers
if line_numbers:
    line_numbers_toggle = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Toggle line numbers"]')))
    line_numbers_toggle.click()

# Wait for preview to generate
wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="image-container"]')))

# Download image
download_button = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@aria-label="Download"]')))
download_button.click()
png_option = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@role="option" and contains(text(), "PNG")]')))
png_option.click()

# Wait for download to complete
time.sleep(5)

# Close browser
driver.quit()