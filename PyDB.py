#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: dely
"""

import sqlite3

#Change this path to where you want the database to reside
connection = sqlite3.connect('/path/to/save/database/TimerRecordsDatabase.db')
cursor = connection.cursor()

def create_table():
    command1 = """Create table if not exists Records(record_id integer primary key autoincrement, Date text, start_time text, end_time text, comments text)"""
    cursor.execute(command1)

def insert_data(DataTuple):
    print('trying')
    cursor.execute("insert into Records values (null,?,?,?,?)", (DataTuple))
    connection.commit()
    print('Data successfully recorded')



