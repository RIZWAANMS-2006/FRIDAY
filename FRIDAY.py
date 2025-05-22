try:
    print()
    print("===============","FRIDAY","===============")
    import pyttsx3
    import pyaudio
    import pyjokes
    import pywhatkit
    import speech_recognition as sr
    import enchant as search
    import mysql.connector as ms
    import wikipedia
    from math import *

    listener = sr.Recognizer()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.runAndWait()


    def speak(process):
        engine.say(process)
        engine.runAndWait()


    def action():
        try:
            with sr.Microphone() as voice_input:
                print('I AM LISTENING......', end=' = ')
                temp_input = listener.listen(voice_input)
                process = listener.recognize_google(temp_input)
                print(process)
                return process
        except:
            print()
            print('ERROR M1: THERE IS A PROBLEM IN YOUR MICROPHONE')


    def check(inputa):
        dictionary = search.Dict('en_us')
        input2 = inputa.lower().split()
        t = 0
        if inputa == 'NONE':
            print("SORRY CAN YOU SPEAK AGAIN")
            print()
        else:
            for i in input2:
                if dictionary.check(i):
                    t += 1
                else:
                    pass
            if len(input2) == t:
                pywhatkit.search(inputa)
            else:
                print('SORRY BUT I AM UNABLE TO UNDERSTAND.')


    def main_action(inputa, v, name, age, phno, dob):

        if 'FUN FACT' in inputa or 'INTERESTING FACTS' in inputa or 'RANDOM FACT' in inputa or 'AMAZING FACT' in inputa:
            print()
            import randfacts
            temp = randfacts.get_fact()
            print(temp)
            if v == 1:
                speak(temp)
        elif 'RANDOM NUMBER' in inputa or 'PICK A RANDOM NUMBER' in inputa:
            import MODULE.random1

            temp = MODULE.random1.random1()
            if v == 1:
                speak(temp)
        elif '/' in inputa or '*' in inputa or '-' in inputa or '+' in inputa or 'sin' in inputa or 'cos' in inputa or 'tan' in inputa:
            try:
                inputa = inputa.replace('YOU', '')
                inputa = inputa.replace('CAN', '')
                inputa = inputa.replace('HELLO', '')
                inputa = inputa.replace('FRIDAY', '')
                inputa = inputa.replace('HEY', '')
                inputa = inputa.replace('HI', '')
                inputa = inputa.replace('CALCULATE', '')
                inputa = inputa.replace('CALCULATOR', '')

                cal1 = str(inputa).lower()
                cal1 = eval(cal1)
                print(cal1)
                if v == 1:
                    speak(cal1)
            except:
                check(inputa)
        elif 'PRESENT DAY' in inputa or 'TODAY DAY' in inputa or "PRESENTS DAY" in inputa or "TODAYS DAY" in inputa or "PRESENTS DAYS" in inputa or "TODAYS DAYS" in inputa or "PRESENT'S DAYS" in inputa or "TODAY'S DAYS" in inputa or "PRESENT DAYS" in inputa or "TODAY DAYS" in inputa or "PRESENT'S DAY" in inputa or "TODAY'S DAY" in inputa:
            import MODULE.tdmy_edit

            temp = MODULE.tdmy_edit.day()
            if v == 1:
                speak(temp)
        elif 'PRESENT DATE' in inputa or 'PRESENT MONTH' in inputa or 'PRESENT YEAR' in inputa or 'TODAY DATE' in inputa or 'TODAY MONTH' in inputa or 'TODAY YEAR' in inputa:
            import MODULE.tdmy_edit

            temp = MODULE.tdmy_edit.today()
            if v == 1:
                speak(temp)
        elif 'PRESENT WEEK' in inputa or 'TODAY WEEK' in inputa or 'PRESENT WEEKS' in inputa or 'TODAY WEEKS' in inputa or "PRESENT'S WEEK" in inputa or "TODAY'S WEEK" in inputa:
            import MODULE.tdmy_edit

            temp = MODULE.tdmy_edit.day()
            if v == 1:
                speak(temp)
        elif 'TIME' in inputa or 'HOUR' in inputa or 'MINUTE' in inputa or 'PRESENT TIME' in inputa or 'PRESENT HOUR' in inputa or 'PRESENT MINUTE' in inputa or 'TODAY TIME' in inputa or 'TODAY HOUR' in inputa or 'TODAY MINUTE' in inputa:
            import MODULE.tdmy_edit

            temp = MODULE.tdmy_edit.time()
            if v == 1:
                speak(temp)
        elif 'COUNT' in inputa:
            import MODULE.count

            temp = MODULE.count.count()
            if v == 1:
                speak(temp)
        elif 'WWW' in inputa or 'COM' in inputa or 'ORG' in inputa or 'EDU' in inputa or 'GOV' in inputa:
            inputa = inputa.replace('HI', '')
            inputa = inputa.replace('HEY', '')
            inputa = inputa.replace('HELLO', '')
            inputa = inputa.replace('FRIDAY', '')
            inputa = inputa.replace('CAN', '')
            inputa = inputa.replace('YOU', '')
            inputa = inputa.replace('OPEN', '')
            inputa = inputa.strip()
            import MODULE.website1

            MODULE.website1.website2(str(inputa))
        elif 'LOVE YOU' in inputa:
            import MODULE.hlmv

            temp = MODULE.hlmv.love()
            if v == 1:
                speak(temp)
        elif 'MARRY YOU' in inputa:
            import MODULE.hlmv

            temp = MODULE.hlmv.marry()
            if v == 1:
                speak(temp)
        elif 'OPEN' in inputa:
            inputa = inputa.replace('HI', '')
            inputa = inputa.replace('HEY', '')
            inputa = inputa.replace('HELLO', '')
            inputa = inputa.replace('FRIDAY', '')
            inputa = inputa.replace('CAN', '')
            inputa = inputa.replace('YOU', '')
            input2 = inputa.replace('OPEN', '')
            input2 = input2.strip()
            input2 = input2.lower()
            import MODULE.app

            MODULE.app.open1(input2)
        elif "MY NAME" in inputa:
            print("YOUR NAME IS", name)
            if v == 1:
                speak(name)
        elif 'SCREEN MIRROR' in inputa:
            import MODULE.app

            MODULE.app.smapp()
        elif 'MAKE A NOTE' in inputa or 'MAKE NOTE' in inputa or 'MAKE A REMINDER' in inputa or 'MAKE REMINDER' in inputa:
            import MODULE.note

            MODULE.note.write_note(account)
        elif 'MY NOTE' in inputa or 'SHOW REMINDER' in inputa or 'SHOW MY REMINDER' in inputa or 'REMINDER' in inputa or 'DISPLAY NOTE' in inputa or 'DISPLAY MY NOTE' in inputa:
            import MODULE.note

            MODULE.note.read_note(account)
        elif "MY AGE" in inputa:
            print("YOUR AGE IS", age)
            if v == 1:
                speak(age)
        elif "MY BIRTHDAY" in inputa or "MY DATE OF BIRTH" in inputa or "MY DOB" in inputa:
            print('YOUR DATE OF BIRTH IS:', dob)
        elif "MY PHONE NUMBER" in inputa or "MY PH NO" in inputa or "MY PH" in inputa or "MY PHNO" in inputa:
            print("YOUR PHONE NUMBER IS", phno)
            if v == 1:
                speak(phno)
        elif "WHO" in inputa:
            inputa = inputa.replace('HEY', '')
            inputa = inputa.replace('HI', '')
            inputa = inputa.replace('HELLO', '')
            inputa = inputa.replace('FRIDAY', '')
            inputa = inputa.replace('CAN', '')
            inputa = inputa.replace('YOU', '')
            temp = inputa.replace("WHO IS THE", "")
            temp = inputa.replace("WHO IS", "")
            temp = str(wikipedia.summary(temp, 10))
            temp = temp.replace(".", ".\n")
            print(temp)
            if v == 1:
                speak(temp)
        elif "WHAT" in inputa:
            pywhatkit.search(inputa)
            print("YOUR ARE SEE THE RESULT IN A NEW WINDOW")
        elif 'FIND MY PHONE' in inputa or 'SEARCH MY PHONE' in inputa or 'FIND MY DEVICE' in inputa or 'SEARCH MY DEVICE' in inputa:
            import MODULE.app

            MODULE.app.find1()
        elif 'JOKE' in inputa:
            print()
            temp = str(pyjokes.get_joke())
            print(temp)
            if v == 1:
                speak(temp)
        elif 'PLAY' in inputa:
            inputa = inputa.replace('HEY', '')
            inputa = inputa.replace('HI', '')
            inputa = inputa.replace('HELLO', '')
            inputa = inputa.replace('FRIDAY', '')
            inputa = inputa.replace('CAN', '')
            inputa = inputa.replace('YOU', '')
            input2 = inputa.replace('PLAY', '')
            pywhatkit.playonyt(input2)
        elif 'WEATHER' in inputa:
            import MODULE.weather
            we = MODULE.weather
        elif 'SIRI' in inputa or 'ALEXA' in inputa or 'GOOGLE' in inputa or 'BIXBY' in inputa:
            import MODULE.hlmv
            temp = MODULE.hlmv.voice1()
            if v == 1:
                speak(temp)
        elif inputa == 'HI' or inputa == 'HELP' or inputa == 'HELLO' or inputa == 'HI FRIDAY' or inputa == 'HELP FRIDAY' or inputa == 'HELLO FRIDAY':
            import MODULE.hlmv
            temp = MODULE.hlmv.hi()
            if v == 1:
                speak(temp)
        elif 'SHUTDOWN MY PC' in inputa or 'SHUTDOWN THE PC' in inputa or 'SHUTDOWN PC' in inputa or 'SHUT PC' in inputa or 'SHUT MY PC' in inputa or 'SHUT THE PC' in inputa:
            import os
            os.system('shutdown /s')
        elif 'RESTART MY PC' in inputa or 'RESTART THE PC' in inputa or 'RESTART PC' in inputa:
            import os
            os.system('shutdown /r')
        elif 'SHUTDOWN' in inputa:
            import os
            os.system('shutdown /s')

        else:
            check(inputa)

    while True:
        connector = ms.connect(host='localhost', user='root', passwd='rizwaan')
        cursor = connector.cursor()
        cursor.execute('create database if not exists friday')
        cursor.execute('use friday')
        cursor.execute(
            "create table if not exists friday(userid int primary key,account varchar(100) unique,name varchar(100) not null,date_of_birth date not null,age int not null,phone_number bigint not null,password varchar(100) not null)")
        cursor.execute('select * from friday')
        record = cursor.fetchall()
        l = cursor.rowcount
        print()
        if record == []:
            idk1 = 0
            print("""YOU DO NOT HAVE A FRIDAY ACCOUNT IN THIS PC.
TO USE THIS APPLICATION YOU NEED TO HAVE A FRIDAY ACCOUNT.""")
            while True:
                print()
                cr = input("""WOULD YOU LIKE TO CREATE A FRIDAY ACCOUNT:
                                          1.YES
                                          2.NO

ANSWER: """).strip().upper()
                if 'YES' in cr or cr == 'S' or cr == '' or cr == '1':
                    import MODULE.creating

                    MODULE.creating.account()
                    print()
                    print("I THINK NOW YOU ARE GOOD TO GO WITH YOUR 'FRIDAY ACCOUNT'")
                    print()
                    break
                elif 'NO' in cr or cr == 'N' or 'NOPE' in cr or cr == '0' or cr == '2':
                    print()
                    print("WITHOUT HAVING A FRIDAY ACCOUNT YOU CAN'T USE THIS PROGRAM")
                    idk1 = 1
                    break
                else:
                    print("KINDLY GIVE PROPER INPUT")
                    continue
            if idk1 == 1:
                break
            elif idk1 == 0:
                continue
        else:
            idk2 = 0
            while True:
                if idk2 == 0:
                    conf = input("""DO YOU HAVE A 'FRIDAY ACCOUNT'?
                                 1. YES  
                                 2. NO

ANSWER: """).strip().upper()
                    if 'YES' in conf or conf == 'S' or conf == '' or conf == '1':
                        break
                    elif 'NO' in conf or conf == 'N' or 'NOPE' in conf or conf == '0' or conf == '2':
                        while True:
                            print()
                            conf2 = input("""WOULD YOU LIKE TO HAVE A 'FRIDAY ACCOUNT'?
                                        1. YES
                                        2. NO
                                
ANSWER: """).strip().upper()
                            if 'YES' in conf2 or conf2 == 'S' or conf2 == '' or conf2 == '1':
                                print()
                                print("YOUR ARE IN THE SETUP PAGE OF 'FRIDAY ACCOUNT':")
                                import MODULE.creating

                                MODULE.creating.account()
                                print()
                                print("I THINK NOW YOU ARE GOOD TO GO WITH YOUR 'FRIDAY ACCOUNT'")
                                break
                            elif 'NO' in conf2 or conf2 == 'N' or conf2 == 'NOPE' or conf2 == '0' or conf2 == '2':
                                idk2 = 1
                                print()
                                print("SORRY WITHOUT HAVING A 'FRIDAY ACCOUNT' YOU CAN'T USE THIS PROGRAM")
                                break
                            else:
                                print("KINDLY GIVE PROPER INPUT")
                                continue
                    else:
                        print("KINDLY GIVE PROPER INPUT")
                        continue
                else:
                    break
            if idk2 == 1:
                break

            while True:
                print()
                account = input('ENTER YOUR ACCOUNT:').lower()
                account = account.replace('@', '')
                account = account.replace('@friday.com', '')
                account = account.replace('@friday', '')
                account = account.replace('.com', '')
                account = account + '@friday.com'
                t = 0
                for tp in range(0, l):
                    if record[tp][1] == account:
                        t = 1
                        break
                    else:
                        continue
                if t == 1:
                    print("OK THEN")
                    break
                else:
                    print("NO ACCOUNT FOUND.")
                    print('TRY ENTERING YOUR ACCOUNT NAME AGAIN:')
                    continue
            while True:
                print()
                password = input("ENTER YOU ACCOUNT's PASSWORD:")
                cursor.execute("select * from friday where account = '%s'" % account)
                f = cursor.fetchone()
                if f[6] == password:
                    print('OK TO GO WITH YOUR PASSWORD')
                    break
                else:
                    print('SORRY YOUR PASSWORD IS WRONG')
                    continue
            print()
            print("IF DO YOU WANT TO SEARCH IN GOOGLE DIRECTLY THE TYPE 'HYPER SEARCH'")
            while True:
                t = 0
                name = record[tp][2]
                age = record[tp][4]
                phno = record[tp][5]
                dob = str(record[tp][3])
                inputm = input("""IN WHICH METHOD WOULD YOU LIKE TO GIVE:
                                                                    1) TEXT
                                                                    2) VOICE
                                                                    3) HYPER SEARCH
                                                                    4) OR DO YOU WANT TO EXIT THE PROGRAM

ANSWER: """).upper().strip()
                while True:
                    if "TEXT" in inputm or inputm == '1':
                        v = 0
                        print()
                        inputn = input('ENTER YOUR OPERATION: ').upper().strip()
                        try:
                            if inputn == 'EXIT' or inputn == 'CLOSE':
                                break
                            else:
                                main_action(inputn, v, name, age, phno, dob)
                        except:
                            check(inputn)

                    elif "VOICE" in inputm or inputm == '2':
                        v = 1
                        print()
                        inputv = str(action()).upper()
                        try:
                            if inputv == 'EXIT' or inputv == 'CLOSE':
                                break
                            else:
                                main_action(inputv, v, name, age, phno, dob)
                                enter_pass = input("PRESS 'ENTER KEY' TO SPEAK AGAIN:").replace(enter_pass, '')
                                if enter_pass == '':
                                    continue

                        except:
                            pass

                    elif 'HYPER SEARCH' in inputm or inputm == '3':
                        print()
                        input1 = input('WHAT DO YOU WANT TO SEARCH: ').lower()
                        if input1 == 'exit' or input1 == 'close':
                            break
                        else:
                            pywhatkit.search(input1)

                    elif "EXIT" in inputm or inputm == '4' or "CLOSE" in inputm:
                        t = 1
                        print()
                        print("SEE YOU NEXT TIME " + "'" + str(name).upper() + "'")
                        print("BYE BYE.")
                        break

                    else:
                        print()
                        print('''WRONG INPUT METHOD.
PLEASE ENTER AGAIN.''')
                        break
                if t == 1:
                    break
            if t == 1:
                break
except ModuleNotFoundError:
    print()
    x = open("G:\\My Drive\\FRIDAY\\SETUP\\SETUP.txt",'r')
    print(x.read())
