#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(img):
    return 0.2126 * img[:, :, 0] + 0.7152 * img[:, : , 1] + 0.0722 * img[:, :, 2]


def to_red(img):
    out = img.copy()

    out[:, :, 1] = 0
    out[:, :, 2] = 0
    return out

def to_green(img):
    out = img.copy()
    out[:, :, 0] = 0
    out[:, :, 2] = 0
    return out

def to_blue(img):
    out = img.copy()
    out[:, :, 0] = 0
    out[:, :, 1] = 0
    return out



def main():
    img = plt.imread('src/painting.png')

    gray_img = to_grayscale(img)

    plt.gray()
    plt.imshow(gray_img)
    plt.show()

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1)

    ax1.imshow(to_red(img))
    ax2.imshow(to_green(img))
    ax3.imshow(to_blue(img))

    plt.show()

if __name__ == "__main__":
    main()
