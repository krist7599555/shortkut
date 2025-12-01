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
        path = resource_path('assets/icon-1024.png')
        if not os.path.exists(path):
            tk.Label(self.root, text="Icon not found").pack()
            return

        # Chain image processing and keep reference in self to prevent GC
        self.photo = ImageTk.PhotoImage(Image.open(path).resize((300, 300)))
        tk.Label(self.root, image=self.photo).pack()

    def quit(self):
        if self.on_quit:
            self.on_quit()
        self.root.quit()
        self.root.destroy()

    def start(self):
        self.root.mainloop()

class AppKeyboardListener:
    def __init__(self):
        self.history = []
        self.limit = 3
        self.listener = None
        self.shortcuts = []

    def add_shortcut(self, triggers, action):
        self.shortcuts.append({'triggers': triggers, 'action': action})

    def on_press(self, key):
        try:
            self.history.append(f"{key}")
            if len(self.history) > self.limit:
                self.history.pop(0)
            
            combo = ' > '.join(self.history)
            
            # Check if any trigger matches the end of the current combo
            for s in self.shortcuts:
                if any(combo.endswith(t) for t in s['triggers']):
                    s['action']()
                    return

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
    
    listener = AppKeyboardListener()
    
    def launch(app):
        print(f"Launching {app}")
        subprocess.run(f"open -a '{app}'", shell=True, capture_output=True, text=True)

    # Register shortcuts
    listener.add_shortcut([
        "Key.f3 > 'b'", "':' > ':' > 'b'",
        "Key.shift_r > Key.shift_r > 'b'", "Key.shift_r > Key.shift_r > 'B'"
    ], lambda: launch("Helium"))
    
    listener.add_shortcut([
        "Key.f3 > 't'", "':' > ':' > 't'",
        "Key.shift_r > Key.shift_r > 't'", "Key.shift_r > Key.shift_r > 'T'"
    ], lambda: launch("Ghostty"))
    
    listener.add_shortcut([
        "Key.f3 > 'c'", "':' > ':' > 'c'",
        "Key.shift_r > Key.shift_r > 'c'", "Key.shift_r > Key.shift_r > 'C'"
    ], lambda: launch("Antigravity"))

    listener.start()
    
    # Start GUI (blocks until quit)
    AppPresentation(on_quit=listener.stop).start()

    # Ensure listener thread finishes
    listener.listener.join()

if __name__ == "__main__":
    main()

