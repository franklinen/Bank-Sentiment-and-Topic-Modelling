import os
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker


class DB:
    def __init__(self):
        self.db_url = os.environ.get("postgres://srgqubtsvuluva:53f09ecfc759c67e2b685959340e55a91587f4235f2e0401498ef89ec1834275@ec2-50-16-108-41.compute-1.amazonaws.com:5432/d30iap1nf7n7g0")

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
