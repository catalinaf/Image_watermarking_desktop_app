from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk
import random

# CONSTANTS

BG_COLOR = '#F7F7F7'
FIELD_COLOR = '#F2E7D5'
TEXT_COLOR = '#393E46'
TEXT2_COLOR = '#6D9886'
MARK_COLOR = '#EDEADE'
FONT = ('Courier', 19, 'normal')

# IMAGE UPLOAD

def UploadAction():
    filename = filedialog.askopenfilename()
    uploaded_image = Image.open(filename)

    if uploaded_image.size[0] > uploaded_image.size[1]:
        reference = uploaded_image.size[0]
    else:
        reference = uploaded_image.size[1]

    denominator = reference / 500

    if reference > 3600:
        new_size = tuple(
            int(item / 10) for item in uploaded_image.size
        )
    elif reference > 500:
        new_size = tuple(
            int(item / denominator) for item in uploaded_image.size
        )
    else:
        new_size = uploaded_image.size

    image = uploaded_image.resize(new_size)
    image.save('image.jpeg')

    image_jpeg = Image.open('image.jpeg')
    show_image = ImageTk.PhotoImage(image_jpeg)

    label.configure(image=show_image)
    label.image = show_image

# INPUT FROM USER

def add_watermark():
    input_value=text_box.get("1.0","end-1c")

    img = Image.open('image.jpeg')
    I1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('Courier', 40)
    I1.text((30, 30), input_value, font=myFont, fill=MARK_COLOR)

    marked_image = ImageTk.PhotoImage(img)
    label.configure(image=marked_image)
    label.image = marked_image
    img.save("marked_image.jpeg")

# IMAGE DOWNLOAD

def download_image():
    folder_selected = filedialog.askdirectory()
    img = Image.open('marked_image.jpeg')
    n = random.randint(1, 9000)
    img.save(f'{folder_selected}/marked_image{n}.jpeg')

# UI SETUP

window = Tk()
window.title('Image Watermarking')
window.minsize(700, 800)
window.config(padx=50, pady=50, bg=BG_COLOR, highlightthickness=0)
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.rowconfigure(2, weight=1)
window.columnconfigure(2, weight=1)

upload_button = Button(
    text='Upload Image', 
    height=2, 
    fg=TEXT_COLOR,
    highlightthickness=0,
    command=UploadAction
)
upload_button.grid(column=0, row=0)

text_box = Text(
    height=2,
    width=16,
    bg=FIELD_COLOR,
    foreground=TEXT_COLOR,
    font=FONT,
    highlightthickness=0
)
text_box.insert('1.0', 'Your watermark')
text_box.bind("<FocusIn>", lambda args: text_box.delete('1.0', 'end'))
text_box.grid(column=1, row=0)

watermark_button = Button(
    text='Add Watermark',
    height=2,
    fg=TEXT_COLOR,
    highlightthickness=0,
    command=add_watermark
)
watermark_button.grid(column=2, row=0)

download_button = Button(
    text='Download Image',
    height=2,
    fg=TEXT_COLOR,
    highlightthickness=0,
    command=download_image
)
download_button.grid(column=3, row=0)

label = Label(
    text='Your image will appear here.',
    font=FONT,
    fg=TEXT2_COLOR,
    bg=BG_COLOR,
    highlightthickness=0
)
label.grid(column=0, row=1, columnspan=4, padx=20, pady=20)

window.mainloop()
