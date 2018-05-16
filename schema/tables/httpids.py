#!/usr/bin/env python
# -*- coding:utf-8 -*-

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

    @classmethod
    def add(cls, db, key, value):
        db.add(HTTPIDS(key=key, value=value))
        db.commit()
        return True
