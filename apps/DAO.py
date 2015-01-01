__author__ = 'Owen'

import MySQLdb
import time
import datetime
from models import User
dao = MySQLdb.connect("gach.cqesbxxoyeoo.us-west-2.rds.amazonaws.com", "owen", "Sksdhdnps86!", "gach_test")
cursor = dao.cursor()
def join(user):
    sql = "insert into User values ('%s', '%s', '%d', '%d', '%s')" % (user.id, user.pw, 1, 0, time.strftime('%Y-%m-%d %H:%M:%S'))
    try:
        cursor.execute(sql)
        dao.commit()
    except:
        dao.rollback()
    return 0

def joinCheck():
    sql = "select * from User where status = '%d'" % 1

    cursor.execute(sql)
    results = cursor.fetchall()
    now = datetime.datetime.now()
    for row in results:
        diff = now - row[4]
        if diff.seconds / 60 >= 30:
            dsql = "delete from User where id = '%s'" % row[0]
            cursor.execute(dsql)
            dao.commit()
def emailCheck(mail):
    sql = "select * from Joined Emails where email = '%s'" % mail
    cursor.execute(sql)
    results = cursor.fetchall()
    if len(results) > 0 :
        #duplicated email
        return False
    else :
        return True