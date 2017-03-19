'''
# sqlenv - SQLAlchemy helper library
#
# Provides the basic SQLAlchemy components and wraps most of the
# automap/declarative logic.
#
# Author: Jon Hannah (jon.hannah01@gmail.com)
'''

from sqlalchemy import ForeignKey, Column, Table
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, String
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.exc import OperationalError
from sqlalchemy.sql.elements import ColumnElement, BinaryExpression

class SqlBase(object):
    __id_column_name__ = None

    @classmethod
    def __get_id_column_name(cls):
        if not cls.__id_column_name__:
            raise NotImplementedError('No ID column specified')

        return cls.__id_column_name__

    @classmethod
    def __get_id_column(cls):
        name = cls.__get_id_column_name()

        if not name:
            raise NotImplementedError('Unable to determine ID column name')

        if not hasattr(cls, cls.__id_column_name__):
            raise NotImplementedError('Unable to find ID column "%s"' % cls.__id_column_name__)

        return getattr(cls, cls.__id_column_name__)

    @classmethod
    def get(cls, session, id_value, return_query=False, return_one=True):
        if isinstance(id_value, BinaryExpression):
            qry = session.query(cls).filter(id_value)
        else:
            qry = session.query(cls).filter_by(**{cls.__get_id_column_name(): id_value})


        if return_query:
            return qry

        cnt = qry.count()

        if cnt == 0:
            return None
        else:
            if cnt > 1:
                if return_one:
                    return qry.first()
            return qry.one()

def sa_setup():
    '''TODO: Docstring'''
    pass

__all__ = ['SqlBase', 'sa_setup']
