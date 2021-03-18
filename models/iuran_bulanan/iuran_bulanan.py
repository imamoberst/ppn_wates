from common.database import Database
from uuid import uuid4


class TahunIuran:
    collection = 'iuran'

    def __init__(self, idwarga, norumah, iuran=None, _id=None):
        self.iuran = iuran or []
        self.norumah = norumah
        self.idwarga = idwarga
        self._id = uuid4().hex

    def json(self):
        return {"iuran": self.iuran, "norumah": self.norumah, "idwarga": self.idwarga, "_id": self._id}

    def update_json(self):
        return {"iuran": self.iuran, "norumah": self.norumah, "idwarga": self.idwarga}

    @classmethod
    def get_iuran_one_warga(cls, idwarga):
        # for d in Database.find(TahunIuran.collection, {"idwarga": idwarga}):
        #     print(d)
        return [cls(**data) for data in Database.find(TahunIuran.collection, {"idwarga": idwarga})]

    @classmethod
    def find_one_warga_by_idwarga(cls, idwarga):
        try:
            return cls(**Database.find_one(cls.collection, {"idwarga": idwarga}))
        except:
            return None

    @classmethod
    def find_all_warga_by_iuran_blm_konfirm(cls):
        try:
            return [cls(**d) for d in Database.find(cls.collection, {"iuran.iuranbulanan.status": "belum_bayar"})]
        except:
            return None

    @classmethod
    def find_all_iuran_warga(cls):
        return [cls(**data) for data in Database.find(cls.collection, {})]

    def save_to_db(self):
        Database.insert_one(TahunIuran.collection, self.json())

    def update_db(self):
        Database.update_one_data(TahunIuran.collection, {"idwarga": self.idwarga}, self.update_json())


class Tahun:
    def __init__(self, tahun, iuranbulanan=None, iurankas=None):
        self.tahun = tahun
        self.iuranbulanan = iuranbulanan or []
        self.iurankas = iurankas or []

    def json(self):
        return {"tahun": self.tahun, "iuranbulanan": self.iuranbulanan, "iurankas": self.iurankas}

    def save_to_db(self):
        Database.insert_one(TahunIuran.collection, self.json())


class DataBulanan:
    def __init__(self, bulan, catatan=None, tanggal_bayar=None, nama_rekening=None, bukti_bayar=None,
                 verifikasi_oleh=None,
                 tanggal_verifikasi=None, status=None):
        self.bulan = bulan
        self.tanggal_bayar = tanggal_bayar or ''
        self.nama_rekening = nama_rekening or ''
        self.bukti_bayar = bukti_bayar or ''
        self.verifikasi_oleh = verifikasi_oleh or ''
        self.tanggal_verifikasi = tanggal_verifikasi or ''
        self.status = status or 'belum_bayar'
        self.catatan = catatan or ''

    def json(self):
        return {"bulan": self.bulan, "tanggal_bayar": self.tanggal_bayar,
                "nama_rekening": self.nama_rekening, "bukti_bayar": self.bukti_bayar,
                "verifikasi_oleh": self.verifikasi_oleh, "tanggal_verifikasi": self.tanggal_verifikasi,
                "status": self.status, "catatan": self.catatan}


class KasBulanan:
    def __init__(self, bulan, catatan=None, tanggal_bayar=None, nama_rekening=None, bukti_bayar=None,
                 verifikasi_oleh=None,
                 tanggal_verifikasi=None, status=None):
        self.bulan = bulan
        self.tanggal_bayar = tanggal_bayar or ''
        self.nama_rekening = nama_rekening or ''
        self.bukti_bayar = bukti_bayar or ''
        self.verifikasi_oleh = verifikasi_oleh or ''
        self.tanggal_verifikasi = tanggal_verifikasi or ''
        self.status = status or 'belum_bayar'
        self.catatan = catatan or ''

    def json(self):
        return {"bulan": self.bulan, "tanggal_bayar": self.tanggal_bayar,
                "nama_rekening": self.nama_rekening, "bukti_bayar": self.bukti_bayar,
                "verifikasi_oleh": self.verifikasi_oleh, "tanggal_verifikasi": self.tanggal_verifikasi,
                "status": self.status, "catatan": self.catatan}
