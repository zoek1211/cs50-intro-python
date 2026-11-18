import csv
import numpy as np
from PIL import Image

def main():
    with open("views.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row["id"]) # loop over id columns


def calculate_brightness(filename):
    with Image.open(filename) as img:
        brightness = np.mean(np.a)