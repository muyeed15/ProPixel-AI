# Modules
from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
import threading
import shutil

# Version
version = "1.0.0"

# Remove cache folder
try:
    shutil.rmtree("cache")
except:
    pass

set_appearance_mode("light")
set_default_color_theme("green")

bg_col = "#1d232a"
can_col = "#15191e"
but_col = "#6419e6"

storage = ["", ""]
resolution = [1920, 1080]
screen = [1220, 592]
position = [int((resolution[0] - screen[0]) / 2), int((resolution[1] - screen[1]) / 2)]

screen2 = [483, 235]
position2 = [int((resolution[0] - screen2[0]) / 2), int((resolution[1] - screen2[1]) / 2)]


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
        root.after(0, lambda: preview(storage[1]))
        splash_screen.destroy()

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
    if storage[0] != "":
        from upscaler import upscale_image
        (execute_function_with_splash(lambda: upscale_image(storage[0]), "Up-scaling Image"))


def remove_bg():
    if storage[0] != "":
        from remover import remove_background
        (execute_function_with_splash(lambda: remove_background(storage[0]), "Removing Background"))


def colorize_photo():
    if storage[0] != "":
        from colorizer import colorize_image
        (execute_function_with_splash(lambda: colorize_image(storage[0]), "Colorizing Image"))


def settings_func():
    s_win = Toplevel(root)
    s_win.title("ProPixel AI : Settings")

    s_win.config(bg=bg_col)

    s_win.geometry(f"{screen2[0]}x{screen2[1]}+{position2[0]}+{position2[1]}")

    s_win.resizable(False, False)

    # Left Frame
    left_frame = Frame(s_win, bg=bg_col)
    left_frame.grid(row=0, column=0, padx=8)

    # Widgets in Left Frame
    Label(left_frame, text="Settings", font=("Arial", 24), bg=bg_col, fg="white").pack(pady=10, anchor=NW)

    upscale_label = Label(left_frame, text="Upscale Factor", bg=bg_col, fg="white", font=("Arial", 12))
    upscale_label.pack(pady=5, anchor=NW)

    def up_box_callback(choice):
        print(choice)

    up_box = CTkOptionMenu(left_frame, values=["2x", "4x"], command=up_box_callback, font=("Arial", 13))
    up_box.pack(pady=10, anchor=NW, ipadx=2)
    up_box.set("2x")

    colorizing_label = Label(left_frame, text="CPL (Color)", bg=bg_col, fg="white", font=("Arial", 12))
    colorizing_label.pack(pady=5, anchor=NW)

    colorizing_options = list(map(str, list(range(0, 110, 10))))

    def col_box_callback(choice):
        print(choice)

    col_box = CTkOptionMenu(left_frame, values=colorizing_options, command=col_box_callback, font=("Arial", 13))
    col_box.pack(pady=10, ipadx=2, anchor=NW)
    col_box.set("50")

    # Right Frame
    right_frame = Frame(s_win, bg=can_col)
    right_frame.grid(row=0, column=1)

    # Widgets in Right Frame
    Label(right_frame, text=" ", bg=can_col, fg="#cac9c9", font=("Arial", 2)).pack(padx=5, anchor=NW)
    Label(right_frame, text="Credits", bg=can_col, fg="white", font=("Arial", 24)).pack(padx=5, anchor=NW)
    Label(right_frame, text="ProPixel AI : muyeed15", bg=can_col, fg="#cac9c9", font=("Arial", 10)).pack(padx=5,
                                                                                                            anchor=NW)
    Label(right_frame, text="Real-ESRGAN : Xintao", bg=can_col, fg="#cac9c9", font=("Arial", 10)).pack(padx=5,
                                                                                                        anchor=NW)
    Label(right_frame, text="CustomTkinter : TomSchimansky", bg=can_col, fg="#cac9c9", font=("Arial", 10)).pack(padx=5,
                                                                                                                anchor=NW)
    Label(right_frame, text="Colorful Image Colorization : richzhang", bg=can_col, fg="#cac9c9",
            font=("Arial", 10)).pack(padx=5, anchor=NW)
    Label(right_frame, text="Dichotomous Image Segmentation (DIS) : xuebinqin", bg=can_col, fg="#cac9c9",
            font=("Arial", 10)).pack(padx=5, anchor=NW)
    Label(right_frame, text="\n"*5, bg=can_col, fg="#cac9c9", font=("Arial", 8)).pack(padx=5, anchor=NW)

    Label(s_win, text=" " * 58 + "Version: " + version, bg=bg_col, fg="#cac9c9", font=("Arial", 10)).grid(row=1, column=1)


