import numpy as np
import matplotlib.pyplot as plt

def center(a):
    h, w = a.shape[:2]
    return ((h - 1) / 2, (w - 1) / 2)

def radial_distance(a):
    # Derive dimensions from the input array 'a'
    h, w = a.shape[:2]
    cy, cx = center(a)
    y, x = np.ogrid[:h, :w]
    return np.sqrt((x - cx)**2 + (y - cy)**2)

def scale(a, tmin=0.0, tmax=1.0):
    a_min = np.min(a)
    a_max = np.max(a)
    if a_max == a_min:
        return np.zeros_like(a) + tmin
    return (a - a_min) / (a_max - a_min) * (tmax - tmin) + tmin

def radial_mask(a):
    # Pass 'a' to radial_distance
    dist = radial_distance(a)
    mask = scale(dist, 0.0, 1.0) 
    return 1.0 - mask 

def radial_fade(a):
    mask = radial_mask(a)
    if a.ndim == 3:
        return a * mask[:, :, np.newaxis]
    else:
        return a * mask

def main():
    img = plt.imread('src/painting.png')
    
    mask = radial_mask(img)
    faded = radial_fade(img)
    
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
    
    ax1.imshow(img)
    ax1.set_title("Original")
    
    ax2.imshow(mask, cmap='gray')
    ax2.set_title("Mask")
    
    ax3.imshow(faded)
    ax3.set_title("Faded")
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()