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

    def _get_conn(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="sistema_estoque_aula",
            user="postgres",
            password="kernel@",
            port="5432"
        )

    def fetchone(self, sql: str, params: tuple = None):
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute(sql, params)
            row = cur.fetchone()
            return dict(row) if row else None
        finally:
            cur.close()
            self.conn.close()

    def fetchall(self, sql: str, params: tuple = None):
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute(sql, params)
            rows = cur.fetchall()
            return [dict(r) for r in rows]
        finally:
            cur.close()
            self.conn.close()

    def execute_commit(self, sql: str, params: tuple = None, returning: bool = False):
        cur = self.conn.cursor()
        try:
            cur.execute(sql, params)
            if returning:
                try:
                    result = cur.fetchone()
                except Exception:
                    result = None
            else:
                result = None
            self.conn.commit()
            return result
        except Exception:
            self.conn.rollback()
            raise
        finally:
            cur.close()
            self.conn.close()

