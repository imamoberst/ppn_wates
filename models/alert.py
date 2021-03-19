from uuid import uuid4
from common.database import Database


class AlertNotif:
    collection = 'alertnotif'

    def __init__(self, tanggal_notif, dbalert, iddbalert, alert_detail, namawarga, noppn, status=None, _id=None):
        self._id = _id or uuid4().hex
        self.tanggal_notif = tanggal_notif
        self.dbalert = dbalert
        self.alert_detail = alert_detail
        self.namawarga = namawarga
        self.noppn = noppn
        self.iddbalert = iddbalert
        self.status = status or 'alert'

    def json(self):
        return {
            "_id": self._id, "tanggal_notif": self.tanggal_notif, "dbalert": self.dbalert,
            "alert_detail": self.alert_detail, "namawarga": self.namawarga, "iddbalert": self.iddbalert,
            "noppn": self.noppn, "status": self.status
        }

    def save_to_db(self):
        Database.insert_one(AlertNotif.collection, self.json())

    @classmethod
    def find_all(cls):
        return [cls(**data) for data in Database.find(AlertNotif.collection, {})]
