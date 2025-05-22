import mysql.connector as ms
from datetime import datetime
tt = str(datetime.now()).split()
yy, mm, dd = str(tt[0]).split('-')
tt_ = str(tt[1]).split('.')
HH, MM, SS = str(tt_[0]).split(':')


def write_note(account):
    try:
        while True:
            while True:
                print()
                title = input('ENTER THE NAME OF THE REMINDER: ').upper().strip()
                if title == '':
                    print('KINDLY ENTER THE DETAILS PROPERLY. ')
                    continue
                else:
                    print('OK THEN.')
                    break
            while True:
                print()
                year = input("IN WHICH YEAR DO YOU WANT TO GET REMINDED: ").strip()
                check = year.isdigit()
                if len(year) == 4:
                    if check:
                        if int(year) >= int(yy):
                            print("OK THEN.")
                            year = int(year)
                            break
                        else:
                            print("YOU CAN'T ENTER THE PAST YEARS")
                            continue
                    else:
                        print("KINDLY JUST ENTER THE YEAR IN NUMERIC FORMAT.")
                        continue
                else:
                    print("ENTER THE YEAR IN 4 DIGIT FORMAT.")
                    continue
            while True:
                print()
                month = input("IN WHICH MONTH DO YOU WANT TO GET REMINDED [ENTER IN NUMERIC FORMAT]: ").strip()
                check = month.isdigit()
                if len(month) == 1 or len(month) == 2:
                    if check:
                        if int(month) <= 12 and int(month) > 0:
                            month = int(month)
                            print("OK THEN.")
                            break
                        else:
                            print("KINDLY ENTER PROPER MONTH NUMBER.")
                            continue
                    else:
                        print("KINDLY ENTER THE MONTH IN NUMERIC FORMAT")
                        continue
                else:
                    print("KINDLY ENTER THE MONTH WITH IN 2 DIGITS")
                    continue
            while True:
                print()
                date = input("IN WHICH DATE DO YOU WANT TO GET REMINDED: ").strip()
                check = date.isdigit()
                if len(date) == 1 or len(date) == 2:
                    if check:
                        if int(date) <= 31 and int(date) > 0:
                            print("OK THEN.")
                            break
                        else:
                            print("KINDLY ENTER DATE PROPERLY.")
                            continue
                    else:
                        print("KINDLY ENTER THE DATE IN NUMERIC FORMAT")
                        continue
                else:
                    print("KINDLY ENTER THE DATE WITH IN 2 DIGITS")
                    continue
            while True:
                print()
                ttry = input("DO YOU WANT TO SPECIFIC TIME IN YOUR REMINDER: ").upper().strip()
                if "YES" in ttry or ttry == 'S' or ttry == "Y" or ttry == "" or ttry == '1':
                    t = True
                    break
                elif "NO" in ttry or ttry == 'N' or "NO" in ttry or ttry == '0':
                    t = False
                    break
                else:
                    print("KINDLY ENTER PROPER INPUT.")
                    continue
            hour = ''
            minutes = ''
            seconds = ''
            while True:
                if t:
                    while True:
                        print()
                        hour = input("IN WHICH HOURS DO YOU WANT TO GET REMINDED: ").strip()
                        check = hour.isdigit()
                        if len(hour) == 1 or len(hour) == 2:
                            if check:
                                if int(hour) <= 23 and int(hour) >= 0:
                                    print("OK THEN.")
                                    break
                                else:
                                    print("KINDLY ENTER HOUR PROPERLY.")
                                    continue
                            else:
                                print("KINDLY ENTER THE HOUR IN NUMERIC FORMAT")
                                continue
                        else:
                            print("KINDLY ENTER THE HOUR WITH IN 2 DIGITS")
                            continue
                    while True:
                        print()
                        minutes = input("IN HOW MANY MINUTES DO YOU WANT TO GET REMINDED: ").strip()
                        check = minutes.isdigit()
                        if len(minutes) == 1 or len(minutes) == 2:
                            if check:
                                if int(minutes) <= 59 and int(minutes) >= 0:
                                    print("OK THEN.")
                                    break
                                else:
                                    print("KINDLY ENTER MINUTE PROPERLY.")
                                    continue
                            else:
                                print("KINDLY ENTER THE MINUTE IN NUMERIC FORMAT")
                                continue
                        else:
                            print("KINDLY ENTER THE MINUTE WITH IN 2 DIGITS")
                            continue
                    while True:
                        print()
                        seconds = input("IN HOW MANY SECONDS DO YOU WANT TO GET REMINDED: ").strip()
                        check = seconds.isdigit()
                        if len(seconds) == 1 or len(seconds) == 2:
                            if check:
                                if int(seconds) <= 59 and int(seconds) >= 0:
                                    print("OK THEN.")
                                    break
                                else:
                                    print("KINDLY ENTER SECONDS PROPERLY.")
                                    continue
                            else:
                                print("KINDLY ENTER THE SECONDS IN NUMERIC FORMAT")
                                continue
                        else:
                            print("KINDLY ENTER THE SECONDS WITH IN 2 DIGITS")
                            continue
                    break
                else:
                    break
            reminder = str(year) + '-' + str(month) + '-' + str(date) + ' ' + str(hour) + ':' + str(
                minutes) + ':' + str(seconds)
            while True:
                print()
                check = input("DO YOU WANT TO ADD ANY DESCRIPTION [Y/N]: ").strip().upper()
                if check == 'Y' or 'YES' in check or check == 'S' or check == '':
                    description = input('ENTER WHAT DO YOU WANT TO DESCRIBE ABOUT REMINDER: ').strip().upper()
                    if description == '':
                        print("OK YOU DON'T WANT TO ADD DESCRIPTION")
                        break
                    else:
                        print("OK THEN.")
                        break
                elif check == 'N' or 'NO' in check or check == 'N' or 'NOPE' in check:
                    description = ''
                    print("OK THEN.")
                    break
                else:
                    print("KINDLY ENTER PROPER INPUT AGAIN.")
                    continue
            con = ms.connect(host='localhost', user='root', passwd='rizwaan', database='friday')
            cur = con.cursor()
            cur.execute(
                "create table if not exists reminder(account varchar(50) not null, title_reminder varchar(50) not null, date_reminder datetime not null, description varchar(100))")
            con.commit()
            if description == '':
                print()
                print('YOUR REMINDER IS SET:')
                print("ACCOUNT : " + account)
                print("REMINDER'S NAME : " + title)
                print("THE REMINDER IS ON : " + reminder)
                print("THE DESCRIPTION FOR THIS REMINDER : " + 'NONE')
            else:
                print()
                print('YOUR REMINDER IS SET:')
                print("ACCOUNT : " + account)
                print("REMINDER'S NAME : " + title)
                print("THE REMINDER IS ON : " + reminder)
                print("THE DESCRIPTION FOR THIS REMINDER : " + description)
            while True:
                print()
                dump = input('ARE YOU OK WITH THIS DETAILS [Y/N]: ').upper().strip()
                if 'YES' in dump or dump == '' or dump == 'Y' or dump == 'S':
                    t = 1
                    break
                elif 'NO' in dump or 'NOPE' in dump or dump == 'N':
                    while True:
                        print()
                        dump1 = input("DO YOU WANT TO RE-ENTER YOUR REMINDER DETAILS").upper().strip()
                        if 'YES' in dump1 or dump1 == '' or dump1 == 'Y' or dump1 == 'S':
                            t = 0
                            print("ENTER YOUR DETAILS AGAIN BUT PROPERLY")
                            break
                        elif 'NO' in dump1 or 'NOPE' in dump1 or dump1 == 'N':
                            t = 1
                            print("OK THEN THE REMINDER IS SET.")
                            cur.execute(
                                "insert into reminder(account,title_reminder,date_reminder) values('{account}','{title}',"
                                "'{reminder}')".format(account=account, title=title, reminder=reminder))
                            con.commit()
                            break
                        else:
                            print("WRONG INPUT JUST TYPE 'YES OR 'NO'.")
                            continue
                        break
                else:
                    print("WRONG INPUT JUST TYPE 'YES OR 'NO'.")
                    continue
                break
            if t == 0:
                continue
            elif t == 1:
                if description == '':
                    cur.execute(
                        "insert into reminder(account,title_reminder,date_reminder) values('{account}','{title}','{reminder}')".format(account=account, title=title, reminder=reminder))
                    con.commit()
                else:
                    cur.execute(
                        "insert into reminder values('{account}','{title}','{reminder}','{description}')".format(account=account, title=title, reminder=reminder, description=description))
                    con.commit()
            break
    except:
        print('SORRY BUT YOU HAVE ENTER THE DETAILS IN-PROPERLY.')


def read_note(account):
    con = ms.connect(host='localhost', user='root', passwd='rizwaan', database='friday')
    cur = con.cursor()
    cur.execute(
        "create table if not exists reminder(account varchar(50) not null, title_reminder varchar(50) not null, date_reminder datetime not null, description varchar(100))")
    con.commit()
    cur.execute("select * from reminder where account = '{account}'".format(account=account))
    x = cur.fetchall()
    if x == []:
        print("THERE ARE NO RECORD IN THE REMINDER")
    else:
        for i in x:
            for j in i:
                print(j,end='\t')
            print()
        print()