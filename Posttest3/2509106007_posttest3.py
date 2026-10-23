from abc import ABC, abstractmethod
from datetime import datetime


class EntitasToko(ABC):
    def __init__(self, nama):
        self.nama = nama

    # Wajib diimplementasikan oleh subclass (Abstract Method 1)
    @abstractmethod
    def tampilkan_info(self):
        pass

    # Wajib diimplementasikan oleh subclass (Abstract Method 2)
    @abstractmethod
    def validasi_data(self):
        pass

    # Method konkret yang bisa dipakai bersama
    def header_sistem(self):
        return "=== SISTEM MANAJEMEN PETSHOP & PET HOTEL ==="



class Kategori:
    total_kategori = 0
    daftar_kategori = []

    def __init__(self, nama_kategori, deskripsi):
        self.nama_kategori = nama_kategori
        self.deskripsi = deskripsi
        Kategori.total_kategori += 1
        Kategori.daftar_kategori.append(nama_kategori)

    def tampilkan_info(self):
        print(f"Kategori: {self.nama_kategori} - {self.deskripsi}")

    @classmethod
    def jumlah_kategori(cls):
        return cls.total_kategori

    @staticmethod
    def validasi_nama_kategori(nama):
        return isinstance(nama, str) and len(nama.strip()) > 0



class Produk(EntitasToko):
    nama_toko = "Whinky Petshop"
    total_produk = 0

    def __init__(self, nama_produk, harga, stok, kategori: Kategori):
        super().__init__(nama_produk)
        self.kategori = kategori
        self._harga = 0     # Protected
        self.__stok = 0     # Private
        self.harga = harga
        self.stok = stok
        Produk.total_produk += 1

    @property
    def harga(self):
        return self._harga

    @harga.setter
    def harga(self, harga_baru):
        if harga_baru < 0:
            print(f"Gagal ubah harga {self.nama}, harga gak boleh negatif.")
            return
        self._harga = harga_baru

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, stok_baru):
        if stok_baru < 0:
            print(f"Gagal ubah stok {self.nama}, stok gak boleh negatif.")
            return
        self.__stok = stok_baru

    def kurangi_stok(self, jumlah):
        if jumlah <= 0 or jumlah > self.__stok:
            return False
        self.__stok -= jumlah
        return True

    def tambah_stok(self, jumlah):
        if jumlah > 0:
            self.__stok += jumlah

    # Implementasi Abstract Method
    def tampilkan_info(self):
        print(f"| {'Nama Produk':<15} : {self.nama:<21}|")
        print(f"| {'Harga':<15} : Rp{self._harga:<10,}".replace(",", "."))
        print(f"| {'Stok':<15} : {self.__stok:<21}|")

    def validasi_data(self):
        return len(self.nama.strip()) > 0 and self._harga >= 0

    # Operator Overloading (__lt__ buat sorting & __add__ buat gabung harga)
    def __lt__(self, other):
        return self._harga < other._harga

    def __add__(self, other):
        return self._harga + other._harga



class ProdukMakanan(Produk):
    def __init__(self, nama_produk, harga, stok, kategori, jenis_hewan, tgl_kadaluarsa):
        super().__init__(nama_produk, harga, stok, kategori)
        self.jenis_hewan = jenis_hewan
        self.tgl_kadaluarsa = tgl_kadaluarsa

    # Method Overriding untuk polimorfisme via pewarisan
    def tampilkan_info(self):
        print("+----------------------------------------+")
        print(f"| {'Produk Makanan':<15} : {self.nama:<21}|")
        print(f"| {'Harga':<15} : Rp{self._harga:<19,}|".replace(",", "."))
        print(f"| {'Stok':<15} : {self.stok:<21}|")
        print(f"| {'Khusus Hewan':<15} : {self.jenis_hewan:<21}|")
        print(f"| {'Kadaluarsa':<15} : {self.tgl_kadaluarsa:<21}|")
        print("+----------------------------------------+")



class ProdukAksesori(Produk):
    def __init__(self, nama_produk, harga, stok, kategori, bahan, ukuran):
        super().__init__(nama_produk, harga, stok, kategori)
        self.bahan = bahan
        self.ukuran = ukuran

    # Method Overriding untuk polimorfisme via pewarisan
    def tampilkan_info(self):
        print("+----------------------------------------+")
        print(f"| {'Produk Aksesori':<15} : {self.nama:<21}|")
        print(f"| {'Harga':<15} : Rp{self._harga:<19,}|".replace(",", "."))
        print(f"| {'Stok':<15} : {self.stok:<21}|")
        print(f"| {'Bahan':<15} : {self.bahan:<21}|")
        print(f"| {'Ukuran':<15} : {self.ukuran:<21}|")
        print("+----------------------------------------+")



class Pelanggan:
    def __init__(self, nama, no_telepon):
        self.nama = nama
        self.no_telepon = no_telepon
        self.__poin_loyalitas = 0

    @property
    def poin_loyalitas(self):
        return self.__poin_loyalitas

    @poin_loyalitas.setter
    def poin_loyalitas(self, poin_baru):
        if poin_baru >= 0:
            self.__poin_loyalitas = poin_baru

    def tambah_poin(self, poin):
        if poin > 0:
            self.__poin_loyalitas += poin

    def tampilkan_ringkasan(self):
        print("+----------------------------------------+")
        print(f"| Nama Pelanggan : {self.nama:<22}|")
        print(f"| Nomor Telepon  : {self.no_telepon:<22}|")
        print(f"| Poin Loyalitas : {self.__poin_loyalitas:<22}|")



