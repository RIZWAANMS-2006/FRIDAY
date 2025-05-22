def smapp():
    print()
    input1 = input(' HAVE YOU CONNECTED YOUR PHONE USING AN USB CABLE [Y/N] :').upper()
    if input1 == 'Y' or input1 == 'YES':
        import os
        os.startfile('G:\\My Drive\\FRIDAY\\APPLICATION\\scrcpy\\scrcpy.exe')
        print()
        print('NOW YOU ARE SCREEN MIRRORING YOUR PHONE.')
    elif input1 == 'N' or input1 == 'NO':
        print()
        print('OK THEN TRY NEXT TIME')
    else:
        print()
        print('''WRONG INPUT
TRY AGAIN LATER''')


def find1():
    print()
    print('NOTE: MAKE SURE YOU HAVE SIGNED IN THE BROWSER WITH THE SAME GOOGLE ACCOUNT WHICH YOU HAVE SIGNED IN YOU PHONE.')
    print()
    temp = input('DO YOU HAVE A GOOGLE ACCOUNT SIGNED IN YOUR PHONE: ').upper()
    if temp == 'YES' or temp == 'Y' or temp == '1':
        import webbrowser
        webbrowser.register('chrome',
                            None,
                            webbrowser.BackgroundBrowser('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'))
        webbrowser.get('chrome').open('https://www.google.com/android/find?u=0')
    elif temp == 'NO' or temp == 'N' or temp == '0':
        print()
        print("SORRY BUT WE CAN'T HELP YOU WITHOUT HAVING A GOOGLE ACCOUNT SIGNED IN YOUR PHONE")
    else:
        print()
        print('WRONG INPUT')


def open1(a):
    operation = a.lower()
    if operation == 'exit' or operation == 'close':
        pass
    else:
        try:
            import os
            os.system('start ' + operation)
        except:
            pass
