#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

from sqlalchemy import and_
from sqlalchemy import Column, BOOLEAN, VARCHAR, INT
from sqlalchemy.sql import func

from schema.tables.base import BaseTable
from common.utils import guid


class IPIDS(BaseTable):

    __tablename__ = 'ipids'

    uid = Column(VARCHAR(32), primary_key=True, default=guid)
    ip = Column(VARCHAR(100))
    reference = Column(VARCHAR(100))

    @classmethod
    def add(cls, ip, reference):
        o = cls()
        o.ip = ip
        o.reference = reference
        cls.db.add(o)
        cls.db.commit()
        return True

    @classmethod
    def getByIP(cls, ip):
        obj = cls.db.query(cls).filter(cls.ip == ip)
        if obj.count() < 1:
            return None
        else:
            return obj.one()

    @classmethod
    def getAllWithKey(cls):
        ret = {}
        for i in cls.db.query(cls).all():
            ret[i.ip] = i.reference
        return ret
