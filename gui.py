def interface():
    # Modules
    from tkinter import Toplevel, Label, filedialog, StringVar, Canvas, Frame, NW, RIGHT, DISABLED
    from customtkinter import CTkButton, CTkFrame, CTkOptionMenu, set_appearance_mode, set_default_color_theme
    from PIL import Image, ImageTk
    import threading
    import shutil
    import requests
    import webbrowser
    from hdpitkinter import HdpiTk
    import ctypes
    import os


    # Version
    version = "1.0.0"

    # Remove cache folder
    try:
        shutil.rmtree("cache")
    except:
        pass

    # Update
    def update():
        try:
            return requests.get("https://raw.githubusercontent.com/muyeed15/ProPixel-AI/main/version.txt").text
        except:
            return "null"


    up_version = update()

    if (up_version == version) or (up_version == "null"):
        ver_tex = fr"v{version}"
        ver_col = "#cac9c9"
    else:
        ver_tex = " Updates are available ! "
        ver_col = "#ebbd34"

    # Config folder
    if os.path.exists("config") == False:
        os.makedirs("config")

    # Config files
    # -- Upscale --
    try:
        up_data_c = int(open(r"config/upscale.ini", "r").read())
        if up_data_c not in [2, 4]:
            open(r"config/upscale.ini", "w").write(str(4))
    except:
        open(r"config/upscale.ini", "w").write(str(4))

    # -- Colorize --
    try:
        col_data_c = int(open(r"config/colorize.ini", "r").read())
        if col_data_c not in list(range(0, 110, 10)):
            open(r"config/colorize.ini", "w").write(str(50))
    except:
        open(r"config/colorize.ini", "w").write(str(50))

    # -- Edge --
    try:
        edge_data_c = int(open(r"config/edge.ini", "r").read())
        if edge_data_c not in [1, 2, 3]:
            open(r"config/edge.ini", "w").write(str(2))
    except:
        open(r"config/edge.ini", "w").write(str(2))

    # Supported files
    s_files = [".jpg", ".jpeg", ".png", ".bmp", ".webp"]

    # Theme
    set_appearance_mode("light")
    set_default_color_theme("green")

    bg_col = "#1d232a"
    can_col = "#15191e"
    but_col = "#6419e6"

    # Data
    storage = ["", ""]

    # GUI (Head)
    root = HdpiTk()

    root.iconbitmap(r"resource/ProPixel-AI.ico")

    # Resolution
    resolution = [root.winfo_screenwidth(), root.winfo_screenheight()]

    try:
        scaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100
    except:
        scaleFactor = 1.0

    if scaleFactor == 1.25:
        posx = 175
        posy = 95
        
        screen = [1220, 620]
        position = [int((resolution[0] - screen[0]) / 2) + posx, int((resolution[1] - screen[1]) / 2) + posy]

        screen2 = [540, 335]
        position2 = [int((resolution[0] - screen2[0]) / 2) + posx, int((resolution[1] - screen2[1]) / 2) + posy]

        screen3 = [300, 130]
        position3 = [int((resolution[0] - screen3[0]) / 2) + posx, int((resolution[1] - screen3[1]) / 2) + posy]

        screen4 = [1022, 600]

        screen5 = [300, 60]
        position5 = [int((resolution[0] - screen5[0]) / 2) + posx, int((resolution[1] - screen5[1]) / 2) + posy]
        
        screen6 = [512, 300]
        
        set_pad = 68

    elif scaleFactor == 1.5:
        posx = 300
        posy = 170

        screen = [1220, 675]
        position = [int((resolution[0] - screen[0]) / 2) + posx, int((resolution[1] - screen[1]) / 2) + posy]

        screen2 = [580, 370]
        position2 = [int((resolution[0] - screen2[0]) / 2) + posx, int((resolution[1] - screen2[1]) / 2) + posy]

        screen3 = [300, 130]
        position3 = [int((resolution[0] - screen3[0]) / 2) + posx, int((resolution[1] - screen3[1]) / 2) + posy]

        screen4 = [1022, 655]

        screen5 = [300, 60]
        position5 = [int((resolution[0] - screen5[0]) / 2) + posx, int((resolution[1] - screen5[1]) / 2) + posy]
        
        screen6 = [512, 322]
        
        set_pad = 83

    elif scaleFactor == 1.75:
        posx = 380
        posy = 185

        screen = [1232, 750]
        position = [int((resolution[0] - screen[0]) / 2) + posx, int((resolution[1] - screen[1]) / 2) + posy]

        screen2 = [620, 410]
        position2 = [int((resolution[0] - screen2[0]) / 2) + posx, int((resolution[1] - screen2[1]) / 2) + posy]

        screen3 = [300, 130]
        position3 = [int((resolution[0] - screen3[0]) / 2) + posx, int((resolution[1] - screen3[1]) / 2) + posy]

        screen4 = [1022, 730]

        screen5 = [300, 60]
        position5 = [int((resolution[0] - screen5[0]) / 2) + posx, int((resolution[1] - screen5[1]) / 2) + posy]
        
        screen6 = [502, 360]
        
        set_pad = 100

    else:
        posx = 0
        posy = 0
        
        screen = [1220, 550]
        position = [int((resolution[0] - screen[0]) / 2) + posx, int((resolution[1] - screen[1]) / 2) + posy]

        screen2 = [501, 303]
        position2 = [int((resolution[0] - screen2[0]) / 2) + posx, int((resolution[1] - screen2[1]) / 2) + posy]

        screen3 = [300, 130]
        position3 = [int((resolution[0] - screen3[0]) / 2) + posx, int((resolution[1] - screen3[1]) / 2) + posy]

        screen4 = [1022, 530]

        screen5 = [300, 60]
        position5 = [int((resolution[0] - screen5[0]) / 2) + posx, int((resolution[1] - screen5[1]) / 2) + posy]
        
        screen6 = [512, 265]
        
        set_pad = 53


    # Splash screen
    def show_splash_screen(message):
        global splash_screen
        
        splash_screen = Toplevel(root)
        splash_screen.iconbitmap(r"resource/ProPixel-AI.ico")
        splash_screen.geometry(f"{screen5[0]}x{screen5[1]}+{position5[0]}+{position5[1]}")
        
        splash_screen.title("Processing")
        splash_screen.configure(bg=bg_col)

        label = Label(splash_screen, text=message, font=("Arial", 10), foreground="#cac9c9", background=bg_col)
        label.place(relx=0.5, rely=0.5, anchor="center")


    def execute_function_with_splash(function, message):
        show_splash_screen(message)

        def execute_and_close_splash():
            global splash_screen
            
            storage[1] = function()
            root.after(0, lambda: preview(storage[1]))
            splash_screen.destroy()

        threading.Thread(target=execute_and_close_splash).start()


    # Canvas elements
    def load_image(event):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", tuple(["*" + item for item in s_files]))]
        )

        if file_path:
            image_path.set(file_path)
            image = Image.open(file_path)

            image.thumbnail((screen4[0], screen4[1]))
            result_image = ImageTk.PhotoImage(image=image)

            canvas.delete("all")

            x_position = (screen4[0] - image.width) // 2
            y_position = (screen4[1] - image.height) // 2
            canvas.create_image(x_position, y_position, anchor=NW, image=result_image)
            canvas.image = result_image
        
        if (
            file_path != ""
            and isinstance(file_path, str)
            and file_path.endswith(tuple(s_files))
        ):
            storage[0] = file_path


    def display_text():
        canvas.create_text(screen6[0], screen6[1], text="Click here to load image", font=("Arial", 10), fill="#cac9c9")


    # Operations
    def upscale_photos():
        if (
            storage[0] != ""
            and isinstance(storage[0], str)
            and storage[0].endswith(tuple(s_files))
        ):
            from upscaler import upscale_image
            execute_function_with_splash(lambda: upscale_image(storage[0]), "Upscaling Image")


    def remove_bg():
        if (
            storage[0] != ""
            and isinstance(storage[0], str)
            and storage[0].endswith(tuple(s_files))
        ):
            from remover import remove_background
            (execute_function_with_splash(lambda: remove_background(storage[0]), "Removing Background"))


    def colorize_photo():
        if (
            storage[0] != ""
            and isinstance(storage[0], str)
            and storage[0].endswith(tuple(s_files))
        ):
            from colorizer import colorize_image
            (execute_function_with_splash(lambda: colorize_image(storage[0]), "Colorizing Image"))


    # Settings
    def settings_func():
        s_win = Toplevel(root)
        
        s_win.iconbitmap(r"resource/ProPixel-AI.ico")
        
        s_win.title("ProPixel AI : Settings")
        s_win.config(bg=bg_col)

        s_win.geometry(f"{screen2[0]}x{screen2[1]}+{position2[0]}+{position2[1]}")
        s_win.resizable(False, False)

        # Left Frame
        left_frame = CTkFrame(s_win, fg_color=bg_col)
        left_frame.grid(row=0, column=0, padx=8)

        # Widgets in Left Frame
        Label(left_frame, text="Settings", font=("Arial", 24), bg=bg_col, fg="white").pack(pady=10, anchor=NW)
        upscale_label = Label(left_frame, text="Upscale Factor", bg=bg_col, fg="white", font=("Arial", 10))
        upscale_label.pack(pady=5, anchor=NW)

        def up_box_callback(choice):
            open(fr"config/upscale.ini", "w").write(str(choice).replace("x", ""))

        up_box = CTkOptionMenu(left_frame, values=["2x", "4x"], command=up_box_callback, font=("Arial", 12))
        up_box.pack(pady=10, anchor=NW, ipadx=2)

        try:
            up_data = int(open(r"config/upscale.ini", "r").read())
            if up_data in [2, 4]:
                up_box.set(f"{up_data}x")
            else:
                open(r"config/upscale.ini", "w").write(str(4))
                up_box.set("4x")
        except:
            open(r"config/upscale.ini", "w").write(str(4))
            up_box.set("4x")

        # Edge Factor
        edge_label = Label(left_frame, text="Edge Factor", bg=bg_col, fg="white", font=("Arial", 10))
        edge_label.pack(pady=5, anchor=NW)

        def edge_box_callback(choice):
            edge_mapping = {"Sharp": 1, "Smooth": 2, "Smoothest": 3}
            factor = edge_mapping.get(choice, 2)
            open(fr"config/edge.ini", "w").write(str(factor))

        edge_options = ["Sharp", "Smooth", "Smoothest"]
        edge_box = CTkOptionMenu(left_frame, values=edge_options, command=edge_box_callback, font=("Arial", 12))
        edge_box.pack(pady=10, ipadx=2, anchor=NW)

        try:
            edge_data = int(open(r"config/edge.ini", "r").read())
            if edge_data in [1, 2, 3]:
                factor_mapping = {1: "Sharp", 2: "Smooth", 3: "Smoothest"}
                selected_factor = factor_mapping.get(edge_data, "Smooth")
                edge_box.set(selected_factor)
            else:
                open(r"config/edge.ini", "w").write(str(2))
                edge_box.set("Smooth")
        except:
            open(r"config/edge.ini", "w").write(str(2))
            edge_box.set("Smooth")

        # Colorize Factor
        colorizing_label = Label(left_frame, text="Colorize Factor", bg=bg_col, fg="white", font=("Arial", 10))
        colorizing_label.pack(pady=5, anchor=NW)

        def col_box_callback(choice):
            open(fr"config/colorize.ini", "w").write(str(choice))

        colorizing_options = list(map(str, list(range(0, 110, 10))))
        col_box = CTkOptionMenu(left_frame, values=colorizing_options, command=col_box_callback, font=("Arial", 12))
        col_box.pack(pady=10, ipadx=2, anchor=NW)

        try:
            col_data = int(open(r"config/colorize.ini", "r").read())
            if col_data in list(range(0, 110, 10)):
                col_box.set(f"{col_data}")
            else:
                open(r"config/colorize.ini", "w").write(str(50))
                col_box.set("50")
        except:
            open(r"config/colorize.ini", "w").write(str(50))
            col_box.set("50")


        # Right Frame
        right_frame = CTkFrame(s_win, fg_color=can_col)
        right_frame.grid(row=0, column=1, ipady=set_pad, pady=10)

        # Widgets in Right Frame
        Label(right_frame, text="Credits", bg=can_col, fg="white", font=("Arial", 24)).pack(padx=5, pady=2, anchor=NW)
        Label(right_frame, text="ProPixel AI : muyeed15", bg=can_col, fg="#cac9c9", font=("Arial", 10)).pack(padx=5, anchor=NW)
        Label(right_frame, text="Real-ESRGAN : Xintao", bg=can_col, fg="#cac9c9", font=("Arial", 10)).pack(padx=5, anchor=NW)
        Label(right_frame, text="CustomTkinter : TomSchimansky", bg=can_col, fg="#cac9c9", font=("Arial", 10)).pack(padx=5, anchor=NW)
        Label(right_frame, text="Colorful Image Colorization : richzhang", bg=can_col, fg="#cac9c9", font=("Arial", 10)).pack(padx=5, anchor=NW)
        Label(right_frame, text="Dichotomous Image Segmentation (DIS) : xuebinqin", bg=can_col, fg="#cac9c9", font=("Arial", 10)).pack(padx=5, anchor=NW)
        Label(right_frame, text="PyTorch implementation of a Real-ESRGAN : ai-forever", bg=can_col, fg="#cac9c9", font=("Arial", 10)).pack(padx=5, anchor=NW)


    # Preview output
    def preview(output_path):
        # Open output
        def open_folder(path):
            os.startfile(path)


        def ex_open_folder():
            open_folder(os.path.split(storage[0])[0])


        # Preview
        p_win = Toplevel(root)
        p_win.iconbitmap(r"resource/ProPixel-AI.ico")
        p_win.title("ProPixel AI : Preview")
        p_win.config(bg=bg_col)
        p_win.geometry(f"{screen[0]}x{screen[1]}+{position[0]}+{position[1]}")
        p_win.resizable(False, False)

        preview_path = StringVar()

        Label(p_win, text=" ", font="Arial, 10", foreground=bg_col, background=bg_col).pack(side=RIGHT)
        out_canvas = Canvas(p_win, width=screen4[0], height=screen4[1], bd=0, highlightthickness=0, relief='ridge')
        out_canvas.configure(bg=can_col)

        preview_path.set(output_path)
        image = Image.open(output_path)
        image.thumbnail((screen4[0], screen4[1]))
        result_image = ImageTk.PhotoImage(image=image)

        x_position = (screen4[0] - image.width) // 2
        y_position = (screen4[1] - image.height) // 2
        out_canvas.create_image(x_position, y_position, anchor=NW, image=result_image)
        out_canvas.image = result_image
        out_canvas.pack(side=RIGHT)

        # Buttons
        pre_font = ("Arial", 12)
        pre_button_frame = Frame(p_win, background=bg_col)
        pre_title = Label(pre_button_frame, text="Preview" + " "*5, font="Arial, 24", foreground="white", background=bg_col)
        pre_browse_button = CTkButton(pre_button_frame, text="Open", font=pre_font, command=ex_open_folder)

        # Buttons layout
        pre_button_frame.pack()
        Label(pre_button_frame, text="", font="Arial, 2", foreground=bg_col, background=bg_col).pack()
        pre_title.pack()
        Label(pre_button_frame, text="", font="Arial, 5", foreground=bg_col, background=bg_col).pack()
        Label(pre_button_frame, text="Open Folder :" + " " * 19, font="Arial, 10", foreground="white", background=bg_col).pack()
        pre_browse_button.pack(padx=10, pady=10, ipadx=20, ipady=15)


    # Update
    def up_gui():
        u_win = Toplevel(root)
        u_win.iconbitmap(r"resource/ProPixel-AI.ico")
        u_win.title("ProPixel AI : Updates")
        u_win.config(bg=bg_col)

        def web_link():
            webbrowser.open_new_tab("https://sourceforge.net/")
            root.destroy()
        
        up_b = CTkButton(u_win, text="Update", font=("Arial", 12), command=web_link)
        
        up_v = update()
        
        if (up_v == version):
            ver_d = "You are up to date !"
            ver_c = "white"
            up_b.configure(state=DISABLED, fg_color=bg_col, text=f"v{version}")
            
        elif (up_v == "null"):
            ver_d = "No Internet !"
            ver_c = "white"
            up_b.configure(state=DISABLED, fg_color=bg_col, text=f"v{version}")
            
        else:
            ver_d = "Updates are available !"
            ver_c = "#ebbd34"
            
        Label(u_win, text=ver_d, background=bg_col, foreground=ver_c, font=("Arial", 18)).pack(pady=22)

        up_b.pack()

        u_win.geometry(f"{screen3[0]}x{screen3[1]}+{position3[0]}+{position3[1]}")
        u_win.resizable(False, False)


    # GUI (Tail)
    root.title("ProPixel AI")
    root.config(bg=bg_col)

    root.geometry(f"{screen[0]}x{screen[1]}+{position[0]}+{position[1]}")
    root.resizable(False, False)

    image_path = StringVar()
    Label(root, text=" ", font="Arial, 10", foreground=bg_col, background=bg_col).pack(side=RIGHT)
    canvas = Canvas(root, width=screen4[0], height=screen4[1], bd=0, highlightthickness=0, relief='ridge')
    canvas.configure(bg=can_col)
    canvas.pack(side=RIGHT)
    display_text()

    # Buttons
    font = ("Arial", 12)
    button_frame = Frame(root, background=bg_col)
    browse_button = CTkButton(button_frame, text="Browse", font=font)
    browse_button.bind("<Button-1>", load_image)
    upscale_button = CTkButton(button_frame, text="Upscale", font=font, fg_color=but_col, command=upscale_photos)
    remove_bg_button = CTkButton(button_frame, text="RemBG", font=font, fg_color=but_col, command=remove_bg)
    colorize_button = CTkButton(button_frame, text="Colorize", font=font, fg_color=but_col, command=colorize_photo)
    settings_button = CTkButton(button_frame, text="Settings", font=font, command=settings_func, fg_color=but_col)
    update_button = CTkButton(button_frame, text="Check Updates", font=font, fg_color=but_col, command=up_gui)

    # Buttons layout
    button_frame.pack()
    Label(button_frame, text="", font="Arial, 2", foreground=bg_col, background=bg_col).pack()

    img_path = r"resource/ProPixel-AI.png"
    org_image = Image.open(img_path).resize((170, 19))
    tk_image = ImageTk.PhotoImage(org_image)

    Label(button_frame, image=tk_image, foreground=bg_col, background=bg_col).pack()
    Label(button_frame, text="", font="Arial, 5", foreground=bg_col, background=bg_col).pack()
    Label(button_frame, text="Browse Image :" + " " * 18, font="Arial, 10", foreground="white", background=bg_col).pack()
    browse_button.pack(padx=10, pady=10, ipadx=20, ipady=15)
    Label(button_frame, text="", font="Arial, 5", foreground=bg_col, background=bg_col).pack()
    Label(button_frame, text="AI Enhancers :" + " " * 18, font="Arial, 10", foreground="white", background=bg_col).pack()
    upscale_button.pack(padx=10, pady=10, ipadx=20, ipady=15)
    remove_bg_button.pack(padx=10, ipadx=20, ipady=15)
    colorize_button.pack(padx=10, pady=10, ipadx=20, ipady=15)
    Label(button_frame, text="", font="Arial, 5", foreground=bg_col, background=bg_col).pack()
    Label(button_frame, text="Tweak Settings :" + " " * 15, font="Arial, 10", foreground="white", background=bg_col).pack()
    settings_button.pack(padx=10, pady=5, ipadx=20)
    update_button.pack(padx=10, pady=5, ipadx=20)
    Label(button_frame, text=ver_tex, bg=bg_col, fg=ver_col, font=("Arial", 9)).pack(pady=17)

    # Canvas command
    canvas.bind("<Button-1>", load_image)

    root.mainloop()