def preview(output_path):
    def open_folder(path):
        try:
            if sys.platform.startswith('win'):
                os.startfile(path)
            elif sys.platform.startswith('darwin'):
                os.system('open "{}"'.format(path))
            elif sys.platform.startswith('linux'):
                os.system('xdg-open "{}"'.format(path))
        except:
            pass

    def ex_open_folder():
        open_folder(os.path.split(storage[0])[0])

    p_win = Toplevel(root)
    p_win.title("ProPixel AI : Preview")

    p_win.config(bg=bg_col)

    p_win.geometry(f"{screen[0]}x{screen[1]}+{position[0]}+{position[1]}")

    p_win.resizable(False, False)

    preview_path = StringVar()

    Label(p_win, text=" ", font="Arial, 10", foreground=bg_col, background=bg_col).pack(side=RIGHT)
    out_canvas = Canvas(p_win, width=1024, height=576, bd=0, highlightthickness=0, relief='ridge')
    out_canvas.configure(bg=can_col)

    preview_path.set(output_path)
    image = Image.open(output_path)

    image.thumbnail((1024, 576))
    result_image = ImageTk.PhotoImage(image=image)

    x_position = (1024 - image.width) // 2
    y_position = (576 - image.height) // 2

    out_canvas.create_image(x_position, y_position, anchor=NW, image=result_image)
    out_canvas.image = result_image

    out_canvas.pack(side=RIGHT)

    # Buttons
    pre_font = ("Arial", 15)
    pre_button_frame = Frame(p_win, background=bg_col)
    pre_title = Label(pre_button_frame, text="Preview" + " "*6, font="Arial, 24", foreground="white", background=bg_col)
    pre_browse_button = CTkButton(pre_button_frame, text="Open", font=pre_font)

    # Buttons layout
    pre_button_frame.pack()
    Label(pre_button_frame, text="", font="Arial, 2", foreground=bg_col, background=bg_col).pack()
    pre_title.pack()
    Label(pre_button_frame, text="", font="Arial, 5", foreground=bg_col, background=bg_col).pack()
    Label(pre_button_frame, text="Open Folder :" + " " * 15, font="Arial, 12", foreground="white",
            background=bg_col).pack()
    pre_browse_button.pack(padx=10, pady=10, ipadx=20, ipady=15)


root = CTk()
root.title("ProPixel AI")

root.config(bg=bg_col)

root.geometry(f"{screen[0]}x{screen[1]}+{position[0]}+{position[1]}")

root.resizable(False, False)

image_path = StringVar()

Label(root, text=" ", font="Arial, 10", foreground=bg_col, background=bg_col).pack(side=RIGHT)
canvas = Canvas(root, width=1024, height=576, bd=0, highlightthickness=0, relief='ridge')
canvas.configure(bg=can_col)
canvas.pack(side=RIGHT)

display_text()

# Buttons
font = ("Arial", 15)
button_frame = Frame(root, background=bg_col)
title = Label(button_frame, text="ProPixel AI", font="Arial, 24", foreground="white", background=bg_col)
browse_button = CTkButton(button_frame, text="Browse", font=font)
browse_button.bind("<Button-1>", load_image)
upscale_button = CTkButton(button_frame, text="Upscale Image", font=font, fg_color=but_col, command=upscale_photos)
remove_bg_button = CTkButton(button_frame, text="Remove Background", font=font, fg_color=but_col, command=remove_bg)
colorize_button = CTkButton(button_frame, text="Colorize B&W Image", font=font, fg_color=but_col,
                            command=colorize_photo)
settings_button = CTkButton(button_frame, text="Settings", font=font, command=settings_func, fg_color=but_col)
update_button = CTkButton(button_frame, text="Check Updates", font=font, fg_color=but_col)

# Buttons layout
button_frame.pack()
Label(button_frame, text="", font="Arial, 2", foreground=bg_col, background=bg_col).pack()
title.pack()
Label(button_frame, text="", font="Arial, 5", foreground=bg_col, background=bg_col).pack()
Label(button_frame, text="Browse Image :" + " " * 12, font="Arial, 12", foreground="white", background=bg_col).pack()
browse_button.pack(padx=10, pady=10, ipadx=20, ipady=15)
Label(button_frame, text="", font="Arial, 5", foreground=bg_col, background=bg_col).pack()
Label(button_frame, text="AI Enhancers :" + " " * 13, font="Arial, 12", foreground="white", background=bg_col).pack()
upscale_button.pack(padx=10, pady=10, ipadx=20, ipady=15)
remove_bg_button.pack(padx=10, ipadx=20, ipady=15)
colorize_button.pack(padx=10, pady=10, ipadx=20, ipady=15)
Label(button_frame, text="", font="Arial, 5", foreground=bg_col, background=bg_col).pack()
Label(button_frame, text="Tweak Settings :" + " " * 10, font="Arial, 12", foreground="white", background=bg_col).pack()
settings_button.pack(padx=10, pady=5, ipadx=20)
update_button.pack(padx=10, pady=5, ipadx=20)
Label(button_frame, text="Version: " + version, bg=bg_col, fg="#cac9c9", font=("Arial", 10)).pack(pady=15)

# Canvas command
canvas.bind("<Button-1>", load_image)

root.mainloop()
