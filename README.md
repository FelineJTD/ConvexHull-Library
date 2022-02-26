# Pustaka myConvexHull

## Deskripsi Singkat
myConvexHull merupakan sebuah library python untuk menghasilkan titik-titik pembentuk convex hull dari sekumpulan titik-titik sembarang menggunakan algoritma divide and conquer.

## Requirement
- python3 dan pip
- library (untuk program utama):
  - numpy
  - pandas
  - sklearn
  - argparse
  - matplotlib

Untuk meng-install library yang dibutuhkan, dapat menggunakan command:  
```
pip install numpy pandas sklearn argparse matplotlib
```

## Instalasi
### Clone Repository
Clone repository ini dengan command:  
```
git clone https://github.com/FelineJTD/ConvexHull-Library.git
```

### Instalasi Library **myConvexHull**
Masuk ke folder src dengan command:
```
cd src
```
Build library dengan command:  
```
python3 setup.py bdist_wheel
```
Install library dengan command:  
```
pip install ./dist/myConvexHull-0.1.0-py3-none-any.whl
```

## Menjalankan Program Utama (Pengujian Pustaka)
### Menggunakan Command Line (`main.py`)
Pastikan Anda telah berada dalam folder src, kemudian jalankan program `main.py` dengan command:
```
python3 main.py [-h] [-o OUTPUT] dataset x y
```

di mana:
- -h : menampilkan bantuan
- -o OUTPUT : nama file output (default: output.png)
- dataset : nama dataset (pilihan: iris, wine, breast_cancer)
- x : atribut pertama
- y : atribut kedua

misalkan:
```
python3 main.py -o output.png iris 0 1
```

### Menggunakan Jupyter Notebook (`main.ipynb`)
Buka file `main.ipynb` pada folder src, ubah parameter yang ditandai dengan komentar `# Ubah ...` sesuai keinginan, kemudian jalankan seluruh kode program.

## Author
Felicia Sutandijo - 13520050