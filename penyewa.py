
class Penyewa:
    def __init__(self, nama, no_hp, kamar_kos):
        self.__nama = nama
        self.__no_hp = no_hp
        self.__kamar_kos = kamar_kos

    def get_nama(self):
        return self.__nama

    def get_no_hp(self):
        return self.__no_hp

    def tampilkan_info(self):
        print("Nama Penyewa :", self.__nama)
        print("Nomor HP     :", self.__no_hp)
        print("Kamar yang Ditempati:")
        self.__kamar_kos.tampilkan_info()

    def cek_tempat_tinggal(self):
        return self.__kamar_kos.get_nomor_kamar()
