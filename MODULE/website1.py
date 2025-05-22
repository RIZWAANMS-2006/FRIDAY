def website1():
    print('ENTER THE NAME OF THE WEBSITE WITH SUFFIX AND PREFIX')
    print()
    while True:
        input1 = input('ENTER THE NAME OF THE WEBSITE: ').lower()
        if input1 == 'exit' or input1 == 'close':
            break
        else:
            import webbrowser
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))
            webbrowser.get('chrome').open(input1)


def website2(input1):
    input1 = input1.lower()
    import os
    os.system('start chrome ' + input1)
    print("WEBSITE IS OPENED IN THE GOOGLE BROWSER")
