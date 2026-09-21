from datetime import datetime

class Kategori: # Class Kategori
    total_kategori = 0 # atribut kelas
    daftar_kategori = [] # atribut kelas

    def __init__(self, nama_kategori, deskripsi):
        self.nama_kategori = nama_kategori # public
        self.deskripsi = deskripsi # public

        Kategori.total_kategori += 1
        Kategori.daftar_kategori.append(nama_kategori)

    def tampilkan_info(self):  # instance method
        print(f"Kategori: {self.nama_kategori} - {self.deskripsi}")

    @classmethod  # class method
    def jumlah_kategori(cls):
        return cls.total_kategori

    @staticmethod  # static method
    def validasi_nama_kategori(nama):
        return isinstance(nama, str) and len(nama.strip()) > 0


class Produk: # Class Produk (induk untuk ProdukMakanan & ProdukAksesori)
    nama_toko = "Whinky petshop and hotel"  # atribut kelas
    total_produk = 0 # atribut kelas

    def __init__(self, nama_produk, harga, stok, kategori: Kategori):
        self.nama_produk = nama_produk  # public
        self.kategori = kategori # public, objek dari class Kategori
        self.__harga = 0 # private, diisi lewat setter biar tervalidasi
        self.__stok = 0 # private
        self.harga = harga # buat memanggil setter harga
        self.stok = stok # buat memanggil setter stok

        Produk.total_produk += 1

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, harga_baru):
        if harga_baru < 0:
            print(f"Gagal ubah harga {self.nama_produk}, harga ga boleh negatif.")
            return
        self.__harga = harga_baru

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, stok_baru):
        if stok_baru < 0:
            print(f"Gagal ubah stok {self.nama_produk}, stok ga boleh negatif.")
            return
        self.__stok = stok_baru

    def kurangi_stok(self, jumlah):  # instance method
        if jumlah <= 0:
            print("Jumlah pengurangan ga valid.")
            return False
        if jumlah > self.__stok:
            print(f"Stok {self.nama_produk} ga cukup buat dikurangi {jumlah}.")
            return False
        self.__stok -= jumlah
        return True

    def tambah_stok(self, jumlah):
        if jumlah <= 0:
            print("Jumlah penambahan ga valid.")
        else:
            self.__stok += jumlah

    def tampilkan_info(self):
        print(f"[{self.kategori.nama_kategori}] {self.nama_produk} - "f"Rp{self.__harga:,} (stok: {self.__stok})")

    @classmethod
    def ubah_nama_toko(cls, nama_baru):
        cls.nama_toko = nama_baru

    @staticmethod
    def validasi_nama_produk(nama):
        return isinstance(nama, str) and len(nama.strip()) > 0


class ProdukMakanan(Produk):
    total_produk_makanan = 0

    def __init__(self, nama_produk, harga, stok, kategori, jenis_hewan, tgl_kadaluarsa):
        super().__init__(nama_produk, harga, stok, kategori)
        self.jenis_hewan = jenis_hewan # public
        self.tgl_kadaluarsa = tgl_kadaluarsa # public

        ProdukMakanan.total_produk_makanan += 1

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f" Untuk: {self.jenis_hewan} | Kadaluarsa: {self.tgl_kadaluarsa}")


class ProdukAksesori(Produk):
    total_produk_aksesori = 0

    def __init__(self, nama_produk, harga, stok, kategori, bahan, ukuran):
        super().__init__(nama_produk, harga, stok, kategori)
        self.bahan = bahan # public
        self.ukuran = ukuran # public

        ProdukAksesori.total_produk_aksesori += 1

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"    Bahan: {self.bahan} | Ukuran: {self.ukuran}")


