# BE SURE TO USE LIGHT MODE IN GOOGLE FORMS

import pyautogui
import time

def click(image, timeout=10, interval=0.01):
    start = time.time()
    while True:
        if time.time() - start > timeout:
            raise TimeoutError(f"Image {image} not found")
        location = pyautogui.locateOnScreen(image, confidence=0.8)
        if location:
            pyautogui.click(location)
            break
        time.sleep(interval)

while True:
    click('your_answer.png')
    pyautogui.write('NAME HERE')
    click('next.png')
    click('other.png')
    pyautogui.write('Outer Wilds')
    click('submit.png') 
    click("submit_another_response.png")