import cv2
import numpy as np

# Baca gambar-gambar input
image_paths = [
    "lagi/1.jpg",
    "lagi/2.jpg",
    "lagi/3.jpg",
    "lagi/4.jpg",
    "lagi/5.jpg",
    "lagi/6.jpg",
    ]

images = [cv2.imread(path) for path in image_paths]

# Buat objek stitcher
stitcher = cv2.createStitcher() if cv2.__version__.startswith("3.") else cv2.Stitcher_create()

# Lakukan proses stitching
status, panorama = stitcher.stitch(images)

if status == cv2.Stitcher_OK:
    # Simpan gambar panorama
    cv2.imwrite("dalam.jpg", panorama)
    print("Panorama berhasil disimpan sebagai 'goblok.png'.")
else:
    print("Gagal membuat panorama. Status:", status)
