from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.exc import InvalidRequestError, DisconnectionError, ResourceClosedError

from business_logic.config.properties import SQL_DB_URL
from business_logic.config.logging.loggers import get_logger
from business_logic.interfaces.idbconnection import IDBConnection
from business_logic.singleton import SingletonMeta

db_logger = get_logger('database')


class DatabaseConnection(IDBConnection):

    __metaclass__ = SingletonMeta

    def __init__(self):
        self.engine = create_engine(SQL_DB_URL)
        self.base = declarative_base()

    def connect(self):
        try:
            self.conn = self.engine.connect()
        except InvalidRequestError as ire:
            db_logger.error(f'{ire.status_code} -> There was an error connecting to the database, \
                         with the following message: {ire.message}')
            raise ire
        return self.conn

    def is_up(self):
        try:
            self.connect()
            self.disconnect()
        except DisconnectionError as de:
            db_logger.error(f'{de.status_code} -> The connection to the database was lost, \
                         with the following message: {de.message}')
            raise de
        return True

    def disconnect(self):
        try:
            self.conn.close()
        except ResourceClosedError as rce:
            db_logger.error(f'{rce.status_code} -> Database connection already closed.')
            raise rce
