from tkinter import *
from PIL import Image

root = Tk()
root.title('Image')
root.iconbitmap('D:\Programowanie\WorkspacePython\windows_logo.jpg')

my_img = Image.open("windows_logo.jpg")

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()