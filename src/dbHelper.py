#coding=utf8
"""
# Author: quheng
# Created Time : Sat Apr  2 15:29:37 2016
"""
import MySQLdb

host = 'localhost'
port = 3306
dbName = "happyDaily"

class dbHelper(object):
    """helper for database"""
    def __init__(self, name, pw):
        super(dbHelper, self).__init__()
        self.conn= MySQLdb.connect(host=host ,port = port,\
                user=name ,passwd=pw ,db =dbName)
        self.cur = self.conn.cursor()

    def insert(self, id, date, image):
        self.str = "insert into article set id = \"%s\", image = \"%s\", date =\"%s\"" %(id, image,date)
        self.cur.execute(self.str)
        self.conn.commit()

    def __del__(self):
        self.cur.close()
        self.conn.close()

