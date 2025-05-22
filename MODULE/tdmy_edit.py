def today():
    print()
    import datetime
    x = datetime.datetime.now()
    a = str(x.strftime('%A')) + ' ' + str(x.strftime('%d')) + '-' + str(x.strftime('%B')) + '(' + str(x.strftime('%m')) + ')' + '-' + str(x.strftime('%Y')) + ' ' + str(x.strftime('%I')) + ':' + str(x.strftime('%M')) + ' ' + str(x.strftime('%p'))
    print(a)
    print()
    return a


def time():
    print()
    import datetime
    x = datetime.datetime.now()
    a = str(x.strftime('%I')) + ':' + str(x.strftime('%M')) + ' ' + str(x.strftime('%p'))
    print(a)
    print()
    return a


def day():
    print()
    import datetime
    x = datetime.datetime.now()
    a = str(x.strftime('%A'))
    print(a)
    print()
    return a