class Pelanggan: # Class Pelanggan
    total_pelanggan = 0 # atribut kelas
    diskon_member = 0.05 # atribut kelas (diskon 5% untuk member)
    poin_per_rupiah = 10000 # atribut kelas: nanti tiap beli Rp10.000 dapat 1 poin

    def __init__(self, nama, no_telepon):
        self.nama = nama # public
        self.no_telepon = no_telepon # public
        self.__poin_loyalitas = 0 # private, poin nya ga boleh diisi sembarangan

        Pelanggan.total_pelanggan += 1

    @property
    def poin_loyalitas(self):
        return self.__poin_loyalitas

    @poin_loyalitas.setter
    def poin_loyalitas(self, poin_baru):
        if poin_baru < 0:
            print(f"Gagal update poin {self.nama}, poin nya ga boleh negatif.")
            return
        self.__poin_loyalitas = poin_baru

    def tambah_poin(self, poin):
        if poin > 0:
            self.__poin_loyalitas += poin

    def tampilkan_info(self):
        print(f"Pelanggan: {self.nama} ({self.no_telepon}) - "f"Poin: {self.__poin_loyalitas}")

    @classmethod
    def dari_dict(cls, data):  # factory method
        return cls(data["nama"], data["no_telepon"])

    @staticmethod
    def validasi_telepon(no_telepon):
        return no_telepon.isdigit() and len(no_telepon) >= 10


class Hewan: # Class Hewan
    total_hewan = 0
    jenis_terdaftar = ["Kucing", "Anjing", "Kelinci", "Hamster", "Burung"]

    def __init__(self, nama_hewan, jenis, umur, pemilik: Pelanggan):
        self.nama_hewan = nama_hewan # public
        self.jenis = jenis # public
        self.pemilik = pemilik # public, objek dari class Pelanggan
        self.__umur = 0 # private
        self.umur = umur # lewat setter biar tervalidasi

        Hewan.total_hewan += 1

    @property
    def umur(self):
        return self.__umur

    @umur.setter
    def umur(self, umur_baru):
        if umur_baru < 0:
            print(f"Gagal update umur {self.nama_hewan}, umur nya ga boleh negatif.")
            return
        self.__umur = umur_baru

    def tampilkan_info(self):
        print(f"Hewan: {self.nama_hewan} "
              f"({self.jenis}, {self.__umur} tahun) - Pemilik: {self.pemilik.nama}")

    @classmethod
    def tambah_jenis_baru(cls, jenis_baru):
        if jenis_baru not in cls.jenis_terdaftar:
            cls.jenis_terdaftar.append(jenis_baru)

    @staticmethod
    def validasi_jenis(jenis, daftar_jenis):
        return jenis in daftar_jenis


class DetailTransaksi: # Class DetailTransaksi
    total_detail = 0

    def __init__(self, produk: Produk, jumlah):
        self.produk = produk # public
        self.__jumlah = 1 # private
        self.jumlah = jumlah # lewat setter biar tervalidasi
        DetailTransaksi.total_detail += 1

    @property
    def jumlah(self):
        return self.__jumlah

    @jumlah.setter
    def jumlah(self, jumlah_baru):
        if jumlah_baru <= 0:
            print("Jumlah beli minimal 1, ga bisa 0 atau negatif.")
            return
        self.__jumlah = jumlah_baru

    def subtotal(self):
        return self.produk.harga * self.__jumlah

    def tampilkan(self):
        print(f"  {self.produk.nama_produk} x{self.__jumlah} = Rp{self.subtotal():,}")


