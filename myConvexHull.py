from math import sqrt
import numpy as np

def distance(p1, p2, p3):
  # Fungsi untuk menghitung jarak dari titik ke garis.
  # Fungsi menerima titik p1 dan p2 pembentuk garis,
  # serta sebuah titik p3.
  # Fungsi mengembalikan jarak dari p3 ke garis p1p2.

  # ALGORITMA
  return (abs((p2[0]-p1[0])*(p1[1]-p3[1])-(p1[0]-p3[0])*(p2[1]-p1[1])))/(sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2))


def partition(bucket, indexList, p1, p2):
  # Fungsi untuk membagi kumpulan titik-titik menjadi dua partisi.
  # Fungsi menerima kumpulan titik-titik yang ditampung di dalam bucket dan 
  # indeksnya ditandai indexList,
  # serta titik p1 dan p2 pembentuk garis.
  # Fungsi mengembalikan dua partisi kiri dan kanan;
  # titik yang berada di kiri garis p1p2 dimasukkan ke partisi kiri,
  # dan titik yang berada di kanan garis p1p2 dimasukkan ke partisi kanan,
  # serta titik yang berada tepat pada garis p1p2 tidak diperhitungkan.

  # KAMUS
  left = [] # partisi kiri
  right = [] # partisi kanan

  # ALGORITMA
  for i in indexList:
    p3 = bucket[i] # titik yang diuji
    d = p1[0]*p2[1]+p3[0]*p1[1]+p2[0]*p3[1]-p3[0]*p2[1]-p2[0]*p1[1]-p1[0]*p3[1]
    if (d > 0): # titik berada di kiri garis
      left.append(i)
    elif (d < 0): # titik berada di kanan garis
      right.append(i)

  return (left, right)


def partConvexHull(hull, bucket, indexList, p1, p2):
  # Prosedur untuk menentukan titik-titik pembentuk convex hull secara rekursif
  # I.S. hull sembarang
  # F.S. hull ditambahkan indeks-indeks titik (yang ditampung dalam bucket)
  # yang membentuk convex hull secara terurut

  # ALGORITMA
  # Titik-titik yang diperiksa adalah titik-titik yang indeksnya berada di dalam indexList
  if (len(indexList) == 0): # basis 0
    pass
  elif (len(indexList) == 1): # basis 1
    hull.append(indexList[0])
  else: # rekursi
    # mencari titik dengan jarak terbesar ke garis p1p2 untuk ditambahkan ke dalam hull
    maxIdx = -1
    maxD = 0
    for i in indexList:
      p3 = bucket[i]
      d = distance(p1, p2, p3)
      if (d >= maxD):
        maxIdx = i
        maxD = d
    # titik dengan jarak terbesar telah ditemukan dan siap ditambahkan ke dalam hull
    
    # partisi titik-titik untuk menentukan titik mana saja yang masih berada 'di luar' convex hull,
    # partisi yang akan digunakan keduanya merupakan partisi kiri dari kedua garis yang baru terbentuk
    # karena algoritma berjalan secara clockwise
    left, right = partition(bucket, indexList, p1, bucket[maxIdx])
    left1, right1 = partition(bucket, right, bucket[maxIdx], p2)

    # memanggil rekursi secara terurut agar memudahkan plotting titik
    partConvexHull(hull, bucket, left1, bucket[maxIdx], p2) # kiri
    hull.append(maxIdx) # tengah (titik yang jaraknya paling jauh tadi)
    partConvexHull(hull, bucket, left, p1, bucket[maxIdx]) # kanan
      

'''FUNGSI UTAMA'''
def convexHull(bucket):
  # Fungsi untuk menentukan titik-titik pembentuk convex hull dari sekumpulan titik.
  # Fungsi menerima kumpulan titik yang ditampung dalam bucket (array of array).
  # Fungsi mengeluarkan hull (array of array) yang berisi titik-titik pembentuk convex hull 
  # yang berurutan, serta titik pertama (indeks 0) dituliskan lagi di akhir array (indeks terakhir)
  # untuk memudahkan plotting grafik (agar convex hull menjadi utuh, nyambung semua dari awal balik ke awal)

  # KAMUS
  hull = [] # penampung titik-titik pembentuk convex hull
  indexList = [i for i in range(len(bucket))] # daftar indeks yang valid dari bucket
  # pada program ini, pemrosesan dan 'pencatatan' titik-titik menggunakan indeksnya, bukan langsung titiknya

  # ALGORITMA
  # mencari titik-titik ekstrem dalam bucket, sesuai absisnya, kemudian bila absis sama, baru ordinat dibandingkan
  # titik-titik ini dipakai sebagai acuan pertama dalam partisi divide and conquer
  minIdx = np.argmin(bucket, axis=0)[0] # p1
  maxIdx = np.argmax(bucket, axis=0)[0] # pn

  # membagi titik-titik menjadi bagian kiri dan kanan dari garis p1pn
  left, right = partition(bucket, indexList, bucket[minIdx], bucket[maxIdx])

  # memanggil rekursi secara terurut agar memudahkan plotting titik
  hull.append(maxIdx) # pn
  partConvexHull(hull, bucket, left, bucket[minIdx], bucket[maxIdx]) # partisi kiri
  hull.append(minIdx) # p1
  partConvexHull(hull, bucket, right, bucket[maxIdx], bucket[minIdx]) # partisi kanan
  hull.append(maxIdx) # pn lagi, supaya grafik utuh
  
  return hull