import random
from datetime import datetime

import mysql.connector as ms


def account():
    try:
        connector = ms.connect(host='localhost', user='root', passwd='rizwaan')
        cursor = connector.cursor()
        cursor.execute('create database if not exists friday')
        connector.commit()
        connector.close()

        connector = ms.connect(host='localhost', user='root', passwd='rizwaan', database='friday')
        cursor = connector.cursor()
        cursor.execute(
            'create table if not exists friday(userid int primary key,account varchar(100) unique,name varchar(100) not null,date_of_birth date not null,age int not null,phone_number bigint not null,password varchar(100) not null)')
        connector.commit()
        cursor.execute('select * from friday')
        x = cursor.fetchall()
        l = cursor.rowcount
        while True:
            while True:
                print()
                name = input('ENTER YOUR NAME:').strip().lower()
                if '!' in name or '@' in name or '#' in name or '$' in name or '%' in name or '^' in name or '&' in name or '*' in name or '(' in name or ')' in name or '_' in name or '=' in name or '/' in name or '-' in name or '+' in name or '<' in name or '>' in name or '?' in name or '\\' in name or ',' in name or "'" in name or '"' in name or ':' in name or ';' in name or '{' in name or '}' in name or '[' in name or ']' in name or '|' in name or '~' in name or '`' in name:
                    print("PLEASE DON'T ENTER ANY SPECIAL CHARACTER IN YOUR NAME.")
                    continue
                else:
                    break
            while True:
                print()
                account = input('CREATE YOUR ACCOUNT:').strip()
                account = account.replace('@', '')
                account = account.replace('@friday.com', '')
                account = account.replace('@friday', '')
                account = account.replace('.com', '')
                if '(' in account or ')' in account or '=' in account or '<' in account or '>' in account or '?' in account or '\\' in account or ',' in account or "'" in account or '"' in account or ':' in account or ';' in account or '{' in account or '}' in account or '[' in account or ']' in account or '|' in account or '~' in account or '`' in account:
                    print("SORRY YOU CAN'T USE FEW SPECIFIC CHARACTERS.")
                    continue
                elif account == '':
                    print("KINDLY FILL YOUR DETAILS PROPERLY")
                else:
                    if l == 0:
                        account = account + '@friday.com'
                        break
                    else:
                        account = account + '@friday.com'
                        t = 0
                        for tp in range(0, l):
                            if x[tp][1] == account:
                                print('''ALREADY THERE IS A ACCOUNT ALREADY EXIST
KINDLY HAVE SOME OTHER ACCOUNT NAME''')
                                t = 0
                                break
                            else:
                                t = 1
                                continue
                        if t == 0:
                            continue
                        else:
                            break
            while True:
                print()
                iy = input("ENTER YOUR 'YEAR OF BIRTH': ")
                check = iy.isdigit()
                year = datetime.now()
                year = str(year).split()
                year = year[0].replace('-', ' ').split()
                year = int(year[0])
                if check:
                    if len(iy) == 4:
                        if int(iy) > year:
                            print('SORRY YOUR ARE NOT FROM', iy)
                            print("I AM SURE.")
                            print("KINDLY ENTER PROPER 'YEAR OF BIRTH'.")
                            continue
                        elif int(iy) < year:
                            iy = int(iy)
                            age = year - iy
                            if age >= 10:
                                print("OK TO GO WITH YOUR 'YEAR OF BIRTH'.")
                                break
                            else:
                                print('''YOUR AGE IS LESS THEN 10.
YOU CAN'T OPEN YOU FRIDAY ACCOUNT WITH THIS AGE.''')
                                print("KINDLY TRY SOME OTHER AGE")
                                continue

                        else:
                            print('SORRY BUT YOU HAVE ENTERED PRESENT YEAR.')
                            continue
                    else:
                        print("PLEASE ENTER YOUR 'YEAR OF BIRTH' IN 4 DIGIT FORMAT.")
                        continue
                else:
                    print("KINDLY ENTER THE 'YEAR OF BIRTH' IN NUMERIC FORMAT.")
                    continue

            while True:
                print()
                month = input("ENTER YOUR 'MONTH OF BIRTH' IN NUMERIC FORMAT: ")
                check = month.isdigit()
                if check:
                    if len(month) == 2 or len(month) == 1:
                        if int(month) <= 12 and int(month) > 0:
                            month = int(month)
                            print('OK TO GO WITH YOU MONTH NUMBER.')
                            break
                        else:
                            print('YOUR MONTH OF BIRTH IS PROPER.')
                            continue
                    else:
                        print("PLEASE ENTER YOUR 'YEAR OF BIRTH' IN 2 DIGIT FORMAT.")
                        continue
                else:
                    print("KINDLY ENTER THE 'MONTH OF BIRTH' IN NUMERIC FORMAT")
                    continue

            while True:
                print()
                date = input("ENTER YOUR 'DATE OF BIRTH': ")
                check = date.isdigit()
                if check:
                    if len(date) == 2 or len(date) == 1:
                        if int(date) <= 31 and int(date) > 0:
                            date = int(date)
                            print("OK TO GO WITH YOUR 'DATE OF BIRTH'.")
                            break
                        else:
                            print("YOUR 'DATE OF BIRTH' IS NOT PROPER")
                            continue
                    else:
                        print("ENTER YOUR 'DATE OF BIRTH' IN 2 DIGIT FORMAT")
                        continue
                else:
                    print("ENTER YOUR 'DATE OF BIRTH' IN NUMERIC FORMAT")
                    continue
            while True:
                print()
                phno = input('ENTER YOUR THE 10 DIGIT PHONE NUMBER: ')
                check = phno.isdigit()
                if check:
                    if len(phno) == 10:
                        phno = int(phno)
                        print('OK TO GO WITH THE ', "'", phno, "'", ' AS YOUR PHONE NUMBER.')
                        break
                    else:
                        print('''JUST ENTER 10 DIGIT PHONE NUMBER.
INSTANT YOU HAVE ENTERED:''', phno)
                        continue
                else:
                    print("ENTER YOUR PHONE NUMBER IN NUMERIC FORMAT")
                    continue
            print()
            print("THE PASSWORD YOU ENTER IS CASE SENSITIVE")
            while True:
                print()
                password1 = input('ENTER YOUR DESIRED PASSWORD: ')
                password2 = input('ENTER YOUR DESIRED PASSWORD TO CONFIRMED:')
                if password1 == password2:
                    password = password1
                    print('OK TO GO WITH THE PASSWORD.')
                    break
                else:
                    print('SORRY CAN YOU RE-ENTER YOUR PASSWORD BECAUSE BOTH THE PASSWORD ARE NOT SAME.')
                    continue
            date_of_birth = str(iy) + '-' + str(month) + '-' + str(date)
            while True:
                print()
                check = """YOUR NAME IS {name}
YOUR ACCOUNT IS {account}
YOUR DATE OF BIRTH IS {date_of_birth}
YOUR PHONE NUMBER IS {ph_no}
YOUR PASSWORD IS {password}
            """.format(name=name.upper(), account=account, date_of_birth=date_of_birth, ph_no=phno, password=password)
                print(check)
                w = 0
                s = input("""IS THE DETAILS ARE CORRECT [Y/N]: """).upper().strip()
                if 'YES' in s or s == 'OK' or s == 'S' or s == '1' or s == 'Y' or s == '':
                    print('OK THEN')
                    break
                elif 'NO' in s or 'NOPE' in s or s == 'N' or s == '0':
                    re = input('DO YOU WANT TO ENTER YOUR DETAILS AGAIN: ').upper().strip()
                    if 'YES' in re or 'OK' in re or re == 'S' or re == '1' or re == 'Y':
                        w = 1
                        break
                    elif 'NO' in re or 'NOPE' in re or re == "N" or re == '0':
                        print("THEN I WILL PRECEDE WITH YOR DETAILS")
                        break
                    else:
                        print('JUST TYPE [Y/N]')
                        continue

            if x == [] and w == 0:
                userid = random.randint(1000, 9999)
                insert = "insert into friday values({userid},'{account}','{name}','{date_of_birth}',{age},{phone_number},'{password}')".format(
                    userid=userid, account=account, name=name, date_of_birth=date_of_birth, age=age, phone_number=phno,
                    password=password)
                cursor.execute(insert)
                connector.commit()
                connector.close()
            elif x != [] and w == 0:
                while True:
                    userid = random.randint(1000, 9999)

                    t = 0
                    for i in range(0, l):
                        if x[i][0] == userid:
                            break
                        else:
                            t += 1
                            continue
                    if t == 0:
                        continue
                    else:
                        break
                insert = "insert into friday values({userid},'{account}','{name}','{date_of_birth}',{age},{phone_number},'{password}')".format(
                    userid=userid, account=account, name=name, date_of_birth=date_of_birth, age=age, phone_number=phno,
                    password=password)
                cursor.execute(insert)
                connector.commit()
                connector.close()
            else:
                print()
                print("ENTER YOUR DETAIL'S AGAIN BUT PROPERLY")
                continue
            break
    except:
        print("""THERE IS A PROBLEM IN THE CREATING YOUR ACCOUNT.
KINDLY TRY LATER""")
