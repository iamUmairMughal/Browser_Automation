import tkinter as tk  # tk package allows to create buttons etc
from tkinter import ttk
from Automation_Task import *
import re
import datetime

main = tk.Tk()
main.geometry("700x500")
main.title("Web Browser Analysis Toolkit")
main.resizable(0, 0)

ttk.Label(main, text="Filters:").grid(column=0, row=1, padx=5, pady=5)
cmb = ttk.Combobox(main, width="20", values=("Create Timeline", "Keyword Search", "Regular Expression Search"))
cmb_files = ttk.Combobox(main, width="20", values=("Bookmarks", "Downloads", "History", "Cookies"))


class TableDropDown(ttk.Combobox):
    def __init__(self, parent):
        self.current_table = tk.StringVar()  # create variable for table
        ttk.Combobox.__init__(self, parent)  # init widget
        self.config(textvariable=self.current_table, state="readonly",
                    values=["Customers", "Pets", "Invoices", "Prices"])
        self.current(0)  # index of values for current table
        self.place(x=25, y=25, anchor="w")  # place drop down box

def open_Toplevel1(title, label):
    top1 = tk.Toplevel(main)

    top1.title(title)
    # top1.geometry("200x200")

    label = tk.Label(top1,
                  text=label)
    label.pack(padx=5, pady=10)
    top1.mainloop()


