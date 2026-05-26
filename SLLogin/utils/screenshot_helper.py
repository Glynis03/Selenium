import os
from datetime import datetime

#SCREENSHOT_PATH=r"C:\Users\Avinash Family\Desktop\Selenium-POM\SLLogin\screenshots"

SCREENSHOT_PATH=os.path.join(os.getcwd(),'screenshots')
os.makedirs(SCREENSHOT_PATH, exist_ok=True)

def take_screenshot(driver,name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{name}_{timestamp}.png"
    path = os.path.join(SCREENSHOT_PATH, filename)
    driver.save_screenshot(path)
    print(f"Screenshot saved: {path}")
