
class Properti:
    def __init__(self, id_properti, alamat, harga_sewa):
        self.__id_properti = id_properti
        self.__alamat = alamat
        self.__harga_sewa = harga_sewa
        self.__status = "Tersedia"

    # Getter
    def get_id(self):
        return self.__id_properti

    def get_alamat(self):
        return self.__alamat

    def get_harga(self):
        return self.__harga_sewa

    def get_status(self):
        return self.__status

    # Mengubah status properti
    def set_status(self, status):
        self.__status = status

    # Menampilkan informasi properti
    def tampilkan_info(self):
        print("ID Properti :", self.__id_properti)
        print("Alamat      :", self.__alamat)
        print("Harga Sewa  : Rp", self.__harga_sewa)
        print("Status      :", self.__status)
