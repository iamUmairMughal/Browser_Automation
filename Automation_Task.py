import os
import json
import sqlite3
import datetime
from winreg import HKEY_CURRENT_USER, OpenKey, QueryValueEx


# reg_path = r'Software\Microsoft\Windows\Shell\Associations\UrlAssociations\https\UserChoice'
#
# with OpenKey(HKEY_CURRENT_USER, reg_path) as key:
#     browser = QueryValueEx(key, 'ProgId')
#
# # print(browser)
#
# if browser[0] == 'ChromeHTML':
#     path = os.path.join(os.path.join(os.environ['USERPROFILE']), r'AppData\Local\Google\Chrome\User Data\Default')
# elif browser[0] == 'FirefoxHTML':
#     path = os.path.join(os.path.join(os.environ['USERPROFILE']), r'AppData\Local\Google\Chrome\User Data\Default')
# elif browser[0] == 'Opera.HTML':
#     path = os.path.join(os.path.join(os.environ['USERPROFILE']), r'AppData\Local\Google\Chrome\User Data\Default')
# elif browser[0] == 'IE.HTTPS':
#     path = os.path.join(os.path.join(os.environ['USERPROFILE']), r'AppData\Local\Google\Chrome\User Data\Default')
# elif browser[0] == 'MSEdgeHTM':
#     path = os.path.join(os.path.join(os.environ['USERPROFILE']), r'AppData\Local\Google\Chrome\User Data\Default')
# else:
#     print('No Browser Found')


path = os.path.join(os.path.join(os.environ['USERPROFILE']), r'AppData\Local\Google\Chrome\User Data\Default')

files = os.listdir(path)

def Bookmarks():
    try:
        bookmarks = open(os.path.join(path,'Bookmarks'),'r')

        bookmarks = json.loads(bookmarks.read())

        bookmarks_list = {}

        for bookmark in bookmarks['roots']['bookmark_bar']['children']:
            bookmarks_list[bookmark['name']] = bookmark['url']
    except:
        print('Error!')
        return 'Error!'

    return bookmarks_list


def History():
    historyDic = {}
    try:
        sqlite_file = os.path.join(path,'History')
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        c.execute("SELECT * FROM urls")
        items = c.fetchall()
        for item in items:
            secs = item[-2]
            x = datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=secs)
            time = str(x.time())[:5]
            date = str(x.date())
            historyDic[item[2]] = {'item':item[1], 'time' : time,'date': date}
    except:
        print('Error!')
        return 'Error!'

    return historyDic

# print(History())

def Downloads():
    downloadsDic = {}
    try:
        sqlite_file = os.path.join(path,'History')
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        c.execute("SELECT * FROM downloads")
        items = c.fetchall()
        # print(items)
        for item in items:
            start_datetime = datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=item[4])
            end_datetime = datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=item[11])
            start_time = str(start_datetime.time())[:8]
            start_date = str(start_datetime.date())
            end_time = str(end_datetime.time())[:8]
            end_date = str(end_datetime.date())
            downloadsDic[item[2].split('\\')[-1]] = {'to': item[2], 'from': item[18], 'type': item[-1],'start_time': [start_time, start_date],'end_time': [end_time, end_date]}
    except:
        print('Error!')
        return 'Error!'
    return downloadsDic

# print(Downloads())

def Cookies():
    cookiesDic = {}
    try:
        sqlite_file = os.path.join(path, 'Cookies')
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        c.execute("SELECT * FROM cookies")
        items = c.fetchall()
        for item in items:
            cookiesDic[item[1]] = [item[2], item[4]]
    except:
        print('Error!')
        return 'Error!'
    return cookiesDic


