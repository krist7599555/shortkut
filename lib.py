import os
import sys
import subprocess
import tkinter as tk
from PIL import Image, ImageTk
from pynput import keyboard

# Tkinter อนุญาตให้มี Tk() แค่ตัวเดียวต่อโปรเซส
TK_ROOT = tk.Tk()

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class AppPresentation:
    def __init__(self, on_quit=None):
        self.on_quit = on_quit
        self.root = TK_ROOT
        self.root.protocol("WM_DELETE_WINDOW", self.quit)
        self.root.geometry("300x300")
        self.root.title("ShortKut")
        
        self._setup_ui()

    def _setup_ui(self):
        img_path = resource_path('assets/icon-1024.png')
        if os.path.exists(img_path):
            original_image = Image.open(img_path)
            resized_image = original_image.resize((300, 300))
            tk_image = ImageTk.PhotoImage(resized_image)
            
            image_label = tk.Label(self.root, image=tk_image)
            image_label.image = tk_image # Keep reference
            image_label.pack()
        else:
            Label(self.root, text="Icon not found").pack()

    def quit(self):
        if self.on_quit:
            self.on_quit()
        self.root.quit()
        self.root.destroy()

    def start(self):
        self.root.mainloop()

class AppKeyboardListener:
    def __init__(self):
        self.key_history = []
        self.max_history = 3
        self.listener = None

    def _open_app(self, app_name):
        print(f"OPEN APP {app_name}")
        subprocess.run(["open", "-a", app_name], capture_output=True, text=True)

    def _check_sequence(self, sequence):
        combo = ' > '.join(self.key_history)
        return combo.endswith(sequence)

    def on_press(self, key):
        try:
            key_str = f"{key}"
            self.key_history.append(key_str)
            
            if len(self.key_history) > self.max_history:
                self.key_history.pop(0)
            
            # Check for shortcuts
            if self._check_sequence("Key.f3 > 'b'") or \
               self._check_sequence("':' > ':' > 'b'") or \
               self._check_sequence("Key.shift_r > Key.shift_r > 'b'") or \
               self._check_sequence("Key.shift_r > Key.shift_r > 'B'"):
                self._open_app("Helium")
                
            elif self._check_sequence("Key.f3 > 't'") or \
                 self._check_sequence("':' > ':' > 't'") or \
                 self._check_sequence("Key.shift_r > Key.shift_r > 't'") or \
                 self._check_sequence("Key.shift_r > Key.shift_r > 'T'"):
                self._open_app("Ghostty")
                
            elif self._check_sequence("Key.f3 > 'c'") or \
                 self._check_sequence("':' > ':' > 'c'") or \
                 self._check_sequence("Key.shift_r > Key.shift_r > 'c'") or \
                 self._check_sequence("Key.shift_r > Key.shift_r > 'C'"):
                self._open_app("Antigravity")

        except Exception as e:
            print(f"Error processing key: {e}")

    def start(self):
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

    def stop(self):
        if self.listener:
            self.listener.stop()

def main():
    print("Starting ShortKut...")
    
    # Initialize Logic
    listener = AppKeyboardListener()
    listener.start()
    
    # Initialize GUI
    # Pass listener stop callback to ensure clean exit
    gui = AppPresentation(on_quit=listener.stop)
    gui.start()

    # Wait for listener thread to finish (optional, as GUI mainloop blocks)
    listener.listener.join()

if __name__ == "__main__":
    main()

