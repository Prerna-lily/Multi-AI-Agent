
import sqlite3
from datetime import datetime

class SharedMemory:
    def __init__(self, db_path='shared_memory.db'):
        self.conn = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source TEXT,
                type TEXT,
                intent TEXT,
                data TEXT,
                timestamp TEXT
            )
        ''')
        self.conn.commit()

    def log(self, source, input_type, intent, data):
        self.conn.execute('''
            INSERT INTO memory (source, type, intent, data, timestamp)
            VALUES (?, ?, ?, ?, ?)
        ''', (source, input_type, intent, data, datetime.utcnow().isoformat()))
        self.conn.commit()

    def get_all(self):
        return self.conn.execute('SELECT * FROM memory').fetchall()
