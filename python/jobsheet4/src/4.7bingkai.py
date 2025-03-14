import cv2

citra = cv2.imread(r"C:\Raiya Yusuf Priatmojo\Praktik Penginderaan Visual Robot\python\jobsheet4\src\kucingCape.png")
scale_percent = 50
width = int(citra.shape[1] * scale_percent / 100)
height = int(citra.shape[0] * scale_percent / 100)
citra = cv2.resize(citra, (width, height), interpolation=cv2.INTER_AREA)

hasil = citra.copy()

TERAL = 20
HITAM = 0

jumBaris = hasil.shape[0]
jumKolom = hasil.shape[1]

for baris in range(TERAL):
    for kolom in range(jumKolom):
        hasil[baris, kolom] = HITAM

for baris in range(jumBaris - TERAL - 1, jumBaris):
    for kolom in range(jumKolom):
        hasil[baris, kolom] = HITAM

for baris in range(TERAL, jumBaris - TERAL - 1):
    for kolom in range(TERAL):
        hasil[baris, kolom] = HITAM

for baris in range(TERAL, jumBaris - TERAL - 1):
    for kolom in range(jumKolom - TERAL - 1, jumKolom):
        hasil[baris, kolom] = HITAM

cv2.imshow('Gambar asal', citra)
cv2.imshow('Gambar hasil', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()