import time
import pyautogui
import tkinter as tk

def screenshot():
    import os
    from tkinter import messagebox
    screenshots_dir = 'C:/Users/HP/Desktop/Udemy Python/ScreenshotApp/screenshots'
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
    name = int(round(time.time() * 1000))
    name = os.path.join(screenshots_dir, '{}.png'.format(name))
    time.sleep(1)  # Shorter delay for better UX
    img = pyautogui.screenshot(name)
    img.show()
    messagebox.showinfo('Screenshot', f'Screenshot saved as:\n{name}')

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text='Take Screenshot', command=screenshot)
button.pack(side=tk.LEFT)
close = tk.Button(frame, text='QUIT', command=quit)
close.pack(side=tk.LEFT)

root.mainloop()