def checkcmbo():

    if cmb.get() == "Create Timeline":
        # cmb_files.config(value=("Downloads", "History"))
        keywordTree.grid_remove()
        regexTree.grid_remove()
        timelineTree.grid_remove()
        regexTree.grid_remove()
        regexLabel.grid_remove()
        regexEntry.grid_remove()
        timelineLabel.grid_remove()
        time1Entry.grid_remove()
        time2Entry.grid_remove()
        date2Entry.grid_remove()
        date1Entry.grid_remove()
        keywordEntry.grid_remove()
        keywordLabel.grid_remove()
        keywordsearch.grid_remove()
        regexsearch.grid_remove()
        timelinesearch.grid_remove()
        selection = False
        timelineTree["columns"] = ("1", "2")
        timelineTree['show'] = 'headings'

        if cmb_files.get() == "History":
            timelineTree.delete(*timelineTree.get_children())
            timelineTree.heading("1", text="Page Name")
            timelineTree.heading("2", text="Page URL")
            selection = True
        elif cmb_files.get() == "Downloads":
            timelineTree.delete(*timelineTree.get_children())
            timelineTree.heading("1", text="File Name")
            timelineTree.heading("2", text="Download Directory")
            selection = True
        else:
            print('Please Select Downloads or History Option from Database Dropdown.')
            open_Toplevel1('Error!', 'Please Select Downloads or History\n Option from Database Dropdown.')
            selection = False

        if selection:
            date1Entry.grid(column=1, row=2, padx=5, pady=5)
            date2Entry.grid(column=2, row=2, padx=5, pady=5)
            time1Entry.grid(column=1, row=3, padx=5, pady=5)
            time2Entry.grid(column=2, row=3, padx=5, pady=5)
            timelinesearch.grid(column=3, row=2, padx=5, pady=5)
            timelineLabel.grid(column=0, row=2, padx=5, pady=5)

            timelineTree.column("1", width=300, anchor='nw', stretch=tk.YES)
            timelineTree.column("2", width=300, anchor='nw', stretch=tk.YES)
            timelineTree.grid(row=4, column=0, columnspan=4, padx=10, pady=5)


    elif cmb.get() == "Keyword Search":
        keywordTree.grid_remove()
        regexTree.grid_remove()
        timelineTree.grid_remove()
        regexTree.grid_remove()
        regexLabel.grid_remove()
        regexEntry.grid_remove()
        timelineLabel.grid_remove()
        time1Entry.grid_remove()
        time2Entry.grid_remove()
        date2Entry.grid_remove()
        date1Entry.grid_remove()
        keywordEntry.grid_remove()
        keywordLabel.grid_remove()
        keywordsearch.grid_remove()
        regexsearch.grid_remove()
        timelinesearch.grid_remove()
        selection = False
        keywordTree["columns"] = ("1", "2")
        keywordTree['show'] = 'headings'

        if cmb_files.get() == "Bookmarks":
            keywordTree.delete(*keywordTree.get_children())
            keywordTree.heading("1", text="Bookmark Name")
            keywordTree.heading("2", text="Bookmark URL")
            selection = True
        elif cmb_files.get() == "Downloads":
            keywordTree.delete(*keywordTree.get_children())
            keywordTree.heading("1", text="File Name")
            keywordTree.heading("2", text="Download Directory")
            selection = True
        elif cmb_files.get() == "History":
            keywordTree.delete(*keywordTree.get_children())
            keywordTree.heading("1", text="Page Name")
            keywordTree.heading("2", text="Page URL")
            selection = True
        elif cmb_files.get() == "Cookies":
            keywordTree.delete(*keywordTree.get_children())
            keywordTree.heading("1", text="Site")
            keywordTree.heading("2", text="Data")
            selection = True
        else:
            print('Please Select Any Option from Database Dropdown.')
            open_Toplevel1('Error!', 'Please Select Any Option\n from Database Dropdown.')
            selection = False

        if selection:
            keywordEntry.grid(column=1, row=2, padx=5, pady=5)
            keywordsearch.grid(column=2, row=2, padx=5, pady=5)
            keywordLabel.grid(column=0, row=2, padx=5, pady=5)

            keywordTree.column("1", width=300, anchor='nw', stretch=tk.YES)
            keywordTree.column("2", width=300, anchor='nw', stretch=tk.YES)
            keywordTree.grid(row=4, column=0, columnspan=4, padx=10, pady=5)

    elif cmb.get() == "Regular Expression Search":
        keywordTree.grid_remove()
        regexTree.grid_remove()
        timelineTree.grid_remove()
        regexTree.grid_remove()
        regexLabel.grid_remove()
        regexEntry.grid_remove()
        timelineLabel.grid_remove()
        time1Entry.grid_remove()
        time2Entry.grid_remove()
        date2Entry.grid_remove()
        date1Entry.grid_remove()
        keywordEntry.grid_remove()
        keywordLabel.grid_remove()
        keywordsearch.grid_remove()
        regexsearch.grid_remove()
        timelinesearch.grid_remove()
        selection = False
        regexTree["columns"] = ("1", "2")
        regexTree['show'] = 'headings'

        if cmb_files.get() == "Bookmarks":
            regexTree.delete(*regexTree.get_children())
            regexTree.heading("1", text="Bookmark Name")
            regexTree.heading("2", text="Bookmark URL")
            selection = True
        elif cmb_files.get() == "Downloads":
            regexTree.delete(*regexTree.get_children())
            regexTree.heading("1", text="File Name")
            regexTree.heading("2", text="Download Directory")
            selection = True
        elif cmb_files.get() == "History":
            regexTree.delete(*regexTree.get_children())
            regexTree.heading("1", text="Page Name")
            regexTree.heading("2", text="Page URL")
            selection = True
        elif cmb_files.get() == "Cookies":
            regexTree.delete(*regexTree.get_children())
            regexTree.heading("1", text="Site")
            regexTree.heading("2", text="Data")
            selection = True
        else:
            print('Please Select Any Option from Database Dropdown.')
            open_Toplevel1('Error!', 'Please Select Any Option\n from Database Dropdown.')
            selection = False

        if selection:
            regexEntry.grid(column=1, row=2, padx=5, pady=5)
            regexsearch.grid(column=2, row=2, padx=5, pady=5)
            regexLabel.grid(column=0, row=2, padx=5, pady=5)

            regexTree.column("1", width=300, anchor='nw', stretch=tk.YES)
            regexTree.column("2", width=300, anchor='nw', stretch=tk.YES)
            regexTree.grid(row=4, column=0, columnspan=4, padx=10, pady=5)

    elif cmb.get() == "stai":
        "What user choose", "you choose stai"

    elif cmb.get() == "":
        print('Plesse Select an Option from Dropdown.')
        open_Toplevel1('Error!', 'Plesse Select an Option from Dropdown.')


cmb.grid(column=1,row=1, padx=5, pady=5)
cmb_files.grid(column=2,row=1, padx=5, pady=5)

