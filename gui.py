from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
import threading

set_appearance_mode("light")
set_default_color_theme("green")

bg_col = "#1d232a"
can_col = "#15191e"
but_col = "#6419e6"

storage = ["", ""]
resolution = [1920, 1080]


def show_splash_screen(message):
    global splash_screen
    splash_screen = Toplevel(root)

    splash_width = 300
    splash_height = 60
    x_position = int((resolution[0] - splash_width) / 2)
    y_position = int((resolution[1] - splash_height) / 2)
    splash_screen.geometry(f"{splash_width}x{splash_height}+{x_position}+{y_position}")

    splash_screen.title("Processing")
    splash_screen.configure(bg=bg_col)

    label = Label(splash_screen, text=message, font=("Arial", 10), foreground="#cac9c9", background=bg_col)
    label.place(relx=0.5, rely=0.5, anchor="center")


def execute_function_with_splash(function, message):
    show_splash_screen(message)

    def execute_and_close_splash():
        storage[1] = function()
        splash_screen.destroy()
        preview(storage[1])

    threading.Thread(target=execute_and_close_splash).start()


def load_image(event):
    file_path = filedialog.askopenfilename()

    if file_path:
        image_path.set(file_path)
        image = Image.open(file_path)

        image.thumbnail((1024, 576))
        result_image = ImageTk.PhotoImage(image=image)

        canvas.delete("all")

        x_position = (1024 - image.width) // 2
        y_position = (576 - image.height) // 2

        canvas.create_image(x_position, y_position, anchor=NW, image=result_image)
        canvas.image = result_image

    storage[0] = file_path


def display_text():
    canvas.create_text(512, 288, text="Click here to load image", font=("Arial", 10), fill="#cac9c9")


def upscale_photos():
    pass


def remove_bg():
    pass


def colorize_photo():
    if storage[0] != "":
        from colorizer import colorize_image
        (execute_function_with_splash(lambda: colorize_image(storage[0]), "Colorizing Image"))


def settings_func():
    pass


def preview(output_path):
    p_win = Toplevel(root)
    p_win.title("Output Preview")
    p_win.config(bg=bg_col)

    p_win.geometry(f"{screen_width}x{screen_height}")

    p_win.resizable(False, False)

    img_path = StringVar()
    out_canvas = Canvas(p_win, width=screen_width, height=screen_height, bd=0, highlightthickness=0, relief='ridge')
    out_canvas.configure(bg=can_col)

    img_path.set(output_path)
    image = Image.open(output_path)

    image.thumbnail((screen_width - 196, screen_height - 16))
    result_image = ImageTk.PhotoImage(image=image)

    x_position = (screen_width - image.width) // 2
    y_position = (screen_height - image.height) // 2

    out_canvas.create_image(x_position, y_position, anchor=NW, image=result_image)
    out_canvas.image = result_image
    out_canvas.pack()


root = CTk()
root.title("ProPixel AI")

root.config(bg=bg_col)

screen_width = 1220
screen_height = 592
root.geometry(f"{screen_width}x{screen_height}+"
              f"{int((resolution[0] - screen_width) / 2)}+{int((resolution[1] - screen_height) / 2)}")

root.resizable(False, False)

image_path = StringVar()

Label(root, text=" ", font="Arial, 10", foreground=bg_col, background=bg_col).pack(side=RIGHT)
canvas = Canvas(root, width=1024, height=576, bd=0, highlightthickness=0, relief='ridge')
canvas.configure(bg=can_col)
canvas.pack(side=RIGHT)

display_text()

# buttons
font = ("Arial", 13)
button_frame = Frame(root, background=bg_col)
title = Label(button_frame, text="ProPixel AI", font="Arial, 20", foreground="white", background=bg_col)
browse_button = CTkButton(button_frame, text="Browse", font=font)
browse_button.bind("<Button-1>", load_image)
upscale_button = CTkButton(button_frame, text="Upscale Image", font=font, fg_color=but_col, command=upscale_photos)
remove_bg_button = CTkButton(button_frame, text="Remove Background", font=font, fg_color=but_col, command=remove_bg)
colorize_button = CTkButton(button_frame, text="Colorize B&W Image", font=font, fg_color=but_col,
                            command=colorize_photo)
settings_button = CTkButton(button_frame, text="Settings", font=font)

# buttons layout
button_frame.pack()
Label(button_frame, text="", font="Arial, 1", foreground=bg_col, background=bg_col).pack()
title.pack()
Label(button_frame, text="", font="Arial, 11", foreground=bg_col, background=bg_col).pack()
Label(button_frame, text="Browse Image :" + " " * 12, font="Arial, 10", foreground="white", background=bg_col).pack()
browse_button.pack(padx=10, pady=10, ipadx=20, ipady=15)
Label(button_frame, text="", font="Arial, 10", foreground=bg_col, background=bg_col).pack()
Label(button_frame, text="AI Enhancers :" + " " * 13, font="Arial, 10", foreground="white", background=bg_col).pack()
upscale_button.pack(padx=10, pady=10, ipadx=20, ipady=15)
remove_bg_button.pack(padx=10, ipadx=20, ipady=15)
colorize_button.pack(padx=10, pady=10, ipadx=20, ipady=15)
Label(button_frame, text="", font="Arial, 11", foreground=bg_col, background=bg_col).pack()
Label(button_frame, text="Tweak Settings :" + " " * 10, font="Arial, 10", foreground="white", background=bg_col).pack()
settings_button.pack(padx=10, pady=10, ipadx=20, ipady=15)

# canvas bind
canvas.bind("<Button-1>", load_image)

root.mainloop()
