#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

from sqlalchemy import and_
from sqlalchemy import Column, BOOLEAN, VARCHAR, INT
from sqlalchemy.sql import func

from schema.tables.base import BaseTable
from common.utils import guid


class HTTPIDS(BaseTable):

    __tablename__ = 'httpids'

    uid = Column(VARCHAR(32), primary_key=True, default=guid)
    key = Column(VARCHAR(30))
    value = Column(VARCHAR(200))
    reference = Column(VARCHAR(100))

    @classmethod
    def add(cls, db, key, value, reference):
        h = HTTPIDS()
        h.key = key
        h.value = value
        h.reference = reference
        db.add(h)
        db.commit()
        return True

    @classmethod
    def match(cls, db, key, value):
        rules = cls.getAll(db)
        for r in rules:
            if r.key == "*" or r.key == key:
                if re.match(r.value, value, re.I):
                    return r
        return False
