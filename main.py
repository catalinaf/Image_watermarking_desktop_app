from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk
from tkinter import simpledialog

# CONSTANTS

WHITE = '#FFFAD7'
GREEN = '#FCDDB0'
YELLOWISH = '#E97777'

# IMAGE UPLOAD

def UploadAction():
    filename = filedialog.askopenfilename()
    uploaded_image = Image.open(filename)

    new_size = tuple(int(item / 10) for item in uploaded_image.size)
    image = uploaded_image.resize(new_size)
    image.save('image.jpeg')

    image_jpeg = Image.open('image.jpeg')
    show_image = ImageTk.PhotoImage(image_jpeg)

    label.configure(image=show_image)
    label.image = show_image

# INPUT FROM USER

def retrieve_input():
    inputValue=text_box.get("1.0","end-1c")

    img = Image.open('image.jpeg')
    I1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('Courier', 40)
    I1.text((50, 50), inputValue, font=myFont, fill = '#FF9F9F')

    marked_image = ImageTk.PhotoImage(img)
    label.configure(image=marked_image)
    label.image = marked_image
    img.save("marked_image.jpg")

# IMAGE DOWNLOAD

def download_image():
    folder_selected = filedialog.askdirectory()
    img = Image.open('marked_image.jpg')
    img.save(f'{folder_selected}/marked_image.jpg')

# UI SETUP

window = Tk()
window.title('Image Watermarking')
window.minsize(700, 800)
window.config(padx=50, pady=50, bg=WHITE, highlightthickness=0)
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.rowconfigure(2, weight=1)
window.columnconfigure(2, weight=1)

upload_button = Button(
    text='Upload Image', 
    height=2, 
    highlightthickness=0,
    fg=YELLOWISH,
    command=UploadAction
)
upload_button.grid(column=0, row=0)

text_box = Text(
    height=2,
    width=16,
    highlightthickness=0,
    bg=GREEN,
    foreground=YELLOWISH,
    font=('Courier', 19, 'normal')
)
text_box.insert('1.0', 'Your watermark')
text_box.bind("<FocusIn>", lambda args: text_box.delete('1.0', 'end'))
text_box.grid(column=1, row=0)

watermark_button = Button(
    text='Add Watermark',
    height=2,
    highlightthickness=0,
    fg=YELLOWISH,
    command=retrieve_input
)
watermark_button.grid(column=2, row=0)

download_button = Button(
    text='Download Image',
    height=2,
    fg=YELLOWISH,
    highlightthickness=0,
    command=download_image
)
download_button.grid(column=3, row=0)

label = Label(
    text='some text'
)
label.grid(column=0, row=1, columnspan=4, padx=20, pady=20)

window.mainloop()
