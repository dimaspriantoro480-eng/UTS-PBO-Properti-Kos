
from properti import Properti
from kamar_kos import KamarKos
from kontrakan import Kontrakan
from penyewa import Penyewa

# Menyimpan data
daftar_properti = []
daftar_penyewa = []


# Fungsi menambahkan properti
def tambah_properti():
    print("\n=== TAMBAH DATA PROPERTI ===")
    print("1. Kamar Kos")
    print("2. Kontrakan")

    pilihan = input("Pilih jenis properti: ")

    id_properti = input("Masukkan ID properti: ")
    alamat = input("Masukkan alamat: ")
    harga = int(input("Masukkan harga sewa: "))

    if pilihan == "1":
        nomor = input("Masukkan nomor kamar: ")
        fasilitas = input("Masukkan fasilitas: ")
        kapasitas = int(input("Masukkan kapasitas: "))

        data = KamarKos(
            id_properti, alamat, harga,
            nomor, fasilitas, kapasitas
        )

    elif pilihan == "2":
        jumlah = int(input("Masukkan jumlah kamar: "))
        luas = float(input("Masukkan luas bangunan: "))
        fasilitas = input("Masukkan fasilitas: ")

        data = Kontrakan(
            id_properti, alamat, harga,
            jumlah, luas, fasilitas
        )

    else:
        print("Pilihan tidak tersedia!")
        return

    # Memeriksa ID agar tidak sama
    for properti in daftar_properti:
        if properti.get_id() == id_properti:
            print("ID properti sudah digunakan!")
            return

    daftar_properti.append(data)
    print("Data properti berhasil ditambahkan!")


# Fungsi menampilkan properti
def tampilkan_properti():
    print("\n=== DAFTAR PROPERTI ===")

    if not daftar_properti:
        print("Belum ada data properti.")
        return

    for properti in daftar_properti:
        print("\n----------------------")
        properti.tampilkan_info()


# Fungsi mencari properti
def cari_properti():
    print("\n=== CARI PROPERTI ===")

    id_cari = input("Masukkan ID properti: ")

    for properti in daftar_properti:
        if properti.get_id() == id_cari:
            print("\nData ditemukan!")
            properti.tampilkan_info()
            return

    print("Data properti tidak ditemukan.")


# Fungsi mengubah status
def ubah_properti():
    print("\n=== UBAH STATUS PROPERTI ===")

    id_cari = input("Masukkan ID properti: ")

    for properti in daftar_properti:
        if properti.get_id() == id_cari:
            print("1. Tersedia")
            print("2. Terisi")
            status = input("Pilih status baru: ")

            if status == "1":
                properti.set_status("Tersedia")
            elif status == "2":
                properti.set_status("Terisi")
            else:
                print("Pilihan tidak valid!")
                return

            print("Status berhasil diubah!")
            return

    print("Data properti tidak ditemukan.")


# Fungsi menambahkan penyewa
def tambah_penyewa():
    print("\n=== TAMBAH DATA PENYEWA ===")

    kamar_tersedia = []

    for properti in daftar_properti:
        if isinstance(properti, KamarKos):
            if properti.get_status() == "Tersedia":
                kamar_tersedia.append(properti)

    if not kamar_tersedia:
        print("Tidak ada kamar kos yang tersedia.")
        return

    print("\nDaftar kamar tersedia:")
    for kamar in kamar_tersedia:
        print(kamar.get_id(), "-", kamar.get_nomor_kamar())

    id_kamar = input("Masukkan ID kamar yang dipilih: ")

    kamar_dipilih = None

    for kamar in kamar_tersedia:
        if kamar.get_id() == id_kamar:
            kamar_dipilih = kamar
            break

    if kamar_dipilih is None:
        print("Kamar tidak ditemukan.")
        return

    nama = input("Masukkan nama penyewa: ")
    no_hp = input("Masukkan nomor HP: ")

    penyewa = Penyewa(nama, no_hp, kamar_dipilih)

    daftar_penyewa.append(penyewa)
    kamar_dipilih.set_status("Terisi")

    print("Data penyewa berhasil ditambahkan!")


# Fungsi menampilkan penyewa
def tampilkan_penyewa():
    print("\n=== DAFTAR PENYEWA ===")

    if not daftar_penyewa:
        print("Belum ada data penyewa.")
        return

    for penyewa in daftar_penyewa:
        print("\n----------------------")
        penyewa.tampilkan_info()


# Fungsi mengecek status
def cek_status():
    print("\n=== CEK STATUS PROPERTI ===")

    id_cari = input("Masukkan ID properti: ")

    for properti in daftar_properti:
        if properti.get_id() == id_cari:
            print("Status:", properti.get_status())
            return

    print("Data properti tidak ditemukan.")


# Menu utama
def menu_utama():
    while True:
        print("\n================================")
        print(" SISTEM PENGELOLAAN PROPERTI")
        print("================================")
        print("1. Tambah Data Properti")
        print("2. Tampilkan Data Properti")
        print("3. Cari Data Properti")
        print("4. Ubah Status Properti")
        print("5. Tambah Data Penyewa")
        print("6. Tampilkan Data Penyewa")
        print("7. Cek Status Properti")
        print("8. Keluar")
        print("================================")

        pilihan = input("Masukkan pilihan: ")

        try:
            if pilihan == "1":
                tambah_properti()

            elif pilihan == "2":
                tampilkan_properti()

            elif pilihan == "3":
                cari_properti()

            elif pilihan == "4":
                ubah_properti()

            elif pilihan == "5":
                tambah_penyewa()

            elif pilihan == "6":
                tampilkan_penyewa()

            elif pilihan == "7":
                cek_status()

            elif pilihan == "8":
                print("Terima kasih telah menggunakan aplikasi!")
                break

            else:
                print("Pilihan tidak valid!")

        except ValueError:
            print("Input angka tidak valid!")


# Menjalankan program
if __name__ == "__main__":
    menu_utama()
