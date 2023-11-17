import cv2
import numpy as np

#ini buat isi input
image_paths = [
    "/home/zorin/Documents/aulah/codingan-opencv/padang_rumput/1.jpg",
    "/home/zorin/Documents/aulah/codingan-opencv/padang_rumput/2.jpg",
    "/home/zorin/Documents/aulah/codingan-opencv/padang_rumput/3.jpg",
    "/home/zorin/Documents/aulah/codingan-opencv/padang_rumput/4.jpg",
    "/home/zorin/Documents/aulah/codingan-opencv/padang_rumput/5.jpg",
    "/home/zorin/Documents/aulah/codingan-opencv/padang_rumput/6.jpg",
    "/home/zorin/Documents/aulah/codingan-opencv/padang_rumput/7.jpg",
    "/home/zorin/Documents/aulah/codingan-opencv/padang_rumput/8.jpg",
    ]

images = [cv2.imread(path) for path in image_paths]

stitcher = cv2.createStitcher() if cv2.__version__.startswith("3.") else cv2.Stitcher_create()

status, panorama = stitcher.stitch(images)

if status == cv2.Stitcher_OK:
    cv2.imwrite("/home/zorin/Documents/aulah/codingan-opencv/padang_rumput.png", panorama) #yang ini buat output
    print("Panorama berhasil disimpan!")
else:
    print("Gagal membuat panorama. Status:", status)