from pynput import keyboard
import subprocess

from tkinter import Tk, StringVar, Label, Button
from PIL import Image, ImageTk

import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class ShortKutGui:
    def __init__(self):
        root = Tk()
        root.protocol("WM_DELETE_WINDOW", lambda: self.quit())
        root.geometry("300x300")
        root.title("ShortKut")
        img_url = resource_path('./icon-1024.png')
        original_image = Image.open(img_url)
        resized_image = original_image.resize((300, 300)) 
        tk_image = ImageTk.PhotoImage(resized_image)
        image_label = Label(root, image=tk_image)
        # Crucial: Keep a reference to the image object
        # This prevents the image from being garbage collected
        image_label.image = tk_image 
        image_label.pack()
        self.root = root

    def quit(self):
        self.root.quit()
        self.root.destroy() 

    def mainloop(self):
        self.root.mainloop()

ls = []

print("Hi")
print(list(keyboard.Key))
def on_press(key, injected):
    print("OnPress")
    global ls
    ls.append(f"{key}")
    while len(ls) > 3: ls.pop(0)
    combo3 = ' > '.join(ls)
    print(combo3)
    def check(app_name, param):
        if (combo3.endswith(param)):
            print(f"OPEN APP {app_name}")
            subprocess.run(["open", "-a", app_name], capture_output=True, text=True)
            return True

    try:
        print('alphanumeric key {} pressed; it was {}'.format(key.char, 'faked' if injected else 'not faked'))

        x = False \
            or check("Helium", "Key.f3 > 'b'") \
            or check("Helium", "':' > ':' > 'b'") \
            or check("Helium", "Key.shift_r > Key.shift_r > 'b'") \
            or check("Helium", "Key.shift_r > Key.shift_r > 'B'") \
            or check("Ghostty", "Key.f3 > 't'") \
            or check("Ghostty", "':' > ':' > 't'") \
            or check("Ghostty", "Key.shift_r > Key.shift_r > 't'") \
            or check("Ghostty", "Key.shift_r > Key.shift_r > 'T'") \
            or check("Antigravity", "Key.f3 > 'c'") \
            or check("Antigravity", "':' > ':' > 'c'") \
            or check("Antigravity", "Key.shift_r > Key.shift_r > 'c'") \
            or check("Antigravity", "Key.shift_r > Key.shift_r > 'C'") \
            or True
        
        
    except AttributeError:
        print('special key {} pressed'.format(key))

def on_release(key, injected):
    print('{} released; it was {}'.format(key, 'faked' if injected else 'not faked'))
    # if key == keyboard.Key.esc:
        # Stop listener
        # return False


def on_activate_h():
    print('<ctrl>+<alt>+h pressed')

def on_activate_i():
    print('<ctrl>+<alt>+i pressed')

with keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+h i': on_activate_h,
        # '<ctrl>+<alt>+h': on_activate_h,
        '<ctrl>+<alt>+i': on_activate_i}) as h:
    h.join()

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
listener.wait()
gui = ShortKutGui()
gui.mainloop()
listener.join()

