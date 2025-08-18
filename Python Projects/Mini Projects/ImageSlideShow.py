import tkinter as tk #This is gui library
import time
from PIL import Image,ImageTk #This PIL is pillow library 
from itertools import cycle

root = tk.Tk()
root.title("Image Slideshow Viewer")

#List of Image Path
image_paths = [
    r"C:\Users\yashm\OneDrive\图片\image1.jpeg",
    r"C:\Users\yashm\OneDrive\图片\image2.jpeg",
    r"C:\Users\yashm\OneDrive\图片\image3.jpeg",
    r"C:\Users\yashm\OneDrive\图片\image4.jpeg",
]

#Resize the images to 1080x1080
image_size = (1080,1080)
images = [Image.open(path). resize(image_size) for path in image_paths]
photo_iamges = [ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_iamges:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)

slideshow = cycle(photo_iamges)

def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()

play_button = tk.Button(root,text = 'Play Slideshow',command=start_slideshow)
play_button.pack()

root.mainloop()