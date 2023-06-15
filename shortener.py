import tkinter as tk
from tkinter import ttk
import pyshorteners
import webbrowser
import tkinter.messagebox as messagebox
import tkinter.scrolledtext as scrolledtext
import clipboard

BACKGROUND_COLOR = "#000000"
FOREGROUND_COLOR = "#00FF00"
BUTTON_COLOR = "#008000"
ENTRY_COLOR = "#FFFFFF"

def shorten_url():
    long_url = entry.get()
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(long_url)
    output_label.configure(text="Short URL:", foreground=FOREGROUND_COLOR)
    hyperlink_label.configure(text=short_url, foreground=FOREGROUND_COLOR, cursor="hand2")
    hyperlink_label.bind("<Button-1>", lambda e: webbrowser.open(short_url))
    copy_button.configure(state="normal", command=lambda: copy_to_clipboard(short_url))

def copy_to_clipboard(text):
    clipboard.copy(text)
    messagebox.showinfo("gURL Shortener", "Short URL copied to clipboard.")

# Create the main window
window = tk.Tk()
window.title("gURL Shortener")
window.configure(bg=BACKGROUND_COLOR)
window.geometry("400x200")
window.resizable(False, False)

# Style the title bar
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", foreground=FOREGROUND_COLOR, background=BACKGROUND_COLOR)
style.configure("TFrame", background=BACKGROUND_COLOR)
style.configure("TButton", foreground=FOREGROUND_COLOR, background=BUTTON_COLOR)
style.configure("TEntry", fieldbackground=ENTRY_COLOR)

# Create the input label and entry field
input_label = ttk.Label(window, text="Enter URL:")
input_label.pack()
entry = ttk.Entry(window)
entry.pack()

# Create the "Shorten" button
button = ttk.Button(window, text="Shorten", command=shorten_url)
button.pack()

# Create the output label and hyperlink label
output_label = ttk.Label(window, text="Short URL:")
output_label.pack()
hyperlink_label = ttk.Label(window, text="", cursor="hand2")
hyperlink_label.pack()

# Create the copy button
copy_button = ttk.Button(window, text="Copy", state="disabled")
copy_button.pack()

# Set the window size
window.geometry("300x150")

# Start the main event loop
window.mainloop()