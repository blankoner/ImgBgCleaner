import cv2 as cv
import tkinter as tk
from tkinter import filedialog
import numpy as np

"""
def find_dominant_color(image):
    # Przekształć obraz na listę kolorów w formacie BGR
    data = np.reshape(image, (-1, 3))
    # Znajdź najczęściej występujący kolor
    unique_colors, counts = np.unique(data, axis=0, return_counts=True)
    dominant_color = unique_colors[counts.argmax()]
    return dominant_color

def create_color_mask(image, dominant_color, tolerance):
    # Stwórz maskę dla pikseli w zadanym zakresie od dominującego koloru
    #lower_bound = np.maximum(dominant_color - tolerance, 0)
    #upper_bound = np.minimum(dominant_color + tolerance, 255)
    lower_bound = np.array([0, 0, 0])
    upper_bound = np.array([50, 50, 50])
    mask = cv.inRange(image, lower_bound, upper_bound)
    return mask

def apply_mask(image, mask):
    # Zastosuj maskę i zamień pasujące piksele na biały kolor
    image[mask > 0] = (255, 255, 255)
    return image
"""

def find_dominant_color(image):
    pixels = np.float32(image.reshape(-1, 3))
    n_colors = 5
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, palette = cv.kmeans(pixels, n_colors, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)
    _, counts = np.unique(labels, return_counts=True)
    dominant = palette[np.argmax(counts)]
    return dominant

def create_mask_for_dominant_color(image, dominant_color, tolerance=40):
    hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    dominant_color_hsv = cv.cvtColor(np.uint8([[dominant_color]]), cv.COLOR_BGR2HSV)[0][0]
    #lower_bound = np.maximum(dominant_color_hsv - tolerance, 0)
    #upper_bound = np.minimum(dominant_color_hsv + tolerance, 255)
    lower_bound = np.array([0, 0, 0])
    upper_bound = np.array([40, 40, 40])
    mask = cv.inRange(hsv_image, lower_bound, upper_bound)
    return mask

def apply_mask(image, mask):
    # Zastosuj maskę i zamień pasujące piksele na biały kolor
    image[mask > 0] = (255, 255, 255)
    return image

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        print("Sciezka do pliku:", file_path)
        root.destroy()
        img = cv.imread(file_path, cv.IMREAD_COLOR)
        if img is not None:
            dominant_color = find_dominant_color(img)
            mask = create_mask_for_dominant_color(img, dominant_color, tolerance=40)

            modified_image = apply_mask(img.copy(), mask)

            cv.imshow('Original', img)
            cv.imshow('Replaced', modified_image)
            cv.waitKey(0)
            cv.destroyAllWindows()
            #cv.imshow("Podglad obrazu", img)
            #cv.waitKey(0)
            #cv.destroyAllWindows()
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