btn = ttk.Button(main, text="Apply Filter", command=checkcmbo)
btn.grid(column=3,row=1, padx=5, pady=5)


def regExSearch():
    if cmb_files.get() == "Bookmarks":
        regexTree.delete(*regexTree.get_children())
        searchBookmark()
    elif cmb_files.get() == "Downloads":
        regexTree.delete(*regexTree.get_children())
        searchDownloads()
    elif cmb_files.get() == "History":
        regexTree.delete(*regexTree.get_children())
        searchHistory()
    elif cmb_files.get() == "Cookies":
        regexTree.delete(*regexTree.get_children())
        searchCookies()
    else:
        print('Please Select Any Option from Database Dropdown.')
        open_Toplevel1('Error!', 'Please Select Any Option\n from Database Dropdown.')
    # matches = re.findall(searchKeyword)

def keywordSearch():
    if cmb_files.get() == "Bookmarks":
        keywordTree.delete(*keywordTree.get_children())
        searchBookmark()
    elif cmb_files.get() == "Downloads":
        keywordTree.delete(*keywordTree.get_children())
        searchDownloads()
    elif cmb_files.get() == "History":
        keywordTree.delete(*keywordTree.get_children())
        searchHistory()
    elif cmb_files.get() == "Cookies":
        keywordTree.delete(*keywordTree.get_children())
        searchCookies()
    else:
        print('Please Select Any Option from Database Dropdown.')
        open_Toplevel1('Error!', 'Please Select Any Option\n from Database Dropdown.')

def createTimeline():

    if cmb_files.get() == "Downloads":
        timelineTree.delete(*timelineTree.get_children())
        # print("createTime() Checked!")
        searchDownloads()
    elif cmb_files.get() == "History":
        timelineTree.delete(*timelineTree.get_children())
        searchHistory()
    else:
        print('Please Select Downloads or History Option from Database Dropdown.')
        open_Toplevel1('Error!', 'Please Select Downloads or History\n Option from Database Dropdown.')


def search():
    if cmb.get() == "Keyword Search":
        keywordSearch()
    elif cmb.get() == "Regular Expression Search":
        regExSearch()
    elif cmb.get() == 'Create Timeline':
        # print('search Checked!')
        createTimeline()

def searchBookmark():
    if cmb.get() == "Keyword Search":
        keywordTree.delete(*keywordTree.get_children())
        keywordTree.heading("1", text="Bookmark Name")
        keywordTree.heading("2", text="Bookmark URL")
        searchkeyword = name.get()
        print("you have entered ... " + searchkeyword)
        bookmark_list = Bookmarks()
        results = {}
        if bookmark_list == 'Error!':
            print('Please Close Your Browser.')
            open_Toplevel1('Error!', 'Please Close Your Browser.')
        else:
            for n, url in bookmark_list.items():
                if searchkeyword.lower() in n.lower():
                    results[n] = url
            if len(results) > 0:
                for n, url in results.items():
                    keywordTree.insert("", 'end', values=(n,url))
            else:
                print('No Results Found.')
                open_Toplevel1('Error!', 'No Results Found.')

    elif cmb.get() == "Regular Expression Search":

        regexTree.delete(*regexTree.get_children())
        regexTree.heading("1", text="Bookmark Name")
        regexTree.heading("2", text="Bookmark URL")
        searchRegex = regex.get()
        print("you have entered ... " + searchRegex)
        bookmark_list = Bookmarks()
        results = {}
        if bookmark_list == 'Error!':
            print('Please Close Your Browser.')
            open_Toplevel1('Error!', 'Please Close Your Browser.')
        else:

            for key in bookmark_list.keys():
                s = re.search(searchRegex, key)
                if s is not None:
                    results[s.string] = bookmark_list.get(s.string)
                s = None

            print(results)
            if len(results) > 0:
                for n, url in results.items():
                    regexTree.insert("", 'end', values=(n, url))
            else:
                print('No Results Found.')
                open_Toplevel1('Error!', 'No Results Found.')

