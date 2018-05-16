#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
from copy import deepcopy

from sqlalchemy.ext.declarative import as_declarative


@as_declarative()
class BaseTable(object):

    def toStr(self, blist=[]):
        s = deepcopy(self.__dict__)
        del(s['_sa_instance_state'])
        for i in s:
            if isinstance(s[i], datetime.datetime):
                s[i] = str(s[i])
        for b in blist:
            if b in s:
                del s[b]
        return s

    @classmethod
    def getAll(cls, db, toStr=False, blist=[]):
        if toStr:
            return [i.toStr(blist) for i in db.query(cls).all()]
        else:
            return db.query(cls).all()

    @classmethod
    def get(cls, db, uid):
        obj = db.query(cls).filter(cls.uid == uid)
        if obj.count() < 1:
            return None
        else:
            return obj.one()

    @classmethod
    def delete(cls, db, uid):
        obj = db.query(cls).filter(cls.uid == uid).delete()
        db.commit()
        return True
