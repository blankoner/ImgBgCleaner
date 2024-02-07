import tkinter as tk
from tkinter import filedialog
from rembg import remove
from PIL import Image
import os

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        root.destroy()
        img = Image.open(file_path)
        if img is not None:
            img_name = file_path.split('/')[-1]
            output_path = "masked/" + img_name

            with open(output_path, 'wb') as f:
                input = open(file_path, 'rb').read()
                subject = remove(input, post_process_mask=True)
                f.write(subject)

        else:
            print("Nie można wczytac obrazu.")
    else:
        print("Nie wybrano pliku.")
        root.destroy()

os.makedirs("masked", exist_ok=True)

root = tk.Tk()
root.title("Wybierz plik")
root.geometry("500x200")

open_button = tk.Button(root, text="Otworz plik", command=open_file)
open_button.pack(expand=True)

root.mainloop()
