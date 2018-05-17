#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import and_
from sqlalchemy import Column, BOOLEAN, VARCHAR, INT, TIMESTAMP
from sqlalchemy.sql import func

from schema.tables.base import BaseTable
from common.utils import guid


class Traffic(BaseTable):

    __tablename__ = 'traffic'

    uid = Column(VARCHAR(32), primary_key=True, default=guid)
    dstport = Column(INT)
    srcport = Column(INT)
    srcip = Column(VARCHAR(32))
    dstip = Column(VARCHAR(32))
    threat = Column(VARCHAR(30))
    severity = Column(VARCHAR(10))
    proto = Column(VARCHAR(10))
    time = Column(TIMESTAMP)
    reference = Column(VARCHAR(100))
    comment = Column(VARCHAR(600))

    @classmethod
    def add(cls, db, dstport, srcport, srcip, dstip,
            threat, severity, proto, time, reference, comment):
        t = Traffic()
        t.dstport = dstport
        t.srcport = srcport
        t.srcip = srcip
        t.dstip = dstip
        t.threat = threat
        t.severity = severity
        t.proto = proto
        t.time = time
        t.reference = reference
        t.comment = comment
        db.add(t)
        db.commit()
        return True

    @classmethod
    def getPage(cls, db):
        return [
            i.toStr() for i in db.query(cls).order_by(cls.time.desc()).limit(11)
        ]
