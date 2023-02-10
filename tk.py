import tkinter as tk
from tkinter import filedialog
from vlkit.medical import read_dicoms
import os.path as osp


window = tk.Tk()
window.title("OsirixSR to dicom structure set")
window.geometry("800x600")

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global data_path
    filename = tk.filedialog.askdirectory()
    data_path.set(filename)
    msg_label['fg'] = 'green'
    msg_label['text'] = data_path.get()
    print(filename)

def convert_button():
    global data_path
    if not osp.isdir(data_path.get()):
        msg_label['fg'] = 'red'
        msg_label['text'] = f"{data_path} is not a path"
    dcm_paths, dicoms = read_dicoms(data_path.get(), return_path=True)
    if len(dcm_paths) == 0:
        msg_label['fg'] = 'red'
        msg_label['text'] = f"{data_path} does not contain any dicom file."



data_path = tk.StringVar()
btn_browse = tk.Button(text="Browse", command=browse_button)
btn_browse.grid(row=0, column=3)

btn_convert = tk.Button(text="Convert", command=convert_button)
btn_convert.grid(row=0, column=4)

msg_label = tk.Label (window, text="")
msg_label.grid(row=2, column=4)


window.mainloop()