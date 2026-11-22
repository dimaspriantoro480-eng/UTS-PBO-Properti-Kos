
from properti import Properti

class Kontrakan(Properti):
    def __init__(self, id_properti, alamat, harga_sewa,
                 jumlah_kamar, luas_bangunan, fasilitas):
        super().__init__(id_properti, alamat, harga_sewa)

        self.__jumlah_kamar = jumlah_kamar
        self.__luas_bangunan = luas_bangunan
        self.__fasilitas = fasilitas

    def get_jumlah_kamar(self):
        return self.__jumlah_kamar

    def get_luas_bangunan(self):
        return self.__luas_bangunan

    def tampilkan_info(self):
        super().tampilkan_info()
        print("Jumlah Kamar :", self.__jumlah_kamar)
        print("Luas Bangunan:", self.__luas_bangunan, "m2")
        print("Fasilitas    :", self.__fasilitas)

    def cek_kondisi(self):
        return "Kontrakan memiliki " + str(self.__jumlah_kamar) + " kamar"
