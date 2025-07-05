import time
import pyautogui
import tkinter as tk

def screenshot():
    name = int(round(time.time()*1000))
    name = 'D:/Projects/Python/Projects/screenshots/{}.png'.format(name)
    time.sleep(5)
    screenshot = pyautogui.screenshot(name)
    screenshot.show()
    print(f'Screenshot saved as {name}')

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
button = tk.Button(frame, text='Take Screenshot', command=screenshot)
button.pack(side=tk.LEFT)
close = tk.Button(frame, text='QUIT', command = root.quit)
close.pack(side=tk.LEFT)

root.mainloop()


