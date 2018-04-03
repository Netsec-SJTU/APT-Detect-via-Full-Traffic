#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import and_
from sqlalchemy import Column, BOOLEAN, VARCHAR, INT
from sqlalchemy.sql import func

from schema.tables.base import BaseTable
from common.utils import guid


class Traffic(BaseTable):

    __tablename__ = 'traffic'

    uid = Column(VARCHAR(32), primary_key=True, default=guid)
    dstport = Column(INT)
    srcip = Column(VARCHAR(32))
    dstip = Column(VARCHAR(32))
    info = Column(VARCHAR(600))

    @classmethod
    def add(cls, db, dstport, srcip, dstip, info=""):
        t = Traffic()
        t.dstport = dstport
        t.srcip = srcip
        t.dstip = dstip
        t.info = info
        db.add(t)
        db.commit()
        return True