def searchDownloads():

    if cmb.get() == "Keyword Search":

        keywordTree.delete(*keywordTree.get_children())
        keywordTree.heading("1", text="File Name")
        keywordTree.heading("2", text="Download Directory")
        searchkeyword = name.get()
        print("you have entered ... " + searchkeyword)
        downloads_list = Downloads()
        results = {}

        if downloads_list == 'Error!':
            print('Please Close Your Browser.')
            open_Toplevel1('Error!', 'Please Close Your Browser.')
        else:
            for n, url in downloads_list.items():
                if searchkeyword.lower() in n.lower():
                    results[n] = url

            # keywordTree.delete(*keywordTree.get_children())
            print(results)
            if len(results)>0:
                for n, url in results.items():
                    keywordTree.insert("", 'end', values=(n, url.get('to')))
            else:
                print('No Results Found.')
                open_Toplevel1('Error!', 'No Results Found.')

    elif cmb.get() == "Regular Expression Search":

        regexTree.delete(*regexTree.get_children())
        regexTree.heading("1", text="File Name")
        regexTree.heading("2", text="Download Directory")
        searchRegex = regex.get()
        print("you have entered ... " + searchRegex)
        downloads_list = Downloads()
        results = {}

        if downloads_list == 'Error!':
            print('Please Close Your Browser.')
            open_Toplevel1('Error!', 'Please Close Your Browser.')
        else:
            for key in downloads_list.keys():
                s = re.search(searchRegex, key)
                if s is not None:
                    results[s.string] = downloads_list.get(s.string)
                s = None

            print(results)
            if len(results) > 0:
                for n, url in results.items():
                    regexTree.insert("", 'end', values=(n, url))
            else:
                print('No Results Found.')
                open_Toplevel1('Error!', 'No Results Found.')

    elif cmb.get() == 'Create Timeline':
        # print('searchDownloads() Checked!')
        timelineTree.delete(*timelineTree.get_children())
        timelineTree.heading("1", text="File Name")
        timelineTree.heading("2", text="Download Directory")
        downloadsDic = Downloads()
        results = {}
        if downloadsDic == 'Error!':
            print('Please Close Your Browser.')
            open_Toplevel1('Error!', 'Please Close Your Browser.')
        else:
            startDate = date1.get()
            endDate = date2.get()

            if len(startDate.split('-')) is 3:
                startDate = datetime.date(int(startDate.split('-')[0]),
                                          int(startDate.split('-')[1]),
                                          int(startDate.split('-')[2]))
            else:
                startDate = datetime.date(2000, 1, 1)

            if len(endDate.split('-')) is 3:
                endDate = datetime.date(int(endDate.split('-')[0]),
                                        int(endDate.split('-')[1]),
                                        int(endDate.split('-')[2]))
            else:
                endDate = datetime.datetime.now().date()

            timestamp1 = time1.get()
            timestamp2 = time2.get()

            if len(timestamp1.split(':')) is 3:
                timestamp1 = datetime.time(int(timestamp1.split(':')[0]),
                                          int(timestamp1.split(':')[1]),
                                          int(timestamp1.split(':')[2]))
            else:
                timestamp1 = datetime.time(00,00,00)

            if len(timestamp2.split(':')) is 3:
                timestamp2 = datetime.time(int(timestamp2.split(':')[0]),
                                        int(timestamp2.split(':')[1]),
                                        int(timestamp2.split(':')[2]))
            else:
                timestamp2 = datetime.datetime.now().time()

            for key in downloadsDic:
                temp = downloadsDic[key]

                tempDate = datetime.date(int(temp['end_time'][1].split('-')[0]),
                                          int(temp['end_time'][1].split('-')[1]),
                                          int(temp['end_time'][1].split('-')[2]))

                tempTime = datetime.time(int(temp['end_time'][0].split(':')[0]),
                                          int(temp['end_time'][0].split(':')[1]),
                                          int(temp['end_time'][0].split(':')[2]))

                if startDate < tempDate < endDate and timestamp1 < tempTime < timestamp2:
                    results[key] = temp

            print(results)
            if len(results) > 0:
                for n, url in results.items():
                    timelineTree.insert("", 'end', values=(n, url.get('to')))
            else:
                print('No Results Found.')
                open_Toplevel1('Error!', 'No Results Found.')

