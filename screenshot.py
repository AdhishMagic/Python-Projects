import time
import pyautogui

def screenshot():
    name = int(round(time.time()*1000))
    name = 'D:/Projects/Python/Projects/screenshots/{}.png'.format(name)
    time.sleep(5)
    screenshot = pyautogui.screenshot(name)
    screenshot.show()
    print(f'Screenshot saved as {name}')
screenshot()


