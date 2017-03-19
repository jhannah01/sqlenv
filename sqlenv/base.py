'''
# sqlenv - SQLAlchemy helper library
#
# Provides the basic SQLAlchemy components and wraps most of the
# automap/declarative logic.
#
# Author: Jon Hannah (jon.hannah01@gmail.com)
'''

from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.automap import automap_base

from sqlenv.errors import SqlBaseError

class _SqlBase(object):
    @classmethod
    def get_by_id(cls, session, value, raw_query=False, force_one=True):
        kwargs = {cls._get_id_column(): value}
        q = session.query(cls).filter_by(**kwargs)

        if raw_query:
            return q

        if force_one:
            return q.one()

        return q.first()

    @classmethod
    def _get_id_column(cls):
        if hasattr(cls, '_id_column_name') and callable(cls._id_column_name):
            return cls._get_id_column_name()

        try:
            tbl_insp = inspect(cls)

            if not tbl_insp or not tbl_insp.primary_keys:
                raise SqlBaseError('Unable to inspect class to determine primary key')

            return tbl_insp.primary_keys[0].name
        except SQLAlchemyError, ex:
            raise SqlBaseError('Error with SQLAlchemy: %s' % str(ex))

SqlBase = automap_base(cls=_SqlBase)

def setup_sa(engine, do_autoflush=True, do_autocommit=True):
    SqlBase.prepare(engine, reflect=True)
    Session = scoped_session(sessionmaker(bind=engine, autoflush=do_autoflush, autocommit=do_autocommit))
    return Session

__all__ = ['SqlBase', 'SqlBaseError', 'setup_sa']

'''####
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
###'''
