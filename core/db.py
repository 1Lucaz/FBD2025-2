import psycopg2
# from psycopg2 import pool
# from contextlib import contextmanager
#
# from core import settings
#
# # from app.core.config import settings
#
# db_pool = pool.SimpleConnectionPool(
#     1, 10,
#     host=settings.DB_HOST,
#     database=settings.DB_NAME,
#     user=settings.DB_USER,
#     password=settings.DB_PASSWORD,
#     port=settings.DB_PORT,
# )
#
# @contextmanager
# def get_conn():
#     conn = db_pool.getconn()
#     try:
#         yield conn
#     finally:
#         db_pool.putconn(conn)


import psycopg2
from psycopg2.extras import RealDictCursor

from core import settings

class DataBase:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=settings.DB_HOST,
            database=settings.DB_NAME,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            port=settings.DB_PORT
        )

    def close(self):
        if self.conn and not self.conn.closed:
            self.conn.close()

    def fetchone(self, sql: str, params: tuple = None):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(sql, params)
            return cur.fetchone()

    def fetchall(self, sql: str, params: tuple = None):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(sql, params)
            return cur.fetchall()

    def commit(self, sql: str, params: tuple = None, returning: bool = False):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(sql, params)
            result = None
            if returning:
                result = cur.fetchone()
            self.conn.commit()
            return result

    def get_db():
        db = DataBase()
        try:
            yield db
        finally:
            db.close()