def searchHistory():
    if cmb.get() == "Keyword Search":

        keywordTree.delete(*keywordTree.get_children())
        keywordTree.heading("1", text="Page Name")
        keywordTree.heading("2", text="Page URL")
        searchkeyword = name.get()
        print("you have entered ... " + searchkeyword)
        history_list = History()

        if history_list == 'Error!':
            print('Please Close Your Browser.')
            open_Toplevel1('Error!', 'Please Close Your Browser.')
        else:
            results = {}
            for n, url in history_list.items():
                if searchkeyword.lower() in n.lower():
                    results[n] = url

            keywordTree.delete(*keywordTree.get_children())
            print(results.items())

            if len(results) > 0:
                for n, url in results.items():
                    keywordTree.insert("", 'end', values=(n, url))
            else:
                print('No Results Found.')
                open_Toplevel1('Error!', 'No Results Found.')

    elif cmb.get() == "Regular Expression Search":

        regexTree.delete(*regexTree.get_children())
        regexTree.heading("1", text="File Name")
        regexTree.heading("2", text="Download Directory")
        searchRegex = regex.get()
        print("you have entered ... " + searchRegex)
        history_list = History()

        if history_list == 'Error!':
            print('Please Close Your Browser.')
            open_Toplevel1('Error!', 'Please Close Your Browser.')
        else:
            results = {}

            for key in history_list.keys():
                s = re.search(searchRegex, key)
                if s is not None:
                    results[s.string] = history_list.get(s.string)
                s = None

            print(results)
            if len(results) > 0:
                for n, url in results.items():
                    regexTree.insert("", 'end', values=(n, url))
            else:
                print('No Results Found.')
                open_Toplevel1('Error!', 'No Results Found.')

    elif cmb.get() == 'Create Timeline':
        # print('searchDownloads() Checked!')
        timelineTree.delete(*timelineTree.get_children())
        timelineTree.heading("1", text="Page Name")
        timelineTree.heading("2", text="Page URL")
        historyDic = History()
        if historyDic == 'Error!':
            print('Please Close Your Browser.')
            open_Toplevel1('Error!', 'Please Close Your Browser.')
        else:
            results = {}
            startDate = date1.get()
            endDate = date2.get()

            if len(startDate.split('-')) is 3:
                startDate = datetime.date(int(startDate.split('-')[0]),
                                          int(startDate.split('-')[1]),
                                          int(startDate.split('-')[2]))
            else:
                startDate = datetime.date(2000, 1, 1)

            if len(endDate.split('-')) is 3:
                endDate = datetime.date(int(endDate.split('-')[0]),
                                        int(endDate.split('-')[1]),
                                        int(endDate.split('-')[2]))
            else:
                endDate = datetime.datetime.now().date()

            timestamp1 = time1.get()
            timestamp2 = time2.get()

            if len(timestamp1.split(':')) is 3:
                timestamp1 = datetime.time(int(timestamp1.split(':')[0]),
                                          int(timestamp1.split(':')[1]),
                                          int(timestamp1.split(':')[2]))
            else:
                timestamp1 = datetime.time(00,00,00)

            if len(timestamp2.split(':')) is 3:
                timestamp2 = datetime.time(int(timestamp2.split(':')[0]),
                                        int(timestamp2.split(':')[1]),
                                        int(timestamp2.split(':')[2]))
            else:
                timestamp2 = datetime.datetime.now().time()

            for key in historyDic.keys():
                temp = historyDic[key]


                tempDate = datetime.date(int(temp['date'].split('-')[0]),
                                          int(temp['date'].split('-')[1]),
                                          int(temp['date'].split('-')[2]))

                tempTime = datetime.time(int(temp['time'].split(':')[0]),
                                          int(temp['time'].split(':')[1]),
                                          00)

                if startDate < tempDate < endDate and timestamp1 < tempTime < timestamp2:
                    results[key] = temp

            print(results)
            if len(results)>0:
                for n, url in results.items():
                    timelineTree.insert("", 'end', values=(n, url.get('item')))
            else:
                print('No Results Found.')
                open_Toplevel1('Error!', 'No Results Found.')

