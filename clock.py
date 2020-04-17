import tkinter as tk
import datetime
from datetime import datetime as dt

HEIGHT = 500
WIDTH = 600

now = dt.now()
currenttime = now.strftime("%H:%M")

currentdate = datetime.datetime.now()
formatedcurrentdate = currentdate.strftime("%D")
timedate = currenttime + "\n" + formatedcurrentdate

root = tk.Tk()

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

background_image = tk.PhotoImage(file="45382444.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#404040", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.125, anchor="n")

label = tk.Label(frame, text=timedate, font=("Courier", 18))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()