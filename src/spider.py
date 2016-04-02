#coding=utf8
"""
# Author: quheng
# Created Time : Sat Apr  2 10:01:35 2016
"""
import MySQLdb
import pycurl
import StringIO
from datetime import date,timedelta
import json
from dbHelper import dbHelper

pic_url = r'http://news-at.zhihu.com/api/4/start-image/1080*1776'
content_url = r'http://news.at.zhihu.com/api/4/news/before/'
startDate = date(2013,5,19) #the start date of zhihuDaily
happy = u"瞎扯 · 如何正确地吐槽"

#the field of json
title = "title"
stoies = "stories"
id = "id"
image = "images"

def getContent(date):
    """
    get the content of content_url in date

    parameter:
        date: YYYYMMDD

    return:
        the content
    """
    c = pycurl.Curl()
    c.setopt(pycurl.URL, content_url + date)
    io = StringIO.StringIO()
    c.setopt(pycurl.WRITEFUNCTION, io.write)
    c.perform()
    return io.getvalue()

def traverseDate(startDate):
    now = date.today()
    delta =  timedelta(days=1)
    name =  raw_input("db username:")
    pw = raw_input("db password:")
    try:
        db = dbHelper(name, pw)
    except Exception, e:
        raise e

    month = startDate.month
    while (startDate <= now):
        if (startDate.month != month):
            month = startDate.month
            print startDate
        try:
            content = getContent(startDate.strftime('%Y%m%d'))
            content = json.loads(content)[stoies]
            for item in content:
                if item[title] == happy:
                    db.insert(item[id], startDate, item[image][0])
        except Exception, e:
            print "there is an error in %s" %startDate.strftime("%Y%m%d")
            print e
            print "********************"
        startDate += delta


if __name__ == "__main__":
    #getContent('20131010')
    traverseDate(startDate)