def searchCookies():
    if cmb.get() == "Keyword Search":
        keywordTree.delete(*keywordTree.get_children())
        keywordTree.heading("1", text="Site")
        keywordTree.heading("2", text="Data")
        searchkeyword = name.get()
        print("you have entered ... " + searchkeyword)
        cookies_list = Cookies()
        if cookies_list == 'Error!':
            print('Please Close Your Browser.')
            open_Toplevel1('Error!', 'Please Close Your Browser.')
        else:
            results = {}
            for n, url in cookies_list.items():
                if searchkeyword.lower() in n.lower():
                    results[n] = url

            keywordTree.delete(*keywordTree.get_children())
            print(results.items())
            if len(results)>0:
                for i, (n, url) in enumerate(results.items()):
                    keywordTree.insert("", 'end', values=(n, url))
            else:
                print('No Results Found.')
                open_Toplevel1('Error!', 'No Results Found.')

    elif cmb.get() == "Regular Expression Search":
        regexTree.delete(*regexTree.get_children())
        regexTree.heading("1", text="File Name")
        regexTree.heading("2", text="Download Directory")
        searchRegex = regex.get()
        print("you have entered ... " + searchRegex)
        cookies_list = Cookies()
        if cookies_list == 'Error!':
            print('Please Close Your Browser.')
            open_Toplevel1('Error!', 'Please Close Your Browser.')
        else:
            results = {}

            for key in cookies_list.keys():
                s = re.search(searchRegex, key)
                if s is not None:
                    results[s.string] = cookies_list.get(s.string)
                s = None

            print(results)
            if len(results)>0:
                for n, url in results.items():
                    regexTree.insert("", 'end', values=(n, url))
            else:
                print('No Results Found.')
                open_Toplevel1('Error!', 'No Results Found.')


def helpMenu():
    help = tk.Tk()
    help.geometry("500x500")
    help.title("Help Menu")
    ttk.Label(help, text="Help Guide",
              font="Helvetica 28 bold italic",
              foreground="black",
              justify="center").grid(row=0, padx=5, pady=5)
    ttk.Label(help, text="Step by step guide on how to use the tool",
              font="Helvetica 14 italic",
              foreground="black").grid(row=1)


ttk.Label(main, text="Web Browser Analysis Toolkit",
          font="Helvetica 28 bold italic",
          foreground="black",
          justify="center").grid(column=1, row=0, columnspan=4, padx=5, pady=5)

helpMenu = tk.Button(main, text='Help',
                     font="Helvetica 12",
                     command=helpMenu)
helpMenu.grid(column=4, row=1, padx=5, pady=5)

name = tk.StringVar()
keywordEntry = ttk.Entry(main, width=30, textvariable=name)
keywordsearch = ttk.Button(main, text='Search', command=search)
keywordLabel = ttk.Label(main, text="Enter Keyword: ",
          foreground="black")

keywordTree = ttk.Treeview(main, selectmode='browse')
keywordscrlbar = ttk.Scrollbar(main,
                           orient="vertical",
                           command=keywordTree.yview)

regex = tk.StringVar()
regexEntry = ttk.Entry(main, width=30, textvariable=regex)
regexsearch = ttk.Button(main, text='Search', command=search)
regexLabel = ttk.Label(main, text="Enter Regular Expression: ",
          foreground="black")

regexTree = ttk.Treeview(main, selectmode='browse')
regexscrlbar = ttk.Scrollbar(main,
                           orient="vertical",
                           command=regexTree.yview)



date1 = tk.StringVar()
date1Entry = ttk.Entry(main, width=30, textvariable=date1)
date2 = tk.StringVar()
date2Entry = ttk.Entry(main, width=30, textvariable=date2)

time1 = tk.StringVar()
time1Entry = ttk.Entry(main, width=30, textvariable=time1)
time2 = tk.StringVar()
time2Entry = ttk.Entry(main, width=30, textvariable=time2)


timelinesearch = ttk.Button(main, text='Search', command=search)
timelineLabel = ttk.Label(main, text="Create Timeline: ",
          foreground="black")

timelineTree = ttk.Treeview(main, selectmode='browse')
timelinescrlbar = ttk.Scrollbar(main,
                           orient="vertical",
                           command=timelineTree.yview)

main.mainloop()