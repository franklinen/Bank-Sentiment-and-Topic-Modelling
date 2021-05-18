# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 12:27:34 2021

@author: MAIN
"""

import os
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker


class DB:
    def __init__(self):
        self.db_url = os.environ.get('DATABASE_URL')

    def create_db_engine(self) -> Engine:
        return create_engine(self.db_url)


@contextmanager
def session_scope():
    db = DB()
    session = sessionmaker(bind=db.create_db_engine())
    session = session()
    try:
        yield session
        session.commit()
    except Exception as e:  # noqa
        session.rollback()
        raise Exception(f'Rolling back due to {e}')
    finally:
        session.close()