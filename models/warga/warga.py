from uuid import uuid4


class Warga:
    def __init__(self, nama_depan, nama_belakang, nik, alamat_ktp, blok_ppn, no_ppn, email, tempat_lahir,
                 tanggal_lahir, no_hp, agama, pekerjaan, password, jumlah_penghuni, rincian_penghuni=None, _id=None,
                 aktif=None):
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
        self.aktif = aktif or False

    def json(self):
        return {"nama_depan": self.nama_depan, "nama_belakang": self.nama_belakang, "nik": self.nik,
                "alamat_ktp": self.alamat_ktp, "blok_ppn": self.blok_ppn, "no_ppn": self.no_ppn, "email": self.email,
                "tempat_lahir": self.tempat_lahir, "tanggal_lahir": self.tanggal_lahir, "no_hp": self.no_hp,
                "agama": self.agama, "pekerjaan": self.pekerjaan, "password": self.password,
                "jumlah_penghuni": self.jumlah_penghuni, "rincian_penghuni": self.rincian_penghuni, "_id": self._id,
                "aktif": self.aktif}
