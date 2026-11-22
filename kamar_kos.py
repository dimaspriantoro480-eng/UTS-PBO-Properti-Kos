
from properti import Properti

class KamarKos(Properti):
    def __init__(self, id_properti, alamat, harga_sewa,
                 nomor_kamar, fasilitas, kapasitas):
        super().__init__(id_properti, alamat, harga_sewa)

        self.__nomor_kamar = nomor_kamar
        self.__fasilitas = fasilitas
        self.__kapasitas = kapasitas

    def get_nomor_kamar(self):
        return self.__nomor_kamar

    def get_fasilitas(self):
        return self.__fasilitas

    def tampilkan_info(self):
        super().tampilkan_info()
        print("Nomor Kamar :", self.__nomor_kamar)
        print("Fasilitas   :", self.__fasilitas)
        print("Kapasitas   :", self.__kapasitas, "orang")

    def cek_kapasitas(self):
        return self.__kapasitas