class Hewan:
    def __init__(self, nama_hewan, jenis, umur, pemilik: Pelanggan):
        self.nama_hewan = nama_hewan
        self.jenis = jenis
        self.pemilik = pemilik  # Relasi asosiasi
        self.umur = umur

    def tampilkan_info(self):
        print(f"Hewan: {self.nama_hewan} ({self.jenis}, {self.umur} tahun) - Pemilik: {self.pemilik.nama}")



class DetailTransaksi:
    def __init__(self, produk, jumlah):
        self.produk = produk
        self.jumlah = jumlah
        self.subtotal = produk.harga * jumlah

    def tampilkan_detail(self):
        teks = f"{self.produk.nama} x {self.jumlah} = Rp{self.subtotal:,}".replace(",", ".")
        print(f"| {teks:<39}|")


class Transaksi:
    def __init__(self, pelanggan: Pelanggan):
        self.pelanggan = pelanggan
        self.tanggal = datetime.now().strftime("%d-%m-%Y")
        self.daftar_detail = []  # Relasi Komposisi
        self.__total_bayar = 0
        self.status = "Belum Dibayar"

    # Magic Method __len__ untuk Operator Overloading
    def __len__(self):
        return len(self.daftar_detail)

    def tambah_detail(self, produk: Produk, jumlah):
        if jumlah > 0 and produk.kurangi_stok(jumlah):
            self.daftar_detail.append(DetailTransaksi(produk, jumlah))
            self.__hitung_total()

    def __hitung_total(self):
        subtotal = sum(d.subtotal for d in self.daftar_detail)
        self.__total_bayar = subtotal + (subtotal * 0.11)  # PPN 11%

    def tampilkan_ringkasan(self):
        print(f"| Pelanggan Transaksi : {self.pelanggan.nama:<17}|")
        print(f"| Jumlah Item Belanja : {len(self):<17}|")

    def cetak_struk(self):
        print()
        print("+----------------------------------------+")
        print("|           STRUK PEMBELIAN              |")
        print("+----------------------------------------+")
        print(f"| Tanggal       : {self.tanggal:<22} |")
        print(f"| Pelanggan     : {self.pelanggan.nama:<22} |")
        print("|----------------------------------------|")
        for detail in self.daftar_detail:
            detail.tampilkan_detail()
        print("|----------------------------------------|")
        print(f"| Total (Inc 11%): Rp{self.__total_bayar:,.0f}             |".replace(",", "."))
        print(f"| Status        : {self.status:<22} |")
        print("+----------------------------------------+")



def tampilkan_ringkasan(objek):
    # Duck typing: asal objek punya method tampilkan_ringkasan(), bisa dipakai!
    objek.tampilkan_ringkasan()



if __name__ == "__main__":
    print("+----------------------------------------+")
    print("|   SISTEM MANAJEMEN PETSHOP & HOTEL     |")
    print("+----------------------------------------+\n")

    # Inisialisasi kategori & produk
    kategori_makanan = Kategori("Makanan", "Makanan kucing dan anjing")
    kategori_aksesori = Kategori("Aksesori", "Perlengkapan hewan")

    makanan_kucing = ProdukMakanan("Royal Canin 1kg", 150000, 20, kategori_makanan, "Kucing", "12-2027")
    kalung_anjing = ProdukAksesori("Kalung Kulit", 45000, 15, kategori_aksesori, "Kulit", "M")

    # 1. Uji Polimorfisme via Pewarisan (1 loop, method sama, hasil beda)
    print("--- 1. UJI POLIMORFISME VIA PEWARISAN ---")
    daftar_produk = [makanan_kucing, kalung_anjing]
    for p in daftar_produk:
        p.tampilkan_info()

    # 2. Uji Operator Overloading (+) dan (<)
    print("\n--- 2. UJI OPERATOR OVERLOADING ---")
    print(f"Total harga Royal Canin + Kalung: Rp{makanan_kucing + kalung_anjing:,}".replace(",", "."))
    print(f"Apakah Royal Canin lebih murah dari Kalung? {makanan_kucing < kalung_anjing}")

    # 3. Uji Pelanggan & Transaksi
    pelanggan = Pelanggan("Syarifah Gea", "081234567890") #pakai nama sama saya aja yah
    transaksi = Transaksi(pelanggan)
    transaksi.tambah_detail(makanan_kucing, 2)

    # 4. Uji Duck Typing
    print("\n--- 3. UJI DUCK TYPING ---")
    tampilkan_ringkasan(pelanggan)
    print("|----------------------------------------|")
    tampilkan_ringkasan(transaksi)
    print("+----------------------------------------+")

    transaksi.cetak_struk()

    # 5. Uji Bukti Abstraksi (TypeError)
    print("\n--- 4. UJI BUKTI ABSTRAKSI (ABC) ---")
    try:
        salah = EntitasToko("Test")
    except TypeError as e:
        print("Pengujian Berhasil: Abstract class EntitasToko tidak bisa diinstansiasi langsung.")
        print(f"Pesan Error: {e}")