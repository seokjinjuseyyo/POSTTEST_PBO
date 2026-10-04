# Sistem Manajemen Penjualan Petshop & Pendataan Pet Hotel
Ini program Python yang aku lanjutin dari posttest sebelumnya buat ngerjain posttest praktikum PBO. Temanya sistem petshop: untuk mengatur penjualan produk (makanan & aksesori), data pelanggan sama hewannya, transaksi, reservasi pet hotel, dan sekarang sudah ditambahin materi baru sesuai modul 4 dan 5 yaitu Relasi UML dan Inheritance.

## Cara biar bisa jalanin sistemnya
python 2509106007_posttest4.py

disini jelas kita nda perlu install apa-apa lagi karena cuma pakai `datetime` bawaan Python aja.


## Class yang Dipakai di Sistem
Total ada 10 class yang saling berinteraksi:
- **`Kategori`** : kategori produk (Makanan, Aksesori)
- **`Produk` (Superclass)** : data produk induk (nama, harga, stok, kategori). Atribut harga dibikin *protected* (`_harga`) supaya bisa diakses oleh subclass-nya, sedangkan stok dibikin *private* (`__stok`).
- **`ProdukMakanan` (Subclass)** : turunan dari `Produk`, nambah atribut unik jenis hewan & tanggal kadaluarsa, serta meng-override method `tampilkan_info()`.
- **`ProdukAksesori` (Subclass)** : turunan dari `Produk`, nambah atribut unik bahan & ukuran, serta meng-override method `tampilkan_info()`.
- **`Pelanggan`** : data pelanggan, poin loyalitas dibikin private.
- **`Hewan`** : hewan punya pelanggan, umurnya private.
- **`DetailTransaksi`** : satu baris belanjaan (produk + jumlah), jumlahnya private.
- **`Transaksi`** : transaksi penjualan, isinya pelanggan + list DetailTransaksi. Total bayar private.
- **`ReservasiHotel`** : reservasi pet hotel buat satu hewan, lama nginapnya private.

Class-class ini saling pakai objek satu sama lain, contohnya Produk nyimpen objek Kategori, Hewan nyimpen objek Pelanggan sebagai pemiliknya, dan Transaksi nyimpen Pelanggan sama DetailTransaksi-nya.


# Materi Modul 4 dan 5 yang Diterapkan
## 1. Relasi UML (untuk Modul 4)
- **Asosiasi**: Hubungan di mana suatu kelas menggunakan objek dari kelas lain sebagai parameter (contoh: class `Hewan` nyimpen referensi objek `Pelanggan`, dan `Transaksi` memproses objek `Produk`).
- **Agregasi / Komposisi**: Hubungan kepemilikan data secara struktural (contoh: class `Transaksi` menampung list objek `DetailTransaksi`).

## 2. Inheritance / Pewarisan (untuk Modul 5)
- **Superclass & Subclass**: Membuat 1 Parent Class (`Produk`) yang diturunkan ke 2 Child Class (`ProdukMakanan` dan `ProdukAksesori`).
- **Penggunaan `super()`**: Subclass wajib manggil konstruktor parent-nya menggunakan `super().__init__(...)`.
- **Atribut Tambahan**: Setiap subclass punya minimal 1-2 atribut spesifik yang membedakannya (seperti `jenis_hewan` & `tgl_kadaluarsa` pada makanan, serta `bahan` & `ukuran` pada aksesori).
- **Method Overriding**: Method `tampilkan_info()` yang ada di superclass `Produk` di-override (didefinisikan ulang) di dalam class `ProdukMakanan` dan `ProdukAksesori` biar output cetakannya nampilin detail spesifik masing-masing produk.
- **Tingkat Akses (Protected & Private)**: 
  - Atribut harga di-set sebagai *protected* (`_harga`) di superclass agar aman tapi tetap bisa diakses dengan fleksibel oleh subclass.
  - Atribut lainnya tetap dijaga ketat pakai *private* (`__`) dan diakses lewat `@property` (getter/setter) dengan validasi agar nilainya tidak negatif.


## Cara Buat Ngetes Programnya
Tinggal jalankan filenya aja di terminal, lalu cek bagian-bagian berikut di outputnya:
1. **Bagian Kategori & Produk Umum**: Menampilkan informasi dasar produk dan validasi static method.
2. **Bagian Produk Makanan & Aksesori**: Membuktikan bahwa subclass berhasil mewarisi dari superclass lewat `super().__init__()`, sekaligus mengetes *method overriding* pada `tampilkan_info()` untuk menampilkan atribut uniknya.
3. **Bagian Pelanggan, Hewan, & Transaksi**: Menguji relasi antar objek, setter/getter yang mencegah nilai negatif, perhitungan PPN, dan sistem penambahan poin loyalitas.
4. **Bagian Reservasi Pet Hotel**: Menguji validasi lama hari menginap dan penanganan error menggunakan `try/except` apabila input tidak valid (`ValueError`).