#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

from sqlalchemy import and_
from sqlalchemy import Column, BOOLEAN, VARCHAR, INT
from sqlalchemy.sql import func

from schema.tables.base import BaseTable
from common.utils import guid


class FILEIDS(BaseTable):

    __tablename__ = 'fileids'

    uid = Column(VARCHAR(32), primary_key=True, default=guid)
    mtype = Column(VARCHAR(20))
    threat = Column(VARCHAR(30))
    severity = Column(VARCHAR(10))
    reference = Column(VARCHAR(100))

    @classmethod
    def add(cls, mtype, threat, severity, reference):
        h = FILEIDS()
        h.mtype = mtype
        h.value = value
        h.threat = threat
        h.severity = severity
        h.reference = reference
        cls.db.add(h)
        cls.db.commit()
        return True

    @classmethod
    def getByMtype(cls, mtype):
        obj = cls.db.query(cls).filter(cls.mtype == mtype)
        if obj.count() < 1:
            return None
        else:
            return obj.one()
