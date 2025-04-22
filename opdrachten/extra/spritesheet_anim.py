import tkinter as tk
from pynput import keyboard
from PIL import Image, ImageTk

run_width = 80
run_height = 64 
run_frames = 8
idle_frames = 7

root = tk.Tk()
root.title("Spritesheet Animation")
root.config(bg = '#add123')
root.wm_attributes('-transparentcolor','#add123')
root.overrideredirect(True)
root.wm_attributes('-topmost', True)

def RGBAImage(Image):
    return Image.convert("RGBA")

def load_frames(sheet_path, frame_width, frame_height, num_frames):
    sheet = Image.open(sheet_path).convert("RGBA")
    frames = []
    for i in range(num_frames):
        left = i * frame_width
        top = 0
        right = left + frame_width
        bottom = top + frame_height
        frame = RGBAImage(sheet.crop((left, top, right, bottom)))
        frames.append(ImageTk.PhotoImage(frame))
    return frames

class SpriteCanvasAnimation(tk.Canvas):
    def __init__(self, master, frames, delay=100, **kwargs):
        width = frames[0].width()
        height = frames[0].height()
        super().__init__(master, width=width, height=height, background=root["bg"], highlightthickness=0, **kwargs)
        
        self.frames = frames
        self.index = 0
        self.delay = delay
        self.sprite = self.create_image(0, 0, anchor='nw', image=self.frames[self.index])
        self.animate()

    def animate(self):
        self.itemconfig(self.sprite, image=self.frames[self.index])
        self.index = (self.index + 1) % len(self.frames)
        self.after(self.delay, self.animate)

def clear_frame():
   for widgets in root.winfo_children():
      widgets.destroy()

def on_key_press(key):
    if hasattr(key, "char") and key.char == "q":
        clear_frame()
        frames = load_frames("C:/Users/hyste.STUDIELP-STEFAN/OneDrive/Documenten/School/python/opdrachten/extra/Mushroom-Idle.png", run_width, run_height, idle_frames)
        anim = SpriteCanvasAnimation(root, frames, delay=150)
        anim.pack()
    
    elif hasattr(key, "char") and key.char == "e":
        clear_frame()
        frames = load_frames("C:/Users/hyste.STUDIELP-STEFAN/OneDrive/Documenten/School/python/opdrachten/extra/Mushroom-Run.png", run_width, run_height, run_frames)
        anim = SpriteCanvasAnimation(root, frames, delay=150)
        anim.pack()


keyboard_listener = keyboard.Listener(
    on_press=on_key_press
)

keyboard_listener.start()

frames = load_frames("C:/Users/hyste.STUDIELP-STEFAN/OneDrive/Documenten/School/python/opdrachten/extra/Mushroom-Run.png", run_width, run_height, run_frames)

anim = SpriteCanvasAnimation(root, frames, delay=150)
anim.pack()

root.mainloop()