class Transaksi: # Class Transaksi
    total_transaksi = 0
    kode_prefix = "TRX"
    ppn_persen = 11

    def __init__(self, pelanggan: Pelanggan, tanggal=None):
        self.pelanggan = pelanggan # public
        self.tanggal = tanggal or datetime.now().strftime("%d-%m-%Y") # public
        self.daftar_detail = [] # public
        self.status = "Belum Dibayar" # public
        self.ppn = Transaksi.ppn_persen  # PPN dikunci saat transaksinya dibuat
        self.__total_bayar = 0 # private
        Transaksi.total_transaksi += 1
        self.kode_transaksi = f"{Transaksi.kode_prefix}{Transaksi.total_transaksi:04d}"

    @property
    def total_bayar(self):  # getter saja, total hanya boleh dihitung oleh class
        return self.__total_bayar

    def tambah_detail(self, produk: Produk, jumlah):  # instance method
        if jumlah <= 0:
            print("Gagal tambah, jumlah beli minimal 1.")
            return
        if jumlah > produk.stok:
            print(f"Gagal tambah, stok {produk.nama_produk} ga cukup.")
            return
        self.daftar_detail.append(DetailTransaksi(produk, jumlah))
        produk.kurangi_stok(jumlah)
        self.__hitung_total()

    def __hitung_total(self):  # private method
        subtotal = sum(d.subtotal() for d in self.daftar_detail)
        self.__total_bayar = subtotal + subtotal * (self.ppn / 100)

    def cetak_struk(self):
        print(f"\n=== Struk {self.kode_transaksi} ({self.tanggal}) ===")
        print(f"Pelanggan: {self.pelanggan.nama}")
        for detail in self.daftar_detail:
            detail.tampilkan()
        print(f"PPN {self.ppn}% udah termasuk")
        print(f"Total Bayar: {Transaksi.format_rupiah(self.__total_bayar)}")
        print(f"Status: {self.status}")

    def bayar(self):
        if self.status == "Lunas":
            print(f"{self.kode_transaksi} sudah dibayar sebelumnya.")
            return
        self.status = "Lunas"
        poin = int(self.__total_bayar // Pelanggan.poin_per_rupiah)
        self.pelanggan.tambah_poin(poin)
        print(f"{self.kode_transaksi} lunas. {self.pelanggan.nama} dapat {poin} poin.")

    @classmethod
    def ubah_ppn(cls, ppn_baru):
        cls.ppn_persen = ppn_baru

    @staticmethod
    def format_rupiah(angka):
        return f"Rp{angka:,.0f}"


class ReservasiHotel: # Class ReservasiHotel
    total_reservasi = 0
    kapasitas_kandang = 20
    tarif_default_per_hari = 50000

    def __init__(self, hewan: Hewan, lama_hari):
        self.hewan = hewan # public
        self.__lama_hari = 1 # private, diisi lewat setter
        self.lama_hari = lama_hari # memanggil setter (raise ValueError kalau ga valid)
        self.status = "Menunggu" # public

        ReservasiHotel.total_reservasi += 1
        self.kode_reservasi = f"HTL{ReservasiHotel.total_reservasi:04d}"

    @property
    def lama_hari(self):
        return self.__lama_hari

    @lama_hari.setter
    def lama_hari(self, hari_baru):
        if hari_baru <= 0:
            raise ValueError("Lama nginap minimal 1 hari.")
        self.__lama_hari = hari_baru

    def hitung_biaya(self):
        return self.__lama_hari * ReservasiHotel.tarif_default_per_hari

    def checkin(self):
        self.status = "Check-in"
        print(f"{self.hewan.nama_hewan} udah check-in di pet hotel.")

    def checkout(self):
        self.status = "Selesai"
        print(f"{self.hewan.nama_hewan} udah check-out, total biaya: Rp{self.hitung_biaya():,}")

    def tampilkan_info(self):
        print(f"[{self.kode_reservasi}] {self.hewan.nama_hewan} - "f"{self.__lama_hari} hari - Status: {self.status}")

    @classmethod
    def ubah_tarif(cls, tarif_baru):
        cls.tarif_default_per_hari = tarif_baru

    @staticmethod
    def validasi_lama_hari(hari):
        return isinstance(hari, int) and hari > 0


if __name__ == "__main__": # Main program untuk testing semua class
    print("=========================================")
    print("  SISTEM MANAJEMEN PETSHOP & PET HOTEL   ")
    print("=========================================\n")

    
    print("-- Kategori --") # Kategori (2 objek)
    kategori_makanan = Kategori("Makanan", "Makanan buat berbagai jenis hewan")
    kategori_aksesori = Kategori("Aksesori", "Perlengkapan & aksesori hewan")
    kategori_makanan.tampilkan_info()
    kategori_aksesori.tampilkan_info()
    print(f"Total kategori terdaftar: {Kategori.jumlah_kategori()}")
    print("Daftar kategori:", Kategori.daftar_kategori)
    print("Validasi nama 'Makanan':", Kategori.validasi_nama_kategori("Makanan"))
    print("Validasi nama kosong:", Kategori.validasi_nama_kategori("  "), "\n")


    print("-- Produk Umum --") # Produk (2 objek)
    voucher = Produk("Voucher Grooming", 100000, 10, kategori_aksesori)
    obat_kutu = Produk("Obat Kutu", 35000, 25, kategori_aksesori)
    voucher.tampilkan_info()
    obat_kutu.tampilkan_info()


    print("\n-- Produk Makanan --") # ProdukMakanan (2 objek)
    dry_food = ProdukMakanan("Royal Canin 1kg", 150000, 20, kategori_makanan, "Kucing", "12-2027")
    wet_food = ProdukMakanan("Whiskas Pouch", 12000, 50, kategori_makanan, "Kucing", "06-2027")
    dry_food.tampilkan_info()
    wet_food.tampilkan_info()

    
    print("\n-- Produk Aksesori --") # ProdukAksesori (2 objek)
    kalung = ProdukAksesori("Kalung Anjing", 45000, 15, kategori_aksesori, "Kulit Sintetis", "M")
    kandang = ProdukAksesori("Kandang Kucing", 200000, 5, kategori_aksesori, "Besi", "L")
    kalung.tampilkan_info()
    kandang.tampilkan_info()
    print(f"\nTotal seluruh produk terdaftar: {Produk.total_produk}")

    # static method
    print("Validasi nama 'Royal Canin':", Produk.validasi_nama_produk("Royal Canin"))
    print("Validasi nama kosong:", Produk.validasi_nama_produk("   "))

    # setter harga: valid & gak valid
    dry_food.harga = 160000 # valid
    dry_food.harga = -5000 # ditolak
    print(f"Harga Royal Canin sekarang: Rp{dry_food.harga:,}")

    # instance method buat tambah_stok & kurangi_stok (valid & gak valid)
    obat_kutu.tambah_stok(15)
    obat_kutu.tambah_stok(-3) # ditolak
    print(f"Stok Obat Kutu setelah restock: {obat_kutu.stok}")
    obat_kutu.kurangi_stok(5) # valid
    obat_kutu.kurangi_stok(999) # ditolak, stok ga cukup
    print(f"Stok Obat Kutu setelah dikurangi: {obat_kutu.stok}")

    # setter stok: valid & tidak valid
    obat_kutu.stok = 40 # valid
    obat_kutu.stok = -10 # ditolak
    print(f"Stok Obat Kutu sekarang: {obat_kutu.stok}")

    # class method
    Produk.ubah_nama_toko("Petshop Cookie Balikpapan")
    print(f"Nama toko sekarang: {Produk.nama_toko}\n")


    print("-- Pelanggan --") # Pelanggan (2 objek)
    jimin = Pelanggan("Jimin", "081234567890")
    jungkook = Pelanggan.dari_dict({"nama": "Jungkook", "no_telepon": "082198765432"})
    jimin.tampilkan_info()
    jungkook.tampilkan_info()
    print(f"Total pelanggan: {Pelanggan.total_pelanggan}")
    print("Validasi telepon Jimin:", Pelanggan.validasi_telepon(jimin.no_telepon))
    print("Validasi telepon 'abc':", Pelanggan.validasi_telepon("abc"))

    # setter poin: valid & tidak valid
    jimin.poin_loyalitas = 10 # valid
    jimin.poin_loyalitas = -5 # ditolak
    print(f"Poin Jimin sekarang: {jimin.poin_loyalitas}\n")

        
    print("-- Hewan --") # Hewan (2 objek)
    kucing_jimin = Hewan("Mochi", "Kucing", 2, jimin)
    anjing_jungkook = Hewan("Yeontan", "Anjing", 3, jungkook)
    kucing_jimin.tampilkan_info()
    anjing_jungkook.tampilkan_info()
    print(f"Total hewan terdaftar: {Hewan.total_hewan}")

    Hewan.tambah_jenis_baru("Reptil")
    print("Jenis hewan yang diterima:", Hewan.jenis_terdaftar)
    print("Validasi jenis 'Kucing':", Hewan.validasi_jenis("Kucing", Hewan.jenis_terdaftar))
    print("Validasi jenis 'Naga':", Hewan.validasi_jenis("Naga", Hewan.jenis_terdaftar))

    # setter umur: valid & tidak valid
    kucing_jimin.umur = 3 # valid
    kucing_jimin.umur = -1 # ditolak
    print(f"Umur Mochi sekarang: {kucing_jimin.umur} tahun\n")


    print("-- Transaksi --") # Transaksi (2 objek)
    transaksi1 = Transaksi(jimin)
    transaksi1.tambah_detail(dry_food, 2)
    transaksi1.tambah_detail(kalung, 1)
    transaksi1.tambah_detail(kalung, 0) # ditolak, jumlah nya ga valid
    transaksi1.tambah_detail(kandang, 100) # ditolak, stok nya ga cukup
    transaksi1.cetak_struk()
    transaksi1.bayar()
    transaksi1.bayar() # ditolak, sudah lunas (poin ga dobel)
    print(f"Poin Jimin setelah belanja: {jimin.poin_loyalitas}")

    Transaksi.ubah_ppn(5) # class method, hanya berlaku untuk transaksi baru
    print(f"PPN transaksi baru sekarang: {Transaksi.ppn_persen}%")
    transaksi2 = Transaksi(jungkook)
    transaksi2.tambah_detail(kandang, 1)
    transaksi2.tambah_detail(wet_food, 4)
    transaksi2.cetak_struk()
    transaksi2.bayar()
    print(f"Total transaksi tercatat: {Transaksi.total_transaksi}")
    print("Total bayar transaksi1 (getter):", Transaksi.format_rupiah(transaksi1.total_bayar), "\n")


    print("-- Detail Transaksi --") # DetailTransaksi (2 objek dibuat langsung)
    detail1 = DetailTransaksi(wet_food, 3)
    detail2 = DetailTransaksi(kalung, 2)
    detail1.tampilkan()
    detail2.tampilkan()
    detail1.jumlah = 5 # valid
    detail1.jumlah = -2 # ditolak
    detail1.tampilkan()
    print()


    print("-- Reservasi Pet Hotel --") # ReservasiHotel (2 objek)
    print("Validasi 3 hari:", ReservasiHotel.validasi_lama_hari(3))
    print("Validasi -1 hari:", ReservasiHotel.validasi_lama_hari(-1))
    reservasi1 = ReservasiHotel(kucing_jimin, 3)
    reservasi2 = ReservasiHotel(anjing_jungkook, 5)
    reservasi1.checkin()
    reservasi2.checkin()
    reservasi1.tampilkan_info()
    reservasi2.tampilkan_info()
    reservasi1.checkout()
    reservasi2.checkout()
    print(f"Total reservasi hotel: {ReservasiHotel.total_reservasi}")

    reservasi1.lama_hari = 4 # valid
    print(f"Lama nginap {reservasi1.hewan.nama_hewan} sekarang: {reservasi1.lama_hari} hari")
    try:
        reservasi1.lama_hari = -2 # tidak valid = ValueError
    except ValueError as e:
        print(f"Gagal ubah lama nginap: {e}")

    ReservasiHotel.ubah_tarif(75000)
    print(f"Tarif per hari sekarang: Rp{ReservasiHotel.tarif_default_per_hari:,}")