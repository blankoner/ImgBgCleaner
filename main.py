import cv2 as cv
import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        print("Sciezka do pliku:", file_path)
        root.destroy()
        img = cv.imread(file_path, cv.IMREAD_COLOR)
        if img is not None:
            cv.imshow("Podglad obrazu", img)
            cv.waitKey(0)
            cv.destroyAllWindows()
        else:
            print("Nie można wczytac obrazu.")
    else:
        print("Nie wybrano pliku.")
        root.destroy()

root = tk.Tk()
root.title("Wybierz plik")
root.geometry("500x200")

open_button = tk.Button(root, text="Otworz plik", command=open_file)
open_button.pack(expand=True)

root.mainloop()




