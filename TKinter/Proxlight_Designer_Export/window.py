from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("862x519")
window.configure(bg = "#d4a373")
canvas = Canvas(
    window,
    bg = "#d4a373",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    646.5, 259.5,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    652.0, 403.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#f1f5ff",
    highlightthickness = 0)

entry0.place(
    x = 479.0, y = 335,
    width = 346.0,
    height = 135)

canvas.create_text(
    657.5, 398.0,
    text = "Phishing is a type of social engineering attack often used to steal \nuser data, including login credentials and credit card numbers. \nIt occurs when an attacker, masquerading as a trusted entity, \ndupes a victim into opening an email, instant message, or \ntext message.",
    fill = "#000000",
    font = ("SmoochSans-Bold", int(17.0)))

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 26, y = 195,
    width = 137,
    height = 46)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 230, y = 195,
    width = 141,
    height = 46)

canvas.create_text(
    199.0, 63.0,
    text = "Phishing Website Detection",
    fill = "#fcfcfc",
    font = ("Roboto-Bold", int(24.0)))

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    198.5, 76.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#fcfcfc",
    highlightthickness = 0)

entry1.place(
    x = 45, y = 74,
    width = 307,
    height = 3)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    198.5, 146.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#f1f5ff",
    highlightthickness = 0)

entry2.place(
    x = 38.0, y = 116,
    width = 321.0,
    height = 59)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 36, y = 274,
    width = 203,
    height = 225)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    647.0, 148.0,
    image=background_img)

canvas.create_text(
    194.0, 101.5,
    text = "Batch C8",
    fill = "#fcfcfc",
    font = ("Tajawal-Regular", int(24.0)))

canvas.create_text(
    563.5, 36.5,
    text = "Your Selections and Output",
    fill = "#000000",
    font = ("SmoochSans-Bold", int(21.0)))

window.resizable(False, False)
window.mainloop()
