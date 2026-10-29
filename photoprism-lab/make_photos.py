#!/usr/bin/env python3
"""Generate the lab's synthetic photos: drawn shapes and landscapes,
with crafted EXIF (dates, GPS, camera) written by piexif.
No real people, no real photos: every pixel is drawn by this script."""
import math, os
from PIL import Image, ImageDraw
import piexif

OUT = os.path.expanduser("~/workspace/photoprism-lab-work/originals")
os.makedirs(OUT, exist_ok=True)
W, H = 1200, 900


def dms(deg):
    """Decimal degrees -> ((deg,1),(min,1),(sec*100,100)) rationals."""
    d = int(abs(deg))
    m = int((abs(deg) - d) * 60)
    s = round(((abs(deg) - d) * 60 - m) * 60 * 100)
    return ((d, 1), (m, 1), (s, 100))


def save(img, name, dt=None, gps=None, desc=None, software="PhotoPrism lab fixture maker 1.0"):
    path = os.path.join(OUT, name)
    exif = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "Interop": {}, "thumbnail": None}
    exif["0th"][piexif.ImageIFD.Make] = "LabCamera"
    exif["0th"][piexif.ImageIFD.Model] = "LabCamera LC-1"
    exif["0th"][piexif.ImageIFD.Software] = software
    if desc:
        exif["0th"][piexif.ImageIFD.ImageDescription] = desc
    if dt:
        exif["0th"][piexif.ImageIFD.DateTime] = dt
        exif["Exif"][piexif.ExifIFD.DateTimeOriginal] = dt
        exif["Exif"][piexif.ExifIFD.DateTimeDigitized] = dt
    exif["Exif"][piexif.ExifIFD.PixelXDimension] = W
    exif["Exif"][piexif.ExifIFD.PixelYDimension] = H
    if gps:
        lat, lon = gps
        exif["GPS"][piexif.GPSIFD.GPSLatitudeRef] = "N" if lat >= 0 else "S"
        exif["GPS"][piexif.GPSIFD.GPSLatitude] = dms(lat)
        exif["GPS"][piexif.GPSIFD.GPSLongitudeRef] = "E" if lon >= 0 else "W"
        exif["GPS"][piexif.GPSIFD.GPSLongitude] = dms(lon)
        exif["GPS"][piexif.GPSIFD.GPSVersionID] = (2, 3, 0, 0)
    img.save(path, "JPEG", quality=88, exif=piexif.dump(exif))
    print("wrote", name)


def gradient(w, h, top, bottom):
    img = Image.new("RGB", (w, h))
    px = img.load()
    for y in range(h):
        t = y / max(h - 1, 1)
        c = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        for x in range(w):
            px[x, y] = c
    return img


# 1. Harbour sunrise, Reykjavik coordinates, 2024-06-14 06:12
img = gradient(W, H, (58, 84, 140), (245, 176, 92))
d = ImageDraw.Draw(img)
d.ellipse([470, 300, 730, 560], fill=(255, 214, 120))          # sun
d.rectangle([0, 600, W, H], fill=(38, 84, 110))                # water
for i in range(9):                                             # reflections
    y = 630 + i * 28
    d.line([430, y, 770, y], fill=(232, 168, 96), width=4)
d.polygon([(120, 600), (230, 470), (340, 600)], fill=(24, 24, 30))  # boat hull
d.line([230, 470, 230, 380], fill=(24, 24, 30), width=6)       # mast
save(img, "harbour-sunrise.jpg", dt="2024:06:14 06:12:00",
     gps=(64.1466, -21.9426), desc="Drawn sunrise over a harbour, lab fixture")

# 2. Mountain lake, Kyoto coordinates, 2023-10-02 15:40
img = gradient(W, H, (140, 180, 205), (232, 238, 240))
d = ImageDraw.Draw(img)
d.polygon([(0, 560), (330, 190), (660, 560)], fill=(96, 116, 96))      # mountain L
d.polygon([(420, 560), (760, 140), (1100, 560)], fill=(80, 102, 88))   # mountain R
d.polygon([(690, 205), (760, 140), (830, 205)], fill=(250, 250, 250))  # snow cap
d.rectangle([0, 560, W, H], fill=(104, 148, 158))                      # lake
d.polygon([(420, 700), (760, 590), (1100, 700)], fill=(120, 160, 165)) # reflection
save(img, "mountain-lake.jpg", dt="2023:10:02 15:40:00",
     gps=(35.0116, 135.7681), desc="Drawn mountain lake, lab fixture")

# 3. City squares (abstract blocks), Reykjavik, same morning as photo 1
img = Image.new("RGB", (W, H), (238, 236, 228))
d = ImageDraw.Draw(img)
colors = [(196, 84, 62), (84, 122, 196), (90, 160, 96), (226, 182, 72), (150, 96, 170)]
k = 0
for r in range(4):
    for c in range(5):
        x, y = 60 + c * 220, 60 + r * 200
        d.rectangle([x, y, x + 160, y + 140], fill=colors[k % len(colors)])
        k += 1
save(img, "city-squares.jpg", dt="2024:06:14 09:05:00",
     gps=(64.1500, -21.9300), desc="Drawn grid of coloured squares, lab fixture")

# 4. Red circle study: no GPS, description only, 2025-01-20
img = Image.new("RGB", (W, H), (250, 250, 248))
d = ImageDraw.Draw(img)
d.ellipse([300, 150, 900, 750], fill=(205, 40, 40))
d.ellipse([520, 370, 680, 530], fill=(250, 250, 248))
save(img, "red-circle-study.jpg", dt="2025:01:20 12:00:00",
     desc="Drawn red circle study, lab fixture")

# 5. Still life (table, bowl, fruit circles), Kyoto, 2023-10-03
img = gradient(W, H, (226, 214, 188), (196, 168, 132))
d = ImageDraw.Draw(img)
d.rectangle([0, 620, W, H], fill=(122, 92, 62))                # table
d.ellipse([380, 520, 820, 660], fill=(70, 90, 120))            # bowl
d.ellipse([450, 470, 560, 580], fill=(220, 120, 40))           # orange
d.ellipse([580, 460, 690, 570], fill=(170, 40, 40))            # apple
d.ellipse([660, 480, 750, 570], fill=(120, 170, 60))           # pear-ish
save(img, "still-life.jpg", dt="2023:10:03 11:25:00",
     gps=(35.0200, 135.7600), desc="Drawn still life with fruit, lab fixture")

# 6. PNG with no metadata at all (dates must fall back to file times)
img = Image.new("RGB", (W, H), (30, 34, 44))
d = ImageDraw.Draw(img)
for i in range(6):
    d.line([100, 120 + i * 110, 1100, 120 + i * 110], fill=(120, 200, 160), width=10)
img.save(os.path.join(OUT, "chart-lines.png"))
print("wrote chart-lines.png")
print("done")
