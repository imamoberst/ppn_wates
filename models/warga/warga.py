from uuid import uuid4
from common.database import Database
from common.utils import Utlis
from datetime import datetime


class Warga:
    collection = 'warga'

    def __init__(self, nama_depan, nama_belakang, nik, alamat_ktp, blok_ppn, no_ppn, email, tempat_lahir,
                 tanggal_lahir, no_hp, agama, pekerjaan, password, jumlah_penghuni,
                 rincian_penghuni=None,
                 _id=None,
                 aktif=None, level=None, tanggal_daftar=None, last_login=None):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nik = nik
        self.alamat_ktp = alamat_ktp
        self.blok_ppn = blok_ppn
        self.no_ppn = no_ppn
        self.email = email
        self.tempat_lahir = tempat_lahir
        self.tanggal_lahir = tanggal_lahir
        self.no_hp = no_hp
        self.agama = agama
        self.pekerjaan = pekerjaan
        self.password = password
        self.jumlah_penghuni = jumlah_penghuni
        self.rincian_penghuni = rincian_penghuni or []
        self._id = _id or uuid4().hex
        self.level = level or 'warga'
        self.aktif = aktif or False
        self.tanggal_daftar = tanggal_daftar or ''
        self.last_login = last_login or ''

    def json(self):
        return {"nama_depan": self.nama_depan, "nama_belakang": self.nama_belakang, "nik": self.nik,
                "alamat_ktp": self.alamat_ktp, "blok_ppn": self.blok_ppn, "no_ppn": self.no_ppn, "email": self.email,
                "tempat_lahir": self.tempat_lahir, "tanggal_lahir": self.tanggal_lahir, "no_hp": self.no_hp,
                "agama": self.agama, "pekerjaan": self.pekerjaan, "password": self.password,
                "jumlah_penghuni": self.jumlah_penghuni, "rincian_penghuni": self.rincian_penghuni, "_id": self._id,
                "aktif": self.aktif, "level": self.level, "tanggal_daftar": self.tanggal_daftar,
                "last_login": self.last_login}

    def save_one_to_db(self):
        Database.insert_one(Warga.collection, self.json())

    def find_one_warga_from_db(self):
        return Database.find_one(Warga.collection, {"blok_ppn": self.blok_ppn, "no_ppn": self.no_ppn})

    @classmethod
    def find_one_warga_by_blok(cls, blokppn):
        blok = blokppn[0]
        no = blokppn[1:]
        data = Database.find_one(Warga.collection, {"blok_ppn": blok, "no_ppn": no, "aktif": True})
        if data:
            return cls(**data)
        else:
            return False

    @classmethod
    def find_one_warga_by_id(cls, idwarga):
        data = Database.find_one(Warga.collection, {"_id": idwarga})
        if data:
            return cls(**data)
        else:
            return False

    @classmethod
    def find_one_warga_by_aktif(cls):
        data = Database.find(Warga.collection, {"aktif": False})
        if data:
            return [cls(**d) for d in data]
        else:
            return False

    def hash_password(self):
        self.password = Utlis.hash_password(self.password)

    def tanggal_awal_daftar(self):
        self.tanggal_daftar = datetime.now().strftime("%Y-%m-%d %H:%M")

    def last_login_app(self):
        self.last_login = datetime.now().strftime("%Y-%m-%d %H:%M")
        Database.update_last_login(Warga.collection, {"_id": self._id}, {"last_login": self.last_login})

    @classmethod
    def is_valid_login(cls, blokppn, password):
        user = cls.find_one_warga_by_blok(blokppn)

        if not Utlis.check_hashed_password(password, user.password):
            return False
        user.last_login_app()
        return user

    def aktivasi_warga(self):
        self.aktif = True
        Database.update_one_data(Warga.collection, {"_id": self._id}, {"aktif": self.aktif})

    def update_level(self, level):
        self.level = level
        Database.update_one_data(Warga.collection, {"_id": self._id}, {"level": self.level})

    @classmethod
    def find_all(cls):
        return [cls(**data) for data in Database.find(cls.collection, {})]
