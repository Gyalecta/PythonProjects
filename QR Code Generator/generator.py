"""
#########################################################################
# QR Code Generator using Python and QRCode API                    #
# Copyright (C) 2022 Avino Domenico                                     #
#                                                                       #
# This program is free software: you can redistribute it and/or modify  #
#########################################################################
"""

import qrcode
import os
import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("900x900")
root.resizable(False, False)

canvas = tk.Canvas(root, width=900, height=900)
canvas.pack()

label = tk.Label(root, text="Enter the link to be encoded:")
label.config(font=("Arial", 20))
canvas.create_window(450, 100, window=label)

entry = tk.Entry(root, width=50)
entry.config(font=("Arial", 20))
canvas.create_window(450, 200, window=entry)

button = tk.Button(root, text="Generate QR Code", command=lambda: generate_qr_code(entry.get()))
button.config(font=("Arial", 20))
canvas.create_window(450, 300, window=button)

def generate_qr_code(link):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image()

    img = img.resize((450, 450), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=img)
    label.image = img
    label.place(x=225, y=350)


button = tk.Button(root, text="Save QR Code", command=lambda: save_qr_code(entry.get()))
button.config(font=("Arial", 20))
canvas.create_window(450, 850, window=button)

def save_qr_code(link):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image()

    img = img.resize((450, 450), Image.ANTIALIAS)
    img.save("qr_code.png")
    os.startfile("qr_code.png")

root.mainloop()