import tkinter as tk
import time
from math import cos, sin, radians
import random

class AlienClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Alien Clock")
        
        self.canvas_size = 400
        self.center = self.canvas_size // 2
        self.radius = 120
        
        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size, bg='black')
        self.canvas.pack()
        
        self.symbols = ["⨀", "⩎", "⨂", "⧉", "⩏", "⨋", "⧫", "⨆", "⩜", "⧊", "⨌", "⩚"]
        
        self.draw_clock_face()
        self.update_time()
        
    def draw_clock_face(self):
        self.canvas.create_oval(50, 50, 350, 350, outline='white', width=3)
        
        for i in range(12):
            angle = radians(i * 30 - 90)
            x = self.center + self.radius * cos(angle)
            y = self.center + self.radius * sin(angle)
            
            self.canvas.create_text(x, y, text=self.symbols[i], font=("Arial", 20), fill='cyan')
        
    def update_time(self):
        self.canvas.delete("hands")
        
        t = time.localtime()
        hour = (t.tm_hour % 12) * 30 + (t.tm_min / 60) * 30
        minute = t.tm_min * 6
        second = t.tm_sec * 6
        
        self.draw_hand(hour, self.radius * 0.5, 6, "red")
        self.draw_hand(minute, self.radius * 0.8, 3, "blue")
        self.draw_hand(second, self.radius * 0.9, 1, "lime")
        
        self.root.after(1000, self.update_time)
        
    def draw_hand(self, angle_deg, length, width, color):
        angle = radians(angle_deg - 90)
        x = self.center + length * cos(angle)
        y = self.center + length * sin(angle)
        
        self.canvas.create_line(self.center, self.center, x, y, width=width, fill=color, tags="hands")
        
if __name__ == "__main__":
    root = tk.Tk()
    clock = AlienClock(root)
    root.mainloop()
