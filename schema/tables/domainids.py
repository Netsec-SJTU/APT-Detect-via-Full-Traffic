#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

from sqlalchemy import and_
from sqlalchemy import Column, BOOLEAN, VARCHAR, INT
from sqlalchemy.sql import func

from schema.tables.base import BaseTable
from common.utils import guid


class DomainIDS(BaseTable):

    __tablename__ = 'domainids'

    uid = Column(VARCHAR(32), primary_key=True, default=guid)
    domain = Column(VARCHAR(100))
    reference = Column(VARCHAR(100))

    @classmethod
    def add(cls, domain, reference):
        o = cls()
        o.domain = domain
        o.reference = reference
        cls.db.add(o)
        cls.db.commit()
        return True

    @classmethod
    def getByDomain(cls, domain):
        obj = cls.db.query(cls).filter(cls.domain == domain)
        if obj.count() < 1:
            return None
        else:
            return obj.one()
