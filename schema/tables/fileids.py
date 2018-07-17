#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

from sqlalchemy import and_
from sqlalchemy import Column, BOOLEAN, VARCHAR, INT
from sqlalchemy.sql import func

from schema.tables.base import BaseTable
from common.utils import guid


class FileIDS(BaseTable):

    __tablename__ = 'fileids'

    uid = Column(VARCHAR(32), primary_key=True, default=guid)
    mtype = Column(VARCHAR(20))
    md5 = Column(VARCHAR(32))
    sha1 = Column(VARCHAR(40))
    severity = Column(VARCHAR(10))
    reference = Column(VARCHAR(100))

    @classmethod
    def add(cls, mtype, md5, sha1, severity, reference):
        h = FileIDS()
        h.mtype = mtype
        h.value = value
        h.md5 = md5
        h.sha1 = sha1
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

    @classmethod
    def getByMd5(cls, md5):
        obj = cls.db.query(cls).filter(cls.md5 == md5)
        if obj.count() < 1:
            return None
        else:
            return obj.one()

    @classmethod
    def getBySha1(cls, sha1):
        obj = cls.db.query(cls).filter(cls.sha1 == sha1)
        if obj.count() < 1:
            return None
        else:
            return obj.one()
