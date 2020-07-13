import time
import pyautogui
import tkinter as tk

def screenshot():
    name=int(round(time.time() * 1000))
    name='C:/Users/HP/Desktop/Python_project/screenshot/screenshot/{}.png'.format(name)
    img = pyautogui.screenshot('test.png')
    img.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text='Capture',
    command=screenshot)

button.pack(side=tk.RIGHT)

root.mainloop()