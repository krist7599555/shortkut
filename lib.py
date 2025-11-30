from pynput import keyboard
import subprocess

from tkinter import Tk, StringVar, Label, Button

root = Tk()
root.geometry("200x200")
root.title("ShortKut")

ls = []

def on_press(key, injected):
    global ls
    ls.append(f"{key}")
    while len(ls) > 3: ls.pop(0)
    combo3 = ' > '.join(ls)
    try:
        match combo3:
            case "':' > ':' > 'b'" | "Key.shift_r > Key.shift_r > 'b'":
                subprocess.run(["open", "-a", "Helium"], capture_output=True, text=True)
            case "':' > ':' > 't'" | "Key.shift_r > Key.shift_r > 't'":
                subprocess.run(["open", "-a", "Ghostty"], capture_output=True, text=True)
            case "':' > ':' > 'c'" | "Key.shift_r > Key.shift_r > 'c'":
                subprocess.run(["open", "-a", "Antigravity"], capture_output=True, text=True)
        
        print('alphanumeric key {} pressed; it was {}'.format(
            key.char, 'faked' if injected else 'not faked'))
    except AttributeError:
        print('special key {} pressed'.format(
            key))

def on_release(key, injected):
    print('{} released; it was {}'.format(
        key, 'faked' if injected else 'not faked'))
    # if key == keyboard.Key.esc:
        # Stop listener
        # return False

if __name__ == "__main__":
    root.mainloop()
    with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()
