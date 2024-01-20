# initializing
try:
    from gui import interface
    interface()
except:
    from tkinter import messagebox
    error_title = "ProPixel AI : Resource Error"
    error_message = (
        "An error occurred while accessing resource files. "
        "The resource files may be corrupted or missing. "
        "Please verify the integrity of the resource files and ensure "
        "that they are available in the correct location."
    )
    messagebox.showwarning(error_title, error_message)
