import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import pygame

pygame.mixer.init()

tracks = [
    {
        "music": r"C:\Users\DELL\Downloads\Calum-Scott-You-Are-The-Reason.mp3",
        "cover": r"C:\Users\DELL\Downloads\you are the reason image.jpg"
    },
    {
        "music": r"C:\Users\DELL\Downloads\time-to-sleep-240958.mp3",
        "cover": r"C:\Users\DELL\Downloads\time to sleep image.jpg"
    },
    {
        "music": r"C:\Users\DELL\Downloads\Khaid-Ft-Boy-Spyce-Carry-Me-Go-(TrendyBeatz.com).mp3",
        "cover": r"C:\Users\DELL\Downloads\carry me go image.jpg"
    },
    {
        "music": r"C:\Users\DELL\Downloads\DJ-Vyrusky-Ft-KiDi-and-Camidoh-Body-2-Body-(TrendyBeatz.com).mp3",
        "cover": r"C:\Users\DELL\Downloads\Body-2-Body image.webp"
    }
]
current_index = 0
cover_photo = None 

root = tk.Tk()
root.geometry("600x800")
root.resizable(True, True)

def play_track():
    global cover_photo
    track = tracks[current_index]
    pygame.mixer.music.load(track["music"])
    pygame.mixer.music.play(-1)
    img = Image.open(track["cover"]).resize((150, 150), Image.LANCZOS)
    cover_photo = ImageTk.PhotoImage(img)
    cover_label.config(image=cover_photo)

def play_music():
    play_track()

def pause_music():
    pygame.mixer.music.pause()
  
def resume_music():
    pygame.mixer.music.unpause()

def next_track():
    global current_index
    current_index = (current_index + 1) % len(tracks)
    play_track()

def previous_track():
    global current_index
    current_index = (current_index - 1) % len(tracks)
    play_track()

bg_img = Image.open(r"C:\Users\DELL\Downloads\backgroung music wallpaper.jpg").resize((600, 800), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_img)
tk.Label(root, image=bg_photo).place(x=0, y=0, relwidth=1, relheight=1)

logo_size = 110
logo_img = Image.open(r"C:\Users\DELL\Downloads\music logo.jpg").convert("RGBA").resize((logo_size, logo_size), Image.LANCZOS)
mask = Image.new("L", (logo_size, logo_size), 0)
ImageDraw.Draw(mask).ellipse((0, 0, logo_size, logo_size), fill=255)
logo_img.putalpha(mask)
logo_photo = ImageTk.PhotoImage(logo_img)
tk.Label(root, image=logo_photo).place(x=10, y=10)
tk.Label(root, text="MIMI DUAL", font=("Arial", 12, "bold"), bg="#fff", fg="black")\
    .place(x=20, y=logo_size + 20)

music_canvas = tk.Canvas(root, width=500, height=600, bg="white", highlightthickness=0)
music_canvas.place(relx=0.5, rely=0.5, anchor="center")

def round_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    pts = [
        x1 + radius, y1,
        x2 - radius, y1,
        x2, y1,
        x2, y1 + radius,
        x2, y2 - radius,
        x2, y2,
        x2 - radius, y2,
        x1 + radius, y2,
        x1, y2,
        x1, y2 - radius,
        x1, y1 + radius,
        x1, y1
    ]
    return canvas.create_polygon(pts, **kwargs, smooth=True)

round_rectangle(music_canvas, 0, 0, 500, 600, radius=25, fill="#fff", outline="")

tk.Label(music_canvas, text="Music", font=("Arial", 50, "bold"), bg="#fff")\
    .place(x=250, y=50, anchor="center")

cover_label = tk.Label(music_canvas, bg="#fff")
music_canvas.create_window(250, 300, window=cover_label)

control_frame = tk.Frame(music_canvas, bg="#fff")
music_canvas.create_window(250, 550, window=control_frame, anchor="center")
tk.Button(control_frame, text="Previous", command=previous_track).grid(row=0, column=0, padx=10)
tk.Button(control_frame, text="Play", command=play_music).grid(row=0, column=1, padx=10)
tk.Button(control_frame, text="Pause", command=pause_music).grid(row=0, column=2, padx=10)
tk.Button(control_frame, text="Resume", command=resume_music).grid(row=0, column=3, padx=10)
tk.Button(control_frame, text="Next", command=next_track).grid(row=0, column=4, padx=10)

play_track()
root.mainloop()
