# Sistem Manajemen Penjualan Petshop & Pendataan Pet Hotel
Ini program Python yang menerapkan OOP buat posttest 1 praktikum PBO. Temanya sistem petshop: untuk ngatur penjualan produk (makanan & aksesori), data pelanggan sama hewannya, transaksi, dan juga reservasi pet hotel

## Cara jalanin sistemnya
python 2509106007_posttest1.py

Ga perlu install apa-apa lagii karna kan cuma pakai `datetime` bawaan Python

## Class yang dipakai

Ada 9 class:
- Kategori : kategori produk (Makanan, Aksesori)
- Produk : data produk umum (nama, harga, stok, kategori). Harga sama stok dibikin private
- ProdukMakanan : turunan Produk, nambah jenis hewan & tanggal kadaluarsa
- ProdukAksesori : turunan Produk, nambah bahan & ukuran
- Pelanggan : data pelanggan, poin loyalitas dibikin private
- Hewan : hewan punya pelanggan, umurnya private
- DetailTransaksi : satu baris belanjaan (produk + jumlah), jumlahnya private
- Transaksi : transaksi penjualan, isinya pelanggan + list DetailTransaksi. Total bayar private
- ReservasiHotel : reservasi pet hotel buat satu hewan, lama nginapnya private

Class-class ini saling pakai objek satu sama lain, contohnya Produk nanti nyimpen objek Kategori, Hewan nyimpen objek Pelanggan sebagai pemilik, dan Transaksi nyimpen Pelanggan sama DetailTransaksi nya

## Materi yang dipakai ada dari modul 1 sampai 3
### penggunaan modul 1 
Semua class pakai `__init__` dan `self`. Tiap class dibikin minimal 2 objek di bagian main

### penggunaan modul 2 
- Atribut kelas contohnya `Kategori.total_kategori`, `Produk.nama_toko`, `Pelanggan.diskon_member`, `Transaksi.ppn_persen`, `ReservasiHotel.tarif_default_per_hari`.
- Atribut instance dibikin di `__init__` pakai `self`, nilainya beda tiap objek (nama produk, nama pelanggan, tanggal transaksi, dll)
- Instance method contohnya `tampilkan_info()`, `tambah_stok()`, `kurangi_stok()`, `tambah_detail()`, `cetak_struk()`, `bayar()`, `checkin()`, `checkout()`
- Class method (`@classmethod`) contohnya `Kategori.jumlah_kategori()`, `Produk.ubah_nama_toko()`, `Hewan.tambah_jenis_baru()`, `Transaksi.ubah_ppn()`, `ReservasiHotel.ubah_tarif()`, dan `Pelanggan.dari_dict()` yang dipakai buat bikin objek dari dictionary (factory method)
- Static method (`@staticmethod`) contohnya `Produk.validasi_nama_produk()`, `Pelanggan.validasi_telepon()`, `Hewan.validasi_jenis()`, `Transaksi.format_rupiah()`, `ReservasiHotel.validasi_lama_hari()`

### penggunaan modul 3 
Data penting dibikin private pakai `__`, terus diaksesnya lewat `@property` (getter) dan `@nama.setter` (setter). Nama setter sama persis kayak getter-nya. Setternya ada validasinya:

- `harga` sama `stok` di Produk: ga boleh negatif
- `poin_loyalitas` di Pelanggan: ga boleh negatif
- `umur` di Hewan: ga boleh negatif
- `jumlah` di DetailTransaksi: minimal 1
- `lama_hari` di ReservasiHotel: minimal 1, kalau ga valid langsung `raise ValueError`

Kalau input ga valid, di kebanyakan setter perubahannya ditolak dan muncul pesan peringatan. Setter ini juga dipanggil waktu kita bikin objek (di `__init__`), jadi kalau ada yang bikin `Produk` dengan harga negatif, nilainya tetap ditolak (harga jadi 0 dan muncul pesan peringatannya). Khusus `ReservasiHotel`, kalau lama nginap ga valid objeknya langsung gagal dibuat karena `ValueError`. Khusus `total_bayar` di Transaksi cuma ada getter aja, soalnya totalnya dihitung otomatis sama class-nya, jadi ga boleh diisi dari luar


## Cara ngetesnyaa

Tinggal kita jalanin filenya, terus lihat outputnya. 
Bagian-bagian yang bisa dicek:
1. Bagian Kategori dan Produk: info tampil, total produk 6, validasi nama produk ngasih `True` dan `False`
2. Tiap setter dites dua kali, sekali pakai nilai valid (contoh `dry_food.harga = 160000`, diterima) dan sekali pakai nilai ga valid (contoh `dry_food.harga = -5000`, ditolak dan muncul pesan)
3. Bagian Transaksi: nambah barang dengan jumlah 0 atau stok ga cukup ditolak. Habis itu `bayar()` dipanggil dua kali, tapi poin cuma nambah sekali
4. `Transaksi.ubah_ppn(5)` cuma ngaruh ke transaksi baru, jadi struk transaksi pertama tetap PPN 11%
5. Bagian Reservasi: `lama_hari = -2` bakal `ValueError`, dan errornya ditangkap pakai `try/except` biar programnya ga berhenti
6. Class method kayak `Pelanggan.dari_dict`, `ubah_tarif`, dan `tambah_jenis_baru` bisa dilihat hasilnya langsung di output