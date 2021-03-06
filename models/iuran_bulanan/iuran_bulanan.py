from uuid import uuid4


class TahunIuran:
    def __init__(self, tahun, datakas=None, dataiuran=None, _id=None):
        self.tahun = tahun
        self._id = _id or uuid4().hex
        self.dataiuran = dataiuran or []
        self.datakas = datakas or []

    def json(self):
        return {"_id": self._id, "tahun": self.tahun, "dataiuran": self.dataiuran, "datakas": self.datakas}


class DataBulanan:
    def __init__(self, bulan, tanggal_bayar=None, nama_rekening=None, bukti_bayar=None, verifikasi_oleh=None,
                 tanggal_verifikasi=None, status=None, _id=None):
        self.bulan = bulan
        self.tanggal_bayar = tanggal_bayar or ''
        self.nama_rekening = nama_rekening or ''
        self.bukti_bayar = bukti_bayar or ''
        self.verifikasi_oleh = verifikasi_oleh or ''
        self.tanggal_verifikasi = tanggal_verifikasi or ''
        self.status = status or 'belum_bayar'
        self._id = _id or uuid4().hex

    def json(self):
        return {"_id": self._id, "bulan": self.bulan, "tanggal_bayar": self.tanggal_bayar,
                "nama_rekening": self.nama_rekening, "bukti_bayar": self.bukti_bayar,
                "verifikasi_oleh": self.verifikasi_oleh, "tanggal_verifikasi": self.tanggal_verifikasi,
                "status": self.status}


class KasBulanan:
    def __init__(self, bulan, tanggal_bayar=None, nama_rekening=None, bukti_bayar=None, verifikasi_oleh=None,
                 tanggal_verifikasi=None, status=None, _id=None):
        self.bulan = bulan
        self.tanggal_bayar = tanggal_bayar or ''
        self.nama_rekening = nama_rekening or ''
        self.bukti_bayar = bukti_bayar or ''
        self.verifikasi_oleh = verifikasi_oleh or ''
        self.tanggal_verifikasi = tanggal_verifikasi or ''
        self.status = status or 'belum_bayar'
        self._id = _id or uuid4().hex

    def json(self):
        return {"_id": self._id, "bulan": self.bulan, "tanggal_bayar": self.tanggal_bayar,
                "nama_rekening": self.nama_rekening, "bukti_bayar": self.bukti_bayar,
                "verifikasi_oleh": self.verifikasi_oleh, "tanggal_verifikasi": self.tanggal_verifikasi,
                "status": self.status}
